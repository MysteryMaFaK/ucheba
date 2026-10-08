import json, glob, re, datetime, sys
VR = {'Stormcrown VR','FUS','Tempus Maledictum VR','Librum VR','Yggdrasil VR',"Panda's Sovngarde",'Tahrovin','Tahrovin - Grit','Spirit of Grit'}
page = set(json.load(open('page_ids.json')))
mods = {}
for f in glob.glob('rep/*.json'):
    d = json.load(open(f)); ln = d['Name']; isvr = ln in VR
    for a in d['Archives']:
        o = a['Original']; s = o['State']; t = s.get('$type', '')
        if 'Nexus' not in t: continue
        g = str(s.get('Game', s.get('GameName', ''))).lower()
        if g and 'skyrim' not in g: continue
        mid = s.get('ModID'); name = s.get('Name') or ''
        ts = [int(m) for m in re.findall(r'-(1[5-9]\d{8})\.', o['Name'])]
        m2 = re.search(r'(20\d\d-\d\d-\d\d)T\d\d-\d\dZ', o['Name'])
        if m2: ts.append(int(datetime.datetime.fromisoformat(m2.group(1)).replace(tzinfo=datetime.UTC).timestamp()))
        e = mods.setdefault(mid, {'name': name, 'vr': set(), 'se': set(), 'newest': 0, 'files': set(), 'author': s.get('Author', '')})
        (e['vr'] if isvr else e['se']).add(ln)
        e['files'].add(o['Name'][:90])
        if ts: e['newest'] = max(e['newest'], max(ts))
TEX = re.compile(r'texture|retex|\b[1-8]k\b|upscal|\bhd\b|hd |remaster|armor|armour|weapon|outfit|hair|body|face|npc replacer|eyes|brows|skin|tattoo|follower|replacer|clothes|pbr|parallax textures|recolor|retexture|mesh improvement|\bcbbe\b|3ba|bodyslide|preset|voiced|vanilla hair|beard|race|elves|orcs|dragons? model|creatures? overhaul|shield|sword|bow\b|jewelry|circlet|landscape|mountain|rocks|terrain texture|snow texture|ruins|dungeon|interior|city|town|village|solitude|whiterun|riften|markarth|windhelm|falkreath|dawnstar|winterhold|morthal|riverwood|player home|house|homestead|banner|furniture|clutter|book|paper|map|icons?\b', re.I)
rows = []
for mid, e in mods.items():
    if mid in page: continue
    nv, ns = len(e['vr']), len(e['se'])
    dt = datetime.datetime.fromtimestamp(e['newest'], datetime.UTC).date() if e['newest'] else None
    score = nv * 2 + ns
    tex = bool(TEX.search(e['name']))
    rows.append(dict(id=mid, name=e['name'], vr=nv, se=ns, score=score, date=str(dt) if dt else '', tex=tex, vrlists=sorted(e['vr']), files=sorted(e['files'])[:3]))
rows.sort(key=lambda r: (-r['score'], r['name']))
json.dump(rows, open('cand_all.json', 'w'), ensure_ascii=False)
sel = [r for r in rows if not r['tex'] and r['score'] >= 5 and (r['date'] >= '2025-01-01' or r['vr'] >= 3)]
json.dump(sel, open('cand_sel.json', 'w'), ensure_ascii=False)
print(len(rows), 'total;', len(sel), 'selected')
for r in sel[:400]: print(f"{r['score']:>3} vr{r['vr']} se{r['se']:>2} {r['date']} #{r['id']} {r['name']}")
