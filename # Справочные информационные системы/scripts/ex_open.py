# -*- coding: utf-8 -*-
"""Досъёмка: открытие найденных документов (НК РФ ст. 333.8 и статья «Главной книги»)."""
from kp import *


def open_field(page, name):
    page.locator('.x-page-card-field-name', has_text=name).first.click()
    page.wait_for_timeout(3500)


with sync_playwright() as pw:
    br, page = browser(pw)

    # ---------- Пример 3: НК РФ (часть вторая), ст. 333.8 ----------
    page.goto(CARD_LAW, wait_until='domcontentloaded')
    page.wait_for_timeout(6000)
    open_field(page, 'Текст документа')
    page.get_by_text('Расширенный поиск', exact=True).first.click()
    page.wait_for_timeout(1500)
    box = page.locator('input[placeholder*="Слова для поиска"]:visible').first
    box.click(); box.type('НАЛОГОПЛАТЕЛЬЩИКАМИ ВОДНОГО НАЛОГА', delay=20)
    page.get_by_text('Как словосочетание', exact=True).first.click()
    page.get_by_text('Точно, как в запросе', exact=True).first.click()
    page.get_by_role('button', name='Найти').first.click()
    page.wait_for_timeout(6000)
    page.get_by_text('Показать список документов', exact=True).first.click()
    page.wait_for_timeout(9000)

    page.get_by_text('"Налоговый кодекс Российской Федерации (часть вторая)" от 05.08.2000 N 117-ФЗ',
                     exact=True).first.click()
    page.wait_for_timeout(10000)
    shot(page, 'ex3_05_nk_333_8')
    print('=== NK ===')
    print(page.evaluate("document.body.innerText.slice(0,900)"))

    # ---------- Пример 1: статья Шароновой ----------
    page.goto(CARD_LAW, wait_until='domcontentloaded')
    page.wait_for_timeout(6000)
    page.get_by_text('Другие разделы', exact=True).first.click()
    page.wait_for_timeout(1500)
    page.get_by_text('Авторские материалы', exact=True).first.click()
    page.wait_for_timeout(6000)
    open_field(page, 'Название документа')
    box = page.locator('input[placeholder*="Слова для поиска"]:visible').first
    box.click(); box.type('ВЫЧЕТЫ НА ОБУЧЕНИЕ', delay=20)
    page.get_by_role('button', name='Найти').first.click()
    page.wait_for_timeout(6000)
    open_field(page, 'Источник публикации')
    box = page.locator('input[type=text]:visible').first
    box.click(); box.type('ГЛАВНАЯ КНИГА 2019', delay=20)
    page.get_by_role('button', name='Найти').first.click()
    page.wait_for_timeout(6000)
    page.get_by_text('"Главная книга", 2019', exact=True).first.click()
    page.wait_for_timeout(5000)
    page.get_by_text('Показать список документов', exact=True).first.click()
    page.wait_for_timeout(9000)

    page.get_by_text('Вычеты на обучение: кому, сколько и как получить', exact=True).first.click()
    page.wait_for_timeout(10000)
    shot(page, 'ex1_07_article')
    print('=== ARTICLE ===')
    print(page.evaluate("document.body.innerText.slice(0,900)"))
    br.close()
