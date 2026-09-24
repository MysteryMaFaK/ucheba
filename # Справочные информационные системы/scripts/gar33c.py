# -*- coding: utf-8 -*-
"""ГАРАНТ: список + открытие первого документа по каждому вопросу 3.3."""
import os, sys, io, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from playwright.sync_api import sync_playwright

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'shots33g')
UA = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
      'Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0')
QUERIES = {
 1: 'социальный налоговый вычет лекарственные препараты назначенные лечащим врачом',
 2: 'ветхие банкноты посторонняя надпись',
 4: 'социальный налоговый вычет на обучение иностранная организация',
 5: 'дни приезда и отъезда 183 дня налоговый резидент',
 6: 'налоговая база НДС увеличивается на суммы связанные с оплатой',
 7: 'передача права собственности на безвозмездной основе признается реализацией',
 8: 'средняя численность работников упрощенная система налогообложения',
}
result = {}
with sync_playwright() as pw:
    br = pw.chromium.launch(channel='msedge', headless=True)
    ctx = br.new_context(user_agent=UA, locale='ru-RU', viewport={'width': 1280, 'height': 800},
                         device_scale_factor=2)
    page = ctx.new_page(); page.set_default_timeout(60000)
    for num, q in QUERIES.items():
        print('---', num)
        page.goto('https://ivo.garant.ru/', wait_until='domcontentloaded')
        page.wait_for_timeout(11000)
        box = page.locator('input[type=text]:visible').first
        box.click(); box.fill(q); page.wait_for_timeout(1500)
        page.keyboard.press('Enter')
        page.wait_for_timeout(14000)
        page.screenshot(path=os.path.join(OUT, f'g{num}_1_list.png'))
        # первая строка списка — ссылка на документ
        links = page.evaluate("""() => [...document.querySelectorAll('a')]
            .map(a=>({t:(a.innerText||'').replace(/\s+/g,' ').trim(), h:a.getAttribute('href')||''}))
            .filter(o=>o.t.length>30 && /document/.test(o.h)).slice(0,3)""")
        title, doc_txt, url = '', '', page.url
        if links:
            title = links[0]['t'][:200]
            page.goto('https://ivo.garant.ru' + links[0]['h'] if links[0]['h'].startswith('/')
                      else links[0]['h'], wait_until='domcontentloaded')
            page.wait_for_timeout(12000)
            page.screenshot(path=os.path.join(OUT, f'g{num}_2_doc.png'))
            doc_txt = page.evaluate("document.body.innerText")[:2500]
            url = page.url
        print('   ', (title or '(ссылка не найдена)')[:100], '| len', len(doc_txt))
        result[num] = {'query': q, 'title': title, 'url': url, 'doc': doc_txt,
                       'list_head': page.evaluate("document.body.innerText")[:900]}
    br.close()
with open('gar33c.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=1)
print('SAVED')
