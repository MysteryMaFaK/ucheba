# -*- coding: utf-8 -*-
"""Задание 3.3: те же вопросы в системе ГАРАНТ (открытая база base.garant.ru)."""
import os, sys, io, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from playwright.sync_api import sync_playwright
from urllib.parse import quote

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'shots33g')
os.makedirs(OUT, exist_ok=True)

QUERIES = {
 1: 'социальный налоговый вычет лекарственные препараты назначенные лечащим врачом',
 2: 'ветхие банкноты посторонняя надпись кассовые операции',
 4: 'социальный налоговый вычет на обучение иностранная организация',
 5: 'дни приезда и отъезда 183 дня налоговый резидент НДФЛ',
 6: 'налоговая база НДС увеличивается на суммы связанные с оплатой реализованных товаров',
 7: 'передача права собственности на товары на безвозмездной основе признается реализацией НДС',
 8: 'средняя численность работников упрощенная система налогообложения 130 человек',
}
result = {}
with sync_playwright() as pw:
    br = pw.chromium.launch(channel='msedge', headless=True)
    ctx = br.new_context(viewport={'width': 1280, 'height': 800}, device_scale_factor=2, locale='ru-RU',
                         user_agent='Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0')
    page = ctx.new_page(); page.set_default_timeout(45000)
    # прогрев: без визита на главную поиск отдаёт 403
    page.goto('https://base.garant.ru/', wait_until='domcontentloaded'); page.wait_for_timeout(5000)
    for num, q in QUERIES.items():
        print('---', num)
        page.goto('https://base.garant.ru/search/?text=' + quote(q), wait_until='domcontentloaded')
        page.wait_for_timeout(7000)
        page.screenshot(path=os.path.join(OUT, f'g{num}_1_list.png'))
        items = page.evaluate("""() => [...document.querySelectorAll('a')]
            .map(a=>({t:(a.innerText||'').replace(/\s+/g,' ').trim(), h:a.getAttribute('href')||''}))
            .filter(o=>/^\/\d+/.test(o.h) && o.t.length>25).slice(0,6)""")
        for i, it in enumerate(items):
            print(f'   {i}. {it["t"][:95]} | {it["h"][:30]}')
        if not items:
            continue
        page.goto('https://base.garant.ru' + items[0]['h'], wait_until='domcontentloaded')
        page.wait_for_timeout(7000)
        page.screenshot(path=os.path.join(OUT, f'g{num}_2_doc.png'))
        txt = page.evaluate("document.body.innerText")
        result[num] = {'query': q, 'title': items[0]['t'][:220],
                       'url': 'https://base.garant.ru' + items[0]['h'],
                       'len': len(txt), 'head': txt[:1500]}
        print('   >> len', len(txt))
    br.close()
with open('gar33.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=1)
print('SAVED')
