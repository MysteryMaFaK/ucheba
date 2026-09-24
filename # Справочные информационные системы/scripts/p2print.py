# -*- coding: utf-8 -*-
"""3.2 п.2: повтор поиска + попытка распечатать список названий."""
from kpfree import *
import os
CARD = 'https://www.consultant.ru/cons/cgi/online.cgi?req=card&div=LAW'


def open_field(page, name):
    page.locator('.x-page-card-field-name', has_text=name).first.click()
    page.wait_for_timeout(3500)


with sync_playwright() as pw:
    br = pw.chromium.launch(channel='msedge', headless=True)
    ctx = br.new_context(viewport={'width':1280,'height':800}, device_scale_factor=2, locale='ru-RU', accept_downloads=True)
    page = ctx.new_page(); page.set_default_timeout(45000)
    page.add_init_script("window.print = () => { window.__printed = true; };")
    page.goto(CARD, wait_until='domcontentloaded'); page.wait_for_timeout(7000)

    open_field(page, 'Принявший орган')
    box = page.locator('input[type=text]:visible').first
    box.click(); box.type('Минфин', delay=20)
    page.get_by_role('button', name='Найти').first.click(); page.wait_for_timeout(4500)
    page.evaluate("""()=>{const e=[...document.querySelectorAll('*')]
        .filter(x=>x.children.length===0 && x.textContent.trim()==='Минфин России');
        if(e.length) e[e.length-1].click();}""")
    page.wait_for_timeout(2500)
    try: page.get_by_text('Применить', exact=True).first.click(timeout=5000); page.wait_for_timeout(5000)
    except Exception: pass

    open_field(page, 'Дата')
    page.wait_for_timeout(1500)
    page.get_by_text('Диапазон дат:', exact=True).first.click(); page.wait_for_timeout(1000)
    ins = page.locator('input[type=text]:visible'); n = ins.count()
    ins.nth(n-2).click(); page.keyboard.press('Home'); page.keyboard.type('01012015', delay=110)
    page.get_by_text('Поиск по полю «Дата»', exact=True).first.click(); page.wait_for_timeout(700)
    ins.nth(n-1).click(); page.keyboard.press('Home'); page.keyboard.type('31122016', delay=110)
    page.get_by_text('Поиск по полю «Дата»', exact=True).first.click(); page.wait_for_timeout(900)
    page.get_by_text('Применить', exact=True).first.click(); page.wait_for_timeout(6000)

    open_field(page, 'Текст документа')
    box = page.locator('input[placeholder*="Слова для поиска"]:visible').first
    box.click(); box.type('БУХГАЛТЕРСКАЯ ОТЧЕТНОСТЬ', delay=18)
    page.get_by_role('button', name='Найти').first.click(); page.wait_for_timeout(6000)
    page.get_by_text('Показать список документов', exact=True).first.click(); page.wait_for_timeout(10000)
    shot(page, "32_p2_list2")
    # попытка отметить все: фокус в список + Num+
    page.mouse.click(1000, 700)
    page.wait_for_timeout(800)
    for k in ['NumpadAdd', '+']:
        page.keyboard.press(k); page.wait_for_timeout(1500)
    page.evaluate("""()=>{document.dispatchEvent(new KeyboardEvent('keydown',
        {key:'+',code:'NumpadAdd',keyCode:107,which:107,bubbles:true}));}""")
    page.wait_for_timeout(2500)
    shot(page, '32_p2_marked')
    print('MARKED:', page.evaluate("""()=>document.querySelectorAll('.x-page-search-list-item--selected, [class*=selected]').length"""))

    tools = page.evaluate("""() => [...document.querySelectorAll('a,button,div,span')]
        .filter(e=>e.offsetParent && e.children.length===0)
        .map(e=>({t:(e.innerText||'').trim(), title:e.getAttribute('title')||'', c:(e.className||'').toString()}))
        .filter(x=>/печат|сохран|word|файл|копиров/i.test(x.t+' '+x.title+' '+x.c)).slice(0,25)""")
    for x in tools: print('TOOL', x)
    br.close()
