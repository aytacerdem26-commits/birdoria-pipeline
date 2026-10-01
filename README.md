# zenn — faceless açıklayıcı video boru hattı

Zenn (`@Zenn0009`) kanalının biçimi çözümlenerek çıkarılan üretim hattı.
Anlatım metninden başlayıp MP4'e kadar otomatik.

## Çalıştırma

```bash
node build.js     # timeline.json -> HTML kareler + süreler
./render.sh       # HTML -> PNG (Chrome) -> MP4 (ffmpeg)
```

`render.sh` zaten `build.js`'i çağırıyor, tek komut yeterli.

## Dosyalar

| Dosya | İş |
|---|---|
| `timeline.json` | Anlatım satırları + her satıra bağlı görsel vuruşlar. **Tek düzenlenecek dosya.** |
| `assets.js` | SVG varlık kütüphanesi. Her varlık bir fonksiyon, 320×180 sahne uzayında. |
| `timing.js` | Süre çözücü. `vo/` içinde MP3 varsa ölçer, yoksa kelime sayısından tahmin eder. |
| `build.js` | Sahneleri HTML'e çevirir, concat listesi ve VO manifest'i üretir. |
| `render.sh` | Chrome headless ile ekran görüntüsü, ffmpeg ile birleştirme, ses mux. |
| `pace.sh` | Brian sesini Zenn temposuna getirir (kırpma + hızlandırma + normalize). |

## Ses akışı (forced alignment ile — kusursuz senkron)

1. `node build.js` → `out/hook-script.txt` / satır metinleri
2. Tüm hook'u **tek çağrıda** Brian (`nPczCjzI2devNBz1zQrb`) ile üret (vidiq voiceover, ~14 kredi),
   `vo/hook-full.mp3` olarak kaydet. (Tek çağrı ucuz; 15 ayrı çağrı 15× yuvarlanır.)
3. **Forced alignment** — sesi 15 satıra kelime düzeyinde hizala ve tam sınırlardan böl:
   ```bash
   ./.venv/bin/python align.py
   ```
   stable-ts (`base` model) sesin İÇİNE bakıp her satırın gerçek [başlangıç,bitiş]'ini bulur.
   Kelime-oranı tahmininin aksine kaymaz — "Fewer than half" gerçekte 0.70s, tahmin 1.17s'di.
4. `./render.sh` → parçalar ölçülür (`OLCULDU`), görsel süreleri sese kilitlenir, ses bindirilir.

`align.py` çıktısı: `vo/L01.mp3..L15.mp3` (bitişik, çakışmasız, toplam = tam ses) +
`out/line-timings.json`. venv: `~/zenn/.venv` (stable-ts + torch, 877M).

Eski yöntem (`pace.sh` + kelime-oranı bölme) hâlâ duruyor ama forced alignment onun yerini aldı.

## Ölçülmüş sabitler

Bunlar tahmin değil, gerçek dosyalardan ölçüldü.

| Değer | Ölçüm | Kaynak |
|---|---|---|
| Brian brüt tempo | 143,2 kelime/dk | 12 MP3, 1588 kelime, 665 sn |
| Brian sessizlik oranı | %17,8 | `silencedetect` |
| Brian artikülasyon | 174 kelime/dk | sessizlik hariç |
| Zenn hedef tempo | ~205 kelime/dk | gece videosu hook'u, 131 kelime / 38,5 sn — **tek örnek, ±%10 pay bırak** |
| `pace.sh` sonrası | ~202 kelime/dk | kırpma + 1,06× |

Kaynak ses dosyaları: `~/Desktop/youutube ar/body-channel/video-01-hormones/vo/`

## Zenn'in kesme temposu

`ffmpeg silencedetect` ile ölçüldü:

| Video | Süre | Kesme | sn/plan |
|---|---|---|---|
| Ancient Humans at Night | 511s | 174 | 2,9 |
| The Calhoun Effect | 512s | 172 | 2,9 |
| The Bliss Point | 482s | 219 | 2,2 |
| Why Don't Dragons Exist | 511s | 210 | 2,4 |

Hedef: **2,2-2,9 saniye/plan.**

## Zemin sistemi

Her satıra `timeline.json` içinde bir `bg` alanı: `white` (diyagram/kanıt/metin),
`field` (gündüz dış mekan: mavi gök + kahve zemin), `night` (lacivert + yıldız),
`warm` (turuncu tek renk vurgu). `background()` fonksiyonu `assets.js`'te.
Renkli zeminde ekran yazısı otomatik beyaza döner. Hedef dağılım ~%60 beyaz / %40 renkli.

## Bilinen sorunlar

- **`thinkingFigure` balonundaki minik çift zayıf.** İki kafa öpüşme teması olmadan
  yan yana; gözler kafaya oranla büyük. Figürün yüzü de gülümsüyor — merak eden bir
  ifade daha doğru olur. İkisi de küçük.
- **ffmpeg ara sıra zaman aşımı veriyor.** Desktop iCloud senkronu kaynaklıydı;
  `~/zenn` altında görülmedi ama `render.sh` içinde 3 deneme hakkı duruyor.

## Çözülmüş

- ~~Fazla beyaz~~ → zemin sistemi eklendi (yukarı bak).
- ~~`crowd` figürleri üst üste biniyor~~ → kenarlara itildi, küçültüldü, zemine oturtuldu.
- ~~`worldMap` kıtalar hücre gibi~~ → meridyen/paralel ızgarası + köşeli kıta siluetleri.
- ~~`secPerWord` 0,419~~ → 0,297 (pace.sh sonrası tempo).

## Gereksinimler

Kurulum yok — hepsi sistemde mevcut:
- Google Chrome (headless render)
- ffmpeg / ffprobe
- node

`cairosvg` kurulu ama `libcairo` eksik olduğu için kullanılmıyor.
