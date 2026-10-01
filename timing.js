// Anlatim suresi cozucu.
// Oncelik: vo/<id>.mp3 varsa GERCEK sure olculur (ffprobe).
// Yoksa Brian'in olculmus temposundan TAHMIN edilir.

const fs = require('fs');
const path = require('path');
const { execFileSync } = require('child_process');

function wordCount(s) {
  const m = s.match(/[A-Za-z0-9'’]+/g);
  return m ? m.length : 0;
}

function probeDuration(file) {
  try {
    const out = execFileSync('ffprobe', [
      '-v', 'error', '-show_entries', 'format=duration',
      '-of', 'csv=p=0', file,
    ], { encoding: 'utf8' });
    const d = parseFloat(out.trim());
    return Number.isFinite(d) ? d : null;
  } catch { return null; }
}

/**
 * Her satir icin { id, text, words, dur, measured } dondurur.
 * @param {object} tl  timeline.json
 * @param {string} root  pipeline klasoru
 */
function resolveLines(tl, root) {
  // tl: timeline.json
  const spw = tl.voice.secPerWord;
  const voDir = path.join(root, tl.voDir || 'vo');

  return tl.lines.map((L) => {
    const words = wordCount(L.text);
    const mp3 = path.join(voDir, `${L.id}.mp3`);
    const wav = path.join(voDir, `${L.id}.wav`);
    let dur = null, measured = false, file = null;

    for (const f of [mp3, wav]) {
      if (fs.existsSync(f)) {
        const d = probeDuration(f);
        if (d) { dur = d; measured = true; file = f; break; }
      }
    }
    if (dur == null) {
      dur = words * spw;
      // Kisa vurucu satirlara editoryal tutus ("Fewer than half.").
      // Bu konusma duraklamasi degil, kasitli bir bekleme — pace.sh
      // duraklamalari kirptigi icin kirpilmis seste daha kisa tutulur.
      if (words <= 5) dur += tl.voice.paced ? 0.25 : 0.35;
    }
    return { ...L, words, dur: +dur.toFixed(3), measured, file };
  });
}

/** Satirlari mutlak zamanli duz olay listesine acar. */
function flatten(lines) {
  const events = [];
  let t = 0;
  for (const L of lines) {
    const beats = L.beats && L.beats.length ? L.beats : [{ at: 0, scene: { asset: 'blank' } }];
    beats.forEach((b, i) => {
      const start = t + (b.at || 0) * L.dur;
      const nextAt = i + 1 < beats.length ? beats[i + 1].at : 1;
      const end = t + nextAt * L.dur;
      events.push({
        line: L.id,
        t: +start.toFixed(3),
        dur: +(end - start).toFixed(3),
        scene: b.scene,
        bg: b.bg || L.bg || 'white',
        text: b.text || null,
        narration: i === 0 ? L.text : '',
      });
    });
    t += L.dur;
  }
  return { events, total: +t.toFixed(3) };
}

module.exports = { wordCount, probeDuration, resolveLines, flatten };
