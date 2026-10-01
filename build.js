#!/usr/bin/env node
// timeline.json -> HTML kareler + ffmpeg concat listesi + VO uretim listesi
// Kullanim: node build.js

const fs = require('fs');
const path = require('path');
const A = require('./assets.js');
const T = require('./timing.js');

const ROOT = __dirname;
const OUT = path.join(ROOT, 'out');
const HTML = path.join(OUT, 'html');
fs.mkdirSync(HTML, { recursive: true });

// Bölüm-farkındalık: TL env'i ile farklı timeline (hook, act1, ...) render edilir.
const TL_FILE = process.env.TL || 'timeline.json';
const tl = JSON.parse(fs.readFileSync(path.join(ROOT, TL_FILE), 'utf8'));

const IMG_DIR = path.join(ROOT, 'assets', 'img');

// Raster (PNG/JPG) varligi SVG icine data-URI olarak gomer.
// preserveAspectRatio slice: sahneyi tam kaplar, tasani kirpar.
function imgTag(file) {
  const p = path.join(IMG_DIR, file);
  if (!fs.existsSync(p)) throw new Error(`Gorsel yok: assets/img/${file}`);
  const ext = path.extname(file).slice(1).replace('jpg', 'jpeg');
  const b64 = fs.readFileSync(p).toString('base64');
  return `<image href="data:image/${ext};base64,${b64}" x="0" y="0" `
       + `width="320" height="180" preserveAspectRatio="xMidYMid slice"/>`;
}

// Raster gorselin USTUNE cizilen isaretler — ChatGPT'nin yapamadigi
// iki sey: tam metin ve tutarli parametrik isaret (nokta rengi, kirmizi X).
function overlayMarks(o) {
  if (!o) return '';
  let s = '';
  if (o.cross) {
    const [x, y, w, h] = o.box || [110, 40, 200, 100]; // sahne koordinati
    s += `<g fill="none" stroke="${A.P.red}" stroke-width="9" stroke-linecap="round">`
      +  `<path d="M${x} ${y} C${x+w*0.34} ${y+h*0.24} ${x+w*0.66} ${y+h*0.5} ${x+w} ${y+h*0.7}"/>`
      +  `<path d="M${x+w} ${y} C${x+w*0.66} ${y+h*0.24} ${x+w*0.34} ${y+h*0.5} ${x} ${y+h*0.7}"/></g>`;
  }
  if (o.dots) {
    // o.dots: [[x,y,'orange'|'gray'], ...] — haritanin uzerine oturur
    s += o.dots.map(([x, y, c]) =>
      `<circle cx="${x}" cy="${y}" r="4.4" fill="${c === 'orange' ? A.P.orange : A.P.gray}" `
      + `stroke="#fff" stroke-width="1.2"/>`).join('');
  }
  return s;
}

// --- sahne cozucu -------------------------------------------------
function renderScene(scene) {
  // raster gorsel: { img: "dosya.png", overlay: {...} }
  if (scene.img) return imgTag(scene.img) + overlayMarks(scene.overlay);

  const name = scene.asset;
  const opts = scene.opts || {};
  switch (name) {
    case 'blank':             return '';
    case 'kissingPair':       return A.kissingPair(opts);
    case 'kissingPairInCrowd':return A.crowd({ n: 6 }) + A.kissingPair({ lean: 1 });
    case 'singleFigure':      return A.figureProfile({ x: 160, y: 32, dir: 1 });
    case 'teacherBoard':      return A.teacherBoard(opts);
    case 'worldMap':          return A.worldMap(opts);
    case 'scale':             return A.scaleAsset(opts);
    case 'greetingRow':       return A.greetingRow(opts);
    case 'disgustFace':       return A.disgustFace();
    case 'thinkingFigure':    return A.thinkingFigure();
    default: throw new Error(`Bilinmeyen varlik: ${name}`);
  }
}

function renderText(t) {
  if (!t) return '';
  const styles = {
    'top-right':   'top:6%; right:7%; font-size:52px;',
    'top':         'top:8%; left:50%; transform:translateX(-50%); font-size:104px;', // Zenn imza: ustte buyuk
    'center-huge': 'top:50%; left:50%; transform:translate(-50%,-50%); font-size:150px;',
    'bottom':      'bottom:9%; left:50%; transform:translateX(-50%); font-size:60px;',
  };
  return `<div class="ost" style="${styles[t.pos] || styles.bottom}">${t.content}</div>`;
}

// renkli zeminde ekran yazısı beyaza döner
const OST_LIGHT = new Set(['field', 'night', 'warm']);

const page = (body, text, bg) => `<!doctype html><html><head><meta charset="utf-8"><style>
  html,body{margin:0;padding:0;width:${tl.width}px;height:${tl.height}px;overflow:hidden;background:#FFFFFF;}
  .stage{position:relative;width:${tl.width}px;height:${tl.height}px;}
  svg{display:block;width:100%;height:100%;}
  .ost{position:absolute;font-family:"Bradley Hand","Chalkboard SE","Comic Sans MS",cursive;
       font-weight:700;color:${OST_LIGHT.has(bg) ? '#FFFFFF' : '#000000'};
       letter-spacing:0.02em;line-height:1;white-space:nowrap;
       /* okunurluk halesi: yogun gorsel uzerinde de secilir */
       paint-order:stroke;-webkit-text-stroke:${OST_LIGHT.has(bg) ? '8px #000' : '8px #fff'};
       text-shadow:0 0 6px ${OST_LIGHT.has(bg) ? '#000' : '#fff'};}
</style></head><body><div class="stage">
<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 180">
${A.background(bg)}
${body}
</svg>${text}</div></body></html>`;

// --- zamanlama ----------------------------------------------------
const lines = T.resolveLines(tl, ROOT);
const { events, total } = T.flatten(lines);

// --- ciktilar -----------------------------------------------------
const concat = [];
events.forEach((e, i) => {
  const id = String(i + 1).padStart(3, '0');
  fs.writeFileSync(
    path.join(HTML, `f${id}.html`),
    page(renderScene(e.scene), renderText(e.text), e.bg)
  );
  concat.push(`file 'frames/f${id}.png'`);
  concat.push(`duration ${e.dur}`);
});
concat.push(`file 'frames/f${String(events.length).padStart(3, '0')}.png'`);
fs.writeFileSync(path.join(OUT, 'concat.txt'), concat.join('\n') + '\n');
fs.writeFileSync(path.join(OUT, 'duration.txt'), total.toFixed(3));

// ElevenLabs icin uretim listesi: her satir ayri dosya
fs.writeFileSync(
  path.join(OUT, 'vo-manifest.tsv'),
  'id\twords\test_sec\ttext\n' +
  lines.map(l => `${l.id}\t${l.words}\t${l.dur}\t${l.text}`).join('\n') + '\n'
);

// ses birlestirme listesi (vo dosyalari varsa)
const haveAll = lines.every(l => l.measured);
if (haveAll) {
  fs.writeFileSync(
    path.join(OUT, 'audio-concat.txt'),
    lines.map(l => `file '${path.relative(OUT, l.file)}'`).join('\n') + '\n'
  );
}

// --- rapor --------------------------------------------------------
const nMeas = lines.filter(l => l.measured).length;
const words = lines.reduce((a, l) => a + l.words, 0);
const mm = Math.floor(total / 60), ss = (total % 60).toFixed(1).padStart(4, '0');

const wpm = tl.voice.paced ? tl.voice.wpmPaced : tl.voice.wpmRaw;
console.log(`Ses         : ${tl.voice.name} @ ${wpm} kelime/dk${tl.voice.paced ? ' (pace.sh uygulanmis)' : ' (ham)'}`);
console.log(`Satir       : ${lines.length}  (${nMeas} olculdu, ${lines.length - nMeas} tahmin)`);
console.log(`Kelime      : ${words}`);
console.log(`Olay        : ${events.length}`);
console.log(`SURE        : ${mm}:${ss}  (${total.toFixed(1)} sn)`);
console.log(`Ort. plan   : ${(total / events.length).toFixed(2)} sn`);
console.log('');
console.log('id    kelime  sure   kaynak  satir');
console.log('-'.repeat(76));
for (const l of lines) {
  const src = l.measured ? 'OLCULDU' : 'tahmin ';
  const txt = l.text.length > 40 ? l.text.slice(0, 37) + '...' : l.text;
  console.log(`${l.id}  ${String(l.words).padStart(5)}  ${l.dur.toFixed(2).padStart(5)}s  ${src}  ${txt}`);
}
if (!haveAll) {
  console.log('');
  console.log(`>> vo/ bos. ${OUT}/vo-manifest.tsv dosyasindaki metinleri Brian ile uretip`);
  console.log(`>> vo/L01.mp3 ... seklinde kaydet, sonra tekrar calistir.`);
  console.log(`>> Sureler o zaman tahminden OLCULDU'ye doner.`);
}
