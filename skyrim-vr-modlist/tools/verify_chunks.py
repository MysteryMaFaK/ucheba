"""Лёгкая проверка второго прохода «Other Mods»: собрать порции для ОДНОГО проверяющего вместо двух.

  python3 -I tools/verify_chunks.py            -> data/other2/verify_chunks/V01.json ..., data/other2/auto_accepted.json, печатает args для воркфлоу
  python3 -I tools/verify_chunks.py --size 120 -> размер порции (по умолчанию 100)

Почему так (по данным 210 пар, проверенных обоими проверяющими): VR-проверка сняла 9 модов, и все 9 сняла бы и проверка
пользы — самостоятельно VR-проверка не отсеяла ни одного. Метки сборщика rec и dont подтверждены в 16 из 16 случаев.
Поэтому:
  * rec и dont сборщика принимаются без агента (auto_accepted.json, с пометкой «без проверки»);
  * остальное идёт одному проверяющему (польза + VR-чеклист в одном проходе), порциями по ~100, без вызовов инструментов;
  * уже проверенное (оба старых проверяющих или новый один) не попадает в порции — повторный запуск ничего не переделывает."""
import collections, glob, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
P = os.path.join(ROOT, 'data', 'partial'); O2 = os.path.join(ROOT, 'data', 'other2'); OUT = os.path.join(O2, 'verify_chunks')
SIZE = int(sys.argv[sys.argv.index('--size') + 1]) if '--size' in sys.argv else 100
ld = lambda p: json.load(open(p, encoding='utf-8'))

cards = {}
for f in glob.glob(os.path.join(O2, 'batches', '*.json')) + glob.glob(os.path.join(O2, 'batches_full_CD', '*.json')):
    d = ld(f)
    for it in d['items']:
        cards.setdefault(it['key'], it)
col = collections.defaultdict(dict)
for f in sorted(glob.glob(f'{P}/other-mods__collect_r2-*.json')):
    b = re.search(r'collect_r2-([A-Z]\d+)', f).group(1)
    for e in ld(f).get('entries', []):
        col[b].setdefault(e['key'], e)
old = collections.defaultdict(dict)       # (batch, lens) -> {key: verdict}
for f in glob.glob(f'{P}/other-mods__verify_*-r2-*.json'):
    m = re.search(r'verify_(vr-compat|value-perf)-r2-([A-Z]\d+)', f)
    if m:
        for v in ld(f).get('verdicts', []):
            old[(m.group(2), m.group(1))][v['key']] = v
single = {}
for f in glob.glob(f'{P}/other-mods__verify_single-*.json'):
    for v in ld(f).get('verdicts', []):
        single[v['key']] = v

pending, auto, kept_names, done = [], [], [], 0
for b, ents in sorted(col.items()):
    for k, e in ents.items():
        if e['decision'] == 'drop':
            continue
        a, c = old[(b, 'vr-compat')].get(k), old[(b, 'value-perf')].get(k)
        if (a and c) or k in single:
            done += 1
            v = single.get(k) or c
            if (v.get('keep') if k in single else (a['keep'] and c['keep'])):
                kept_names.append(e['name'])
            continue
        if e['decision'] == 'dont' or e['tag'] == 'rec':
            auto.append(dict(batch=b, key=k, name=e['name'], reason='метка сборщика ' + ('dont' if e['decision'] == 'dont' else 'rec') + ' — по данным подтверждается в 100% случаев'))
            kept_names.append(e['name'])
            continue
        cd = cards.get(k, {})
        it = dict(key=k, id=e['id'], name=e['name'][:90], sec=e['section'], tag=e['tag'], what=e['what'][:170], note=e['note'][:160],
                  vs=e['vr_status'], vr=cd.get('vr'), se=cd.get('se'), lists=[x[:10] for x in cd.get('vr_lists', [])], new=cd.get('newest', '')[:7])
        if e['choose_one_group']: it['grp'] = e['choose_one_group']
        if e['requires']: it['req'] = [r[:40] for r in e['requires'][:4]]
        if e.get('member_ids'): it['members'] = e['member_ids']
        pending.append(it)

os.makedirs(OUT, exist_ok=True)
for f in glob.glob(os.path.join(OUT, 'V*.json')):
    os.remove(f)
pending.sort(key=lambda x: (x['sec'], x['name']))
chunks = [pending[i:i + SIZE] for i in range(0, len(pending), SIZE)]
# номера порций не повторяются между запусками: иначе save_journal.py не запишет новый результат поверх старого файла
used = [int(m.group(1)) for f in glob.glob(f'{P}/other-mods__verify_single-V*.json') for m in [re.search(r'verify_single-V(\d+)', f)] if m]
start = max(used, default=0) + 1
sizes = {}
for n, ch in enumerate(chunks, start):
    cid = 'V%02d' % n
    json.dump(dict(chunk=cid, fields='sec=раздел tag=метка what=что делает note=заметка сборщика vs=VR-статус сборщика vr/se=число VR/SE-сборок lists=VR-сборки new=дата файла grp=группа «одно из» req=требует',
                   already_kept_round2=sorted(set(kept_names)), picks=ch), open(os.path.join(OUT, cid + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    sizes[cid] = len(ch)
json.dump(auto, open(os.path.join(O2, 'auto_accepted.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
print(json.dumps(dict(уже_проверено=done, принято_без_проверки=len(auto), в_проверку=len(pending), порций=len(chunks)), ensure_ascii=False))
print('args для workflows/skyrim-vr-verify-light.js:')
print(json.dumps(dict(root=ROOT, sizes=sizes), ensure_ascii=False))
