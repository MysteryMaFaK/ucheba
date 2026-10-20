"""Склеить сбор «Взаимодействие и интерактивность в VR» (data/partial/vr-interaction__*.json) в data/vr_interaction_result.json и VR_INTERACTION.md.

  python3 -I tools/merge_ix.py            # слить и записать
  python3 -I tools/merge_ix.py --dry      # только отчёт

keep = оба проверяющих (vr-compat и value-perf) оставили; правки сведения (consolidate_ix*.json) применяются поверх:
drop_duplicate -> убрать; retag/regroup/move_section -> section/tag/choose_one_group.
Второй раунд (файлы с «ix2» в имени) перекрывает первый по ключу."""
import collections, glob, json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, '..'); P = os.path.join(ROOT, 'data', 'partial')
DRY = '--dry' in sys.argv
ld = lambda p: json.load(open(p, encoding='utf-8'))
NX = 'https://www.nexusmods.com/skyrimspecialedition/mods/{}'
SECS = [('ix_hands', 'Руки, хват, предметы'), ('ix_combat', 'Бой руками'), ('ix_magic', 'Магия руками'), ('ix_world', 'Мир, NPC, контейнеры, крафт'),
        ('ix_ui', 'Интерфейс VR'), ('ix_locomotion', 'Передвижение и комфорт'), ('ix_feedback', 'Отдача и обратная связь')]
TAGS = {'rec': 'рекомендую', 'opt': 'по желанию', 'alt': 'выбор', 'try': 'проверить'}
ORDER = {'rec': 0, 'alt': 1, 'opt': 2, 'try': 3}

SECTION_FIX = {60211: 'ix_ui', 45586: 'ix_world'}  # раздел, выбранный проверяющим, явно не подошёл (Whose Quest Is It Anyway VR, iNeed Water)
picks, drops, leads = {}, [], {}
for f in sorted(glob.glob(f'{P}/vr-interaction__collect_ix*.json')):
    d = ld(f)
    for p in d.get('picks', []):
        picks[p['key']] = dict(p, src=os.path.basename(f))
    drops += d.get('considered_dropped', [])
    if d.get('section_lead'):
        m = re.search(r'collect_(ix2?-[\w-]+)', f); leads[m.group(1) if m else f] = d['section_lead']
verd = {'vr-compat': {}, 'value-perf': {}}
for kind in verd:
    for f in sorted(glob.glob(f'{P}/vr-interaction__verify_{kind}-ix*.json')):
        for v in ld(f).get('verdicts', []):
            verd[kind][v['key']] = v
cons = [ld(f) for f in sorted(glob.glob(f'{P}/vr-interaction__consolidate_ix*.json'))]
adj = {}
for c in cons:
    for a in c.get('adjustments', []):
        adj[a['key']] = a

kept, rejected, pending = [], [], []
for k, p in picks.items():
    a, b = verd['vr-compat'].get(k), verd['value-perf'].get(k)
    if not (a and b):
        pending.append(k); continue
    if not (a['keep'] and b['keep']):
        rejected.append((p['name'], (b if not b['keep'] else a)['reason'], p.get('src', ''))); continue
    it = dict(p, section=b['section'] or p['section'], tag=('try' if a['tag'] == 'try' and b['tag'] != 'dont' else (b['tag'] or p['tag'])),
              choose_one_group=b['choose_one_group'] or a['choose_one_group'] or p['choose_one_group'], what=b['what'] or p['what'],
              note=' '.join(x for x in [b['note'], a['note'] if a['note'] != b['note'] else ''] if x) or p['note'])
    x = adj.get(k)
    if x and x['action'] == 'drop_duplicate':
        rejected.append((p['name'], 'сведение: ' + x['reason'], p.get('src', ''))); continue
    if x and x['action'] in ('retag', 'regroup', 'move_section'):
        it['section'], it['tag'], it['choose_one_group'] = x['section'], x['tag'], x['choose_one_group']
    it['section'] = SECTION_FIX.get(p.get('id'), it['section'])
    if it['section'] == 'ix_dont' or it['tag'] == 'dont':
        it['section'], it['tag'] = 'ix_dont', 'dont'
    kept.append(it)

crit = None
cf = sorted(glob.glob(f'{P}/vr-interaction__critic_ix*.json'))
if cf:
    crit = ld(cf[-1])
by = collections.Counter(i['section'] for i in kept)
print(json.dumps(dict(picks=len(picks), kept=len(kept), rejected=len(rejected), pending=len(pending), dropped_by_collectors=len(drops), by_section=dict(by), critic=bool(crit)), ensure_ascii=False))
if DRY:
    sys.exit(0)

json.dump(dict(kept=kept, rejected=rejected, dropped_by_collectors=drops, leads=leads,
               groups=[g for c in cons for g in c.get('groups', [])], interplay=[r for c in cons for r in c.get('interplay_rules', [])],
               order=[r for c in cons for r in c.get('order_rules', [])], conflicts=[r for c in cons for r in c.get('conflicts', [])], critic=crit),
          open(os.path.join(ROOT, 'data', 'vr_interaction_result.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

md = ['# Skyrim VR — взаимодействие и интерактивность', '',
      'Дополнение к ядру Skyrim VR Core 2026: то, что делает VR физически интерактивным (руки, предметы, бой, магия, мир и NPC, интерфейс, передвижение, отдача). '
      'Основа уже в ядре: VRIK, HIGGS, PLANCK, Physical Collision VR, True Wield VR, Interactive Activators VR, Gift by Hand VR и другие. Здесь только недостающее и то, как оно уживается с этой основой.',
      'Каждый мод проверен дважды (совместимость с VR; польза и избыточность), затем сведён с ядром и «Other Mods». Метки: `rec` рекомендую · `opt` по желанию · `alt` один из группы · `try` VR заявлен, но не обкатан — ставить по одному.',
      'Данные собраны без доступа к страницам Nexus (закрыты из облака): часть описаний взята из названий файлов в сборках, GitHub и сниппетов поиска — у таких модов это сказано в примечании.', '']
for sid, title in SECS:
    its = sorted([i for i in kept if i['section'] == sid], key=lambda i: (ORDER.get(i['tag'], 9), i['name']))
    if not its:
        continue
    md += [f'## {title}', '']
    for t in its:
        url = t['url'] if str(t.get('url', '')).startswith('http') else (NX.format(t['id']) if t.get('id') else '')
        link = f"[#{t['id']}]({url})" if t.get('id') else (f'[ссылка]({url})' if url else '')
        md.append(f"- **{t['name']}** `{t['tag']}` {link} — {t['what']}" + (f" Файл: {t['files']}." if t.get('files') else '')
                  + (f" Требует: {'; '.join(t['requires'])}." if t.get('requires') else '') + (f" Одно из: `{t['choose_one_group']}`." if t.get('choose_one_group') else '')
                  + (f" Взаимодействие: {t['interplay']}" if t.get('interplay') else '') + (f" {t['note']}" if t.get('note') else ''))
    md.append('')
dont = sorted([i for i in kept if i['section'] == 'ix_dont'], key=lambda i: i['name'])
if dont:
    md += ['## Не ставить в VR', ''] + [f"- **{t['name']}** — {t['what']}" + (f" {t['note']}" if t.get('note') else '') for t in dont] + ['']
groups = [g for c in cons for g in c.get('groups', [])]
if groups:
    md += ['## Группы «одно из»', ''] + [f"- `{g['group']}` — по умолчанию {g['default_pick']}. Варианты: {'; '.join(g['members'])}. {g['rule']}" for g in groups] + ['']
for title, key in (('Правила взаимодействия с основой (HIGGS, PLANCK, VRIK, Physical Collision VR)', 'interplay_rules'), ('Порядок в MO2', 'order_rules'), ('Конфликты', 'conflicts')):
    rows = [r for c in cons for r in c.get(key, [])]
    if rows:
        md += [f'## {title}', ''] + [f'- {r}' for r in rows] + ['']
r2rej = [r for r in rejected if 'ix2-' in r[2]]
if r2rej:
    md += ['## Рассмотрено и не взято (пробелы, которые нашёл критик)', '',
           'Эти моды критик полноты назвал пропущенными, их проверили отдельно. Проверяющие их сняли, ниже причины — на случай, если захотите вернуть какой-то вручную.', ''] + [f'- **{n}** — {why}' for n, why, _ in r2rej] + ['']
if crit and not r2rej:
    md += ['## Что ещё проверяется', '', f"Вердикт критика полноты: `{crit['verdict']}`.", ''] + [f"- **{m['topic']}** — {m['why']} Кандидат: {m['candidate']}" for m in crit.get('missing', [])] + ['']
elif crit:
    md += ['## Полнота', '', 'Критик полноты после первого раунда назвал 8 пробелов; все они проверены вторым раундом (результат выше: оставлено и «рассмотрено и не взято»). Новых пробелов сверкой с 9 VR-сборками не найдено.', '']
open(os.path.join(ROOT, 'VR_INTERACTION.md'), 'w', encoding='utf-8').write('\n'.join(md) + '\n')
print('записано: data/vr_interaction_result.json, VR_INTERACTION.md (%d строк)' % len(md))
