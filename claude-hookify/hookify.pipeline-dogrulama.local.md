---
name: warn-hat-dogrulamasi
enabled: true
event: file
action: warn
conditions:
  - field: file_path
    operator: regex_match
    pattern: (render\.sh|build\.js|check-frames\.py|timeline.*\.json)$
---

⚠️ **Render hattina dokunuluyor — dogrulamayi atlama**

Bu dosya kare uretimini etkiliyor. Degisiklikten sonra:

```
cd ~/zenn && python3 check-frames.py out/frames
```

Neden onemli: 2026-07-25'te `f014.png` tamamen beyaz (tek renk) olarak videoya
sizmisti ve kimse fark etmemisti, cunku `render.sh` Chrome'un tum cikisini
`>/dev/null 2>&1` ile yutuyordu. Artik `out/render.log`'a yaziliyor ve
`check-frames.py` bos kareyi hata sayiyor — ama sadece calistirilirsa.

Kontrol listesi:
- Bos kare = HATA (kasitliysa `ALLOW_BLANK=1`)
- Yinelenen kare = UYARI (sahne tutmak kasitli olabilir)
- ffmpeg 3 denemede de coktuyse artik durur, sessizce eski video'yu kullanmaz
