# usage: python3 -I whouses.py <nexus_mod_id or name substring>
import json, glob, sys, re, os
q = sys.argv[1]
VR = {'Stormcrown VR','FUS','Tempus Maledictum VR','Librum VR','Yggdrasil VR',"Panda's Sovngarde",'Tahrovin','Tahrovin - Grit','Spirit of Grit'}
for f in sorted(glob.glob(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'rep', '*.json'))):
    d = json.load(open(f))
    hits = []
    for a in d['Archives']:
        o = a['Original']; s = o['State']
        if (q.isdigit() and str(s.get('ModID')) == q) or (not q.isdigit() and q.lower() in (str(s.get('Name','')) + o['Name']).lower()):
            hits.append(o['Name'])
    if hits:
        print(('[VR] ' if d['Name'] in VR else '[SE] ') + d['Name'] + ': ' + '; '.join(sorted(set(hits))[:4]))
