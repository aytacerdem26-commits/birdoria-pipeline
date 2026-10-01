# Birdoria — YouTube Faceless Bird Channel

## Kanal bilgileri
- Kanal: **Birdoria** (@Birdoria)
- Channel ID: `UCWdXE1dzN3Kkc1lk38V2atw`
- Hedef kitle: **US**, İngilizce, backyard birding meraklıları
- Niş: kuşların gizli davranışları, kişisel ilişki kuran anlatı
- Abone: erken aşama (< 100)
- Görsel stil: **flat graphic-novel comic** (watercolor reddedildi)
- VO sesi: **Nathaniel C - Documentary Narrator** (voice_id: z7i51AlFqQJ8JzM16o7e, speed 0.95)

## Rakip analiz yöntemi
- Rakip video: `watch` skill ile frame extraction + Groq Whisper transkripsiyon
- ffmpeg scene detection: `select='gt(scene,0.25)'` — rakip ~11 cuts/min
- Analiz çıktısı: görsel stil, cut rhythm, ses vurgu/tempo, emphasis pattern

## Kazanan formül (Crow kalıbı)
En iyi video: "The Crow in Your Yard Has Been Watching You for Years" (86 view, breakout 5.06)
- Başlık: **tehdit + kişisel ("SENİ") + merak açığı** (cevap başlıkta sızdırılmaz)
- Thumbnail: kuş gözü direkt kameraya, koyu zemin, **max 3 kelime** metin
- Script: 2. şahıs komut açılış, open loop, numbered beats, multi-species, duygusal 3-beat kapanış, yorum CTA
- Cold-open: ilk 8 sn TEHDİT + KİŞİSEL çarpması

## İçerik kuralları
- Başlıkta merak açığı zorunlu — cevap sezilmemeli
- Thumbnail metin max 3 kelime, okunabilir font, karanlık ton
- Video hedef 6-7 dk (10+ dk retention'ı kesiyor)
- Görsellere baked-text YOK (istatistik/etiket = editör overlay)
- İlk 30 sn'de net vaat + geciktirilecek cevap
- Cold-open: soru/tehdit, belgesel ısınması YOK

## Kurul sistemi (9 agent + Baş Editör)

### Araştırma katmanı (kuruldan ÖNCE çalışır)
7. **Rakip Analizcisi** — rakip kanalları tarar, tutan başlık kalıbı/thumbnail şablonu çıkarır, VPH+breakout proxy. "Rakipler ne yapıyor ve hangisi BİZİM kanalda işler?"
8. **Trend Avcısı** — yükselen konular, arama hacmi, mevsimsel trendler, düşük rekabet boşlukları. Her trende atlamaz, kanal uyumunu filtreler. "Bu konu ŞİMDİ yükseliyor ve Birdoria güvenilir anlatabilir mi?"
9. **Fikir Jeneratörü** — Rakip + Trend verisini birleştirir, Crow kalıbında somut video fikirleri + başlık/thumbnail draft'ı üretir. 3'lü filtreden geçirir. Haftalık 5-10 fikir havuzu.

Akış: Rakip Analizcisi + Trend Avcısı paralel çalışır → çıktıları Fikir Jeneratörü'ne → Fikir Jeneratörü TEKLİF sunar → mevcut 6 üye değerlendirir.

### Değerlendirme katmanı (teklif gelince paralel çalışır)
1. **Kanal Stratejisti** — kanal kimliği uyumu, kısa/orta/uzun vade
2. **İzleyici Temsilcisi** — izleyici gözü, tıklama motivasyonu, sıkılma noktaları
3. **İçerik ve Hikâye Editörü** — senaryo, cold-open, tempo, retention yapısı
4. **Başlık ve Küçük Resim Uzmanı** — paketleme, merak açığı, başlık+thumbnail uyumu
5. **Veri Analisti** — CTR, retention, trafik kaynağı, n güvenilirliği, confound tespiti
6. **Eleştirel Muhalif** — başarısızlık senaryoları, varsayım sorgusu, fırsat maliyeti

### Tartışma düzeni
1. **Araştırma** — Rakip Analizcisi + Trend Avcısı paralel veri toplar
2. **Teklif** — Fikir Jeneratörü veriyi birleştirir, somut fikir + başlık/thumb draft sunar
3. **Bağımsız değerlendirme** — 6 değerlendirici paralel, birbirini görmeden, 7 kriter /10
4. **Çapraz sorgu** — agentlar birbirine itiraz
5. **Revizyon** — tartışmadan sonra yeniden yaz
6. **Baş Editör sentezi** — uzlaşma, ayrılık, risk, karar: Üret / Test / Revize / Beklet / Reddet

### Agentlara verilecek ortak veri
- Son 8 video: başlık, view, CTR, retention, breakout
- Crow kalıbı referansı
- Studio'dan gerçek CTR/retention (varsa)
- Kanal DNA tanımı
- Rakip Analizcisi + Trend Avcısı çıktıları (değerlendirme katmanına)

## Üretim pipeline

### Video yapısı (2 katman)
- **İlk ~90 sn = animasyonlu açılış** — 8-10 kısa video klip (image-to-video), hızlı kesim, cold-open hook'u taşır
  - Üretim: genaipro Veo (`/v2/veo/frames-to-video`) veya Nim LTX-2 Fast
  - Kaynak: flat-comic görselden cinemagraph/subtle motion (kanat çırpma, buhar, göz kırpma)
  - Seedance Fast v1 BAŞARISIZ (3x denendi) — kullanma
- **90 sn sonrası = sabit görseller + Ken Burns** — gövde anlatı, bilgi aktarımı
  - Geçiş keskin değil, son animasyon klipten ilk Ken Burns'e yumuşak bağlanır

### Görsel üretim
- Model: **GPT Image 2** (Nim MCP, model_id: 445ae371-607e-4e0c-b307-2115f5bcd4d2, 2 credit)
- GPT Image Low (`ccc4d808...`) KULLANMA — kalite düşük, stil kayıyor
- Stil prompt: "flat graphic-novel comic illustration, bold outlines, muted earth tones with accent color pops, no text, no watermark"
- Referans: 3 onaylı flat-comic screenshot mevcut
- Hedef yoğunluk: ~5.5 sn/görsel (8 dk video = ~87 görsel moment)

### Ken Burns (ffmpeg)
```bash
ffmpeg -loop 1 -i img.png -t 7 -r 30 \
  -vf "scale=5760:-2,zoompan=z='...':x='...':y='...':d=210:s=1920x1080:fps=30,setsar=1,format=yuv420p" \
  -c:v libx264 -pix_fmt yuv420p clip.mp4
```
4 motion preset (zoom-in, zoom-out, pan-left, pan-right) index%4 ile dön.

### Infografik reveal (geq alpha sweep)
```bash
[0:v]scale=1920:1080...,split[b][t];
[b]eq=brightness=-0.6:saturation=0.2[dd];
[t]format=rgba,geq=r='r(X,Y)':g='g(X,Y)':b='b(X,Y)':a='255*clip((W*min(1,T/3.5)-X)/50,0,1)'[r];
[dd][r]overlay=0:0
```

### VO / TTS
- Provider: **genaipro** (base: https://genaipro.io/api)
- API key env: `GENAIPRO_API_KEY` (~/.config/birdoria/.env)
- Endpoint: `POST /v1/labs/task`
- Docs: https://docs.genaipro.io/ (OpenAPI: /openapi.yaml)
- Request body fields (flat, nested `voice_settings` KULLANMA):
  - `input`: metin (eski `text` YANLIŞ)
  - `model_id`: `eleven_turbo_v2_5` | `eleven_multilingual_v2` | `eleven_flash_v2_5` | `eleven_v3` (eski `model` YANLIŞ)
  - `voice_id`: `z7i51AlFqQJ8JzM16o7e` (Nathaniel C)
  - `stability`: 0.7
  - `similarity`: 0.8 (eski `similarity_boost` YANLIŞ)
  - `style`: 0.3
  - `speed`: 0.95
- Sonuç poll: `GET /v1/labs/task/{task_id}` — anahtar `task_id`, sonuç `result` (MP3 URL)
- Char limit yok (6600+ char tek seferde kabul edildi)
- Cloudflare bloğu: urllib yerine **curl** kullan

### Whisper transkripsiyon
- Provider: **Groq** (whisper-large-v3)
- API key env: `GROQ_API_KEY` (~/.config/watch/.env)
- Params: verbose_json, timestamp_granularities: word+segment
- Kullanım: VO timecode çıkarma, beat senkron

### Video (genaipro Veo)
- Endpoint: `POST /v2/veo/frames-to-video`
- Quota ayrı (100 başlangıç)

### Slow-down (pitch-preserved)
```bash
[0:v]setpts=PTS/0.9[v];[0:a]atempo=0.9[a]
```

## Thumbnail üretim
- vidIQ `generate_thumbnail` kullan
- Photoreal stil (video içi flat-comic'ten FARKLI — kasıtlı)
- vidIQ thumbnail SKOR motoru GÜVENİLMEZ (gerçek 1.4% CTR'lı thumba 95/100 verdi)
- Gerçek CTR: sadece YouTube Studio'dan oku (Chrome MCP ile)

## Yayın stratejisi
- Yayın sıklığı: 2 günde 1 (genç kanal momentum gerek, ama kalite düşerse azalt)
- Yükleme zamanı: TR 21:30, yayına alma 22:30 (US prime time hedefi)
- YouTube açıklama: chapters (timecode'lu), tag listesi, açıklama v3 script'e uyumlu
- Test & Compare: her videoya 3 thumbnail varyantı, 7 gün süre ver

## Beat-görsel senkron
- Whisper'dan beat başlangıç zamanları çıkar (vo2_whisper.json)
- Her beat'e doğru görsel atanır (override map ile düzeltme yapıldı)
- setpts ile klip süresi VO beat süresine stretch edilir
- concat demuxer ile sıralı birleştirme
- Beat-görsel uyumsuzluğu kontrol: "beat de yanlış görsel var mı" sorgusu

## Açıklama + SEO formatı
- Başlık A/B: ana başlık + alternatif (Test & Compare)
- Açıklama: hook cümle + chapters (timecode'lu) + CTA + hashtag
- Tags: vidIQ keyword_research'ten yüksek hacim/düşük rekabet
- End screen: abone + sonraki video

## Önemli dersler
- vidIQ analytics: kanal sahipliği gerektirir, başkasının kanalı reddedilir
- `crop` w/h'de `t` kullanılamaz (ffmpeg "t not defined at init") — setpts + geq kullan
- Seedance Fast v1 image-to-video: 3x başarısız oldu, LTX-2 Fast veya genaipro Veo kullan
- fileInputs static.nim.video URL'leri fal-backed modellerde BAŞARISIZ — önce media_upload yap
- genaipro poll: anahtar `task_id` (labs/nova), `id` değil; sonuç `result` URL veya `file_urls` array
- Scratchpad dosyaları session ortasında temizlenebilir — final deliverable'ları ~/Downloads'a kopyala

## Dosya konumları
- Deliverables: `~/Downloads/Birdoria_Hummingbird/`
- Script: `hb_script.txt` (v3, 7123 char)
- Asset manifest: `birdoria-hummingbird-assets.md` (46 image ID mapping)
- Edit sheet: `edit_sheet.md` (beat-timecode-clip mapping)
- VO transcript: `vo2_whisper.json` (Nathaniel, 524s, 114 segment)

## Kurulu skills
- **faceless-explainer** — script'ten faceless explainer video, sahne bazlı overlay. Tetik: `/faceless-explainer`
- **motion-graphics** — kinetic text, stat count-up, chart animasyon, lower-third. Tetik: `/motion-graphics`
- **beat-sync-video-editing** — Whisper timecode + beat senkronlu kesim, EditPlan format
- **video-editing** — ffmpeg/Remotion/ElevenLabs/fal.ai pipeline
- **youtube-seo** — başlık/açıklama/tag/thumbnail SEO optimizasyonu
- **captions-overlay** — drop/rail/embed altyazı modeli
- **watch** — video izleme, frame extraction, transkripsiyon

## Altyazı / Overlay sistemi
- Skill: `captions-overlay` (global skill, ~/.claude/skills/captions-overlay/)
- 3 katman modeli: **drop** (filler, gösterme) / **rail** (varsayılan alt yazı, ön katman) / **embed** (nadir doruk, öznenin arkasında)
- Rail = verbatim lower-third, her zaman okunabilir
- Embed = kıt, beat başı max 1, ardışık/aynı anda 2 embed YASAK, en az 1 beat ara
- Overlay yasası: altyazı İÇERİĞİN ÜSTÜNE bindirme — alt band ayırma, içeriği yukarı kaydırma YOK
- Kompozisyon gerçek dikey merkeze hizalı (y = H/2), full-bleed serbest
- Alt ~80px merkez alanında kritik küçük metin (URL, legal) koymaktan kaçın

## Nihai karar kuralı (3'lü filtre)
Her video fikri 3 koşulda değerlendirilir:
1. **İzleyici bunu istiyor mu?**
2. **Kanal bunu güvenilir biçimde sunabilir mi?**
3. **Bu içerik kanalın geleceğini güçlendiriyor mu?**
- 1/3 güçlü = yanıltıcı, reddet
- 2/3 güçlü = test edilmeye değer
- 3/3 güçlü = üretim önceliği

## Script yazım kuralları
- Sayılar yazıyla ("four point two percent", "seven fifteen")
- Dil: İngilizce (US kitle)
- Yapı: 2. şahıs komut açılış, open loop, numbered beats, multi-species, duygusal 3-beat kapanış, yorum CTA

## MCP araçları referans
- **vidIQ** (fab77e79): keyword_research, score_title, generate_thumbnail, channel_videos, channel_stats, channel_analytics, voiceover_generate/list_voices, outliers, similar_thumbnails, video_transcript/comments, job_poll
- **Nim** (ca73b40e): generate_image, generate_video, media_upload, get_generation_status, models_explore (~6389 credit). OAuth connector — kopuksa claude.ai connector settings'den yeniden authorize et
- **genaipro**: REST API (curl), TTS labs + Veo video
- **Chrome** (claude-in-chrome): YouTube Studio erişimi, gerçek CTR/retention okuma
- **Groq**: Whisper transkripsiyon (watch skill entegre)

## Kırmızı çizgiler
- Clickbait-yalan YASAK — başlık vaadi video içeriğinde karşılanmalı
- Watercolor stil YASAK (user rejected)
- 10+ dk video: retention kanıtlanmadan yapma
- Ölü videoyu kurtarmaya batık maliyet harcama — 7 gün ver, toparlamazsa bırak
