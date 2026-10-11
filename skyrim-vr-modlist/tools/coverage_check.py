"""Детерминированная проверка полноты (вместо дорогого агента-критика): какие популярные в VR-сборках моды не попали ни в одно решение.

  python3 -I tools/coverage_check.py [минимум_VR_сборок=2]
Считает моды Nexus из data/rep (>= N VR-сборок), которых нет в ядре, в Other Mods (любое решение: оставлено/отброшено),
во «взаимодействии в VR», в списках auto_excluded и prefilter_skipped. Печатает остаток по темам. Токенов не тратит."""
import collections, glob, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE); DATA = os.path.join(ROOT, 'data'); O2 = os.path.join(DATA, 'other2')
MIN_VR = int(sys.argv[1]) if len(sys.argv) > 1 else 2
VR = {'Stormcrown VR', 'FUS', 'Tempus Maledictum VR', 'Librum VR', 'Yggdrasil VR', "Panda's Sovngarde", 'Tahrovin', 'Tahrovin - Grit', 'Spirit of Grit'}
norm = lambda s: re.sub(r'[^a-z0-9]+', '', s.lower())
mods = {}
for f in glob.glob(os.path.join(DATA, 'rep', '*.json')):
    d = json.load(open(f, encoding='utf-8')); ln = d['Name']
    for a in d['Archives']:
        s = a['Original']['State']
        if 'Nexus' not in s.get('$type', ''): continue
        e = mods.setdefault(s.get('ModID'), dict(name=s.get('Name') or '', vr=set(), se=set()))
        (e['vr'] if ln in VR else e['se']).add(ln)
seen = set()
man = open(os.path.join(ROOT, 'manifest.yaml'), encoding='utf-8').read()
seen |= {int(x) for x in re.findall(r'nexusmods\.com/skyrimspecialedition/mods/(\d+)', man)}
seen |= set(json.load(open(os.path.join(DATA, 'page_ids.json'))))
for v in json.load(open(os.path.join(DATA, 'other_result.json'), encoding='utf-8'))['result']['verified']:
    if v.get('id'): seen.add(v['id'])
for p in ('done_ids.json',):
    q = os.path.join(O2, p)
    if os.path.exists(q): seen |= set(json.load(open(q)))
for f in glob.glob(os.path.join(DATA, 'partial', 'other-mods__collect_r2-*.json')):
    for e in json.load(open(f, encoding='utf-8')).get('entries', []):
        if e.get('id'): seen.add(e['id'])
for f in glob.glob(os.path.join(DATA, 'partial', 'vr-interaction__collect_ix*.json')):
    d = json.load(open(f, encoding='utf-8'))
    for p in d.get('picks', []) + d.get('considered_dropped', []):
        if p.get('id'): seen.add(p['id'])
for t in ('auto_excluded.tsv', 'prefilter_skipped.tsv'):
    q = os.path.join(O2, t)
    if os.path.exists(q):
        for ln in open(q, encoding='utf-8').read().split('\n')[1:]:
            if ln.split('\t')[0].isdigit(): seen.add(int(ln.split('\t')[0]))
bp = set()
for f in glob.glob(os.path.join(DATA, 'pools', 'b*.txt')):
    for l in open(f, encoding='utf-8'):
        if l.startswith('#'): bp.add(int(l.split('|')[0][1:]))
rest = [(len(e['vr']), len(e['se']), mid, e['name']) for mid, e in mods.items() if mid not in seen and mid not in bp and len(e['vr']) >= MIN_VR]
rest.sort(key=lambda r: (-r[0], -r[1], r[3]))
print(f'не покрыто решениями, в >= {MIN_VR} VR-сборках: {len(rest)}')
for r in rest[:60]: print(f'  vr{r[0]} se{r[1]:2d} #{r[2]} {r[3][:80]}')
