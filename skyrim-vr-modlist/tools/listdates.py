import json,sys,re,datetime
d=json.load(open(sys.argv[1]))
seen={}
for a in d['Archives']:
    o=a['Original']; s=o['State']
    ts=[int(m) for m in re.findall(r'-(1[5-9]\d{8})\.', o['Name'])]
    m2=re.search(r'(20\d\d-\d\d-\d\d)T\d\d-\d\dZ', o['Name'])
    dt=datetime.datetime.fromtimestamp(max(ts),datetime.UTC).date().isoformat() if ts else (m2.group(1) if m2 else '')
    key=s.get('Name') or o['Name']
    seen.setdefault(key,[]).append((dt,o['Name'][:80], s.get('ModID','')))
for k in sorted(seen, key=str.lower):
    v=max(seen[k]); print(f"{k} | {v[2]} | {v[0]} | {v[1]}")
