# -*- coding: utf-8 -*-
"""Нормативка по дистанционной продаже БАД: карточка поиска раздела «Законодательство»."""
from kpfree import *
import json
CARD = 'https://www.consultant.ru/cons/cgi/online.cgi?req=card&div=LAW'

with sync_playwright() as pw:
    br, page = browser(pw)
    page.goto(CARD, wait_until='domcontentloaded'); page.wait_for_timeout(7000)
    page.locator('.x-page-card-field-name', has_text='Текст документа').first.click()
    page.wait_for_timeout(3500)
    box = page.locator('input[placeholder*="Слова для поиска"]:visible').first
    box.click(); box.type('БИОЛОГИЧЕСКИ АКТИВНЫЕ ДОБАВКИ И ДИСТАНЦИОННЫЙ СПОСОБ ПРОДАЖИ', delay=14)
    page.get_by_role('button', name='Найти').first.click(); page.wait_for_timeout(7000)
    shot(page, '32_p4_card')
    try:
        page.get_by_text('Показать список документов', exact=True).first.click()
        page.wait_for_timeout(9000)
    except Exception as e:
        print('нет кнопки списка:', e)
    shot(page, '32_p4_law_list')
    print(page.evaluate("document.body.innerText")[:1200].replace('\n', ' | '))
    items = page.evaluate("""() => [...document.querySelectorAll('a[href*="req=doc"]')]
        .map(a=>({t:(a.innerText||'').replace(/\s+/g,' ').trim(), h:a.href}))
        .filter(x=>x.t.length>25).slice(0,15)""")
    for i, it in enumerate(items): print(i, it['t'][:170])
    json.dump(items, open('p4_law.json','w',encoding='utf-8'), ensure_ascii=False, indent=1)
    br.close()
