"""Склеить результаты второго прохода «Other Mods 2026» (data/partial/other-mods__*r2*.json) в data/other_result.json.

  python3 -I tools/merge_other2.py            # слить; первый проход не трогает, прежние записи второго прохода заменяет
  python3 -I tools/merge_other2.py --dry      # только отчёт, ничего не писать

Что делает:
  1. читает оценки пакетов (collect_r2-<ПАКЕТ>[-retryN]) и два прохода проверки (verify_vr-compat-r2-<ПАКЕТ>, verify_value-perf-r2-<ПАКЕТ>);
  2. keep = оба проверяющих оставили; серии разворачиваются в состав (по data/other2/batches/<ПАКЕТ>.json);
  3. правки сведения (consolidate_r2-*): drop_duplicate -> keep=false; retag/regroup/move_section -> правят value.tag/section/choose_one_group;
  4. пишет data/other_result.json (verified первого прохода + второго, поле round), data/other2/dispositions.json (по каждому кандидату:
     решение, причина), data/other2/done_ids.json (все оценённые id — other2_batches.py их больше не предложит),
     data/other2/consolidation.json (группы «одно из», порядок, конфликты, критик)."""
import glob, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__)); DATA = os.path.join(HERE, '..', 'data'); P = os.path.join(DATA, 'partial'); O2 = os.path.join(DATA, 'other2')
DRY = '--dry' in sys.argv
ld = lambda p: json.load(open(p, encoding='utf-8'))

res_path = os.path.join(DATA, 'other_result.json')
res = ld(res_path)['result']
round1 = [v for v in res['verified'] if v.get('round', 1) == 1]

batch_cache = {}
def batch_items(bid):
    if bid not in batch_cache:
        p = os.path.join(O2, 'batches', f'{bid}.json')
        batch_cache[bid] = {i['key']: i for i in ld(p)['items']} if os.path.exists(p) else {}
    return batch_cache[bid]

evals, verd = {}, {}
for f in sorted(glob.glob(f'{P}/other-mods__collect_r2-*.json')):
    m = re.search(r'collect_r2-([A-Z]\d+)', f); bid = m.group(1)
    d = ld(f)
    evals.setdefault(bid, {})
    for e in d.get('entries', []):
        evals[bid].setdefault(e['key'], e)
for kind in ('vr-compat', 'value-perf'):
    for f in sorted(glob.glob(f'{P}/other-mods__verify_{kind}-r2-*.json')):
        bid = re.search(r'-r2-([A-Z]\d+)', f).group(1)
        for v in ld(f).get('verdicts', []):
            verd.setdefault((bid, kind), {})[v['key']] = v

single = {}    # лёгкая проверка: один проверяющий (workflows/skyrim-vr-verify-light.js)
for f in sorted(glob.glob(f'{P}/other-mods__verify_single-*.json')):
    for v in ld(f).get('verdicts', []):
        single[v['key']] = v
autop = os.path.join(O2, 'auto_accepted.json')
auto = {a['key']: a for a in ld(autop)} if os.path.exists(autop) else {}

verified, disp, done = [], [], set()
pending = []
for bid in sorted(evals):
    items = batch_items(bid)
    ma, mb = verd.get((bid, 'vr-compat'), {}), verd.get((bid, 'value-perf'), {})
    for key, e in evals[bid].items():
        src = items.get(key, {})
        for mem in [src.get('id')] + [m['id'] for m in src.get('members', [])]:
            if mem: done.add(mem)
        row = dict(batch=bid, key=key, id=e['id'], name=e['name'], decision=e['decision'], drop_code=e['drop_code'], note=e['note'] if e['decision'] == 'drop' else '')
        if e['decision'] == 'drop':
            disp.append(row); continue
        a, b = ma.get(key), mb.get(key)
        if key in single:                      # один проверяющий заменяет оба старых
            a = b = single[key]
        elif not (a and b) and key in auto:    # rec/dont сборщика — без проверки
            syn = dict(key=key, keep=True, section='dont' if e['decision'] == 'dont' else e['section'], tag='dont' if e['decision'] == 'dont' else e['tag'],
                       choose_one_group=e['choose_one_group'], what=e['what'], note=e['note'], reason='без проверки: ' + auto[key]['reason'])
            a = b = syn
        if not (a and b):
            pending.append((bid, key)); row['decision'] = 'pending_verify'; disp.append(row); continue
        keep = bool(a and b and a['keep'] and b['keep'])
        row['decision'] = ('keep' if keep else 'rejected_by_verifier') + (':dont' if e['decision'] == 'dont' else '')
        disp.append(row)
        mem_ids = set(e.get('member_ids') or [])
        mems = [m for m in src.get('members', []) if not mem_ids or m['id'] in mem_ids]
        files = e['files']
        note = e['note']
        if mems:
            files = (files + ' ' if files else '') + 'Состав: ' + '; '.join(f"#{m['id']} {m['name']}" for m in mems) + '.'
        verified.append(dict(key=key, src='r2-' + bid, also=[], id=e['id'], name=e['name'], url=e['url'], section=e['section'], tag=e['tag'],
                             choose_one_group=e['choose_one_group'], what=e['what'], vr_status=e['vr_status'], files=files, requires=e['requires'],
                             note=note, evidence=e['evidence'], compat=a, value=b, keep=keep, round=2, member_ids=sorted(mem_ids)))

# правки сведения
cons = []
for f in sorted(glob.glob(f'{P}/other-mods__consolidate_r2-*.json')):
    cons.append(ld(f))
adj = {}
for c in cons:
    for a in c.get('adjustments', []):
        adj[a['key']] = a
applied = {'drop_duplicate': 0, 'retag': 0, 'regroup': 0, 'move_section': 0}
for v in verified:
    a = adj.get(v['key'])
    if not a or a['action'] == 'keep':
        continue
    if a['action'] == 'drop_duplicate':
        v['keep'] = False; v['dropped_by'] = 'consolidation: ' + a['reason']
    else:
        val = v['value'] or {}
        val['section'] = a['section']; val['tag'] = a['tag']; val['choose_one_group'] = a['choose_one_group']
        v['value'] = val
    applied[a['action']] = applied.get(a['action'], 0) + 1

# точечные правки первого прохода (data/other2/fixups.json: {"round1": {"<nexus id>": {"tag": ..., "section": ..., "what": ..., "note": ...}}})
fxp = os.path.join(O2, 'fixups.json')
fx = ld(fxp).get('round1', {}) if os.path.exists(fxp) else {}
for v in round1:
    f1 = fx.get(str(v.get('id')))
    if f1 and v.get('value'):
        v['value'] = dict(v['value'], **f1)
        if v.get('compat') and f1.get('tag') == 'dont':
            v['compat'] = dict(v['compat'], tag='dont')

for l in res.get('leads', []):        # правки описаний разделов (fixups.json: {"leads": {"<раздел>": "<текст>"}})
    if l['section'] in (ld(fxp).get('leads', {}) if os.path.exists(fxp) else {}):
        l['lead'] = ld(fxp)['leads'][l['section']]

critic = ld(f'{P}/other-mods__critic_r2.json') if os.path.exists(f'{P}/other-mods__critic_r2.json') else None
summary = dict(single_verdicts=len(single), auto_accepted=len(auto), round1_fixups=len(fx), batches=len(evals), dispositions=len(disp), kept=sum(v['keep'] for v in verified), verified=len(verified), pending_verify=len(pending), consolidation_files=len(cons), applied=applied)
print(json.dumps(summary, ensure_ascii=False))
import collections
print('решения:', dict(collections.Counter(d['decision'] for d in disp)))
print('причины отказа:', dict(collections.Counter(d['drop_code'] for d in disp if d['decision'] == 'drop')))
if DRY:
    sys.exit(0)
res['verified'] = round1 + verified
json.dump({'result': res}, open(res_path, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
os.makedirs(O2, exist_ok=True)
json.dump(disp, open(os.path.join(O2, 'dispositions.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
old = set(ld(os.path.join(O2, 'done_ids.json'))) if os.path.exists(os.path.join(O2, 'done_ids.json')) else set()
json.dump(sorted(old | done), open(os.path.join(O2, 'done_ids.json'), 'w'))
json.dump(dict(groups=[g for c in cons for g in c.get('groups', [])], order_rules=[r for c in cons for r in c.get('order_rules', [])],
               conflicts=[x for c in cons for x in c.get('conflicts', [])], notes=[c.get('notes', '') for c in cons], critic=critic),
          open(os.path.join(O2, 'consolidation.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print('записано: other_result.json (первый проход %d + второй %d), other2/dispositions.json, done_ids.json, consolidation.json' % (len(round1), len(verified)))
