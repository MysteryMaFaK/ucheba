"""Сводная выгрузка всего исследования: по каждому моду Nexus из 27 сборок — где он у нас и почему.

  python3 -I tools/export_all.py
    -> data/export/mods_all.csv       одна строка на мод (Excel/LibreOffice: UTF-8, разделитель «;»)
    -> data/export/mods_all.json      то же + полные решения агентов
    -> data/export/flat_candidates.csv  подборка для ПЛОСКОЙ версии (Skyrim SE/AE): моды, отсеянные только из-за VR,
                                        и популярные в SE-сборках, которые мы не оценивали
Нужна папка data/rep (python tools/fetch_reports.py). Токенов не тратит.

status — итоговое решение (по приоритету):
  core                  в ядре Skyrim VR Core 2026 (manifest.yaml)
  interaction_keep/_dont  «Взаимодействие в VR» (VR_INTERACTION.md): взят / «не ставить в VR»
  other_keep/_dont      «Other Mods 2026» (первый или второй проход): взят / «не ставить в VR»
  core_research_keep/_dont  исследование ядра (data/wf1.json, wf2.json): одобрен / «не ставить в VR» (обычно — нет VR-версии)
  se_twin_of_core       SE/AE-аналог мода ядра (SKSE64, Address Library, Engine Fixes, SkyUI...): в VR взят VR-вариант
  rejected              предложен агентом, снят проверяющим (причина в reason)
  dropped               отброшен агентом-сборщиком (drop_code и причина в reason)
  auto_excluded         отсеян правилами владельца без агентов (контент, спутники, оверхолы сложности, NSFW...)
  prefilter_skipped     отсеян предфильтром без агентов (только SE-сборки / ENB / патч к моду вне списков)
  core_pool_considered  был в пуле кандидатов ядра, отдельного решения не сохранилось
  not_evaluated         не рассматривался (непопулярен: < 4 очков популярности)
flat_hint — подсказка для плоской версии:
  flat_base             SE/AE-основа вместо VR-варианта из ядра
  vr_only               VR-специфичный мод (в плоской версии не нужен или есть SE-аналог)
  flat_candidate        отсеян ТОЛЬКО из-за VR (нет VR-версии, flat-only, DLL без VR) — для плоской версии стоит рассмотреть
  se_popular_unreviewed популярен в SE-сборках (>= 4), но нами не оценивался"""
import collections, csv, glob, json, os, re

import yaml

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE); DATA = os.path.join(ROOT, 'data'); O2 = os.path.join(DATA, 'other2'); P = os.path.join(DATA, 'partial')
OUT = os.path.join(DATA, 'export')
NX = 'https://www.nexusmods.com/skyrimspecialedition/mods/{}'
VR = {'Stormcrown VR', 'FUS', 'Tempus Maledictum VR', 'Librum VR', 'Yggdrasil VR', "Panda's Sovngarde", 'Tahrovin', 'Tahrovin - Grit', 'Spirit of Grit'}
ld = lambda p: json.load(open(p, encoding='utf-8'))
VR_NAME = re.compile(r'\bvr\b|virtual reality|higgs|planck|vrik|room.?scale|openxr|opencomposite|skyrimvr', re.I)
VR_DROP = re.compile(r'vr|флэт|flat|плоск|dll без|нет vr|только se|se-only|не работает в vr', re.I)

# --- 1. все моды Nexus из 27 сборок
mods = {}
for f in sorted(glob.glob(os.path.join(DATA, 'rep', '*.json'))):
    d = ld(f); ln = d['Name']
    for a in d['Archives']:
        o = a['Original']; s = o['State']
        if 'Nexus' not in s.get('$type', ''):
            continue
        mid = s.get('ModID')
        if mid is None:
            continue
        mid = int(mid)
        e = mods.setdefault(mid, dict(id=mid, name=s.get('Name') or '', author=s.get('Author') or '', vr=set(), se=set(), files=set(), newest=''))
        (e['vr'] if ln in VR else e['se']).add(ln)
        e['files'].add(o['Name'])
        m = re.search(r'-(1[5-9]\d{8})\.', o['Name'])
        if m:
            import datetime
            dt = datetime.datetime.fromtimestamp(int(m.group(1)), datetime.timezone.utc).date().isoformat()
            e['newest'] = max(e['newest'], dt)

rows = {}
def row(mid, name=''):
    if mid not in rows:
        e = mods.get(mid)
        rows[mid] = dict(id=mid, name=(e['name'] if e else name) or name, author=e['author'] if e else '', url=NX.format(mid) if isinstance(mid, int) else '',
                         vr_lists_n=len(e['vr']) if e else 0, se_lists_n=len(e['se']) if e else 0,
                         vr_lists=', '.join(sorted(e['vr'])) if e else '', se_lists=', '.join(sorted(e['se'])) if e else '',
                         newest_file=e['newest'] if e else '', sample_file=sorted(e['files'])[-1] if e and e['files'] else '',
                         status='not_evaluated', where='', section='', tag='', what='', reason='', vr_status='', flat_hint='', decisions=[])
    return rows[mid]
for mid in mods:
    row(mid)

RANK = ['core', 'interaction_keep', 'interaction_dont', 'other_keep', 'other_dont', 'core_research_keep', 'core_research_dont', 'se_twin_of_core', 'rejected', 'dropped',
        'auto_excluded', 'prefilter_skipped', 'core_pool_considered', 'not_evaluated']
def put(mid, status, where, name='', **kw):
    if mid in (None, '', 'null'):
        return
    try:
        mid = int(mid)
    except (TypeError, ValueError):
        return
    r = row(mid, name)
    r['decisions'].append(dict(status=status, where=where, **kw))
    if RANK.index(status) < RANK.index(r['status']):
        r['status'], r['where'] = status, where
        for k in ('section', 'tag', 'what', 'reason', 'vr_status'):
            if kw.get(k):
                r[k] = str(kw[k])

# --- 2. решения, от слабых к сильным (put сам держит самое сильное)
for f in glob.glob(os.path.join(DATA, 'pools', 'b*.txt')):
    for l in open(f, encoding='utf-8'):
        if l.startswith('#'):
            put(l.split('|')[0][1:].strip(), 'core_pool_considered', 'пул кандидатов ядра ' + os.path.basename(f))
for t, st in (('prefilter_skipped.tsv', 'prefilter_skipped'), ('auto_excluded.tsv', 'auto_excluded')):
    q = os.path.join(O2, t)
    if os.path.exists(q):
        lines = open(q, encoding='utf-8').read().split('\n')
        hdr = lines[0].split('\t')
        for ln in lines[1:]:
            c = ln.split('\t')
            if c and c[0].isdigit():
                put(c[0], st, 'Other Mods, второй проход (без агентов)', name=c[1], reason=c[hdr.index('причина')] if 'причина' in hdr else c[-1])
# второй проход: решения сборщиков
for f in glob.glob(f'{P}/other-mods__collect_r2-*.json'):
    for e in ld(f).get('entries', []):
        if e['decision'] == 'drop':
            put(e.get('id'), 'dropped', 'Other Mods, второй проход', name=e['name'], reason=f"{e['drop_code']}: {e['note']}", vr_status=e.get('vr_status'))
# первый проход: что сборщики назвали в заметках как отложенное — нет решений по id, пропускаем
# взаимодействие в VR: отброшенные сборщиками и снятые проверяющими
ixr = os.path.join(DATA, 'vr_interaction_result.json')
ix = ld(ixr) if os.path.exists(ixr) else {}
for d in ix.get('dropped_by_collectors', []):
    put(d.get('id'), 'dropped', 'Взаимодействие в VR', name=d['name'], reason=d['reason'])
ix_picks = {}
for f in glob.glob(f'{P}/vr-interaction__collect_ix*.json'):
    for p in ld(f).get('picks', []):
        ix_picks[p['name']] = p
for name, why, *_ in ix.get('rejected', []):
    p = ix_picks.get(name)
    if p:
        put(p.get('id'), 'rejected', 'Взаимодействие в VR', name=name, reason=why, vr_status=p.get('vr_status'), section=p.get('section'), what=p.get('what'))
# исследование ядра
for f in ('wf1.json', 'wf2.json'):
    d = ld(os.path.join(DATA, f)); r = d.get('result', d)
    for v in r['verified']:
        st = 'core_research_dont' if v.get('verdict') == 'warn_dont' else ('core_research_keep' if v.get('keep') else 'rejected')
        put(v.get('id'), st, 'исследование ядра (' + f + ')', name=v['name'], section=v.get('section'), tag=v.get('verdict'), what=v.get('what'),
            reason=(v.get('vr_note') or '') + (' ' + v.get('reason', '') if v.get('reason') else ''), vr_status=v.get('vr_status'))
# Other Mods: оба прохода
for v in ld(os.path.join(DATA, 'other_result.json'))['result']['verified']:
    b, a = v.get('value') or {}, v.get('compat') or {}
    where = 'Other Mods, ' + ('второй' if v.get('round') == 2 else 'первый') + ' проход'
    if v.get('keep'):
        dont = 'dont' in (a.get('tag'), b.get('tag')) or b.get('section') == 'dont'
        put(v.get('id'), 'other_dont' if dont else 'other_keep', where, name=v['name'], section=b.get('section') or v.get('section'), tag=b.get('tag') or v.get('tag'),
            what=b.get('what') or v.get('what'), reason=b.get('note') or v.get('note'), vr_status=v.get('vr_status'))
    elif a or b:
        why = (b.get('reason') if b and not b.get('keep') else '') or (a.get('reason') if a and not a.get('keep') else '') or v.get('dropped_by', '')
        put(v.get('id'), 'rejected', where, name=v['name'], section=v.get('section'), what=v.get('what'), reason=why, vr_status=v.get('vr_status'))
for v in ix.get('kept', []):
    put(v.get('id'), 'interaction_dont' if v.get('tag') == 'dont' else 'interaction_keep', 'Взаимодействие в VR', name=v['name'], section=v.get('section'), tag=v.get('tag'),
        what=v.get('what'), reason=v.get('interplay') or v.get('note'), vr_status=v.get('vr_status'))
# SE/AE-аналоги модов ядра: в VR взят VR-вариант (список из tools/cats.py), для плоской версии — основа
SE_TWINS = {17230, 32444, 30379, 60805, 36869, 12604, 76649, 12688, 18619, 34705, 92454, 61950, 117389, 86492, 111991, 52897, 97720, 23316, 137741, 60690, 111236}
for mid in SE_TWINS:
    put(mid, 'se_twin_of_core', 'SE/AE-аналог мода ядра', reason='В VR-ядре стоит VR-вариант или тот же инструмент; для SE/AE брать этот')
# ядро
man = yaml.safe_load(open(os.path.join(ROOT, 'manifest.yaml'), encoding='utf-8'))
nonnexus = []
for m in man['mods']:
    ids = re.findall(r'mods/(\d+)', str(m.get('url', '')))
    mid = m.get('id') if m.get('id') not in (None, 'null') else (ids[0] if ids else None)
    kw = dict(name=m['name'], section=m.get('separator'), tag=m.get('tag'), what=m.get('note') or '', reason=m.get('files') or '', vr_status=m.get('kind'))
    if mid:
        put(mid, 'core', 'ядро (manifest.yaml)', **kw)
    else:
        nonnexus.append(dict(id='', url=m.get('url', ''), status='core', where='ядро (manifest.yaml), не Nexus', **kw))

# --- 3. подсказки для плоской версии
for r in rows.values():
    multi = bool(re.search(r'\bSSE\b|\bSE\b|\bAE\b|special edition', r['name'], re.I))   # «SSE AE VR» — общий мод для всех версий
    vr_only = (bool(VR_NAME.search(r['name'])) and not multi) or (r['vr_status'] == 'vr_native' and r['se_lists_n'] == 0)
    if r['status'] == 'se_twin_of_core':
        r['flat_hint'] = 'flat_base'
    elif vr_only:
        r['flat_hint'] = 'vr_only'
    elif r['status'] in ('core_research_dont', 'other_dont', 'interaction_dont') or (r['status'] in ('rejected', 'dropped') and (r['vr_status'] == 'flat_only' or 'vr_incompatible' in r['reason'] or VR_DROP.search(r['reason'] or ''))):
        r['flat_hint'] = 'flat_candidate'
    elif r['status'] in ('prefilter_skipped', 'not_evaluated', 'core_pool_considered') and r['se_lists_n'] >= 4:
        r['flat_hint'] = 'se_popular_unreviewed'

# --- 4. запись
os.makedirs(OUT, exist_ok=True)
allrows = sorted(rows.values(), key=lambda r: (RANK.index(r['status']), -(r['vr_lists_n'] * 2 + r['se_lists_n']), r['name'])) + nonnexus
COLS = ['id', 'name', 'status', 'where', 'section', 'tag', 'what', 'reason', 'vr_status', 'flat_hint', 'vr_lists_n', 'se_lists_n', 'vr_lists', 'se_lists', 'newest_file', 'sample_file', 'author', 'url']
def wcsv(path, rs):
    with open(path, 'w', encoding='utf-8-sig', newline='') as f:
        w = csv.writer(f, delimiter=';')
        w.writerow(COLS)
        for r in rs:
            w.writerow([str(r.get(c, '')).replace('\n', ' ') for c in COLS])
wcsv(os.path.join(OUT, 'mods_all.csv'), allrows)
json.dump(allrows, open(os.path.join(OUT, 'mods_all.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=0)
ORDER_FH = {'flat_base': 0, 'flat_candidate': 1, 'se_popular_unreviewed': 2}
flat = sorted([r for r in rows.values() if r['flat_hint'] in ORDER_FH], key=lambda r: (ORDER_FH[r['flat_hint']], -r['se_lists_n'], r['name']))
wcsv(os.path.join(OUT, 'flat_candidates.csv'), flat)
st = collections.Counter(r['status'] for r in allrows)
fh = collections.Counter(r['flat_hint'] for r in rows.values() if r['flat_hint'])
summary = dict(mods_in_27_lists=len(mods), rows=len(allrows), by_status=dict(st), flat_hint=dict(fh), flat_candidates_file=len(flat))
json.dump(summary, open(os.path.join(OUT, 'summary.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(json.dumps(summary, ensure_ascii=False, indent=1))
