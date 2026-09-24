# -*- coding: utf-8 -*-
"""Пример 1: статья «Вычеты на обучение» в журнале «Главная книга» — карточка «Авторские материалы»."""
from kp import *


def open_field(page, name):
    page.locator('.x-page-card-field-name', has_text=name).first.click()
    page.wait_for_timeout(3500)


with sync_playwright() as pw:
    br, page = browser(pw)
    page.goto(CARD_LAW, wait_until='domcontentloaded')
    page.wait_for_timeout(6000)

    # вкладка «Другие разделы» → «Авторские материалы» (там живут пресса и книги)
    page.get_by_text('Другие разделы', exact=True).first.click()
    page.wait_for_timeout(1500)
    shot(page, 'ex1_01_sections_menu')
    page.get_by_text('Авторские материалы', exact=True).first.click()
    page.wait_for_timeout(6000)
    shot(page, 'ex1_02_card_authors')

    open_field(page, 'Название документа')
    box = page.locator('input[placeholder*="Слова для поиска"]:visible').first
    box.click(); box.type('ВЫЧЕТЫ НА ОБУЧЕНИЕ', delay=20)
    page.wait_for_timeout(600)
    shot(page, 'ex1_03_title_dialog')
    page.get_by_role('button', name='Найти').first.click()
    page.wait_for_timeout(6000)

    open_field(page, 'Источник публикации')
    page.wait_for_timeout(2000)
    shot(page, 'ex1_04a_source_dialog_raw')
    print('=== SOURCE DIALOG ===')
    print(page.evaluate("document.body.innerText.slice(-1200)"))
    box = page.locator('input[type=text]:visible').first
    box.click(); box.type('ГЛАВНАЯ КНИГА 2019', delay=20)
    page.wait_for_timeout(600)
    shot(page, 'ex1_04_source_dialog')
    page.get_by_role('button', name='Найти').first.click()
    page.wait_for_timeout(6000)
    shot(page, 'ex1_04b_source_found')
    # выбираем издание за весь 2019 год
    page.get_by_text('"Главная книга", 2019', exact=True).first.click()
    page.wait_for_timeout(5000)
    shot(page, 'ex1_05_card_filled')

    page.get_by_text('Показать список документов', exact=True).first.click()
    page.wait_for_timeout(9000)
    shot(page, 'ex1_06_list')
    print(page.evaluate("document.body.innerText.slice(0,1500)"))
    br.close()
