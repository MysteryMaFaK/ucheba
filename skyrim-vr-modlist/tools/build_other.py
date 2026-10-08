"""Build 'Skyrim VR Other Mods 2026' page + markdown from the other-mods workflow output."""
import json, sys, html, re, collections, os

HERE = os.path.dirname(os.path.abspath(__file__))
SCR = os.path.dirname(HERE)
NX = 'https://www.nexusmods.com/skyrimspecialedition/mods/{}'
res = json.load(open(sys.argv[1]))['result']

PARTS = [
    ('Часть 1 · Пробелы ядра', 'Ставится сразу после ядра, до текстур.',
     [('start', 'Альтернативный старт'), ('followers', 'Фреймворк спутников'), ('navigation', 'Навигация'), ('controls', 'Управление и пресеты'),
      ('russian', 'Русификация'), ('saves', 'Сохранения'), ('cc', 'Creation Club из AE'), ('equipment', 'Снаряжение на теле'),
      ('voice', 'Голосовые команды'), ('music', 'Музыка'), ('niche', 'Ниша: тактильность и передвижение')]),
    ('Часть 2 · Текстуры', 'По умолчанию 2K: в VR видеопамять уходит на два глаза. 4K — только для того, что видно вплотную. После текстур: PGPatcher, прекэш травы, xLODGen, TexGen, DynDOLOD.',
     [('tex_strategy', 'Стратегия и инструменты VRAM'), ('tex_land', 'Ландшафт и горы'), ('tex_flora', 'Флора'), ('tex_water_sky', 'Вода и небо'),
      ('tex_arch', 'Города и архитектура'), ('tex_dungeons', 'Подземелья и руины'), ('tex_clutter', 'Клаттер и мебель'), ('tex_pbr_tools', 'PBR и патчеры')]),
    ('Часть 3 · Внешний вид и мир', 'Тела ставятся до брони, после них — BodySlide. Тяжёлые меши городов в VR бьют по процессору сильнее, чем в плоской игре.',
     [('chars_body', 'Тела'), ('chars_faces', 'Лица, волосы, глаза'), ('physics', 'Физика тел и одежды'), ('armor', 'Броня, оружие, одежда'),
      ('creatures', 'Существа'), ('city_meshes', 'Города и постройки'), ('clutter_meshes', 'Клаттер, мебель, еда'), ('reshade', 'ReShade поверх Open Shaders')]),
]
TAGS = {'rec': 'рекомендую', 'opt': 'по желанию', 'alt': 'выбор', 'try': 'проверить'}

leads = {}
for l in res['leads']:
    leads.setdefault(l['section'], l['lead'])
items = collections.defaultdict(list)
dont = []
for x in res['verified']:
    if not x['keep']:
        continue
    a, b = x['compat'], x['value']
    tag = 'dont' if 'dont' in (a['tag'], b['tag']) else ('try' if a['tag'] == 'try' else b['tag'])
    sec = b['section']
    if tag == 'dont' or sec == 'dont':
        dont.append((x['name'], b['what'] if b['what'] else b['note']))
        continue
    url = x['url'] if x.get('url', '').startswith('http') else (NX.format(x['id']) if x.get('id') else '')
    group = b.get('choose_one_group') or a.get('choose_one_group') or x.get('choose_one_group')
    note = b['note']
    if a['tag'] == 'try' and a.get('note') and a['note'] not in note:
        note = (note + ' ' + a['note']).strip()
    items[sec].append(dict(id=x.get('id'), name=x['name'], url=url, tag=tag if tag in TAGS else 'opt', what=b['what'], note=note,
                           files=x.get('files', ''), requires=x.get('requires', []), group=group))


def esc(s):
    return html.escape(s or '', quote=True)


def li(sec, it, i):
    key = f"{sec}-{it['id'] or i}"
    meta = []
    if it['id']:
        meta.append(f'<span class="mid">#{it["id"]}</span>')
    if it['files']:
        meta.append(f'<span class="file">{esc(it["files"])}</span>')
    if it['group']:
        meta.append(f'<span class="ver">одно из: {esc(it["group"])}</span>')
    req = f'<p class="note">Требует: {esc("; ".join(it["requires"]))}</p>' if it['requires'] else ''
    note = ' '.join(p for p in [it['what'], it['note']] if p)
    return (f'<li class="mod" data-tag="{it["tag"]}" data-key="{esc(key)}"><input type="checkbox" id="c-{esc(key)}" aria-label="Отметить: {esc(it["name"])}">'
            f'<div class="body"><div class="head"><label for="c-{esc(key)}" class="nm"><a href="{esc(it["url"])}" target="_blank" rel="noopener">{esc(it["name"])}</a></label>'
            f'<span class="tag t-{it["tag"]}">{TAGS[it["tag"]]}</span></div><div class="meta">{"".join(meta)}</div><p class="note">{esc(note)}</p>{req}</div></li>')


order = {'rec': 0, 'alt': 1, 'opt': 2, 'try': 3}
html_secs, nav, md, total = [], [], ['# Skyrim VR Other Mods 2026', '',
    'Дополнение к ядру Skyrim VR Core 2026: пробелы ядра, текстуры, внешний вид. Совместимость с VR проверена дважды, данные на 08.10.2026.',
    'Метки: `rec` рекомендую · `opt` по желанию · `alt` один из группы · `try` VR заявлен, но не обкатан.', ''], 0
for ptitle, plead, secs in PARTS:
    pid = 'part' + str(PARTS.index((ptitle, plead, secs)) + 1)
    html_secs.append(f'<h2 class="part" id="{pid}">{esc(ptitle)}<small>{esc(plead)}</small></h2>')
    nav.append(f'<a href="#{pid}"><b>{esc(ptitle.split(" · ")[1])}</b></a>')
    md += [f'## {ptitle}', '', plead, '']
    for sid, stitle in secs:
        its = sorted(items.get(sid, []), key=lambda t: (order.get(t['tag'], 9), t['name']))
        if not its:
            continue
        total += len(its)
        lead = leads.get(sid, '')
        html_secs.append(f'<section id="{sid}" class="sec"><h2>{esc(stitle)} <span class="cnt" data-sec="{sid}"></span></h2>'
                         + (f'<p class="lead">{esc(lead)}</p>' if lead else '') + '<ul class="mods">' + ''.join(li(sid, t, i) for i, t in enumerate(its)) + '</ul></section>')
        nav.append(f'<a href="#{sid}">{esc(stitle)}</a>')
        md += [f'### {stitle}', ''] + ([lead, ''] if lead else [])
        for t in its:
            link = f"[#{t['id']}]({t['url']})" if t['id'] else (f"[ссылка]({t['url']})" if t['url'] else '')
            md.append(f"- **{t['name']}** `{t['tag']}` {link} — {t['what']}" + (f" Файл: {t['files']}." if t['files'] else '')
                      + (f" Требует: {'; '.join(t['requires'])}." if t['requires'] else '') + (f" Одно из: `{t['group']}`." if t['group'] else '') + (f" {t['note']}" if t['note'] else ''))
        md.append('')
md += ['## Не ставить в VR', ''] + [f'- **{a}** — {b}' for a, b in dont]
SRC = [('Отчёты Wabbajack по 27 сборкам', 'https://github.com/wabbajack-tools/mod-lists/tree/master/reports'),
       ('Отчёт Panda\'s Sovngarde (VR, упор на графику)', 'https://github.com/wabbajack-tools/mod-lists/blob/master/reports/VirtualPanda/PandasSovngarde/status.md'),
       ('Отчёт Stormcrown VR', 'https://github.com/wabbajack-tools/mod-lists/blob/master/reports/Stormcrown_VR/Stormcrown_VR/status.md'),
       ('Отчёт Yggdrasil VR', 'https://github.com/wabbajack-tools/mod-lists/blob/master/reports/wj-featured/yggdrasil_vr/status.md'),
       ('Ядро: Skyrim VR Core 2026', 'https://claude.ai/artifact/CtFycL6Py2fC2TDY7NZgCa')]
tpl = open(f'{SCR}/tools/template_other.html', encoding='utf-8').read()
page = (tpl.replace('{{NAV}}', ''.join(nav)).replace('{{SECTIONS}}', ''.join(html_secs)).replace('{{TOTAL}}', str(total))
        .replace('{{DONT}}', ''.join(f'<li><strong>{esc(a)}</strong><span>{esc(b)}</span></li>' for a, b in dont))
        .replace('{{SRC}}', ''.join(f'<li><a href="{esc(u)}" target="_blank" rel="noopener">{esc(t)}</a></li>' for t, u in SRC)))
open(sys.argv[2], 'w', encoding='utf-8').write(page)
open(sys.argv[3], 'w', encoding='utf-8').write('\n'.join(md) + '\n')
print('items', total, 'dont', len(dont), {k: len(v) for k, v in items.items()})
