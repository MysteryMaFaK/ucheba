# -*- coding: utf-8 -*-
"""Пример 4: подборка действующих документов по защите прав потребителей."""
from kp import *


def open_field(page, name):
    page.locator('.x-page-card-field-name', has_text=name).first.click()
    page.wait_for_timeout(3500)


with sync_playwright() as pw:
    br, page = browser(pw)
    page.goto(CARD_LAW, wait_until='domcontentloaded')
    page.wait_for_timeout(6000)

    # --- Тематика
    open_field(page, 'Тематика')
    box = page.locator('.x-dialog input[type=text]:visible, .x-modal input[type=text]:visible').first
    if box.count() == 0:
        box = page.locator('input[type=text]:visible').first
    box.click()
    box.type('Защита прав потребителей', delay=20)
    page.get_by_role('button', name='Найти').first.click()
    page.wait_for_timeout(4000)
    shot(page, 'ex4_01_theme_search')

    # клик по рубрике сразу подставляет её в карточку, «Применить» не требуется
    page.get_by_text('Защита прав потребителей', exact=True).first.click()
    page.wait_for_timeout(4000)
    shot(page, 'ex4_02_theme_selected')

    # --- Поиск по статусу
    open_field(page, 'Поиск по статусу')
    page.wait_for_timeout(1500)
    shot(page, 'ex4_03_status_dialog')

    page.get_by_text('Все акты, кроме утративших силу, отмененных и не вступивших в силу',
                     exact=True).first.click()
    page.wait_for_timeout(4000)
    shot(page, 'ex4_04_card_filled')

    page.get_by_text('Показать список документов', exact=True).first.click()
    page.wait_for_timeout(9000)
    shot(page, 'ex4_05_list')
    print(page.evaluate("document.body.innerText.slice(0,1200)"))
    br.close()
