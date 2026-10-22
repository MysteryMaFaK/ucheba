"""Вход для лёгкого сведения дублей «Other Mods 2026» (после проверки и tools/merge_other2.py).

  python3 -I tools/consolidate_input.py   -> data/other2/consolidate/<часть>.json, печатает args для workflows/skyrim-vr-consolidate-light.js

Три части (как на странице): gaps (пробелы ядра и прочее), textures, world (внешний вид, мир, «не ставить»).
В каждой — компактные карточки принятых модов второго прохода (их можно править) и первого прохода (только для сверки,
правки первого прохода делаются через data/other2/fixups.json)."""
import json, os

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE); O2 = os.path.join(ROOT, 'data', 'other2'); OUT = os.path.join(O2, 'consolidate')
PARTS = {
    'gaps': ['start', 'followers', 'navigation', 'controls', 'russian', 'saves', 'cc', 'equipment', 'voice', 'music', 'niche', 'misc'],
    'textures': ['tex_strategy', 'tex_land', 'tex_flora', 'tex_water_sky', 'tex_arch', 'tex_dungeons', 'tex_clutter', 'tex_pbr_tools'],
    'world': ['chars_body', 'chars_faces', 'physics', 'armor', 'creatures', 'city_meshes', 'clutter_meshes', 'reshade', 'dont'],
}
res = json.load(open(os.path.join(ROOT, 'data', 'other_result.json'), encoding='utf-8'))['result']
os.makedirs(OUT, exist_ok=True)
sizes = {}
for part, secs in PARTS.items():
    new, old = [], []
    for v in res['verified']:
        if not v.get('keep'):
            continue
        b = v.get('value') or {}
        sec = b.get('section') or v.get('section')
        if sec not in secs:
            continue
        card = dict(id=v.get('id'), name=v['name'][:90], sec=sec, tag=b.get('tag') or v.get('tag'), grp=b.get('choose_one_group') or v.get('choose_one_group'), what=(b.get('what') or v.get('what') or '')[:130])
        if v.get('round') == 2:
            new.append(dict(key=v['key'], **card))
        else:
            old.append(card)
    json.dump(dict(part=part, sections=secs, new_round2=new, first_pass_fixed=old), open(os.path.join(OUT, part + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, separators=(',', ':'))
    sizes[part] = len(new)
    print(part, 'второй проход', len(new), 'первый проход', len(old), os.path.getsize(os.path.join(OUT, part + '.json')), 'байт')
print('args для workflows/skyrim-vr-consolidate-light.js:')
print(json.dumps(dict(root=ROOT, sizes={k: v for k, v in sizes.items() if v}), ensure_ascii=False))
