"""Второй проход «Other Mods 2026»: нарезка непросмотренных кандидатов на пакеты для агентов.

  python3 -I tools/other2_batches.py            -> data/other2/batches/<полоса>_<NN>.json, data/other2/auto_excluded.tsv, data/other2/summary.json

Кандидат = мод с Nexus из архивов 27 сборок (data/rep/), которого нет ни в ядре, ни среди проверенных в первом проходе,
ни в пулах ядра (data/pools/b*.txt). Ничего не отбрасывается молча: авто-исключения по правилам владельца лежат в auto_excluded.tsv.
Полосы по популярности (score = 2*VR-сборки + SE-сборки): A >= 12, B 8-11, C 6-7, D 4-5. Ниже 4 не берём (видно в summary.json).
Серии (FYX, Cathedral 3D, «... Armors and Weapons Retexture SE» и т. п.) склеиваются в один элемент с перечнем участников."""
import collections, datetime, glob, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, 'data')
OUT = os.path.join(DATA, 'other2')
BATCH_DIR = os.path.join(OUT, 'batches')
VR = {'Stormcrown VR', 'FUS', 'Tempus Maledictum VR', 'Librum VR', 'Yggdrasil VR', "Panda's Sovngarde", 'Tahrovin', 'Tahrovin - Grit', 'Spirit of Grit'}
BATCH_SIZE = 36   # «вес» пакета: одиночный мод = 1, серия = 1 + 0.15 * участников


def norm(s):
    return re.sub(r'[^a-z0-9]+', '', s.lower())


# --- 1. все моды Nexus из 27 сборок
mods = {}
for f in glob.glob(os.path.join(DATA, 'rep', '*.json')):
    d = json.load(open(f, encoding='utf-8'))
    ln = d['Name']
    for a in d['Archives']:
        o = a['Original']; s = o['State']
        if 'Nexus' not in s.get('$type', ''):
            continue
        g = str(s.get('Game', s.get('GameName', ''))).lower()
        if g and 'skyrim' not in g:
            continue
        mid = s.get('ModID')
        ts = [int(m) for m in re.findall(r'-(1[5-9]\d{8})\.', o['Name'])]
        m2 = re.search(r'(20\d\d-\d\d-\d\d)T\d\d-\d\dZ', o['Name'])
        if m2:
            ts.append(int(datetime.datetime.fromisoformat(m2.group(1)).replace(tzinfo=datetime.timezone.utc).timestamp()))
        e = mods.setdefault(mid, {'name': s.get('Name') or '', 'vr': set(), 'se': set(), 'newest': 0, 'files': set(), 'author': s.get('Author', '')})
        (e['vr'] if ln in VR else e['se']).add(ln)
        e['files'].add(o['Name'][:100])
        if ts:
            e['newest'] = max(e['newest'], max(ts))

# --- 2. что уже покрыто
core = set(json.load(open(os.path.join(DATA, 'page_ids.json'))))
man = open(os.path.join(ROOT, 'manifest.yaml'), encoding='utf-8').read()
core |= {int(x) for x in re.findall(r'nexusmods\.com/skyrimspecialedition/mods/(\d+)', man)}
core |= {int(x) for x in re.findall(r'^\s*-?\s*id: (\d+)\s*$', man, re.M)}
for f in ('additions.py', 'build_page.py'):
    core |= {int(x) for x in re.findall(r'mods/(\d{3,6})', open(os.path.join(HERE, f), encoding='utf-8').read())}
ver = json.load(open(os.path.join(DATA, 'other_result.json'), encoding='utf-8'))['result']['verified']
done_ids = {v['id'] for v in ver if v.get('id')}
done_names = {norm(v['name']) for v in ver}
extra_done = os.path.join(OUT, 'done_ids.json')   # id из второго прохода (пополняется после каждого запуска)
if os.path.exists(extra_done):
    done_ids |= set(json.load(open(extra_done)))
bpool = set()
for f in glob.glob(os.path.join(DATA, 'pools', 'b*.txt')):
    for l in open(f, encoding='utf-8'):
        if l.startswith('#'):
            bpool.add(int(l.split('|')[0][1:]))
SKIP = {17230, 32444, 30379, 60805, 36869, 12604, 76649, 12688, 18619, 34705, 92454, 61950, 117389, 86492, 111991, 52897, 97720, 23316, 137741, 60690, 111236}

# отложенные в первом проходе: id из заметок сборщиков (берём независимо от популярности)
leftover = set()
for f in glob.glob(os.path.join(DATA, 'partial', 'other-mods__collect_*.json')):
    d = json.load(open(f, encoding='utf-8'))
    leftover |= {int(x) for x in re.findall(r'\b(\d{4,6})\b', d.get('notes', '')) if not 2018 <= int(x) <= 2030 and int(x) not in (1024, 2048, 4096, 8192, 1280, 1920)}

# --- 3. правила владельца: контент, оверхолы сложности, пакеты заклинаний, узкий SimonRim, NSFW
EXCL = [
    ('контент: квесты/земли/реплики', r'quest expansion|lines expansion|quest mod|quest and|and quest|- quest|quest\)|wyrmstooth|legacy of the dragonborn|\blotd\b|beyond skyrim|bruma|forgotten city|saints and seducers|vigilant|dialogue|new land|nilheim|\bsiege\b'),
    ('контент: спутники/NPC-персонажи', r'follower|companion|inigo|lucien|serana|interesting npcs|3dnpc|\bnpc overhaul'),
    ('контент: дома игрока', r'player home|homestead|outpost|hendraheim|\bmanor\b.*home|home\b.*(player|owner)'),
    ('крупные оверхолы сложности', r'requiem|wildlander|ordinator|vokrii|vokriinator'),
    ('пакеты заклинаний и криков', r'apocalypse|arcanum|triumvirate|thunderchild|\bodin\b'),
    ('узкие части SimonRim', r'aetherius|\bscion\b|manbeast|\bpilgrim\b'),
    ('NSFW', r'sexlab|ostim|nsfw|erotic|\bsex\b|lovers|nude'),
]
EXCL = [(r, re.compile(p, re.I)) for r, p in EXCL]


def excluded(name):
    for reason, rx in EXCL:
        if rx.search(name):
            return reason
    return None


# --- 4. кандидаты и полосы
def band(score):
    return 'A' if score >= 12 else 'B' if score >= 8 else 'C' if score >= 6 else 'D' if score >= 4 else None


cands, auto = [], []
for mid, e in mods.items():
    if mid in core or mid in done_ids or norm(e['name']) in done_names or mid in bpool or mid in SKIP:
        continue
    nv, ns = len(e['vr']), len(e['se'])
    score = nv * 2 + ns
    b = band(score)
    if mid in leftover and b is None:
        b = 'D'
    if mid in leftover and b in ('C', 'D'):
        b = 'A'   # отложенное в первом проходе — в первую очередь
    if b is None:
        continue
    dt = datetime.datetime.fromtimestamp(e['newest'], datetime.timezone.utc).date().isoformat() if e['newest'] else ''
    r = dict(id=mid, name=e['name'], vr=nv, se=ns, score=score, band=b, newest=dt, vr_lists=sorted(e['vr']), se_lists=len(e['se']),
             files=sorted(e['files'])[:3], author=e['author'], leftover=mid in leftover)
    why = excluded(e['name'])
    if why and not r['leftover']:
        auto.append((mid, e['name'], b, nv, ns, why))
    else:
        cands.append(r)

# --- 5. серии: общий префикс (2 слова) или общий хвост (3+ слов) у >= 3 модов
def words(n):
    return [w for w in re.split(r'[^a-z0-9\']+', n.lower()) if w]


pref, suf = collections.defaultdict(list), collections.defaultdict(list)
for r in cands:
    w = words(r['name'])
    if len(w) >= 3:
        pref[' '.join(w[:2])].append(r['id'])
        suf[' '.join(w[-3:])].append(r['id'])
by_id = {r['id']: r for r in cands}
GENERIC = {'the', 'a', 'an', 'skyrim', 'sse', 'se', 'vr', 'new', 'old', 'better', 'improved', 'simple', 'realistic', 'dynamic', 'immersive', 'more', 'vanilla', 'hd', 'enhanced', 'special', 'edition', 'high', 'quality', 'elder', 'dragon', 'ancient', 'complex', 'smart', 'unofficial', 'real'}
series_of = {}
for key, ids in sorted(list(pref.items()) + list(suf.items()), key=lambda kv: -len(kv[1])):
    ids = [i for i in ids if i not in series_of]
    ks = key.split()
    if len(ids) < 3 or all(k in GENERIC for k in ks):
        continue
    for i in ids:
        series_of[i] = key
groups = collections.defaultdict(list)
for r in cands:
    groups[series_of.get(r['id'], 'id:%d' % r['id'])].append(r)
items = []
for key, rs in groups.items():
    rs.sort(key=lambda r: (-r['score'], r['name']))
    head = rs[0]
    it = dict(head, key='id:%d' % head['id'])
    if len(rs) > 1:
        it['series'] = key
        it['members'] = [dict(id=m['id'], name=m['name'], vr=m['vr'], se=m['se'], newest=m['newest'], files=m['files'][:1]) for m in rs]
        it['name'] = '[серия «%s», %d модов] %s и др.' % (key, len(rs), head['name'])
        it['vr'] = max(m['vr'] for m in rs); it['se'] = max(m['se'] for m in rs); it['score'] = max(m['score'] for m in rs)
        it['band'] = min(m['band'] for m in rs)
        it['leftover'] = any(m['leftover'] for m in rs)
    items.append(it)

# --- 6. тема пакета (для соседства похожих модов; агент вправе поменять раздел)
THEMES = [
    ('armor', r'armor|armour|weapon|sword|bow\b|shield|dagger|helm|outfit|cloth|robe|jewel|circlet|amulet|ring\b|gear|retexture se|\bsets?\b|cuirass|boots|cloak|hood|quiver|staff'),
    ('body_face', r'body|bodyslide|cbbe|3ba|himbo|bhunp|skin|face|hair|eyes|brows|beard|makeup|warpaint|tattoo|nord|preset|race|breton|redguard|argonian|khajiit|elf|orc|imperial|npc|head|teeth|mouth|lips|scar|freckle|racemenu|expression'),
    ('creatures', r'dragon|draugr|falmer|troll|spriggan|wolf|bear|sabrecat|mammoth|giant|horse|creature|animal|hagraven|atronach|daedra|dremora|skeleton|bat|bird|fish|deer|rabbit|goat|skeever|spider|chaurus|death hound|werewolf|vampire|undead|monster|ghost|wisp'),
    ('land_nature', r'landscape|terrain|mountain|rock|stone|snow|ice|road|path|grass|tree|flora|plant|flower|forest|aspen|pine|fern|bush|swamp|water|waterfall|river|sky|cloud|moon|star|galaxy|aurora|cave|lod|cliff|dirt|mud|sand|ash|volcan'),
    ('arch_city', r'city|town|village|whiterun|solitude|riften|markarth|windhelm|falkreath|dawnstar|winterhold|morthal|riverwood|rorikstead|ivarstead|helgen|fort|castle|tower|wall|gate|bridge|dock|house|inn\b|tavern|building|ruin|dwemer|nordic|dungeon|interior|door|window|chimney|roof|fence|sign|banner|smim|jk\'s|fyx|medieval|market|shack|stable|mill|farm|cathedral|temple|shrine'),
    ('clutter_misc', r'clutter|furniture|food|book|bottle|potion|barrel|crate|candle|lantern|torch|chair|table|bed|bucket|pot|basket|plate|mug|key|coin|gem|ingot|ore|pelt|scroll|map|paper|icon|ui\b|menu|hud|font|loading|sound|music|audio|reshade|enb|preset|tool|script|fix|patch|framework|utility|manager|loader'),
]
THEMES = [(t, re.compile(p, re.I)) for t, p in THEMES]
for it in items:
    txt = it['name'] + ' ' + ' '.join(m['name'] for m in it.get('members', []))
    it['theme'] = next((t for t, rx in THEMES if rx.search(txt)), 'other')

# --- 7. пакеты
def weight(it):
    return 1 + 0.15 * len(it.get('members', []))


os.makedirs(BATCH_DIR, exist_ok=True)
for f in glob.glob(os.path.join(BATCH_DIR, '*.json')):
    os.remove(f)
summary = collections.OrderedDict()
for bnd in 'ABCD':
    pool = sorted([it for it in items if it['band'] == bnd], key=lambda it: (it['theme'], -it['score'], it['name']))
    batches, cur, w = [], [], 0.0
    for it in pool:
        if cur and w + weight(it) > BATCH_SIZE:
            batches.append(cur); cur, w = [], 0.0
        cur.append(it); w += weight(it)
    if cur:
        batches.append(cur)
    summary[bnd] = dict(items=len(pool), mods=sum(1 + len(i.get('members', [])) - (1 if i.get('members') else 0) for i in pool), batches=len(batches))
    for n, b in enumerate(batches, 1):
        themes = collections.Counter(i['theme'] for i in b)
        json.dump(dict(batch='%s%02d' % (bnd, n), band=bnd, themes=dict(themes), items=b), open(os.path.join(BATCH_DIR, '%s%02d.json' % (bnd, n)), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
with open(os.path.join(OUT, 'auto_excluded.tsv'), 'w', encoding='utf-8') as f:
    f.write('id\tname\tband\tvr\tse\tpричина\n'.replace('pричина', 'причина'))
    for row in sorted(auto, key=lambda x: (x[2], -x[3], x[1])):
        f.write('\t'.join(str(x) for x in row) + '\n')
below = sum(1 for mid, e in mods.items() if not (mid in core or mid in done_ids or mid in bpool or mid in SKIP) and band(len(e['vr']) * 2 + len(e['se'])) is None)
summary['auto_excluded'] = len(auto)
summary['below_threshold_not_taken'] = below
summary['series_items'] = sum(1 for i in items if i.get('members'))
json.dump(summary, open(os.path.join(OUT, 'summary.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(json.dumps(summary, ensure_ascii=False, indent=1))
