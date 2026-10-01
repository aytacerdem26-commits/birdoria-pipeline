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

### Adım sırası (zorunlu)
1. Kurul onayı (fikir + başlık/thumb)
2. Script yazımı (beat yapısı)
3. VO üretimi + Whisper timecodes
4. **faceless-explainer** — script'ten sahne listesi + overlay plan (görsel üretimden ÖNCE çalışmalı, beat başına ne lazım belirler)
5. Görsel üretim (Nim GPT Image 2)
6. Veo animasyon (ilk 90 sn) + Ken Burns (geri kalan)
7. Beat-sync montaj (concat demuxer)
8. **captions-overlay** — montaj BİTTİKTEN SONRA, altyazı montajın üstüne biner
9. Müzik + ducking + loudness normalizasyon
10. QA kontrol (siyah kare, A/V sync, caption taşması)
11. Thumbnail üretimi + Test & Compare varyantları
12. Yükleme + YouTube metadata

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
- **zoompan süresini doğrudan hedef beat süresine ayarla** (`d = beat_süresi × fps`). Önce sabit süre üretip sonra setpts ile esnetme — zoompan takılır, kalite düşer.
- Titreme önleme: önce büyük ölçek (`scale=8000:-1`), sonra zoompan uygula.

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
- **Bilinen sorun:** Whisper ASR yanlış duyduğu kelimelerle beat eşlemesi kayabilir. Script metni zaten biliniyor — ideal çözüm:
  1. genaipro/ElevenLabs `with-timestamps` karakter hizalama (varsa Whisper'a gerek kalmaz)
  2. Yoksa forced alignment (`whisperx` veya `aeneas`) ile script metnine hizala
  3. Son çare: ham Whisper + `difflib` kelime eşleme

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
- **DİKKAT:** Test & Compare kazananı CTR'a göre DEĞİL, **watch time share**'e göre seçer. Değerlendirmede bunu kullan.

## Beat-görsel senkron
- Whisper'dan beat başlangıç zamanları çıkar (vo2_whisper.json)
- Her beat'e doğru görsel atanır (override map ile düzeltme yapıldı)
- **Ken Burns klipleri:** zoompan'ı doğrudan beat süresine üret (setpts esnetme KULLANMA)
- **Veo klipleri:** 1.3x'ten fazla yavaşlatma yapma (slow-mo görünür). Uzun beat'te kırp veya 2 klibe böl.
- **concat öncesi klip normalizasyonu ZORUNLU:** Veo + ffmpeg çıktıları farklı fps/çözünürlük/pix_fmt/SAR taşır.
  Her klibi birleştirmeden önce tek formata çevir:
  ```bash
  ffmpeg -i clip.mp4 -vf "scale=1920:1080:force_original_aspect_ratio=decrease,pad=1920:1080:(ow-iw)/2:(oh-ih)/2,fps=30,setsar=1,format=yuv420p" -c:v libx264 -an normalized_clip.mp4
  ```
- Sesi videodan ayrı tut, en sonda VO'yu tek parça olarak ekle
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

## YouTube AI politika uyumu
- Yüklemede **"altered/synthetic content" beyanı** zorunlu (Temmuz 2025 kuralı)
- Script'te özgün editoryal katkı: kaynak göster, yorum kat, saf şablon tekrarı yapma
- Videolar arası açılış kalıbı ve görsel stilde küçük varyasyonlar koy (mass-produced algısını kır)
- Faceless + AI ses + AI görsel = YouTube "inauthentic content" hedefinde. Editoryal derinlik tek savunma.

## Post-prodüksiyon kontrol listesi
- **Müzik + ducking:** BGM ekle, VO konuşurken `sidechaincompress` veya `-af "volume=0.15"` ile kıs
- **Loudness:** YouTube hedef **−14 LUFS**. `ffmpeg -af loudnorm=I=-14:TP=-1.5:LRA=11`
- **QA kontrol:** siyah kare, ses-görüntü kayması, altyazı taşması, concat bozulması
- **Retention geri besleme:** yayınlanan videonun retention grafiğinde düşüş noktaları → sonraki script'e not olarak geri dönsün (şu an döngü sadece thumbnail'de var)

## Maliyet optimizasyonu
- 87 görsel × 2 credit = video başına ~174 Nim credit
- **Görsel cache:** tekrar eden sahne/karakter/mekan görselleri yeniden üretme, cache'ten çek
- **Veo stil kayması:** flat-comic'ten I2V foto-gerçekçiliğe kayabilir. Prompt'a stil kilidi koy, ilk 2-3 klibi kontrol et.

## Orkestrasyon (TODO)
- Tek `manifest.json`: beat → prompt → görsel_id → klip_path → durum (pending/done/failed)
- Kaldığı yerden devam edebilen orkestratör script (Nim batch hatası vb. durumda baştan başlama yok)
- Maliyet takibi aynı manifest'e eklenebilir

## Kırmızı çizgiler
- Clickbait-yalan YASAK — başlık vaadi video içeriğinde karşılanmalı
- Watercolor stil YASAK (user rejected)
- 10+ dk video: retention kanıtlanmadan yapma
- Ölü videoyu kurtarmaya batık maliyet harcama — 7 gün ver, toparlamazsa bırak
