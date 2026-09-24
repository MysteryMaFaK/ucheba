# -*- coding: utf-8 -*-
"""3.2 п.2: полный список названий 168 документов (некоммерческая версия), постранично."""
from kpfree import *
import os, json
CARD = 'https://www.consultant.ru/cons/cgi/online.cgi?req=card&div=LAW'
OUTJ = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'spisok168.json')


def open_field(page, name):
    page.locator('.x-page-card-field-name', has_text=name).first.click()
    page.wait_for_timeout(3500)


def page_titles(page):
    return page.evaluate("""()=>[...document.querySelectorAll('a[href*="req=doc"]')]
        .map(a=>(a.innerText||'').replace(/\\s+/g,' ').trim())
        .filter(t=>t.length>30)""")


with sync_playwright() as pw:
    br, page = browser(pw)
    page.goto(CARD, wait_until='domcontentloaded'); page.wait_for_timeout(7000)

    open_field(page, 'Принявший орган')
    box = page.locator('input[type=text]:visible').first
    box.click(); box.type('Минфин', delay=20)
    page.get_by_role('button', name='Найти').first.click(); page.wait_for_timeout(4500)
    page.evaluate("""()=>{const e=[...document.querySelectorAll('*')]
        .filter(x=>x.children.length===0 && x.textContent.trim()==='Минфин России');
        if(e.length) e[e.length-1].click();}""")
    page.wait_for_timeout(2500)
    try:
        page.get_by_text('Применить', exact=True).first.click(timeout=5000); page.wait_for_timeout(5000)
    except Exception:
        pass

    open_field(page, 'Дата')
    page.get_by_text('Диапазон дат:', exact=True).first.click(); page.wait_for_timeout(1000)
    ins = page.locator('input[type=text]:visible'); n = ins.count()
    ins.nth(n - 2).click(); page.keyboard.press('Home'); page.keyboard.type('01012015', delay=110)
    page.get_by_text('Поиск по полю «Дата»', exact=True).first.click(); page.wait_for_timeout(700)
    ins.nth(n - 1).click(); page.keyboard.press('Home'); page.keyboard.type('31122016', delay=110)
    page.get_by_text('Поиск по полю «Дата»', exact=True).first.click(); page.wait_for_timeout(900)
    page.get_by_text('Применить', exact=True).first.click(); page.wait_for_timeout(6000)

    open_field(page, 'Текст документа')
    box = page.locator('input[placeholder*="Слова для поиска"]:visible').first
    box.click(); box.type('БУХГАЛТЕРСКАЯ ОТЧЕТНОСТЬ', delay=18)
    page.get_by_role('button', name='Найти').first.click(); page.wait_for_timeout(6000)
    page.get_by_text('Показать список документов', exact=True).first.click(); page.wait_for_timeout(10000)

    titles, seen = [], set()
    stall = 0
    for step in range(250):
        for t in page_titles(page):
            if t not in seen:
                seen.add(t); titles.append(t)
        page.mouse.move(1000, 600)
        page.mouse.wheel(0, 1400)
        page.wait_for_timeout(2500)
        got = len(titles)
        for t in page_titles(page):
            if t not in seen:
                seen.add(t); titles.append(t)
        stall = stall + 1 if len(titles) == got else 0
        if step % 10 == 0:
            print('шаг %d: собрано %d' % (step, len(titles)), flush=True)
        if stall >= 15:
            break

    json.dump(titles, open(OUTJ, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    print('СОБРАНО:', len(titles), flush=True)
    shot(page, '32_p2_list_last')
    br.close()
