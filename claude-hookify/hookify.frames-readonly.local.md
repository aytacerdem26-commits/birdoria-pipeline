---
name: block-frames-elle-duzenleme
enabled: true
event: file
action: block
conditions:
  - field: file_path
    operator: regex_match
    pattern: out/frames/
---

🚫 **Kareler elle duzenlenmez**

`out/frames/` icerigini `render.sh` uretir. Elle yazmak sessiz tutarsizlik yaratir:
PNG'ler `out/html/` icindeki HTML ile artik eslesmez, ama hicbir sey hata vermez.

Yapilacak dogru sey:
- Kare yanlissa kaynagini duzelt: `timeline.json`, `build.js` ya da sahne gorseli
- Sonra `./render.sh` calistir — kareler bastan uretilir
- `render.sh` zaten `rm -f out/frames/*.png` ile temizlik yapiyor
