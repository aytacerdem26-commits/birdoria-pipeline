---
name: wildlife-rescue-shorts-channel
description: "Yeni AI shorts kanalı — Mundos Salvajes formatının İngilizce klonu, otomatik üretim hedefi"
metadata: 
  node_type: memory
  type: project
  originSessionId: de2b7da6-b0c5-432c-a045-66a5978d4013
  modified: 2026-09-06T20:32:18.761Z
---

Kullanıcı 2026-09-03'te yeni bir YouTube Shorts kanalı kurmaya karar verdi: **Mundos Salvajes** (@mundossalvajes, İspanyolca, 1.15M abone, 734M view, breakout) formatının **İngilizce klonu**. Hedef: videoları otomatik/tekrarlanabilir pipeline ile üretmek (Birdoria'nın 8dk uzun format pipeline'ından ayrı — bu tamamen farklı bir format).

## Kaynak kanal format analizi (competitor-format-analyzer ile yapıldı)
- **%100 Shorts, ~60 saniye**, tek sahne AI-generated
- Format: first-person POV "rescue" mini-drama — anlatıcı (yüzü net görünmeyen "ben" karakteri) egzotik/yavru hayvan kurtarıyor veya onunla bağ kuruyor
- Hayvan çeşitliliği çok geniş (kutup ayısı, kar leoparı, vaşak, kurt, albino puma, kartal, baykuş, rakun, panda kırmızısı vb.) — gerçek çekim OLAMAZ, tutarlı karakter + değişen hayvan = AI image/video generation
- Diyalog minimal (3-6 kısa cümle), çoğu sahne sadece müzik/atmosfer
- Başlık kalıbı (İspanyolca orijinal): "Rescaté a Este/Esta [bebek hayvan] y Esto Pasó", "Salvé a Esta [hayvan] y Esto Pasó/Me Dio Un Regalo", "Adopté a Este [hayvan]", "Este [hayvan] Me Pidió Ayuda", "Este [hayvan] Salvó a Su Cría" (rol tersi)
- Yapı: Hook (0-3sn tehlike/keşif) → Rescue act (3-15sn sessiz aksiyon) → Bond montaj (15-45sn müzik ağırlıklı) → Kapanış (45-60sn duygusal cümle + açık uçlu CTA)

## Karar
Kullanıcı üç seçenekten (yeni kanal+İngilizce, yeni kanal+İspanyolca, Birdoria'ya entegre) **"yeni kanal, İngilizce klon"**u seçti.

**Why:** Kaynak kanal İspanyolca pazarda çalışıyor; İngilizce klon farklı/daha büyük pazara (US/global) hitap eder, Birdoria'nın mevcut uzun-format DNA'sını bozmadan ayrı bir ürün olur.

**How to apply:** Bundan sonraki oturumlarda bu kanal için: kanal adı, marka kimliği, karakter tasarımı (tutarlı "rescuer" POV karakter), VO sesi (İngilizce, muhtemelen Nathaniel C değil — farklı ton gerekebilir, henüz karar verilmedi), ilk pilot video üretimi gündemde olacak. Henüz kanal adı/branding/VO sesi kullanıcıyla netleşmedi — bu detaylar sorulmalı, varsayılmamalı.

### Netleşen kararlar (2026-09-03)
- **Kanal adı: Wild Rescue Diaries**
- **Karakter tasarımı: yüz görünmez** — POV eller/sırt açısı, orijinal Mundos Salvajes kanalıyla aynı yaklaşım. Neden: karakter tutarlılığı çok daha kolay (yüz çizim hatası/drift riski yok), her videoda AI generation tutarlılığı garanti edilir.
- **VO sesi: Harry – Gentle, Soft-Spoken and Caring** (genaipro Labs voice_id: `SMmCzq0obKgqq4BpVwlt`, model_id: `eleven_turbo_v2_5`, stability 0.7, similarity 0.8, style 0.3, speed 0.95). Neden: conversational/caring ton, rescue bonding sahnelerine Rowan'dan (alternatif, narrative_story) daha yakın.
- Yayın sıklığı henüz karara bağlanmadı.
- Pilot video 1: kutup ayısı yavrusu, başlık "I Rescued This Baby Polar Bear and This Happened", 4 replikli minimal script, VO üretildi ve onaylandı (bkz. scratchpad/wild_rescue_diaries/pilot_vo_preview.mp3 — final deliverable değil, session-scratch).

## Referans örnek: flood-rescue overlay formatı (2026-09-06)
İncelenen örnek: https://youtube.com/shorts/bPputVQ_a7U (Mr, slah) — AI-generated 10sn klip, dalgıç POV'dan sel suyundan sincap kurtarma, "You might save a life with a smile or a helping hand" overlay metni + reposter'ın küçük yuvarlak profil fotoğrafı köşede. AI tespiti: el/parmak deformasyonu, sincap kuyruğu kare-kare tutarsız, arka plan direkleri kamera hareketine rağmen paralaks göstermiyor, dalgıç maskesi yansıması statik.

**Karar:** Bu formatın overlay/sunum taktiği referans alınacak ama **süre 10sn'de tutulmayacak** — Wild Rescue Diaries kendi 60sn hedef süresini korur (Mundos Salvajes kalıbıyla uyumlu).

**Why:** 10sn format tek-an şok değeri üzerine kurulu (hızlı geçiş, tekrar izlemeye zorlar); 60sn format ise hook→rescue→bond→kapanış yapısıyla duygusal yatırım ve retention'a izin veriyor — kanal DNA'sı (bond/duygusal kapanış) kısa formatta kaybolur.

**How to apply:** Overlay stratejisinden (küçük profil foto + tek satır slogan metin) ilham alınabilir ama klip süresi kısaltma yönünde bir emsal olarak KULLANILMAYACAK.

## Teknik pipeline notu
Nim MCP (character-consistency, image/video generation) şu an bu oturumda **yetkilendirilmemiş** (auth gerekiyor). Mevcut alternatif: genaipro Veo (frames-to-video), GPT Image 2, Topview generation tool'ları — [[birdoria-board-system]] pipeline'ındaki genaipro/TTS altyapısı bu kanal için de kullanılabilir ama karakter tutarlılığı stratejisi (ingredients-to-video / master-still grup mantığı, bkz. ai-sinematik-film skill) ayrıca kurulmalı.
