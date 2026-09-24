# -*- coding: utf-8 -*-
"""Задание 3.2, пункт 2: подборка документов Минфина 2015-2016 гг. по бухгалтерской отчётности."""
from kpfree import *
CARD = 'https://www.consultant.ru/cons/cgi/online.cgi?req=card&div=LAW'


def open_field(page, name):
    page.locator('.x-page-card-field-name', has_text=name).first.click()
    page.wait_for_timeout(3500)


def dict_pick(page, query, value):
    """Словарное поле: ищем значение и отмечаем его, затем «Применить»."""
    box = page.locator('input[type=text]:visible').first
    box.click(); box.type(query, delay=20)
    page.get_by_role('button', name='Найти').first.click()
    page.wait_for_timeout(4500)
    page.evaluate("""(v)=>{
      const els=[...document.querySelectorAll('*')]
        .filter(e=>e.children.length===0 && e.textContent.trim()===v);
      if(els.length) els[els.length-1].click();
    }""", value)
    page.wait_for_timeout(2500)


with sync_playwright() as pw:
    br, page = browser(pw)
    page.goto(CARD, wait_until='domcontentloaded'); page.wait_for_timeout(7000)

    open_field(page, 'Принявший орган')
    dict_pick(page, 'Минфин', 'Минфин России')
    shot(page, '32_p2_organ')
    try:
        page.get_by_text('Применить', exact=True).first.click(timeout=6000)
        page.wait_for_timeout(5000)
    except Exception:
        pass

    open_field(page, 'Тематика')
    dict_pick(page, 'Бухгалтерская отчетность', 'Бухгалтерская отчетность')
    shot(page, '32_p2_theme')
    page.wait_for_timeout(4000)

    print('карточка:', page.evaluate("document.body.innerText")[:520].replace('\n', ' | '))
    br.close()
