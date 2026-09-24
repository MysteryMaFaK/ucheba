# -*- coding: utf-8 -*-
"""Задание 3.2, пункт 2: документы Минфина 2015-2016 гг. по бухгалтерской отчётности."""
from kpfree import *
CARD = 'https://www.consultant.ru/cons/cgi/online.cgi?req=card&div=LAW'


def open_field(page, name):
    page.locator('.x-page-card-field-name', has_text=name).first.click()
    page.wait_for_timeout(3500)


with sync_playwright() as pw:
    br, page = browser(pw)
    page.goto(CARD, wait_until='domcontentloaded')
    page.wait_for_timeout(7000)

    # Принявший орган
    open_field(page, 'Принявший орган')
    box = page.locator('input[type=text]:visible').first
    box.click(); box.type('Минфин России', delay=20)
    page.get_by_role('button', name='Найти').first.click()
    page.wait_for_timeout(4000)
    shot(page, '32_p2_organ')
    page.get_by_text('МИНФИН РОССИИ', exact=True).first.click()
    page.wait_for_timeout(4000)

    # Дата — диапазон 2015-2016
    open_field(page, 'Дата')
    page.wait_for_timeout(1500)
    page.get_by_text('Диапазон дат:', exact=True).first.click()
    page.wait_for_timeout(800)
    ins = page.locator('input[type=text]:visible')
    ins.nth(3).click(); page.keyboard.press('Home'); page.keyboard.type('01012015', delay=110)
    page.wait_for_timeout(600)
    page.get_by_text('Поиск по полю «Дата»', exact=True).first.click()
    page.wait_for_timeout(600)
    ins.nth(4).click(); page.keyboard.press('Home'); page.keyboard.type('31122016', delay=110)
    page.wait_for_timeout(600)
    page.get_by_text('Поиск по полю «Дата»', exact=True).first.click()
    page.wait_for_timeout(800)
    shot(page, '32_p2_date')
    page.get_by_text('Применить', exact=True).first.click()
    page.wait_for_timeout(6000)

    # Тематика
    open_field(page, 'Тематика')
    box = page.locator('input[type=text]:visible').first
    box.click(); box.type('Бухгалтерская отчетность', delay=18)
    page.get_by_role('button', name='Найти').first.click()
    page.wait_for_timeout(4000)
    shot(page, '32_p2_theme')
    print(page.evaluate("document.body.innerText")[-700:].replace('\n', ' | '))
    br.close()
