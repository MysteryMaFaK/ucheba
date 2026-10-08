import json, re
rows = json.load(open('cand_all.json'))
# SE-only twins of things already on the page (VR equivalents present) or SE base tools
SKIP_IDS = {17230, 32444, 30379, 60805, 36869, 12604, 76649, 12688, 18619, 34705, 92454, 61950, 117389, 86492, 111991, 52897, 97720, 23316, 137741, 60690, 111236}
CONTENT = re.compile(r'quest|lines expansion|dialogue|follower|inigo|lucien|serana|wyrmstooth|bruma|legacy of the dragonborn|lotd|player home|outpost|vigilant|siege|sirenroot|saturalia|icerunner|derkeethus|helgi|dibella|brotherhood|whispering door|infiltration|innocence lost|caught red handed|only cure|nilheim|paarthurnax|clockwork|darkend|karstaag|tools of kagrenac|soul cairn|praedy|saints and seducers|missives|jk\'s|identity crisis|gift of saturalia|beyond skyrim|interesting npcs|pandorable|kalilies|modpocalypse|bijin|northborn|marks of beauty|makeup|rustic|\bjs |fyx|rally|cathedral - 3d|stonewalls|signs|statues|pottery|garlic|kitchenware|knapsacks|purses|septims|claws|chalice|cages|shrines|utopia|amulets|peltapalooza|rugnarok|giant|troll|draugr|mammoth|sabrecat|spriggan|frostbite|death hound|elderscroll|daedra|reliefs|cooking|soulgems|ancient dwemer metal|dwemer pipework|iconic|blackreach|candlehearth|jorrvaskr|rowboat|dock|shack|stockades|wells|chimney|ravenrock|horns|potions redone|security overhaul|lock', re.I)
CATS = [
 ('fixes_frameworks', re.compile(r'fix|framework|distributor|papyrus|extender|injector|engine|crash|freeze|patch hub|console|ini manipulator|dtry|plugin updates|recursion|categorization|keyword|function|loader|skeleton|xpmsse|uiextensions|mfg', re.I)),
 ('animation_physics', re.compile(r'animation|anim|idle|motion|movement|get up|hands|seat|gesture|vanargand|goetia|cbpc|physics|smp|ragdoll|behavior|nemesis|pandora|dodge|casting|sneak', re.I)),
 ('visuals_vfx_world', re.compile(r'vfx|effect|ember|light|lux|weather|sky|moon|star|cloud|fog|mist|volumetric|water|waterfall|snow|ash|grass|tree|aspen|flora|forest|plant|terrain|lod|smok|torch|candle|fire|frost|lightning|impact|spell impacts|particle|reflection|wetness|footprint|road|blended|aurora|shader|parallax|glow|dust|wind|reshade|enb', re.I)),
 ('audio', re.compile(r'sound|audio|music|bard|song|reverb|ambien|voice|echo|winds|symphony|acoustic', re.I)),
 ('gameplay_systems', re.compile(r'overhaul|perk|ordinator|vokrii|adamant|mysticism|apocalypse|thaumaturgy|apothecary|alchemy|sorcerer|artificer|scion|manbeast|growl|pilgrim|mundus|gourmet|experience|level|encounter|loot|barter|trade|bribe|bounty|headhunter|survival|sunhelm|campfire|travel|carriage|recipe|reading|skill|soul trap|gist|enchant|smart npc|ai |detection|raid|pathing|combat|stagger|archery|attack|reanimation|necromancy|invisibility|frenzy|death drop|mum|water ai|rejections|honed metal|ore veins|cc\'s', re.I)),
 ('ui_qol', re.compile(r'hud|ui|menu|favorite|quest objectives|ebqo|subtitles|descriptions|skip|loading screen|truce|photo|mcm|map|compass|talk|whose quest|informative', re.I)),
]
out = {c: [] for c, _ in CATS}; out['other'] = []
for r in rows:
    if r['id'] in SKIP_IDS or r['tex']: continue
    if CONTENT.search(r['name']): continue
    if r['score'] < 7: continue
    if not (r['date'] >= '2024-01-01' or r['vr'] >= 3): continue
    for c, rx in CATS:
        if rx.search(r['name']): out[c].append(r); break
    else: out['other'].append(r)
for c, v in out.items():
    print(c, len(v))
    with open(f'cat_{c}.txt', 'w') as f:
        for r in v:
            f.write(f"#{r['id']} | {r['name']} | VR-lists:{r['vr']} SE-lists:{r['se']} | newest file {r['date']} | in VR lists: {', '.join(r['vrlists']) or '-'} | files: {'; '.join(r['files'][:2])}\n")
