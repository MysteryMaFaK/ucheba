"""Склеить частичные результаты из data/partial/ в файлы, которые читают build_kit.py и build_other.py.
  python tools/merge_partials.py install-spec  -> data/install_spec.json  (+ data/specs_merged.json для критика)
  python tools/merge_partials.py other-mods    -> data/other_picks.json   (и data/other_result.json, если есть оба прохода проверки)
Какие группы ещё не посчитаны — печатается в конце."""
import glob, json, os, sys, re
HERE = os.path.dirname(os.path.abspath(__file__)); DATA = os.path.join(HERE, '..', 'data'); P = os.path.join(DATA, 'partial')
mode = sys.argv[1]
ld = lambda p: json.load(open(p, encoding='utf-8'))

if mode == 'install-spec':
    specs, notes, proc, critic = {}, [], None, {}
    for f in sorted(glob.glob(f'{P}/install-spec__*.json')):
        d = ld(f); name = os.path.basename(f)
        if 'enrich_' in name:
            for it in d['items']: specs[it['key']] = it
            notes.append(f"{name}: {d.get('group_notes', '')}")
        elif 'procedure' in name: proc = d
        elif 'critic' in name: critic = d
    json.dump({'result': {'specs': list(specs.values()), 'group_notes': notes, 'procedure': proc, 'critic': critic}}, open(f'{DATA}/install_spec.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    json.dump({'specs': list(specs.values())}, open(f'{DATA}/specs_merged.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    draft = ld(f'{DATA}/kit/draft_manifest.json')['items']
    missing = [x['key'] for x in draft if x['key'] not in specs]
    print(f'карточек установки: {len(specs)} из {len(draft)}; процедура: {"есть" if proc else "НЕТ"}; критик: {"есть" if critic else "НЕТ"}')
    by = {}
    for k in missing: by.setdefault(k.split('-')[0], []).append(k)
    print('нет карточек по разделам:', {s: len(v) for s, v in by.items()})

elif mode == 'other-mods':
    picks, seen, leads = [], {}, []
    for f in sorted(glob.glob(f'{P}/other-mods__collect_*.json')):
        d = ld(f); src = os.path.basename(f).split('collect_')[1][:-5]
        leads += [dict(l, src=src) for l in d.get('section_leads', [])]
        for p in d['picks']:
            key = f"id:{p['id']}" if p.get('id') else 'n:' + re.sub(r'[^a-z0-9а-я]+', '', p['name'].lower())
            if key in seen: seen[key]['also'].append(src); continue
            it = dict(key=key, src=src, also=[], **p); seen[key] = it; picks.append(it)
    json.dump({'picks': picks, 'leads': leads}, open(f'{DATA}/other_picks.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('уникальных кандидатов:', len(picks), '; сбор по агентам:', sorted({p['src'] for p in picks}))
    A, B = f'{P}/other-mods__verify_vr-compat.json', f'{P}/other-mods__verify_value-perf.json'
    if os.path.exists(A) and os.path.exists(B):
        ma = {v['key']: v for v in ld(A)['verdicts']}; mb = {v['key']: v for v in ld(B)['verdicts']}
        ver = [dict(p, compat=ma.get(p['key']), value=mb.get(p['key']), keep=bool(ma.get(p['key']) and mb.get(p['key']) and ma[p['key']]['keep'] and mb[p['key']]['keep'])) for p in picks]
        json.dump({'result': {'leads': leads, 'verified': ver, 'notes': []}}, open(f'{DATA}/other_result.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
        print('проверено:', len(ver), '; оставлено:', sum(v['keep'] for v in ver))
    else:
        print('проверка совместимости/ценности ещё не выполнена (нужны оба прохода verify_*)')
