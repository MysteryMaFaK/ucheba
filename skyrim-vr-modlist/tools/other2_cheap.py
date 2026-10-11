"""Дешёвый проход по полосам C и D второго прохода «Other Mods»: предфильтр без агентов + крупные пакеты + компактный перечень уже взятого.

  python3 -I tools/other2_cheap.py   (после tools/other2_batches.py)
    -> data/other2/batches/E01.json ...   пакеты по ~80 элементов (полосы C и D после предфильтра)
    -> data/other2/prefilter_skipped.tsv  всё, что отсеяно без агентов, с причиной
    -> data/other2/inventory_compact.txt  ядро + Other-1 + «взаимодействие в VR»: id и название, ~15 КБ вместо чтения MODLIST/OTHER_MODS
Правила предфильтра (по данным оценки полос A и B: у таких признаков доля «оставлено» минимальна или нулевая польза для VR):
  1. VR-сборок 0 (мод есть только в SE-сборках)  -> пропуск
  2. «ENB» в названии (ENB в сборке нет)          -> пропуск
  3. «patch» в названии, а база не в наших списках -> пропуск
Исходные пакеты C/D переносятся в data/other2/batches_full_CD/ (они не нужны воркфлоу).
ВАЖНО: tools/other2_batches.py при запуске стирает все пакеты в batches/ и создаёт C/D заново — после него запускайте этот скрипт снова."""
import collections, glob, json, os, re, shutil

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE); O2 = os.path.join(ROOT, 'data', 'other2'); B = os.path.join(O2, 'batches')
BATCH_W = 80


def norm(s):
    return re.sub(r'[^a-z0-9]+', '', s.lower())


# --- перечень уже взятого
inv = []
man = open(os.path.join(ROOT, 'manifest.yaml'), encoding='utf-8').read().split('\n')
cur = None
for ln in man:
    m = re.match(r'- id: (\d+|null)\s*$', ln)
    if m:
        cur = m.group(1); continue
    m = re.match(r'  name: (.*)$', ln)
    if m and cur is not None:
        inv.append(('core', None if cur == 'null' else int(cur), m.group(1).strip().strip("'\""))); cur = None
for v in json.load(open(os.path.join(ROOT, 'data', 'other_result.json'), encoding='utf-8'))['result']['verified']:
    if v.get('keep') and v.get('round', 1) == 1:
        inv.append(('other1', v.get('id'), v['name']))
ixp = os.path.join(ROOT, 'data', 'vr_interaction_result.json')
if os.path.exists(ixp):
    for v in json.load(open(ixp, encoding='utf-8'))['kept']:
        inv.append(('ix', v.get('id'), v['name']))
with open(os.path.join(O2, 'inventory_compact.txt'), 'w', encoding='utf-8') as f:
    f.write('# Уже взято: [core]=ядро, [other1]=Other Mods первый проход, [ix]=взаимодействие в VR. Формат: #id название\n')
    for src, i, n in inv:
        f.write(f"[{src}] {'#%d ' % i if i else ''}{n}\n")
covered = [norm(n) for _, _, n in inv if len(norm(n)) >= 8]

# --- исходные пакеты C/D
full = os.path.join(O2, 'batches_full_CD')
os.makedirs(full, exist_ok=True)
for fpath in glob.glob(os.path.join(B, '[CD]*.json')):   # свежие C/D от other2_batches.py заменяют прежние
    shutil.move(fpath, os.path.join(full, os.path.basename(fpath)))
rows = []
for fpath in sorted(glob.glob(os.path.join(full, '[CD]*.json'))):
    d = json.load(open(fpath, encoding='utf-8'))
    rows += d['items']
for fpath in glob.glob(os.path.join(B, 'E*.json')):
    os.remove(fpath)

skipped, keep = [], []
for r in rows:
    reason = None
    if r['vr'] == 0:
        reason = 'только SE-сборки, ни одна VR-сборка не ставит'
    elif re.search(r'\benb\b', r['name'], re.I):
        reason = 'ENB в сборке не используется'
    elif re.search(r'patch', r['name'], re.I):
        n = norm(r['name'])
        if not any(c in n for c in covered):
            reason = 'патч к моду вне наших списков'
    if reason:
        skipped.append((r['id'], r['name'], r['band'], r['vr'], r['se'], reason, 1 + len(r.get('members', [])) - (1 if r.get('members') else 0)))
    else:
        keep.append(r)
with open(os.path.join(O2, 'prefilter_skipped.tsv'), 'w', encoding='utf-8') as f:
    f.write('id\tname\tband\tvr\tse\tпричина\tмодов\n')
    for row in sorted(skipped, key=lambda x: (x[5], x[2], -x[3], x[1])):
        f.write('\t'.join(str(x) for x in row) + '\n')

keep.sort(key=lambda r: (r['theme'], -r['score'], r['name']))
batches, cur, w = [], [], 0.0
for r in keep:
    wt = 1 + 0.1 * len(r.get('members', []))
    if cur and w + wt > BATCH_W:
        batches.append(cur); cur, w = [], 0.0
    cur.append(r); w += wt
if cur:
    batches.append(cur)
sizes = {}
for n, b in enumerate(batches, 1):
    bid = 'E%02d' % n
    slim = []
    for i in b:   # компактная карточка кандидата: всё, что нужно для решения без вызовов инструментов
        c = dict(key=i['key'], id=i['id'], name=i['name'][:110], vr=i['vr'], se=i['se'], newest=i['newest'], vr_lists=[x[:14] for x in i['vr_lists']], file=(i['files'][0][:70] if i['files'] else ''), theme=i['theme'])
        if i.get('members'):
            c['members'] = [dict(id=m['id'], name=m['name'][:80], vr=m['vr'], se=m['se']) for m in i['members']]
        slim.append(c)
    json.dump(dict(batch=bid, band='E', themes=dict(collections.Counter(i['theme'] for i in b)), items=slim), open(os.path.join(B, bid + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    sizes[bid] = len(b)
by = collections.Counter(s[5] for s in skipped)
print(json.dumps(dict(исходно=len(rows), пропущено=len(skipped), причины=dict(by), осталось=len(keep), пакетов=len(batches), sizes=sizes, инвентарь=len(inv)), ensure_ascii=False))
