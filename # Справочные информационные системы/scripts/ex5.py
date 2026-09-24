# -*- coding: utf-8 -*-
"""Пример 5: Правовой навигатор — документы для налогового вычета на обучение."""
from kp import *

with sync_playwright() as pw:
    br, page = browser(pw)
    page.goto(HOME, wait_until='domcontentloaded')
    page.wait_for_timeout(6000)

    page.get_by_text('Ещё', exact=True).first.click()
    page.wait_for_timeout(1500)
    shot(page, 'ex5_01_more_menu')
    page.get_by_text('Правовой навигатор', exact=True).first.click()
    page.wait_for_timeout(8000)
    shot(page, 'ex5_02_navigator')
    print('URL:', page.url)

    box = page.locator('input[type=text]:visible').first
    box.click(); box.type('ВЫЧЕТ ОБУЧЕНИЕ', delay=25)
    page.wait_for_timeout(1500)
    page.get_by_text('Фильтр', exact=True).first.click()
    page.wait_for_timeout(6000)
    shot(page, 'ex5_03_query')
    print('=== AFTER FILTER ===')
    print(page.evaluate("document.body.innerText.slice(0,1500)"))

    page.get_by_text('НДФЛ', exact=True).first.click()
    page.wait_for_timeout(5000)
    shot(page, 'ex5_04_group_ndfl')

    # клик по тексту только подсвечивает понятие — отмечать надо чекбокс в той же строке
    lab = page.get_by_text('Налоговый вычет за обучение', exact=True).first
    lab.scroll_into_view_if_needed()
    page.wait_for_timeout(800)
    b = lab.bounding_box()
    page.mouse.click(b['x'] - 26, b['y'] + b['height'] / 2)   # квадратик чекбокса слева от подписи
    page.wait_for_timeout(2000)
    print('checked:',
          page.evaluate("[...document.querySelectorAll('input[type=checkbox]')].filter(c=>c.checked).length"))
    shot(page, 'ex5_05_concept_selected')

    page.keyboard.press('F9')   # то же, что кнопка «Построить список документов»
    page.wait_for_timeout(10000)
    shot(page, 'ex5_06_list')
    print(page.evaluate("document.body.innerText.slice(0,1500)"))
    br.close()
