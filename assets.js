// Varlık kütüphanesi — Zenn üslubu
// Her varlık bir fonksiyon: opts alır, SVG <g> string'i döndürür.
// Tüm koordinatlar 320x180 sahne uzayında (16:9). Render 1920x1080'e ölçeklenir.

const P = {
  ground: '#FFFFFF',
  ink: '#000000',
  orange: '#E8862A',
  navy: '#3D5A80',
  green: '#4CA64C',
  brown: '#8B5A2B',
  red: '#E02020',
  gray: '#9A9A9A',
};

const SW = 4.6; // standart kontur kalınlığı

// Ortak kontur grubu açıcı
const ink = (inner, w = SW) =>
  `<g fill="none" stroke="${P.ink}" stroke-width="${w}" stroke-linecap="round" stroke-linejoin="round">${inner}</g>`;

// ---------------------------------------------------------------
// A-01 — Çöp adam (profil). dir: 1 sağa bakar, -1 sola bakar
// ---------------------------------------------------------------
function figureProfile({ x = 160, y = 32, dir = 1, scale = 1 }) {
  const f = dir < 0 ? `translate(${2 * x},0) scale(-1,1)` : '';
  return `<g transform="translate(${x - 160},${y - 32}) ${f ? '' : ''}">
    <g transform="${f}">
      ${ink(`
        <path d="M138 56 C138 42 127 32 113 32 C99 32 88 42 88 56 C88 70 99 80 113 80 C127 80 138 70 138 56 Z" fill="#fff"/>
        <path d="M113 80 C114 100 113 118 114 132"/>
        <path d="M113 94 C122 100 130 105 137 106"/>
        <path d="M114 132 C110 145 105 156 101 166"/>
        <path d="M114 132 C120 145 124 155 127 166"/>
      `)}
      <circle cx="122" cy="53" r="3.4" fill="${P.ink}"/>
    </g>
  </g>`;
}

// ---------------------------------------------------------------
// A-01b — Öpüşen çift. lean: 0..1 yaklaşma miktarı
// ---------------------------------------------------------------
function kissingPair({ lean = 0 } = {}) {
  const d = lean * 3;
  return `<g>
    <g transform="translate(${d},0)">
      ${ink(`
        <path d="M138 56 C138 42 127 32 113 32 C99 32 88 42 88 56 C88 70 99 80 113 80 C127 80 138 70 138 56 Z" fill="#fff"/>
        <path d="M113 80 C114 100 113 118 114 132"/>
        <path d="M113 94 C122 100 130 105 137 106"/>
        <path d="M114 132 C110 145 105 156 101 166"/>
        <path d="M114 132 C120 145 124 155 127 166"/>
        <path d="M139 57 C145 55 152 55 158 57" stroke-width="4"/>
      `)}
      <circle cx="122" cy="53" r="3.4" fill="${P.ink}"/>
    </g>
    <g transform="translate(${-d},0)">
      ${ink(`
        <path d="M182 56 C182 42 193 32 207 32 C221 32 232 42 232 56 C232 70 221 80 207 80 C193 80 182 70 182 56 Z" fill="#fff"/>
        <path d="M207 80 C206 100 207 118 206 132"/>
        <path d="M207 94 C198 100 190 105 183 106"/>
        <path d="M206 132 C210 145 215 156 219 166"/>
        <path d="M206 132 C200 145 196 155 193 166"/>
        <path d="M181 57 C175 55 168 55 162 57" stroke-width="4"/>
      `)}
      <circle cx="198" cy="53" r="3.4" fill="${P.ink}"/>
    </g>
  </g>`;
}

// ---------------------------------------------------------------
// Kalabalık — arka plandaki nötr figürler.
// Merkezdeki çift 88-232 arasını kaplıyor; kalabalık o bandın
// DIŞINDA kalır ve daha küçük çizilir ki ön planla yarışmasın.
// ---------------------------------------------------------------
function crowd({ n = 6 } = {}) {
  // [x, ölçek] — kenarlara doğru küçülür, derinlik hissi
  const spots = [
    [16, 0.46], [46, 0.52], [72, 0.44],
    [248, 0.44], [274, 0.52], [304, 0.46],
  ];
  return spots.slice(0, n).map(([cx, s], i) => {
    // ayaklar 155'teki zemin çizgisine otursun
    const footY = 166 * s;
    const ty = 155 - footY;
    const armX = i % 2 ? 96 : 130;
    return `<g transform="translate(${cx - 113 * s},${ty}) scale(${s})">
      ${ink(`
        <path d="M138 56 C138 42 127 32 113 32 C99 32 88 42 88 56 C88 70 99 80 113 80 C127 80 138 70 138 56 Z" fill="#fff"/>
        <path d="M113 80 C114 98 113 116 114 130"/>
        <path d="M113 96 C${armX} 102 ${armX} 104 ${armX} 108"/>
        <path d="M114 130 C110 144 106 156 103 166"/>
        <path d="M114 130 C119 144 122 156 125 166"/>
      `, 7)}
      <circle cx="105" cy="53" r="4.6" fill="${P.ink}"/>
      <circle cx="121" cy="53" r="4.6" fill="${P.ink}"/>
    </g>`;
  }).join('');
}

// ---------------------------------------------------------------
// A-02 — Öğretmen + boş tahta. x: kırmızı çarpı görünürlüğü
// ---------------------------------------------------------------
function teacherBoard({ cross = false } = {}) {
  return `<g>
    ${ink(`
      <rect x="150" y="34" width="140" height="94" rx="2" fill="#fff"/>
      <path d="M96 62 C96 48 85 38 71 38 C57 38 46 48 46 62 C46 76 57 86 71 86 C85 86 96 76 96 62 Z" fill="#fff"/>
      <path d="M71 86 C72 106 71 124 72 138"/>
      <path d="M71 100 C86 96 102 88 116 78"/>
      <path d="M71 100 C62 108 55 116 50 124"/>
      <path d="M72 138 C68 150 64 160 61 170"/>
      <path d="M72 138 C78 150 82 160 85 170"/>
    `)}
    <circle cx="62" cy="59" r="3.4" fill="${P.ink}"/>
    <circle cx="80" cy="59" r="3.4" fill="${P.ink}"/>
    ${cross ? `<g fill="none" stroke="${P.red}" stroke-width="9" stroke-linecap="round">
      <path d="M166 50 C200 74 232 96 274 112"/>
      <path d="M274 50 C240 74 208 96 166 112"/>
    </g>` : ''}
  </g>`;
}

// ---------------------------------------------------------------
// A-03 — Dünya haritası. dots: 'none' | 'gray' | 'split'
// ---------------------------------------------------------------
const GRAY_DOTS = [[96,62],[112,120],[176,60],[200,70],[176,118],[234,122],[126,76],[150,140]];
const ORANGE_DOTS = [[84,72],[106,56],[164,70],[190,58],[168,106],[184,128],[240,118]];

function worldMap({ dots = 'none', magnifier = false, dim = false } = {}) {
  // Küre gövdesi
  const globe = `<ellipse cx="160" cy="90" rx="118" ry="72" fill="#EAF2F8"/>`;

  // Meridyen + paralel ızgarası — küreyi "dünya" yapan şey bu.
  // Izgara olmadan kıtalar mikroskop altındaki hücre gibi okunuyordu.
  const grid = `<g fill="none" stroke="#A8BFD0" stroke-width="1.6">
    <path d="M42 90 C42 50 90 18 160 18 C230 18 278 50 278 90"/>
    <path d="M42 90 C42 130 90 162 160 162 C230 162 278 130 278 90"/>
    <path d="M56 54 L264 54"/>
    <path d="M42 90 L278 90"/>
    <path d="M56 126 L264 126"/>
    <ellipse cx="160" cy="90" rx="40" ry="72"/>
    <ellipse cx="160" cy="90" rx="80" ry="72"/>
    <path d="M160 18 L160 162"/>
  </g>`;

  // Kıtalar — daha köşeli, tanınabilir siluetler
  const land = `<g stroke="${P.ink}" stroke-width="3.4" stroke-linejoin="round" fill="${P.green}">
    <path d="M72 52 L104 46 L118 58 L112 72 L96 78 L98 92 L86 96 L74 80 L68 64 Z"/>
    <path d="M100 106 L118 104 L124 118 L116 136 L106 144 L100 132 L104 118 Z"/>
    <path d="M150 46 L176 40 L200 46 L208 58 L196 68 L172 72 L154 64 Z"/>
    <path d="M160 78 L184 74 L198 88 L196 112 L182 134 L170 132 L162 110 L156 92 Z"/>
    <path d="M212 62 L246 56 L262 72 L254 86 L232 88 L214 78 Z"/>
    <path d="M228 112 L252 108 L258 122 L246 132 L230 128 Z"/>
  </g>`;

  let d = '';
  if (dots === 'gray' || dots === 'split') {
    d += `<g fill="${P.gray}"${dim ? ' opacity="0.4"' : ''} stroke="#fff" stroke-width="1.2">` +
      GRAY_DOTS.map(([x, y]) => `<circle cx="${x}" cy="${y}" r="4.4"/>`).join('') + '</g>';
    d += `<g fill="${dots === 'split' ? P.orange : P.gray}" stroke="#fff" stroke-width="1.2">` +
      ORANGE_DOTS.map(([x, y]) => `<circle cx="${x}" cy="${y}" r="4.4"/>`).join('') + '</g>';
  }

  const mag = magnifier ? ink(`
      <circle cx="206" cy="64" r="26" fill="none"/>
      <path d="M225 83 C232 91 240 99 246 106" stroke-width="7"/>
    `, 5) : '';

  const rim = `<ellipse cx="160" cy="90" rx="118" ry="72" fill="none"
     stroke="${P.ink}" stroke-width="4.6"/>`;

  return `<g>${globe}${grid}${land}${rim}${d}${mag}</g>`;
}

// ---------------------------------------------------------------
// Tiksinen yüz — yakın plan
// ---------------------------------------------------------------
function disgustFace() {
  return `<g>
    ${ink(`
      <path d="M232 90 C232 52 202 26 160 26 C118 26 88 52 88 90 C88 128 118 154 160 154 C202 154 232 128 232 90 Z" fill="#fff"/>
      <path d="M118 68 C126 60 138 60 146 66"/>
      <path d="M202 68 C194 60 182 60 174 66"/>
      <path d="M132 122 C142 112 178 112 188 122"/>
      <path d="M152 128 C156 138 164 138 168 128"/>
    `)}
    <circle cx="132" cy="86" r="4.2" fill="${P.ink}"/>
    <circle cx="188" cy="86" r="4.2" fill="${P.ink}"/>
  </g>`;
}

// ---------------------------------------------------------------
// Düşünen figür + düşünce balonu.
// Balonun içinde DUDAK değil, minik öpüşen çift var — dudak
// tek başına göz gibi okunuyordu. Figür büyütüldü, balon küçültüldü.
// ---------------------------------------------------------------
function thinkingFigure() {
  // balon içindeki minyatür çift
  const mini = `<g transform="translate(206,52) scale(0.30) translate(-160,-90)">
    ${ink(`
      <path d="M138 56 C138 42 127 32 113 32 C99 32 88 42 88 56 C88 70 99 80 113 80 C127 80 138 70 138 56 Z" fill="#fff"/>
      <path d="M113 80 C114 100 113 118 114 132"/>
      <path d="M114 132 C110 145 105 156 101 166"/>
      <path d="M114 132 C120 145 124 155 127 166"/>
      <path d="M182 56 C182 42 193 32 207 32 C221 32 232 42 232 56 C232 70 221 80 207 80 C193 80 182 70 182 56 Z" fill="#fff"/>
      <path d="M207 80 C206 100 207 118 206 132"/>
      <path d="M206 132 C210 145 215 156 219 166"/>
      <path d="M206 132 C200 145 196 155 193 166"/>
    `, 11)}
    <circle cx="122" cy="53" r="9" fill="${P.ink}"/>
    <circle cx="198" cy="53" r="9" fill="${P.ink}"/>
  </g>`;

  return `<g>
    ${ink(`
      <path d="M126 96 C126 76 110 62 90 62 C70 62 54 76 54 96 C54 116 70 130 90 130 C110 130 126 116 126 96 Z" fill="#fff"/>
      <path d="M90 130 C91 148 90 160 91 172"/>
      <path d="M90 142 C76 150 66 158 60 168"/>
      <path d="M90 142 C104 150 114 158 120 168"/>
      <path d="M156 52 C156 30 178 16 206 16 C236 16 258 30 258 50 C258 70 236 84 206 84 C182 84 164 74 156 62 Z" fill="#fff"/>
      <circle cx="140" cy="88" r="7.5" fill="#fff"/>
      <circle cx="128" cy="102" r="4.6" fill="#fff"/>
    `)}
    <circle cx="78" cy="92" r="4" fill="${P.ink}"/>
    <circle cx="102" cy="92" r="4" fill="${P.ink}"/>
    <path d="M80 112 C86 118 96 118 102 112" fill="none" stroke="${P.ink}"
      stroke-width="4" stroke-linecap="round"/>
    ${mini}
    <text x="240" y="62" font-family="Georgia, serif" font-size="34"
      font-weight="700" fill="${P.red}" text-anchor="middle">?</text>
  </g>`;
}

// ---------------------------------------------------------------
// Terazi — iki kefe, biri yukarı biri aşağı. tip: 'left'|'right'
// Kefe etiketleri opts.left / opts.right (ekranda büyük harf).
// ---------------------------------------------------------------
function scaleAsset({ left = 'INSTINCT', right = '?', tip = 'right' } = {}) {
  // tip = AĞIR (aşağı inen) taraf. Beam o tarafa eğilir.
  const down = tip === 'right' ? 1 : -1;
  // AĞIR taraf AŞAĞI iner (ekranda daha büyük y). Formüller buna göre.
  const beamL = 60 - down * 14;   // tip='left' => sol aşağı
  const beamR = 60 + down * 14;   // tip='right' => sağ aşağı
  const panL = beamL + 34;        // sol kefe (askıdan aşağı)
  const panR = beamR + 34;
  const pan = (cx, cy) =>
    `<path d="M${cx-30} ${cy} C${cx-26} ${cy+18} ${cx+26} ${cy+18} ${cx+30} ${cy}" `
    + `fill="#fff" stroke="${P.ink}" stroke-width="4.6" stroke-linecap="round"/>`;
  const label = (cx, cy, txt, big, red) => txt ?
    `<text x="${cx}" y="${cy}" text-anchor="middle" font-family="'Bradley Hand','Comic Sans MS',cursive" `
    + `font-size="${big ? 30 : 17}" font-weight="700" fill="${red ? P.red : P.ink}" `
    + `paint-order="stroke" stroke="#fff" stroke-width="3">${txt}</text>` : '';
  return `<g>
    ${ink(`
      <path d="M160 34 L160 150"/>
      <path d="M128 156 C144 150 176 150 192 156"/>
      <path d="M72 ${beamL} L248 ${beamR}" stroke-width="5.4"/>
      <path d="M72 ${beamL} L72 ${panL-2}"/>
      <path d="M248 ${beamR} L248 ${panR-2}"/>
    `)}
    ${pan(72, panL)}${pan(248, panR)}
    ${label(72, panL + 34, left, false, false)}
    ${label(248, panR + 34, right, right === '?', right === '?')}
  </g>`;
}

// ---------------------------------------------------------------
// Selam biçimleri sırası — 4 hücre: ağız / burun / alın / yanak.
// İki küçük kafa temas noktasına göre; ağız hücresi turuncu vurgulu
// ("ağız sadece bir seçenek"). highlight: vurgulanacak index (0=ağız).
// ---------------------------------------------------------------
function greetingRow({ highlight = 0 } = {}) {
  const cells = [
    { label: 'MOUTH',    cy: 70, tilt: 0,   mark: 'mouth' },
    { label: 'NOSE',     cy: 70, tilt: 0,   mark: 'nose' },
    { label: 'FOREHEAD', cy: 62, tilt: -10, mark: 'top' },
    { label: 'CHEEK',    cy: 72, tilt: 0,   mark: 'cheek' },
  ];
  const cx = [52, 122, 192, 262];
  return cells.map((c, i) => {
    const x = cx[i], hl = i === highlight;
    const r = 15;
    // iki kafa, temas noktasına göre konumlanır
    const ax = x - 10, bx = x + 10;
    const ay = c.cy + (c.mark === 'top' ? 4 : 0), by = c.cy + (c.mark === 'top' ? 4 : 0);
    let contact = '';
    if (c.mark === 'mouth') contact = `<circle cx="${x}" cy="${c.cy}" r="2.6" fill="${P.red}"/>`;
    if (c.mark === 'nose')  contact = `<path d="M${x-2} ${c.cy-2} L${x} ${c.cy+2} L${x+2} ${c.cy-2}" fill="none" stroke="${P.ink}" stroke-width="2"/>`;
    if (c.mark === 'top')   contact = `<circle cx="${x}" cy="${c.cy-11}" r="2.4" fill="${P.orange}"/>`;
    if (c.mark === 'cheek') contact = `<circle cx="${x+4}" cy="${c.cy+2}" r="2.4" fill="${P.orange}"/>`;
    return `<g>
      ${hl ? `<rect x="${x-30}" y="30" width="60" height="86" rx="6" fill="none" stroke="${P.orange}" stroke-width="3"/>` : ''}
      <circle cx="${ax}" cy="${ay}" r="${r}" fill="#fff" stroke="${P.ink}" stroke-width="4"/>
      <circle cx="${bx}" cy="${by}" r="${r}" fill="#fff" stroke="${P.ink}" stroke-width="4"/>
      ${contact}
      <text x="${x}" y="108" text-anchor="middle" font-family="'Bradley Hand','Comic Sans MS',cursive"
        font-size="12" font-weight="700" fill="${hl ? P.orange : P.ink}">${c.label}</text>
    </g>`;
  }).join('');
}

// ---------------------------------------------------------------
// ZEMİN SİSTEMİ
// Zenn beyaz "diyagram" sahneleriyle tam renkli "dünya" sahnelerini
// dönüşümlü kullanıyor — kabaca %60 beyaz / %40 renkli. Hepsi beyaz
// olunca görsel enerji düzleşiyor.
//
//   white  — diyagram, soyut kanıt, metin kartı, kırmızı X
//   field  — gündüz dış mekan: mavi gök + kahve zemin
//   night  — gece: koyu lacivert + yıldız
//   warm   — duygusal vurgu, tek renk dolgu
// ---------------------------------------------------------------
const STARS = [
  [28, 26], [62, 44], [96, 20], [134, 38], [188, 24],
  [222, 46], [258, 22], [292, 40], [46, 66], [276, 68],
];

function background(kind = 'white') {
  switch (kind) {
    case 'field':
      return `<rect width="320" height="180" fill="${P.navy}"/>` +
             `<rect x="0" y="150" width="320" height="30" fill="${P.brown}"/>`;
    case 'night':
      return `<rect width="320" height="180" fill="#1C2740"/>` +
             `<rect x="0" y="152" width="320" height="28" fill="#3A2A1E"/>` +
             `<g fill="#fff">` +
             STARS.map(([x, y]) => `<circle cx="${x}" cy="${y}" r="1.5"/>`).join('') +
             `</g>`;
    case 'warm':
      return `<rect width="320" height="180" fill="${P.orange}"/>`;
    case 'white':
    default:
      return `<rect width="320" height="180" fill="${P.ground}"/>`;
  }
}

module.exports = {
  P, ink, background,
  figureProfile, kissingPair, crowd, scaleAsset, greetingRow,
  teacherBoard, worldMap, disgustFace, thinkingFigure,
};
