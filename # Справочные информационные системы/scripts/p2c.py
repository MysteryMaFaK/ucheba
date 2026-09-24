# -*- coding: utf-8 -*-
"""Задание 3.2, пункт 2: Минфин России, 2015-2016 гг., бухгалтерская отчётность."""
from kpfree import *
CARD = 'https://www.consultant.ru/cons/cgi/online.cgi?req=card&div=LAW'


def open_field(page, name):
    page.locator('.x-page-card-field-name', has_text=name).first.click()
    page.wait_for_timeout(3500)


with sync_playwright() as pw:
    br, page = browser(pw)
    page.goto(CARD, wait_until='domcontentloaded'); page.wait_for_timeout(7000)

    # Принявший орган = Минфин России
    open_field(page, 'Принявший орган')
    box = page.locator('input[type=text]:visible').first
    box.click(); box.type('Минфин', delay=20)
    page.get_by_role('button', name='Найти').first.click(); page.wait_for_timeout(4500)
    page.evaluate("""()=>{
      const els=[...document.querySelectorAll('*')]
        .filter(e=>e.children.length===0 && e.textContent.trim()==='Минфин России');
      if(els.length) els[els.length-1].click();
    }""")
    page.wait_for_timeout(2500)
    try:
        page.get_by_text('Применить', exact=True).first.click(timeout=5000); page.wait_for_timeout(5000)
    except Exception:
        pass
    shot(page, '32_p2_organ')

    # Дата — диапазон 01.01.2015 … 31.12.2016
    open_field(page, 'Дата')
    page.wait_for_timeout(1500)
    page.get_by_text('Диапазон дат:', exact=True).first.click(); page.wait_for_timeout(1000)
    ins = page.locator('input[type=text]:visible')
    n = ins.count()
    print('видимых полей:', n)
    ins.nth(n - 2).click(); page.keyboard.press('Home'); page.keyboard.type('01012015', delay=110)
    page.wait_for_timeout(600)
    page.get_by_text('Поиск по полю «Дата»', exact=True).first.click(); page.wait_for_timeout(700)
    ins.nth(n - 1).click(); page.keyboard.press('Home'); page.keyboard.type('31122016', delay=110)
    page.wait_for_timeout(600)
    page.get_by_text('Поиск по полю «Дата»', exact=True).first.click(); page.wait_for_timeout(900)
    shot(page, '32_p2_date')
    page.get_by_text('Применить', exact=True).first.click(); page.wait_for_timeout(6000)

    # Текст документа
    open_field(page, 'Текст документа')
    box = page.locator('input[placeholder*="Слова для поиска"]:visible').first
    box.click(); box.type('БУХГАЛТЕРСКАЯ ОТЧЕТНОСТЬ', delay=18)
    page.get_by_role('button', name='Найти').first.click(); page.wait_for_timeout(6000)
    shot(page, '32_p2_card')

    page.get_by_text('Показать список документов', exact=True).first.click()
    page.wait_for_timeout(10000)
    shot(page, '32_p2_list')
    print(page.evaluate("document.body.innerText")[:900].replace('\n', ' | '))
    br.close()
