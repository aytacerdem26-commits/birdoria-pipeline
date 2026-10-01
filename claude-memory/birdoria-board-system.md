---
name: birdoria-board-system
description: 9-agent YouTube advisory board system for Birdoria — 3 research + 6 evaluation + chief editor synthesis
metadata: 
  node_type: memory
  type: project
  originSessionId: ccbe3bb4-f4d6-4db9-81fd-173108ea9acc
  modified: 2026-08-01T12:22:58.396Z
---

Birdoria video kararları 9 agentlı kurul sistemiyle alınır.

**Why:** Tek agent = tek bakış açısı = kör nokta. Farklı roller birbirine itiraz ederek kötü kararları engeller. User bu sistemi tasarladı ve onayladı (2026-08-01).

**How to apply:** Her yeni video fikri veya mevcut video değerlendirmesi kurula sunulur. "Kurula soralım" veya "kurulu topla" tetikler.

## Araştırma katmanı (kuruldan ÖNCE çalışır)

7. **Rakip Analizcisi** — rakip kanalları tarar, tutan başlık kalıbı + thumbnail şablonu çıkarır, VPH + breakout proxy karşılaştırma. Soru: "Rakipler ne yapıyor ve hangisi BİZİM kanalda işler?"
8. **Trend Avcısı** — yükselen konular, arama hacmi, mevsimsel trendler, düşük rekabet boşlukları. Her trende atlamaz, kanal uyumunu filtreler. Soru: "Bu konu ŞİMDİ yükseliyor ve Birdoria güvenilir anlatabilir mi?"
9. **Fikir Jeneratörü** — Rakip + Trend verisini birleştirir, Crow kalıbında somut video fikirleri + başlık/thumbnail draft'ı üretir. 3'lü filtreden geçirir. Haftalık 5-10 fikir havuzu.

Akış: Rakip Analizcisi + Trend Avcısı paralel → çıktıları Fikir Jeneratörü'ne → TEKLİF → değerlendirme katmanı.

## Değerlendirme katmanı (teklif gelince 6 agent paralel)

1. **Kanal Stratejisti** — kanal kimliği uyumu, büyüme stratejisi. Soru: "Bu içerik kanalın büyümesine hizmet ediyor mu?"
2. **İzleyici Temsilcisi** — izleyici gözünden, tıklama/sıkılma. İtiraz: "İçerik üreticisi için ilginç ama izleyici için yeterince güçlü değil."
3. **İçerik ve Hikaye Editörü** — senaryo, cold-open, tempo, retention. Sorular: ilk 30sn neden izlenmeli? Ortada neden kalınsın? Sonda ne kazanılır?
4. **Başlık ve Küçük Resim Uzmanı** — paketleme, merak açığı. Editörden BAĞIMSIZ. Soru: "Öneriler arasında neden bunu seçsin?"
5. **Veri Analisti** — CTR, retention, trafik, n güvenilirliği, confound. Sadece "çok izlendi" değil: doğru izleyici mi, tekrarlanır mı, abone kazandırdı mı?
6. **Eleştirel Muhalif** — başarısızlık senaryoları, varsayım sorgusu, fırsat maliyeti. "Başarısız olacağı en olası 3 neden?" + çözüm sunmalı.

## Tartışma protokolü

1. **Araştırma** — Rakip Analizcisi + Trend Avcısı paralel veri toplar
2. **Teklif** — Fikir Jeneratörü veriyi birleştirir, somut fikir + başlık/thumb draft sunar
3. **Bağımsız değerlendirme** — 6 değerlendirici paralel, birbirini görmeden. 7 kriter /10: izleyici ilgisi, kanal uyumu, tıklanabilirlik, izlenme potansiyeli, üretim zorluğu, tekrarlanabilirlik, stratejik katkı
4. **Çapraz sorgu** — agentlar birbirine itiraz
5. **Revizyon** — tartışma sonrası yeniden yazım
6. **Baş Editör sentezi** — uzlaşma noktaları, çözülemeyen ayrılıklar, riskler, varsayımlar, karar

## Karar seçenekleri
- **Üret** — 3/3 filtre güçlü
- **Test et** — 2/3 güçlü, ucuz deney
- **Revize et** — fikir potansiyelli ama eksik
- **Beklet** — zamanlama yanlış
- **Reddet** — 1/3 veya altı

## Ortak veri (her agente verilmeli)
- Son videolar: başlık, view, CTR, retention, breakout
- Crow kalıbı referansı
- Studio gerçek CTR/retention (Chrome MCP ile)
- Kanal DNA tanımı
- Rakip Analizcisi + Trend Avcısı çıktıları (değerlendirme katmanına)

## Teknik uygulama
- Araştırma katmanı: 2 agent paralel spawn (Rakip + Trend) → sonuçlar Fikir Jeneratörü'ne
- Değerlendirme katmanı: 6 agent paralel spawn, her biri kendi rolüyle prompt alır
- Baş Editör sentezi ana thread'de yapılır — ayrı agent değil
