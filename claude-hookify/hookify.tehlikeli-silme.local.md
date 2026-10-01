---
name: block-tehlikeli-silme
enabled: true
event: bash
pattern: rm\s+(-[a-zA-Z]*[rR]|--recursive)|\bdd\s+if=|\bmkfs\b
action: block
---

🛑 **Ozyinelemeli silme engellendi**

Bu makinede ozel risk var: proje `~/Desktop` altinda ve **iCloud senkronu**
aktif. Yanlis silme yerelde bitmez, buluttaki kopyaya da gider.

Silinmesi pahaliya gelen seyler:
- `~/zenn/vo/`, `~/zenn/vo-act1/` — uretilmis ElevenLabs seslendirmesi
- `~/zenn/assets/` — fal.ai ile uretilmis gorseller (her biri ucretli)
- `kanal_muhru_E.png` — kanal imzasi
- `~/.hermes/.env`, `auth.json`, `youtube_token.json` — kimlik bilgileri

Onun yerine:
- Tek dosya: `rm dosya` (bayraksiz)
- Kareler: `render.sh` zaten `rm -f out/frames/*.png` yapiyor, elle gerekmez
- Klasor gercekten gidecekse sen kendi terminalinde calistir — bilerek yapilmis olsun

Not: `rm -f` (ozyinelemesiz) bu kurala takilmaz, `render.sh` calismaya devam eder.
