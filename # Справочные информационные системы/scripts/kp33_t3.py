# -*- coding: utf-8 -*-
"""Задание 3.3, пункт 3: список последних открытых документов."""
from kp33 import *
with sync_playwright() as pw:
    br, page = browser(pw)
    # открываем несколько документов, чтобы список заполнился
    for q, tab in [('признаки платежеспособности банкнот Банка России ветхие', True),
                   ('статья 219 социальные налоговые вычеты', True),
                   ('вычеты на обучение главная книга', False)]:
        quick_search(page, q)
        if tab:
            try:
                page.get_by_text('Законодательство', exact=True).first.click()
                page.wait_for_timeout(5000)
            except Exception:
                pass
        items = page.evaluate("""() => [...document.querySelectorAll('a[href*="req=doc"]')]
            .map(a=>a.getAttribute('href'))""")
        if items:
            page.goto('https://www.consultant.ru/cons/cgi/' + items[0].replace('../cgi/', ''),
                      wait_until='domcontentloaded')
            page.wait_for_timeout(9000)
    page.goto('https://www.consultant.ru/cons/cgi/online.cgi?req=home', wait_until='domcontentloaded')
    page.wait_for_timeout(8000)
    shot(page, 'n3_1_home_recent')
    t = page.evaluate("document.body.innerText")
    i = t.find('Последние')
    print(t[i:i+700].replace('\n', ' | '))
    br.close()
