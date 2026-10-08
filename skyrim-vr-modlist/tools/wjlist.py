import json, sys
d = json.load(open(sys.argv[1]))
print('#', d['Name'], d['Version'], len(d['Archives']))
rows = []
for a in d['Archives']:
    o = a['Original']; s = o['State']; t = s.get('$type', '')
    if 'Nexus' in t:
        rows.append(f"N {s.get('ModID')}\t{s.get('Name')}\t{s.get('Version')}\t[{o['Name']}]")
    elif 'GameFile' in t:
        continue
    else:
        rows.append(f"O {t.split(',')[0]}\t{o['Name']}\t{s.get('Url', '')[:100]}")
for r in sorted(rows): print(r)
