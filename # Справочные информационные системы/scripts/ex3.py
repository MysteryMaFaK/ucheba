# -*- coding: utf-8 -*-
"""Пример 3: расширенный поиск по полю «Текст документа» — «налогоплательщиками водного налога»."""
from kp import *

with sync_playwright() as pw:
    br, page = browser(pw)

    page.goto(CARD_LAW, wait_until='domcontentloaded')
    page.wait_for_timeout(6000)
    shot(page, 'ex3_01_card')

    page.get_by_text('Текст документа', exact=True).first.click()
    page.wait_for_timeout(2500)
    page.get_by_text('Расширенный поиск', exact=True).first.click()
    page.wait_for_timeout(2000)

    box = page.locator('input[placeholder*="Слова для поиска"]:visible').first
    box.click()
    box.type('НАЛОГОПЛАТЕЛЬЩИКАМИ ВОДНОГО НАЛОГА', delay=20)
    page.wait_for_timeout(500)
    page.get_by_text('Как словосочетание', exact=True).first.click()
    page.wait_for_timeout(400)
    page.get_by_text('Точно, как в запросе', exact=True).first.click()
    page.wait_for_timeout(1000)
    shot(page, 'ex3_02_dialog')

    page.get_by_role('button', name='Найти').first.click()
    page.wait_for_timeout(6000)
    shot(page, 'ex3_03_card_filled')

    page.get_by_text('Показать список документов', exact=True).first.click()
    page.wait_for_timeout(8000)
    shot(page, 'ex3_04_list')

    print('URL:', page.url)
    print(page.evaluate("document.body.innerText.slice(0,1200)"))
    br.close()
