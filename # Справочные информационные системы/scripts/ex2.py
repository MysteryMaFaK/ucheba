# -*- coding: utf-8 -*-
"""Пример 2: льготы по НДФЛ с 01.01.2019, имущественный вычет + печать списка."""
from kp import *


def open_field(page, name):
    page.locator('.x-page-card-field-name', has_text=name).first.click()
    page.wait_for_timeout(3500)


with sync_playwright() as pw:
    br, page = browser(pw)
    page.goto(CARD_LAW, wait_until='domcontentloaded')
    page.wait_for_timeout(6000)

    # --- Текст документа
    open_field(page, 'Текст документа')
    box = page.locator('input[placeholder*="Слова для поиска"]:visible').first
    box.click(); box.type('ИМУЩЕСТВЕННЫЙ ВЫЧЕТ', delay=20)
    page.wait_for_timeout(600)
    shot(page, 'ex2_01_text_dialog')
    page.get_by_role('button', name='Найти').first.click()
    page.wait_for_timeout(5000)

    # --- Дата (разведка содержимого диалога)
    open_field(page, 'Дата')
    page.wait_for_timeout(2000)
    # выбираем режим «Позже чем» и печатаем дату в маскированное поле как пользователь
    page.get_by_text('Позже чем:', exact=True).first.click()
    page.wait_for_timeout(1000)
    print('radio ok')
    date_inputs = page.locator('input[type=text]:visible')
    print('visible inputs:', date_inputs.count())
    date_inputs.nth(1).click()
    page.keyboard.press('Home')     # маска ДД.ММ.ГГГГ — курсор должен стоять в начале
    page.keyboard.type('01012019', delay=120)
    page.wait_for_timeout(1200)
    # Escape закрыл бы весь диалог — гасим календарь кликом по заголовку
    page.get_by_text('Поиск по полю «Дата»', exact=True).first.click()
    page.wait_for_timeout(1000)
    print('date typed')
    shot(page, 'ex2_03_date_filled')
    page.get_by_text('Применить', exact=True).first.click()
    page.wait_for_timeout(7000)
    print('applied')
    shot(page, 'ex2_03b_after_apply')

    # --- Тематика
    open_field(page, 'Тематика')
    box = page.locator('input[type=text]:visible').first
    box.click(); box.type('Льготы по налогу на доходы физических лиц', delay=15)
    page.get_by_role('button', name='Найти').first.click()
    page.wait_for_timeout(4000)
    shot(page, 'ex2_04_theme_search')
    page.get_by_text('Льготы по налогу на доходы физических лиц', exact=True).first.click()
    page.wait_for_timeout(5000)
    shot(page, 'ex2_05_card_filled')

    page.get_by_text('Показать список документов', exact=True).first.click()
    page.wait_for_timeout(9000)
    shot(page, 'ex2_06_list')
    print(page.evaluate("document.body.innerText.slice(0,1000)"))

    # пробуем печать списка (в схеме — с выбором полей «Название» и «Примечание»)
    print('=== PRINT TOOLBAR ===')
    print(page.evaluate("""() => {
      return [...document.querySelectorAll('[title],[aria-label],button')]
        .map(e=>(e.getAttribute('title')||e.getAttribute('aria-label')||e.innerText||'').trim())
        .filter(t=>t && t.length<40).slice(0,40);
    }"""))
    br.close()
