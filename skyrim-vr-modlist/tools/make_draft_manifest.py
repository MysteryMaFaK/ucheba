"""Пересобрать data/kit/draft_manifest.json (275 модов ядра) из tools/build_page.py + tools/additions.py
и разложить по группам data/kit/g*.json. Запускать после любой правки списка ядра."""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
sys.path.insert(0, HERE)
src = open(os.path.join(HERE, 'build_page.py'), encoding='utf-8').read()
ns = {'__file__': os.path.join(HERE, 'build_page.py')}
exec(compile(src.split('if __name__')[0], 'build_page', 'exec'), ns)
ns['merge']()
SECTIONS = ns['SECTIONS']
wf = {}
for f in ('wf1.json', 'wf2.json'):
    p = os.path.join(ROOT, 'data', f)
    if os.path.exists(p):
        for x in json.load(open(p, encoding='utf-8'))['verified']:
            if x.get('id'):
                wf.setdefault(x['id'], []).append({'vr_note': (x.get('compat') or {}).get('vr_note') or x.get('vr_note'), 'overlaps': x.get('overlaps'), 'evidence': (x.get('evidence') or '')[:400]})
SEP = {'tools': '00 Инструменты и корень', 'base': '01 Мастера и USSEP', 'frameworks': '02 SKSEVR и библиотеки', 'fixes': '03 Фиксы движка',
       'gfx': '04 Шейдеры и свет', 'vr': '05 VR-ядро', 'hitech': '06 Хайтек 2026', 'ui': '07 Интерфейс', 'audio': '08 Звук',
       'world': '09 Свет, погода, вода, VFX', 'land': '10 Ландшафт, трава, деревья', 'anim': '11 Анимации и физика', 'combat': '12 Бой и геймплей',
       'immersion': '13 Мир, ИИ, погружение', 'ai': '14 ИИ-NPC', 'perf': '15 VR-рантайм и производительность'}
items = []
for s in SECTIONS:
    for i, it in enumerate(s['items']):
        e = dict(key=f"{s['id']}-{it.get('id', i)}", section=s['id'], separator=SEP.get(s['id'], s['id']), order=len(items), name=it['name'], id=it.get('id'),
                 url=it.get('url') or (ns['nx'](it['id']) if it.get('id') else None), extra=[{'label': t, 'url': u} for t, u in it.get('extra', [])],
                 tag=it['tag'], version=it.get('ver'), vr_file=it.get('file'), note=it.get('note', ''), new=bool(it.get('new')))
        if it.get('id') in wf: e['research'] = wf[it['id']]
        items.append(e)
kit = os.path.join(ROOT, 'data', 'kit'); os.makedirs(kit, exist_ok=True)
json.dump({'items': items, 'dont': ns['DONT'], 'gen_steps': ns['GEN_STEPS'], 'mo2_order': ns['MO2_ORDER']}, open(os.path.join(kit, 'draft_manifest.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
groups = {'g1a_tools_base_frameworks': ['tools', 'base', 'frameworks'], 'g1b_fixes': ['fixes'], 'g2_gfx_world_land': ['gfx', 'world', 'land', 'perf'],
          'g3_vr_hitech_ui': ['vr', 'hitech', 'ui'], 'g4_anim_combat': ['anim', 'combat'], 'g5_immersion_audio_ai': ['immersion', 'audio', 'ai']}
for g, secs in groups.items():
    sub = [x for x in items if x['section'] in secs]
    json.dump(sub, open(os.path.join(kit, g + '.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print(g, len(sub))
print('всего', len(items))
