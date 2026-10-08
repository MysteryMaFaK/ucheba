"""Build manifest.yaml, MODLIST.md, CONFLICTS.md and links/ from the draft manifest + enrichment workflow output."""
import json, sys, re, os, collections
import yaml

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.dirname(HERE)
SCR = os.path.join(OUT, 'data')
draft = json.load(open(f'{SCR}/kit/draft_manifest.json'))
wf = json.load(open(sys.argv[1]))['result']
extra_cfg = json.load(open(f'{SCR}/kit/fixups.json')) if os.path.exists(f'{SCR}/kit/fixups.json') else {}

TAG_RU = {'core': 'обязательно', 'rec': 'рекомендую', 'opt': 'по желанию', 'alt': 'выбор', 'try': 'проверить'}
PHASES = [
    (1, 'Инструменты, корень игры, мастера и USSEP', ['tools', 'base']),
    (2, 'SKSEVR, библиотеки, фиксы движка, производительность', ['frameworks', 'fixes', 'perf']),
    (3, 'Шейдеры, свет и VR-ядро', ['gfx', 'vr']),
    (4, 'Интерфейс и звук', ['ui', 'audio']),
    (5, 'Свет, погода, вода, VFX, ландшафт', ['world', 'land']),
    (6, 'Анимации и физика, затем Pandora', ['anim']),
    (7, 'Бой, геймплей, мир и ИИ', ['combat', 'immersion']),
    (8, 'Хайтек-новинки 2026 — по одному', ['hitech']),
    (9, 'ИИ-NPC', ['ai']),
]
SEC_PHASE = {s: n for n, _, secs in PHASES for s in secs}

specs = {s['key']: s for s in wf['specs']}
crit = wf.get('critic') or {}

mods = []
for it in draft['items']:
    sp = specs.get(it['key']) or specs.get(extra_cfg.get('key_aliases', {}).get(it['key'], ''), {})
    m = collections.OrderedDict()
    m['id'] = it['id']
    m['key'] = it['key']
    m['name'] = it['name']
    m['tag'] = it['tag']
    m['url'] = it['url']
    if it['extra']:
        m['also_download'] = [f"{e['label']}: {e['url']}" for e in it['extra']]
    m['separator'] = it['separator']
    m['order'] = it['order']
    m['phase'] = SEC_PHASE.get(it['section'], 9)
    if it.get('version'):
        m['version'] = it['version']
    m['kind'] = sp.get('kind', 'unknown')
    m['install_target'] = sp.get('install_target', 'mo2_mod')
    m['files'] = sp.get('files') or (f"VR-файл: {it['vr_file']}" if it.get('vr_file') else 'основной файл')
    m['fomod'] = sp.get('fomod', 'неизвестно — общие правила')
    m['requires'] = sp.get('requires', [])
    if sp.get('incompatible_with'):
        m['incompatible_with'] = sp['incompatible_with']
    if sp.get('choose_one_group'):
        m['choose_one_group'] = sp['choose_one_group']
    for k in ('mo2_order', 'plugin_order', 'config'):
        if sp.get(k):
            m[k] = sp[k]
    m['verify'] = sp.get('verify', '')
    m['note'] = it['note']
    m['risk'] = sp.get('risk', 'medium')
    m['confidence'] = sp.get('confidence', 'low')
    if sp.get('sources'):
        m['sources'] = sp['sources']
    if it.get('new'):
        m['added'] = '2026-10-08'
    mods.append(m)

# requirements added by the critic
SECTION_SEP = {it['section']: it['separator'] for it in draft['items']}
system_reqs = []
for r in crit.get('add_requirements', []):
    if r.get('id') is None:
        system_reqs.append({'name': r['name'], 'needed_by': r['needed_by'], 'note': r.get('note', '')})
        continue
    sec = r.get('separator_section') or 'frameworks'
    if sec not in SECTION_SEP:
        sec = 'frameworks'
    if r.get('id') and any(m['id'] == r['id'] for m in mods):
        continue
    needed_tags = [m['tag'] for m in mods if m['key'] in r['needed_by'] or m['name'] in r['needed_by']]
    tag = 'core' if 'core' in needed_tags else 'rec' if 'rec' in needed_tags else 'opt'
    m = collections.OrderedDict(
        id=r.get('id'), key=f"req-{r.get('id') or re.sub(r'[^a-z0-9]+', '-', r['name'].lower())}", name=r['name'], tag=tag,
        url=(f"https://www.nexusmods.com/skyrimspecialedition/mods/{r['id']}" if r.get('id') else None),
        separator=SECTION_SEP[sec], order=max(x['order'] for x in mods) + 1, phase=SEC_PHASE.get(sec, 9),
        kind='unknown', install_target='mo2_mod', files='основной файл; VR-вариант, если есть', fomod='неизвестно — общие правила',
        requires=[], verify='', note=f"Требование для: {', '.join(r['needed_by'])}. {r.get('note', '')}".strip(),
        risk='medium', confidence='medium', added='2026-10-08', added_by='проверка согласованности')
    mods.append(m)

for key, patch in extra_cfg.get('mod_patches', {}).items():
    for m in mods:
        if m['key'] == key:
            m.update(patch)

def _fix(v):
    if isinstance(v, str):
        for a, b in extra_cfg.get('text_fixes', []):
            v = v.replace(a, b)
        return v
    if isinstance(v, list):
        return [_fix(x) for x in v]
    return v
for m in mods:
    for k in list(m.keys()):
        m[k] = _fix(m[k])

groups = crit.get('choose_one_groups', [])
if not groups:  # критик ещё не отработал — собираем группы из карточек
    _g = collections.OrderedDict()
    for m in mods:
        if m.get('choose_one_group'):
            _g.setdefault(m['choose_one_group'], []).append(m['name'])
    groups = [{'group': k, 'members': v, 'default': v[0], 'rule': 'ставится один; по умолчанию первый, пока критик не уточнил'} for k, v in _g.items() if len(v) > 1]
manifest = collections.OrderedDict()
manifest['meta'] = {
    'name': 'Skyrim VR Core 2026', 'date': '2026-10-08', 'game': 'Skyrim VR 1.4.15', 'script_extender': 'SKSEVR 2.0.12',
    'mod_manager': 'Mod Organizer 2 2.5.2 (портативный) + Root Builder 5.x',
    'scope': 'ядро сборки без текстур', 'page': 'https://claude.ai/artifact/CtFycL6Py2fC2TDY7NZgCa',
    'tags': TAG_RU,
    'fields': {
        'kind': 'plugin_only | skse_dll | assets_only | mixed | external_tool | mo2_plugin | root_files | guide_steps',
        'install_target': 'mo2_mod | root_builder | external_tool | mo2_plugins_folder | manual_steps',
        'confidence': 'насколько проверены files/fomod/requires: high | medium | low',
    },
}
manifest['phases'] = [{'phase': n, 'title': t, 'sections': secs} for n, t, secs in PHASES] + [
    {'phase': 10, 'title': 'Текстуры — отдельный этап, затем финальная генерация', 'sections': []}]
def _fix_all(v):
    if isinstance(v, str): return _fix(v)
    if isinstance(v, list): return [_fix_all(x) for x in v]
    if isinstance(v, dict): return {k: _fix_all(x) for k, x in v.items()}
    return v
crit = _fix_all(crit)
groups = _fix_all(groups)
keymap = {m['key']: m['name'] for m in mods}
for _new, _old in extra_cfg.get('key_aliases', {}).items():
    if _new in keymap: keymap[_old] = keymap[_new]
_kre = re.compile(r'\b([a-z]+-[0-9]+)\b')
def _names(t):
    return _kre.sub(lambda mo: f"{keymap[mo.group(1)]} [{mo.group(1)}]" if mo.group(1) in keymap else mo.group(1), t) if isinstance(t, str) else t
groups = [{'group': g['group'], 'members': [_names(x) for x in g['members']], 'default': _names(g['default']), 'rule': _names(g['rule'])} for g in groups]
manifest['system_requirements'] = [dict(r, needed_by=[_names(x) for x in r['needed_by']]) for r in system_reqs]
manifest['choose_one_groups'] = groups
manifest['order_rules'] = crit.get('order_rules', [])
manifest['plugin_rules'] = crit.get('plugin_rules', [])
manifest['resolved_contradictions'] = crit.get('contradictions', [])
manifest['do_not_install'] = [{'what': a, 'why': b} for a, b in draft['dont']]
manifest['final_generation'] = [t for t, _ in draft['gen_steps']]
manifest['mods'] = mods


class D(yaml.SafeDumper):
    pass


def _odict(d, data):
    return d.represent_mapping('tag:yaml.org,2002:map', data.items())


D.add_representer(collections.OrderedDict, _odict)
with open(f'{OUT}/manifest.yaml', 'w', encoding='utf-8') as f:
    f.write('# Skyrim VR Core 2026 — манифест установки. Читает агент по SYSTEM_PROMPT.md.\n')
    yaml.dump(manifest, f, Dumper=D, allow_unicode=True, sort_keys=False, width=140)

# MODLIST.md
lines = ['# Skyrim VR Core 2026 — карточки модов', '',
         'Тот же манифест в читаемом виде. Порядок карточек — порядок в левой панели MO2 сверху вниз внутри разделителя.',
         'Метки: ' + ' · '.join(f'`{k}` — {v}' for k, v in TAG_RU.items()) + '.', '']
by_sep = collections.OrderedDict()
for m in sorted(mods, key=lambda x: (x['separator'], x['order'])):
    by_sep.setdefault(m['separator'], []).append(m)
lines.append('## Разделители')
lines += [f"- [{s}](#{re.sub(r'[^0-9a-zа-яё -]', '', s.lower()).replace(' ', '-')}) — {len(v)}" for s, v in by_sep.items()]
lines.append('')
for sep, ms in by_sep.items():
    lines += [f'## {sep}', '']
    for m in ms:
        link = f"[#{m['id']}]({m['url']})" if m.get('id') else (f"[ссылка]({m['url']})" if m.get('url') else '')
        lines.append(f"### {m['name']} — `{m['tag']}` {link}")
        if m.get('also_download'):
            lines.append('- Также скачать: ' + '; '.join(m['also_download']))
        lines.append(f"- Фаза {m['phase']} · тип `{m['kind']}` · установка `{m['install_target']}` · надёжность данных `{m['confidence']}`")
        lines.append(f"- Файл: {m['files']}")
        lines.append(f"- Установщик: {m['fomod']}")
        if m.get('requires'):
            lines.append('- Требует: ' + '; '.join(m['requires']))
        if m.get('incompatible_with'):
            lines.append('- Не вместе с: ' + '; '.join(m['incompatible_with']))
        if m.get('choose_one_group'):
            lines.append(f"- Группа «одно из»: `{m['choose_one_group']}`")
        if m.get('mo2_order'):
            lines.append(f"- Порядок в MO2: {m['mo2_order']}")
        if m.get('plugin_order'):
            lines.append(f"- Порядок плагина: {m['plugin_order']}")
        if m.get('config'):
            lines.append(f"- Настройки: {m['config']}")
        if m.get('verify'):
            lines.append(f"- Проверка: {m['verify']}")
        if m.get('note'):
            lines.append(f"- Заметка: {m['note']}")
        lines.append('')
open(f'{OUT}/MODLIST.md', 'w', encoding='utf-8').write('\n'.join(lines))

# CONFLICTS.md
c = ['# Конфликты, порядок и запреты', '',
     'Агент сверяется с этим файлом перед каждой фазой. Если правило расходится с карточкой мода, главнее это правило.', '',
     '## Группы «одно из»', '', 'В каждой группе ставится один мод. По умолчанию — указанный, если пользователь не выбрал иначе в `OVERRIDES`.', '',
     '| Группа | Варианты | По умолчанию | Правило |', '|---|---|---|---|']
for g in groups:
    c.append(f"| `{g['group']}` | {'; '.join(g['members'])} | {g['default']} | {g['rule']} |")
if system_reqs:
    c += ['', '## Системные требования (не моды MO2)', '', 'Проверить на компьютере до установки; из MO2 не ставятся.', '']
    c += [f"- **{r['name']}** — нужен для: {', '.join(_names(x) for x in r['needed_by'])}. {r.get('note', '')}" for r in system_reqs]
c += ['', '## Порядок в MO2 (левая панель)', '', 'Разделители сверху вниз: ' + ' → '.join(by_sep.keys()) + '.', '']
c += [f'{i}. {_names(r)}' for i, r in enumerate(crit.get('order_rules', []), 1)]
c += ['', '## Порядок плагинов', '', 'Сначала LOOT, затем эти правила:', '']
c += [f'{i}. {_names(r)}' for i, r in enumerate(crit.get('plugin_rules', []), 1)]
if crit.get('contradictions'):
    c += ['', '## Найденные противоречия и как они решены', '']
    for x in crit['contradictions']:
        c.append(f"- **{', '.join(_names(k) for k in x['keys'])}**: {_names(x['problem'])} → {_names(x['fix'])}")
c += ['', '## Не ставить в VR', '', '| Что | Почему |', '|---|---|']
c += [f'| {a} | {b} |' for a, b in draft['dont']]
open(f'{OUT}/CONFLICTS.md', 'w', encoding='utf-8').write('\n'.join(c) + '\n')

# links
os.makedirs(f'{OUT}/links', exist_ok=True)
for n, t, secs in PHASES:
    L = [f'# Фаза {n}: {t}', '# Открыть ссылки в браузере, скачать нужный файл (см. manifest.yaml → files). Метка в скобках — tag.', '']
    for m in sorted([x for x in mods if x['phase'] == n], key=lambda x: (x['separator'], x['order'])):
        L.append(f"# [{m['tag']}] {m['name']} — {m['files']}")
        if m.get('url'):
            L.append(m['url'])
        for e in m.get('also_download', []):
            L.append(e.split(': ', 1)[1])
        L.append('')
    open(f'{OUT}/links/phase-{n}.txt', 'w', encoding='utf-8').write('\n'.join(L))
print('mods', len(mods), 'groups', len(groups), 'order_rules', len(crit.get('order_rules', [])), 'plugin_rules', len(crit.get('plugin_rules', [])))
