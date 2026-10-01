import json

STYLE = ("Victorian era painterly realism, warm golden tones, subtle oil painting brushstrokes, "
         "fine detail, soft natural lighting, no frame, no border, full bleed edge to edge "
         "composition filling the entire frame, no blank margins, no canvas border. ")
SUFFIX = " No text, no watermarks."

def ai(desc):
    return STYLE + desc + SUFFIX

mapping = json.load(open('/tmp/para_mapping.json'))
mapping = {int(k): v for k, v in mapping.items()}

MAXOLD = max(mapping.keys())
def M(a):
    if a in mapping:
        return mapping[a]
    if a > MAXOLD:
        return mapping[MAXOLD]
    return mapping[a + 1]

# original scenes, indexed against millbrook_story_v1_original.txt (title = para 0)
old_scenes = [
(0,2,"AI","Hollis in bakehouse doorway watching Meg cross the yard at night",
 ai("A man of 61 with a weathered kind face standing in the doorway of a small stone bakehouse at night, holding a candle-lantern, watching a girl of 16 cross a dark yard toward him, her shawl pulled tight against the November chill, boots too big for her feet, cold blue night light, warm lantern glow spilling from the doorway")),
(3,4,"AI","You're early / Meg follows him inside",
 ai("A man of 61 in the lit doorway of a stone bakehouse speaking to a girl of 16 standing just outside, warm lantern light on both their faces, cold dark yard behind her, gentle welcoming exchange")),
(5,5,"STOCK","Bakehouse interior establishing, cold oven, empty trough table",
 "old stone bakery interior empty cold oven brick dome rustic"),
(6,7,"AI","First thing is the fire — Hollis explains, Meg smiles",
 ai("A man of 61 setting a lantern on a wall hook inside a low stone bakehouse, speaking earnestly to a girl of 16 who smiles for the first time, a great cold brick oven dome visible behind them, warm lantern light")),
(8,9,"AI","Hollis shows the firebox and kindling technique",
 ai("A man of 61 crouched beside the small iron firebox door of a brick oven, showing a girl of 16 how to lay kindling in a loose lattice, warm lantern light, close teaching moment")),
(10,10,"AI","Hollis reflects on the worn habit of the lesson",
 ai("A man of 61 crouched at an oven firebox, a quiet thoughtful expression, lantern light warm on his weathered face, a girl of 16 watching attentively beside him")),
(11,12,"AI","Meg lights the first fire",
 ai("A girl of 16 kneeling at a small iron firebox door, orange firelight catching her face as kindling catches flame, a man of 61 watching proudly beside her, dark stone bakehouse around them")),
(13,13,"STOCK","Firelight through the iron door seam, room warming",
 "fire glow through iron door crack dark room warm light closeup"),
(14,15,"AI","Why only one window — Hollis explains the bakehouse's purpose",
 ai("A man of 61 and a girl of 16 standing in a warm stone bakehouse, he gesturing toward a single small high window, explaining something earnestly, lantern light, low beamed ceiling")),
(16,16,"STOCK","Bakehouse details: dried herbs on beams, notched trough table",
 "dried herbs hanging rustic wooden beam kitchen vintage closeup"),
(17,19,"AI","Hollis explains the night's rhythm and long waiting ahead",
 ai("A man of 61 speaking to a girl of 16 in a warm lantern-lit stone bakehouse, a long wooden trough table between them, sacks of flour along the wall, a great oven behind, quiet instructive moment")),
(20,21,"AI","Setting up sieves and flour",
 ai("A man of 61 setting two wide sieves and sacks of flour on a long wooden trough table beside a girl of 16, lantern light, stone bakehouse interior")),
(22,22,"STOCK","Millbrook village asleep at night, quiet lane",
 "english village night quiet lane stone cottages dark sleeping"),
(23,23,"STOCK","Flour dust glowing in lantern light",
 "flour dust cloud light beam closeup baking rustic"),
(24,26,"AI","Meg sieves flour, talks of her siblings",
 ai("A girl of 16 sieving flour at a wooden trough table, fine flour falling in the lantern light, a man of 61 listening warmly nearby, stone bakehouse interior")),
(27,29,"AI","Hollis tends the barm starter, explains its age",
 ai("A man of 61 lifting a cloth from an old covered stoneware crock behind a brick oven, a girl of 16 leaning in curiously to look, warm lantern light, stone bakehouse")),
(30,31,"AI","The barm crock revealed — 'kept alive, and fed'",
 ai("Close view of a man of 61's weathered hands holding back a cloth over an old stoneware crock, pale bubbled sourdough starter visible inside, a girl of 16 watching with quiet wonder, warm lantern light")),
(32,34,"AI","What happens if it dies — Meg understands the inheritance",
 ai("A girl of 16 looking thoughtfully at an old stoneware crock on a wooden shelf, a man of 61 standing beside her, warm lantern light, stone bakehouse interior, quiet contemplative mood")),
(35,36,"AI","Making the well in the flour heap",
 ai("A man of 61 showing a girl of 16 how to press a crater into a heap of pale flour on a wooden trough table, lantern light, close hands-on teaching moment")),
(37,40,"AI","The water mistake begins — Meg reaches for the hot jug",
 ai("A girl of 16 tilting a steaming jug of water over a flour well on a wooden table, a man of 61 reaching quickly to catch her wrist, urgent gentle motion, warm lantern light, stone bakehouse")),
(41,43,"AI","Hollis explains the danger, Meg's shame",
 ai("A man of 61 holding a girl of 16's hand near a steaming jug, explaining something seriously, her face tight with quiet embarrassment, warm lantern light, close teaching moment")),
(44,45,"AI","The lesson lands — Meg waits and retests the water",
 ai("A girl of 16 testing the temperature of water against her wrist over a steaming jug, watchful and careful, a man of 61 nearby, lantern-lit stone bakehouse")),
(46,46,"AI","Mixing the barm into the water, beginning the dough",
 ai("A man of 61 and a girl of 16 with hands together in a wide flour well on a wooden trough table, drawing flour and water into a shaggy dough, warm lantern light")),
(47,48,"AI","The kneading begins — Hollis explains its purpose",
 ai("A man of 61 turning a rough mass of pale dough onto a floured wooden table, a girl of 16 watching closely, warm lantern light, stone bakehouse interior")),
(49,50,"AI","Hollis demonstrates kneading, Meg struggles",
 ai("A man of 61 kneading dough with practiced rhythm on a wooden table, a girl of 16 beside him kneading her own portion clumsily, flour dust in lantern light, close hands-on scene")),
(51,53,"AI","Hollis guides her hands, 'you have it'",
 ai("A man of 61 standing near a girl of 16 at a trough table, both working dough side by side, warm lantern light, focused teaching moment")),
(54,54,"STOCK","Close-up hands kneading dough rhythmically",
 "hands kneading bread dough closeup rustic wooden table flour"),
(55,58,"AI","Were you always going to be a baker — Hollis reflects",
 ai("A man of 61 kneading dough thoughtfully at a wooden table, a girl of 16 across from him listening, warm lantern light, quiet reflective conversation, stone bakehouse")),
(59,61,"AI","Hollis speaks of Grace, his late wife",
 ai("A man of 61 pausing over his kneading, a faraway tender expression, a girl of 16 watching him gently, warm lantern light, stone bakehouse interior, quiet emotional moment")),
(62,65,"AI","What was she like — Hollis remembers Grace",
 ai("A man of 61 speaking softly at a trough table, dough beneath his hands, a girl of 16 listening with quiet sympathy, warm lantern light, tender nostalgic mood")),
(65,65,"STOCK","A faint old burn scar on a wooden beam by the door",
 "old wooden beam burn mark scorch closeup rustic vintage"),
(66,68,"AI","Hollis speaks of his son in Bristol",
 ai("A man of 61 kneading dough, speaking with quiet resignation and affection, a girl of 16 listening attentively across the table, warm lantern light, stone bakehouse")),
(69,70,"AI","Do you miss him terribly — grief for the living",
 ai("A man of 61 with a thoughtful melancholy expression at a wooden trough table, dough beneath his hands, a girl of 16 watching him with quiet care, warm lantern light")),
(71,74,"AI","Meg mentions Tam Aldous and the marriage question",
 ai("A girl of 16 kneading dough with more force than needed, a troubled thoughtful expression, a man of 61 watching her closely, warm lantern light, stone bakehouse")),
(75,78,"AI","The trade, or the not-being-decided-for — Hollis's advice",
 ai("A man of 61 speaking earnestly to a girl of 16 across a wooden trough table, both hands still in dough, warm lantern light, a serious exchange")),
(79,82,"AI","Does your mother know — Meg smiles, resolved",
 ai("A girl of 16 smiling a real quiet smile while kneading dough, a man of 61 nearby with a satisfied expression, warm lantern light, stone bakehouse interior")),
(83,86,"AI","The dough is ready — springs back under the thumb",
 ai("A man of 61 pressing a thumb into a smooth ball of pale dough on a wooden table, a girl of 16 doing the same beside him with a hopeful expression, warm lantern light, close hands-on moment")),
(87,88,"STOCK","Two bowls of dough covered with damp cloth, set to rise",
 "bread dough bowl covered cloth rising rustic kitchen closeup"),
(89,89,"STOCK","Tin kettle on the grate, bread and cheese for a break",
 "old tin kettle fireplace bread cheese rustic table candlelight"),
(90,91,"AI","Tell me about the fair — Hollis and Meg share bread and cheese",
 ai("A man of 61 and a girl of 16 sitting on a low stone wall outside a bakehouse at night, eating bread and cheese, cold starry sky above, warm doorway light behind them, companionable quiet mood")),
(92,93,"AI","Because of the barm — loyalty over novelty",
 ai("A man of 61 speaking with a small satisfied smile, a girl of 16 listening beside him outside a stone bakehouse at night, starry sky, warm doorway light")),
(94,96,"AI","The Elmscombe rival's failed iron oven, and the goat story",
 ai("A man of 61 telling an amused story to a girl of 16 who laughs, both sitting outside a stone bakehouse at night, starry sky, warm doorway light, warm humor")),
(97,99,"AI","Hollis's first fair at ten years old",
 ai("A man of 61 with a distant remembering expression, a girl of 16 listening intently beside him outside a stone bakehouse at night, starry sky, warm doorway light")),
(100,101,"AI","The stall was mine in earnest after that",
 ai("A man of 61 speaking with quiet gravity, a girl of 16 listening with sympathy, sitting outside a stone bakehouse at night, starry sky, warm doorway light")),
(102,102,"STOCK","Church clock tower faint across the yard at night",
 "old stone church clock tower night village silhouette"),
(102,102,"AI","Hollis checks the risen dough",
 ai("A man of 61 lifting the corner of a damp cloth from a large bowl of risen pale dough, careful gentle motion, warm lantern light, stone bakehouse interior at night")),
(103,105,"AI","Knocking back the dough",
 ai("A man of 61 pressing a firm fist into a large risen dome of dough on a wooden table, a girl of 16 watching in surprise, warm lantern light, stone bakehouse")),
(106,109,"AI","Shaping the loaves — plaiting lesson",
 ai("A man of 61 and a girl of 16 shaping bread dough together at a wooden table, plaited loaves and round loaves taking form, flour dust in lantern light, close hands-on scene")),
(110,110,"AI","Shaping the vicarage loaves, playful moment",
 ai("A girl of 16 shaping small loaves of dough with exaggerated careful attention, a man of 61 smiling and lightly teasing her with a floury hand, warm lantern light, stone bakehouse")),
(111,111,"STOCK","Shaped loaves proving on boards under cloth",
 "bread dough loaves proving wooden board cloth rustic bakery"),
(112,112,"AI","Hollis rakes the fire, sweeps the oven floor",
 ai("A man of 61 raking glowing embers from a brick oven with a long-handled tool, steam rising from a wet birch broom, warm firelight, stone bakehouse interior")),
(113,115,"AI","The flour heat test — 'she's hungry'",
 ai("A man of 61 flinging a pinch of flour onto the swept floor of a glowing brick oven, a girl of 16 watching closely beside him, warm ember glow, stone bakehouse interior")),
(116,117,"STOCK","The swept oven floor radiating heat, close detail",
 "hot brick oven floor glowing embers closeup bakery rustic"),
(118,119,"AI","How long before you knew the count without thinking",
 ai("A man of 61 and a girl of 16 crouched together before a glowing brick oven firebox, warm ember light on their faces, quiet instructive moment")),
(120,121,"AI","My father used to say the oven had moods",
 ai("A man of 61 crouched thoughtfully before a glowing oven firebox, studying the embers, a girl of 16 crouched beside him matching his stillness, warm firelight")),
(122,123,"AI","Do you think of it as a person — Hollis's fondness for the oven",
 ai("A man of 61 speaking warmly beside a glowing brick oven, a girl of 16 listening with a small smile, warm ember light, stone bakehouse interior")),
(124,124,"AI","Loading the oven with the peel",
 ai("A man of 61 sliding a shaped loaf of bread into a glowing brick oven using a long wooden peel, a girl of 16 counting loaves beside him, warm firelight, stone bakehouse")),
(125,126,"AI","Counting the loaves in, 'say it again in an hour'",
 ai("A girl of 16 reciting numbers proudly to a man of 61 standing beside a brick oven with a long wooden peel, warm firelight, stone bakehouse interior")),
(127,127,"STOCK","The old wooden peel, worn smooth by generations",
 "old wooden bread peel paddle worn handle rustic bakery closeup"),
(128,128,"STOCK","The heavy iron oven door swinging shut",
 "old iron oven door closing heavy metal bakery rustic closeup"),
(129,130,"AI","The final wait begins — Meg growing tired",
 ai("A girl of 16 sitting on a flour barrel, eyelids heavy with tiredness, a man of 61 watching her with quiet warmth, dim warm firelight, stone bakehouse")),
(131,132,"AI","You did well — does it get easier",
 ai("A man of 61 speaking gently to a tired girl of 16 sitting on a flour barrel, warm dim firelight, stone bakehouse interior, late-night quiet mood")),
(133,134,"AI","But you'll mind it less, given time",
 ai("A girl of 16 considering a quiet answer thoughtfully, a man of 61 beside her in the dim warm firelight of a stone bakehouse, late-night reflective mood")),
(135,136,"AI","Do you never grow tired of it — forty years, still surprised",
 ai("A man of 61 speaking with quiet warmth to a girl of 16 in a dim firelit stone bakehouse, both tired but companionable, late night mood")),
(137,138,"AI","Tonight's been a surprise too — the company",
 ai("A man of 61 speaking with unguarded warmth to a girl of 16 in a dim firelit bakehouse, an honest moment between them, late night quiet")),
(139,140,"AI","Comfortable silence between them",
 ai("A man of 61 and a girl of 16 sitting quietly together near a dim glowing oven, comfortable silence, warm low firelight, stone bakehouse interior, late night")),
(141,141,"STOCK","Small high window paling with the first hint of dawn",
 "small window dawn light pale grey stone wall rustic closeup"),
(142,144,"AI","You may sleep a quarter hour — Meg's transparent lie",
 ai("A man of 61 smiling gently at a girl of 16 who yawns despite herself, warm dim firelight, stone bakehouse interior, tender late-night humor")),
(145,145,"AI","Meg falls asleep, Hollis watches over her",
 ai("A girl of 16 asleep sitting upright on a flour barrel, chin dropped, a man of 61 watching her with quiet warmth in the dim firelight, stone bakehouse interior")),
(146,148,"AI","The smell reaches them — 'there it is'",
 ai("A girl of 16 sitting up with her nose lifting eagerly, a man of 61 smiling beside her, warm golden light beginning to touch a small high window, stone bakehouse interior")),
(149,149,"STOCK","Dawn breaking over Millbrook, cock crowing, chimney smoke",
 "english village dawn sunrise chimney smoke rooster countryside"),
(150,150,"AI","Hollis opens the oven, the smell rolls out",
 ai("A man of 61 swinging open a heavy iron oven door, golden light and steam rolling out, a girl of 16 beside him with delighted surprise, warm morning light, stone bakehouse")),
(151,151,"AI","Drawing the loaves with the peel",
 ai("A man of 61 sliding golden-brown loaves of bread out of a brick oven with a long wooden peel, a girl of 16 receiving them onto cooling racks, warm morning light, stone bakehouse")),
(152,153,"AI","Not one lost — the full racks of bread",
 ai("A girl of 16 and a man of 61 standing before racks filled with golden-brown loaves of bread, warm morning light streaming through a window, quiet pride, stone bakehouse interior")),
(154,154,"STOCK","Cooling bread crusts crackling on the rack",
 "fresh bread loaves cooling rack golden crust closeup bakery"),
(155,156,"AI","It sings — the crust song lesson",
 ai("A girl of 16 listening with her head tilted toward racks of cooling bread, a man of 61 explaining gently beside her, warm morning light, stone bakehouse interior")),
(157,158,"AI","Look at that — Meg's quiet pride",
 ai("A man of 61 and a girl of 16 standing together before racks of golden bread, warm morning light through a window, both wearing an expression of quiet earned pride, stone bakehouse")),
(159,159,"AI","Carrying baskets of bread out into the waking lane",
 ai("A man of 61 and a girl of 16 walking together down a village lane at dawn, each carrying a basket of bread, smoke rising from cottage chimneys, soft golden morning light")),
(160,160,"AI","Arriving at the green — the Elmscombe baker's cool greeting",
 ai("A man of 61 lifting a hand in greeting to a rival baker across a village green being set up for a fair, a girl of 16 beside him, morning light, trestles and bunting in the background")),
(161,161,"AI","Setting the trestle, arranging the loaves",
 ai("A man of 61 and a girl of 16 arranging golden plaited loaves of bread on a wooden trestle table near a church wall, warm morning light, village fair green in the background")),
(162,162,"AI","The first customer — Meg takes the coin",
 ai("A girl of 16 taking a coin from a farmer's wife and handing over a loaf of bread at a market stall, a man of 61 standing back with a proud quiet smile, warm morning light, village fair")),
(163,164,"AI","Go on home — Meg leaves, tired and proud",
 ai("A man of 61 speaking kindly to a girl of 16 at a bread stall on a village green, morning market bustle around them, warm golden light")),
(165,165,"AI","Hollis watches her go — the closing reflection",
 ai("A man of 61 standing behind a market trestle table watching a girl of 16 walk away down a village lane in the low gold morning light, flour still on her skirt, quiet contentment, English village fair in the background")),
(165,165,"STOCK","Village fair morning in full swing, wide closing shot",
 "english village fair market green morning sunny bunting stalls"),
]

# new scenes to insert (new-paragraph-index range, TYPE, desc, prompt), placed by "insert_after" old scene position (0-indexed in old_scenes list)
new_inserts = {
    22: [  # after "The kneading begins — Hollis explains its purpose" scene index 22 (0-based) -> old_scenes[22] is (47,48,...)
        ("hydration", "AI", "Hollis judges the dough's hydration, holds back flour",
         ai("A man of 61 working a wide flour well by handfuls on a wooden trough table, judging the dough's wetness by touch, a girl of 16 watching closely, warm lantern light, stone bakehouse interior")),
    ],
    24: [  # after "Hollis guides her hands" scene (old index 24) -> insert new kneading-technique scenes
        ("kneading_test", "AI", "Hollis shows the stretch test, Meg practices tearing dough",
         ai("A man of 61 gently stretching a small piece of pale dough thin between his fingers to test it, a girl of 16 watching and trying the same motion herself, flour dust in lantern light, close hands-on teaching moment")),
    ],
}

# rebuild scenes with remapped indices, inserting new scenes at the right points
def remap_range(a, b):
    return M(a), M(b)

final_scenes = []
for idx, (a, b, typ, desc, prompt) in enumerate(old_scenes):
    na, nb = remap_range(a, b)
    final_scenes.append((na, nb, typ, desc, prompt))
    if idx in new_inserts:
        for _, ntyp, ndesc, nprompt in new_inserts[idx]:
            pass  # handled below via explicit paragraph indices

# Instead of index-based fuzzy insertion, place new scenes by explicit new-paragraph position.
extra_scenes = [
    (45, 45, "AI", "Hollis judges hydration, holds back the last flour",
     ai("A man of 61 working a wide flour well by handfuls on a wooden trough table, judging the dough's wetness by touch, a girl of 16 watching closely, warm lantern light, stone bakehouse interior")),
    (50, 51, "AI", "Flour your hands not the dough — the stretch test",
     ai("A man of 61 gently stretching a small piece of pale dough thin between his fingers to test it, a girl of 16 trying the same motion on her own dough beside him, flour dust in lantern light, close hands-on teaching moment")),
    (112, 115, "AI", "Meg's seam mistake — a flattened loaf, corrected",
     ai("A girl of 16 studying a flattened loaf of dough on a wooden table with a puzzled frown, a man of 61 pointing out the seam without looking up from his own work, warm lantern light, stone bakehouse interior")),
    (121, 128, "AI", "Meg and Hollis banter over the fire, she sweeps the embers",
     ai("A man of 61 gently stopping a girl of 16 from adding another log to a low fire, handing her a long-handled broom instead, warm ember glow, stone bakehouse interior, playful teaching moment")),
    (137, 137, "AI", "Checking the second rise before loading",
     ai("A man of 61 pressing a fingertip lightly into a row of shaped loaves on wooden boards, a girl of 16 watching and trying it herself on a small loaf, warm lantern light, stone bakehouse interior")),
    (174, 174, "STOCK", "Village green waking — cart, fiddler tuning, stallholders",
     "english village market green morning stalls fiddler bunting rustic"),
]

final_scenes.extend(extra_scenes)

# sort by start paragraph index, keep stable order for same-index scenes (church clock stock+AI, closing AI+STOCK)
final_scenes.sort(key=lambda s: (s[0], s[1]))

wc = None
text = open('/Users/aytacerdem/zenn/millbrook_story.txt').read().strip()
paras = [p for p in text.split('\n\n') if p.strip()]
wc = [len(p.split()) for p in paras]

def wcount(a, b):
    return sum(wc[i] for i in range(a, b + 1))

VO_DURATION = json.load(open('/tmp/vo_duration.json'))['seconds']

raw_durs = []
for (a, b, typ, desc, prompt) in final_scenes:
    w = wcount(a, b)
    raw_durs.append(max(w * 1.0, 8.0))  # placeholder scale, corrected below

total_w = sum(raw_durs)
scale = VO_DURATION / total_w

rows = []
t = 0.0
for (a, b, typ, desc, prompt), rd in zip(final_scenes, raw_durs):
    dur = rd * scale
    rows.append((t, dur, typ, desc, prompt, a, b))
    t += dur

total = t
print("TOTAL SCENES:", len(rows))
print("TOTAL TIME:", total, "target:", VO_DURATION)

json.dump([(a,b,typ,desc,prompt) for (a,b,typ,desc,prompt) in final_scenes], open('/tmp/final_scenes_check.json','w'))

def fmt(s):
    m = int(s // 60)
    sec = s - m * 60
    return f"{m:02d}:{sec:05.2f}"

lines = ["# The Night Bakers of Millbrook — Visual Plan v2", "",
         f"VO duration: {VO_DURATION:.2f}s | {len(rows)} scenes", "",
         "## Visual Type Legend",
         "- AI = GPT Image 2 (Hollis 61yo master baker, Meg 16yo apprentice — character consistency)",
         "- STOCK = verified period-appropriate stock video",
         "", "---", "",
         "| # | Time | Dur | Type | Scene | Prompt/Keywords |",
         "|---|---|---|---|---|---|"]
scenes_json = []
for i, (t0, dur, typ, desc, prompt, a, b) in enumerate(rows, 1):
    icon = "AI" if typ == "AI" else "STOCK"
    p = prompt.replace("|", "/")
    lines.append(f"| {i} | {fmt(t0)} | {dur:.1f}s | {icon} | {desc} | {p} |")
    scenes_json.append({"num": i, "time": fmt(t0), "dur": f"{dur:.2f}s", "type": typ, "desc": desc, "prompt": prompt})

open('/Users/aytacerdem/zenn/millbrook_visual_plan_v2.md', 'w').write('\n'.join(lines))
json.dump(scenes_json, open('/Users/aytacerdem/zenn/millbrook_scenes_v2.json', 'w'), indent=2)
print("written millbrook_visual_plan_v2.md and millbrook_scenes_v2.json")
