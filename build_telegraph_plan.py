import json

STYLE = ("Victorian era painterly realism, warm golden tones, subtle oil painting brushstrokes, "
         "fine detail, soft natural lighting, no frame, no border, full bleed edge to edge "
         "composition filling the entire frame, no blank margins, no canvas border. ")
SUFFIX = " No text, no watermarks."

def ai(desc):
    return STYLE + desc + SUFFIX

# scenes: (para_start, para_end_inclusive, TYPE, short_desc, prompt_or_keywords)
scenes = [
(0,0,"AI","Arthur arrives at the station gate at night, storm brewing",
 ai("A man of 26 in a railway clerk's coat walking through a station gate at night under a bruised, storm-heavy sky, an old gatekeeper nearby turning up his collar, gas lamps glowing along the platform")),
(1,1,"AI","Small Victorian railway junction station exterior at night",
 ai("A small Victorian railway junction station at night, gas lamps glowing along an empty platform, storm clouds overhead, wet cobblestones, no modern signage, no cars, no modern rail infrastructure")),
(2,2,"AI","Arthur unlocks the telegraph office",
 ai("A man of 26 unlocking a small stone telegraph office door at a railway station at night, key ring in hand, dark platform behind him, first light spilling from the doorway")),
(3,3,"AI","The telegraph office interior comes to life in gaslight",
 ai("Interior of a small Victorian telegraph office, brass sounder and Morse key on a worn wooden counter, a mahogany block instrument with two needles, a ledger open on the desk, warm gaslight, no one visible, cozy technical detail")),
(4,4,"AI","Arthur glances through the day's paperwork",
 ai("A man of 26 in a railway clerk's coat reading papers at a wooden counter in a small gaslit telegraph office, late evening, quiet concentration")),
(5,6,"AI","Alice arrives to hand over the shift",
 ai("A young woman of 24 in a railway booking clerk's dress entering a small gaslit telegraph office with a ledger under her arm, bonnet half-tied, a man of 26 greeting her, warm evening light")),
(7,8,"AI","Arthur and Alice talk of the coming storm",
 ai("A man of 26 and a young woman of 24 standing together at a railway office window looking out at a darkening stormy sky, warm gaslight behind them, quiet conversation")),
(9,10,"AI","Alice speaks of her father, an old signalman",
 ai("A young woman of 24 in a railway booking clerk's dress drawing on her gloves, speaking with quiet authority, warm gaslit office interior, a man of 26 listening")),
(11,13,"AI","Playful argument about wind and wire",
 ai("A man of 26 and a young woman of 24 in a small Victorian railway office, mid conversation, warm expressions, gaslight, one gesturing lightly as if making a point")),
(14,16,"AI","The banter sharpens, both enjoying the argument",
 ai("A man of 26 and a young woman of 24 mid-debate in a small gaslit Victorian railway office, animated warm expressions, wooden counter between them, evening light")),
(17,18,"AI","The banter continues, easy and familiar",
 ai("A young woman of 24 laughing gently in a small gaslit Victorian railway office, a man of 26 smiling across a wooden counter, warm evening light, comfortable friendship")),
(19,21,"AI","Alice ties her bonnet, says goodnight",
 ai("A young woman of 24 tying her bonnet at the door of a small gaslit railway office, ledger in hand, a man of 26 standing near the counter, warm farewell moment")),
(22,22,"STOCK","Rain begins to strike the station window",
 "rain starting window glass night closeup victorian"),
(23,23,"AI","Arthur settles in for the long night",
 ai("A man of 26 in a railway clerk's coat sitting at a wooden counter, opening a large ledger, ruling the first line, gaslight, small stone telegraph office at night")),
(24,24,"STOCK","Close detail of railway timetable board and clock",
 "vintage railway timetable board clock brass closeup rustic"),
(25,25,"AI","The ordinary traffic of the wire — messages through the night",
 ai("A man of 26 working a brass telegraph key at a wooden counter in a small gaslit railway office, concentrated expression, ledger open beside him")),
(26,29,"AI","Arthur exchanges the first bell code with Tom at Hollow Bank",
 ai("A man of 61 signalman sitting alone at a mahogany block instrument in a small signal box at night, oil lamp glow, rain on the window behind him, working a brass key")),
(30,33,"AI","Ned the porter reports on the lamps",
 ai("A young man of 22 porter in a railway uniform putting his head round a office door, rain on his cap, a man of 26 clerk listening from behind a counter, gaslight")),
(34,37,"AI","Sam the messenger boy dashes in about a hamper",
 ai("A boy of 17 messenger, lean and energetic, bursting through a railway office door out of breath, a man of 26 clerk half-amused at a counter, gaslight, storm building outside")),
(38,38,"STOCK","Storm clouds gathering over the railway line at dusk",
 "storm clouds gathering dusk countryside railway line dramatic sky"),
(39,39,"AI","The 22:40 train departs — Arthur hands over the train staff",
 ai("A man of 26 railway clerk on a lamplit platform at night handing up an engraved iron staff rod to a train driver leaning from a steam locomotive cab, steam and lamplight, rain beginning")),
(40,40,"STOCK","Heavy rain lashes the station platform",
 "heavy rain railway platform night storm downpour"),
(41,41,"AI","Arthur explains the single line's oldest safeguard, the train staff",
 ai("Close view of a man of 26's hand holding an old engraved iron train staff rod beside a brass telegraph block instrument on a wooden counter, warm gaslight, technical detail")),
(42,42,"STOCK","Close detail of an antique brass telegraph block instrument",
 "antique brass telegraph instrument closeup vintage railway signal"),
(43,43,"AI","The midnight mail passes — the staff itself goes north",
 ai("A man of 26 railway clerk handing an iron staff rod up to a fireman on a steam locomotive footplate at a rainy nighttime platform, firebox glow, motion blur of steam")),
(44,49,"AI","Tom and Arthur trade dry jokes over the wire",
 ai("A man of 61 signalman smiling faintly while working a telegraph key in a small lamplit signal box at night, rain streaking the window, quiet companionable mood")),
(50,51,"AI","Arthur waits alone for the freight, tea gone cold",
 ai("A man of 26 railway clerk sitting alone at a wooden counter in a small gaslit office at night, a cup of tea forgotten beside him, listening to rain and distant thunder, pensive")),
(52,53,"AI","The freight is offered — Line Clear — then silence",
 ai("Close view of a man of 26's hand resting on a brass telegraph key beside a block instrument with two needles, tense focused expression, warm gaslight, night")),
(54,54,"STOCK","Rain streaming down a dark railway office window",
 "rain streaming window glass dark night railway closeup"),
(55,59,"AI","Sam complains about his boots, Arthur gives advice",
 ai("A boy of 17 messenger propping a wet boot on a fender in a small gaslit railway office, a man of 26 clerk looking on with dry amusement, warm firelight")),
(60,63,"AI","Growing unease — Arthur tries the silent wire",
 ai("A man of 26 railway clerk leaning tensely over a brass telegraph key and block instrument in a small gaslit office at night, concentrated worried expression")),
(64,67,"AI","Still nothing — Arthur tries a third time",
 ai("A man of 26 railway clerk tapping a telegraph key slowly and deliberately, listening hard, small gaslit office at night, growing tension on his face")),
(68,69,"AI","Arthur turns over the possibilities in his mind",
 ai("A man of 26 railway clerk sitting very still at a wooden counter, staring at a silent block instrument in a small gaslit office at night, rain on the window, deep thought")),
(70,71,"AI","The worst possibility — a train already unaccounted for",
 ai("A man of 26 railway clerk standing abruptly from a wooden counter, alarmed realization crossing his face, small gaslit railway office at night, rain streaked window")),
(72,72,"AI","Arthur checks the instrument's battery connections",
 ai("A man of 26 railway clerk crouched beside an open wooden battery box under a counter in a small gaslit telegraph office, checking wires, methodical, night")),
(73,74,"AI","Arthur finds Ned and lays out the facts plainly",
 ai("A man of 26 railway clerk speaking urgently but calmly to a young porter in a lamplit railway lamp room at night, rain visible through a small window")),
(75,79,"AI","Ned agrees to send Sam up the line",
 ai("A young man of 22 porter setting down a wick trimmer, listening intently to a man of 26 clerk in a small lamplit railway room, night, storm outside")),
(80,83,"AI","Arthur gives Sam careful instructions before he runs into the storm",
 ai("A man of 26 railway clerk speaking earnestly to a boy of 17 messenger by a lamplit doorway, catching his eye directly, storm lantern in the boy's hand, rain and wind outside")),
(84,86,"AI","One last warning about the live wire, then Sam is off",
 ai("A man of 26 railway clerk speaking a final serious word to a boy of 17 messenger at a lamplit doorway, the boy nodding solemnly, storm lantern ready, wind and rain outside")),
(87,87,"AI","Sam vanishes into the wet dark with his lantern",
 ai("A boy of 17 messenger running down a dark cinder path beside railway tracks at night, a small storm lantern swinging, heavy rain, distant station lights behind him")),
(88,90,"AI","Arthur and Ned wait, trading a few words by the fire",
 ai("A man of 26 railway clerk and a young man of 22 porter sitting near a small office fire at night, mugs in hand, rain audible outside, quiet waiting mood")),
(91,93,"AI","Ned asks how long they can really wait",
 ai("A young man of 22 porter and a man of 26 railway clerk talking quietly near a small office fire late at night, thoughtful expressions, storm still audible outside")),
(94,94,"AI","Arthur works the silent key again, patient and even",
 ai("A man of 26 railway clerk tapping a brass telegraph key steadily in a small gaslit office at night, listening intently for a reply, rain streaked window")),
(95,98,"AI","Arthur tells Ned of Tom, who has seen worse nights than this",
 ai("A man of 26 railway clerk speaking thoughtfully to a young porter beside a small office fire at night, turning a tin cup slowly, warm firelight, a quiet moment")),
(99,101,"AI","Tom's old rule — never trust what you hope is true",
 ai("A man of 26 railway clerk speaking with quiet conviction to a young porter beside a dying office fire at night, firelight on both faces, a serious thematic moment")),
(102,102,"STOCK","Storm-lashed railway line disappearing into darkness",
 "storm dark railway line countryside night rain dramatic"),
(103,106,"AI","Sam returns soaked, reporting the broken wire",
 ai("A boy of 17 messenger dripping wet, breathing hard, reporting urgently to a man of 26 clerk in a small gaslit railway office at night, storm lantern in hand")),
(107,107,"AI","Arthur weighs what the news does and does not tell him",
 ai("A man of 26 railway clerk standing very still in a small gaslit office at night, processing troubling news, rain on the window, tense stillness")),
(108,109,"AI","Arthur asks Ned to walk the full mile and a half to Hollow Bank",
 ai("A man of 26 railway clerk speaking urgently to a young porter in a small lamplit railway office at night, storm visible through the open door")),
(110,111,"AI","Ned pulls on his coat and sets off without argument",
 ai("A young man of 22 porter pulling on a heavy coat and reaching for a lantern in a small lamplit railway office at night, a man of 26 clerk watching, storm through the doorway")),
(112,113,"AI","Sam rests on the bench with tea while Arthur works",
 ai("A boy of 17 messenger sitting on a wooden bench with a tin mug, resting, a man of 26 clerk working at a counter nearby, small gaslit railway office, night")),
(114,114,"AI","Arthur logs a signal change, working too fast",
 ai("A man of 26 railway clerk writing quickly in a large ledger by gaslight, glancing at a wall clock, small railway office interior at night, rushed concentration")),
(115,116,"AI","He catches the error — a single clean correction line",
 ai("Close view of a man of 26's hands writing in a large ledger by gaslight, a pen striking a single clean correction line through an entry, careful precise motion")),
(117,119,"AI","Arthur explains why the mistake matters, and why catching it does",
 ai("A man of 26 railway clerk speaking gently to a boy of 17 messenger across a wooden counter in a small gaslit office, ledger open between them, warm quiet moment")),
(120,120,"STOCK","A storm lantern swinging along a dark wet cinder path",
 "lantern swinging dark path night rain storm walking"),
(121,122,"AI","Ned returns — the freight entered the section, staff in hand",
 ai("A young man of 22 porter soaked through, standing in a small gaslit railway office doorway at night, reporting urgently to a man of 26 clerk, rain streaming off his coat")),
(123,123,"AI","Arthur weighs the answer he least wanted and most needed",
 ai("A man of 26 railway clerk standing thoughtfully in a small gaslit railway office at night, processing difficult news, rain streaked window, quiet resolve forming")),
(124,126,"AI","Arthur decides he will go find her himself",
 ai("A man of 26 railway clerk reaching for his coat and lantern with quiet determination in a small gaslit office at night, a young porter watching, storm outside")),
(127,129,"AI","Sam is posted at the platform with a hand signal lamp",
 ai("A boy of 17 messenger standing alone on a rain-swept railway platform at night holding a red hand signal lamp, solemn and focused, storm light")),
(130,130,"AI","Arthur logs his own departure before stepping into the storm",
 ai("Close view of a man of 26's hand writing a time into a ledger beside a brass block instrument, gaslight, a lantern and coat ready nearby, night")),
(131,131,"AI","Arthur walks out alone into the storm's last hard hour",
 ai("A man of 26 railway clerk walking alone along a dark cinder path beside railway tracks in driving rain at night, storm lantern held out, wind bending the grass, dramatic weather")),
(132,132,"STOCK","A fallen branch and broken telegraph pole in the storm",
 "fallen tree branch broken wooden pole storm night rustic railway"),
(133,135,"AI","Arthur finds the stalled freight train, driver holds up the staff",
 ai("A man of 26 railway clerk with a lantern approaching a stopped steam freight locomotive on a dark rainy track at night, the driver leaning from the cab holding up an iron staff rod, headlamp glow")),
(136,137,"AI","Arthur explains the broken wire and offers to guide the way",
 ai("A man of 26 railway clerk standing on a locomotive footplate step at night, speaking to the driver over the rain, storm and headlamp light, eleven dark wagons behind")),
(138,138,"AI","Arthur rides the footplate, calling the road through the storm",
 ai("A man of 26 railway clerk standing on a steam locomotive footplate beside the driver at night, both peering ahead into driving rain, firebox glow lighting their faces, motion")),
(139,140,"AI","The freight arrives safely at Drayton, Sam's lamp turns white",
 ai("A steam locomotive arriving at a rain-slicked railway platform at night, a boy of 17 messenger swinging a hand lamp from red to white, station lights glowing warmly")),
(141,142,"AI","Arthur tells Ned the freight is through, no harm done",
 ai("A man of 26 railway clerk dripping wet, speaking with quiet relief to a young porter in a small gaslit office at night, exhaustion and satisfaction on his face")),
(143,144,"AI","Ned and Sam are stood down for the night",
 ai("A man of 26 railway clerk clasping a young porter's shoulder warmly in a small gaslit office at night, a boy of 17 messenger nearby, relief and camaraderie")),
(145,147,"AI","Ned lingers by the fire before finally heading home",
 ai("A young man of 22 porter sitting near a small office fire late at night, unfocused tired gaze, a man of 26 clerk nearby at a counter, warm dying firelight")),
(148,148,"AI","Arthur writes up the full clean account in the ledger",
 ai("A man of 26 railway clerk writing steadily in a large ledger by gaslight, focused and calm, small railway office interior, deep night")),
(149,149,"STOCK","Dawn breaking grey over a wet English railway line",
 "dawn breaking grey sky railway line wet tracks countryside morning"),
(150,150,"AI","Arthur steps onto the platform as a blackbird sings",
 ai("A man of 26 railway clerk standing alone on a wet railway platform at first light, stretching, pale dawn sky, mist rising off the rails, quiet morning")),
(151,151,"AI","A small Victorian railway station waking at dawn",
 ai("A small Victorian railway station at first light, empty platform, pale golden dawn sky, wet rails catching the light, mist rising, no modern signage, no cars, no modern rail infrastructure")),
(152,153,"AI","Mr. Hargreaves arrives and reads the night's ledger",
 ai("An older stationmaster of 55 in a formal coat reading a ledger over spectacles at a wooden counter, a man of 26 clerk standing attentively beside him, morning light through a window")),
(154,155,"AI","Hargreaves reads every entry carefully, including the correction",
 ai("An older stationmaster of 55 studying a ledger closely, finger pausing on a corrected entry, soft morning light, small railway office interior, quiet scrutiny")),
(156,157,"AI","'Clean work.' — the whole of Hargreaves's praise",
 ai("An older stationmaster of 55 looking up over spectacles at a man of 26 clerk in a small railway office, morning light, a rare small moment of approval")),
(158,160,"AI","Hargreaves mentions the wire will be mended today",
 ai("An older stationmaster of 55 turning back at a doorway with a ledger under his arm, speaking to a man of 26 clerk, morning light flooding a small railway office")),
(161,163,"AI","Whitfield the morning clerk takes over the shift",
 ai("A cheerful young man of 24 clerk settling into a chair at a telegraph counter, reaching for a brass key, morning light, a tired man of 26 clerk standing nearby with his coat")),
(164,164,"AI","Arthur gathers his coat and steps out into the washed morning",
 ai("A man of 26 railway clerk in a coat walking out through a station gate into a soft pale morning, wet platforms and shining rails behind him, storm passed")),
(165,165,"AI","The sounder chatters on behind him — Arthur walks on",
 ai("A man of 26 railway clerk walking away down a quiet English lane in soft early morning light, small railway station visible behind him, calm and unhurried departure")),
]

wc = None
text = open('/Users/aytacerdem/zenn/telegraph_story.txt').read()
lines = text.split('\n')
if lines[0].strip() == "The Night Telegraph Clerk":
    text = '\n'.join(lines[1:]).lstrip('\n')
paras = [p for p in text.split('\n\n') if p.strip()]
wc = [len(p.split()) for p in paras]
print("total paras in story:", len(paras), "total scenes defined:", len(scenes))

def wcount(a,b):
    return sum(wc[i] for i in range(a,b+1))

VO_DURATION = 5185.840181

raw_durs = []
for (a,b,typ,desc,prompt) in scenes:
    w = wcount(a,b)
    raw_durs.append(max(w * 1.0, 8.0))

scale = VO_DURATION / sum(raw_durs)

rows = []
t = 0.0
for (a,b,typ,desc,prompt), rd in zip(scenes, raw_durs):
    dur = rd * scale
    rows.append((t, dur, typ, desc, prompt, a, b))
    t += dur

total = t
print("TOTAL SCENES:", len(rows))
print("TOTAL TIME:", total, "target:", VO_DURATION)

def fmt(s):
    m = int(s//60)
    sec = s - m*60
    return f"{m:02d}:{sec:05.2f}"

lines_out = ["# The Night Telegraph Clerk — Visual Plan", "",
         f"VO duration: {VO_DURATION:.2f}s | {len(rows)} scenes", "",
         "## Visual Type Legend",
         "- AI = GPT Image 2 (Arthur 26yo clerk, Tom 61yo signalman, Ned 22yo porter, Sam 17yo messenger, Alice 24yo booking clerk, Hargreaves 55yo stationmaster, Whitfield 24yo morning clerk — character consistency)",
         "- STOCK = verified period-appropriate stock video",
         "", "---", "",
         "| # | Time | Dur | Type | Scene | Prompt/Keywords |",
         "|---|---|---|---|---|---|"]
scenes_json = []
for i,(t0,dur,typ,desc,prompt,a,b) in enumerate(rows,1):
    icon = "AI" if typ=="AI" else "STOCK"
    p = prompt.replace("|","/")
    lines_out.append(f"| {i} | {fmt(t0)} | {dur:.1f}s | {icon} | {desc} | {p} |")
    scenes_json.append({"num": i, "time": fmt(t0), "dur": f"{dur:.2f}s", "type": typ, "desc": desc, "prompt": prompt})

open('/Users/aytacerdem/zenn/telegraph_visual_plan.md','w').write('\n'.join(lines_out))
json.dump(scenes_json, open('/Users/aytacerdem/zenn/telegraph_scenes.json','w'), indent=2)
print("written telegraph_visual_plan.md and telegraph_scenes.json")

ai_count = sum(1 for r in rows if r[2]=="AI")
stock_count = sum(1 for r in rows if r[2]=="STOCK")
print("AI:", ai_count, "STOCK:", stock_count)
