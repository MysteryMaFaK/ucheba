import json, sys, re, datetime, collections
files = sys.argv[1:]
mods = {}
for f in files:
    d = json.load(open(f))
    ln = d['Name']
    for a in d['Archives']:
        o = a['Original']; s = o['State']; t = s.get('$type', '')
        if 'Nexus' not in t: continue
        if 'skyrim' not in str(s.get('GameName', 'skyrimspecialedition')).lower(): pass
        mid = s.get('ModID'); name = s.get('Name')
        ts = [int(m) for m in re.findall(r'-(1[5-9]\d{8})\.', o['Name'])]
        e = mods.setdefault(mid, {'name': name, 'lists': set(), 'newest': 0, 'file': ''})
        e['lists'].add(ln)
        if ts and max(ts) > e['newest']:
            e['newest'] = max(ts); e['file'] = o['Name']
out = []
for mid, e in mods.items():
    dt = datetime.datetime.fromtimestamp(e['newest'], datetime.UTC).date() if e['newest'] else ''
    out.append((len(e['lists']), mid, e['name'], str(dt), e['file'], ','.join(sorted(x[:6] for x in e['lists']))))
out.sort(key=lambda x: (-x[0], str(x[2])))
for r in out: print('\t'.join(str(x) for x in r))
