#!/usr/bin/env python3
"""
Forced alignment: hook-full.mp3'u timeline.json'daki 15 satira kelime
duzeyinde hizalar, her satirin gercek [baslangic, bitis] suresini bulur,
sesi tam o sinirlardan 15 parcaya boler.

Kullanim:  ~/zenn/.venv/bin/python align.py
Sonra:     ./render.sh   (parcalar olculur, kusursuz senkron)
"""
import json, re, subprocess, sys, os

ROOT = os.path.dirname(os.path.abspath(__file__))
TL_FILE = os.environ.get('TL', 'timeline.json')
AUDIO = os.environ.get('AUDIO', os.path.join(ROOT, 'vo', 'hook-full.mp3'))
MODEL = os.environ.get('ALIGN_MODEL', 'base')  # base yeterli; small daha isabetli

def norm(w):
    return re.sub(r"[^a-z0-9']", '', w.lower())

def main():
    import stable_whisper
    tl = json.load(open(os.path.join(ROOT, TL_FILE)))
    lines = tl['lines']
    full = ' '.join(L['text'] for L in lines)

    print(f"[1/4] model yukleniyor: {MODEL}")
    model = stable_whisper.load_model(MODEL)

    print(f"[2/4] hizalama: {AUDIO}")
    result = model.align(AUDIO, full, language='en')

    # tum kelimeleri duz listeye al
    words = []
    for seg in result.segments:
        for w in seg.words:
            t = norm(w.word)
            if t:
                words.append((t, w.start, w.end))
    print(f"       {len(words)} kelime hizalandi")

    # her satirin kelimelerini sirayla tuket
    print("[3/4] satir sinirlari:")
    bounds = []
    wi = 0
    for L in lines:
        toks = [norm(t) for t in re.findall(r"[A-Za-z0-9']+", L['text'])]
        toks = [t for t in toks if t]
        start = words[wi][1] if wi < len(words) else None
        # bu satirin kelime sayisi kadar ilerle (kaba ama saglam eslesme)
        end_i = min(wi + len(toks), len(words))
        end = words[end_i-1][2] if end_i > 0 else None
        bounds.append((L['id'], start, end))
        print(f"   {L['id']}  {start:6.2f} - {end:6.2f}  ({end-start:4.2f}s)  {L['text'][:38]}")
        wi = end_i

    # Bitisik, cakismayan parcalar: bolme noktasi = SONRAKI satirin baslangici.
    # clip_i = [bu_satir_baslangic, sonraki_satir_baslangic]. Ilk parca 0'dan,
    # son parca ses sonuna kadar. Boylece toplam = tam ses suresi, konusma kesilmez.
    dur = float(subprocess.run(['ffprobe','-v','error','-show_entries','format=duration',
        '-of','csv=p=0', AUDIO], capture_output=True, text=True).stdout.strip())
    starts = [b[1] for b in bounds]
    fixed = []
    for i, (id, s, e) in enumerate(bounds):
        cs = 0.0 if i == 0 else starts[i]
        ce = starts[i+1] if i+1 < len(bounds) else dur
        fixed.append((id, round(cs, 3), round(ce, 3)))

    print("[4/4] ses 15 parcaya boluluyor...")
    for id, s, e in fixed:
        subprocess.run(['ffmpeg','-y','-loglevel','error','-i',AUDIO,
            '-ss',f'{s:.3f}','-to',f'{e:.3f}','-c','copy',
            os.path.join(ROOT, tl.get('voDir','vo'), f'{id}.mp3')], check=True)
    json.dump({id:[s,e] for id,s,e in fixed},
              open(os.path.join(ROOT,'out', os.environ.get('TAG','hook')+'-timings.json'),'w'), indent=2)
    print("TAMAM -> vo/L01.mp3 ... L15.mp3  |  simdi ./render.sh")

if __name__ == '__main__':
    main()
