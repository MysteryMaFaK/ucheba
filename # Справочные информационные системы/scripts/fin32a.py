# -*- coding: utf-8 -*-
"""Добор скриншотов из «КонсультантПлюс: Студент»: папки и документы на контроле."""
from kp2 import *

D = shots_dir('s32')
FAV = BASE + '/cgi/online.cgi?req=home#favorite'


def collapse(page):
    """Свернуть левую панель Избранного, иначе она перекрывает названия папок."""
    page.evaluate("""()=>{const e=[...document.querySelectorAll('*')]
        .filter(x=>x.children.length===0 && /Свернуть/.test(x.textContent.trim()));
        if(e.length) e[e.length-1].click();}""")
    page.wait_for_timeout(1500)


def section(page, name):
    page.evaluate("""(n)=>{const e=[...document.querySelectorAll('*')]
        .filter(x=>x.children.length===0 && x.textContent.trim()===n);
        if(e.length) e[e.length-1].click();}""", name)
    page.wait_for_timeout(4000)


def open_folder(page, name):
    page.evaluate("""(n)=>{const e=[...document.querySelectorAll('*')]
        .filter(x=>x.children.length===0 && x.textContent.trim().startsWith(n));
        if(e.length) e[e.length-1].click();}""", name)
    page.wait_for_timeout(1200)
    page.keyboard.press('Enter')
    page.wait_for_timeout(4000)


with sync_playwright() as pw:
    ctx, page = open_ctx(pw)
    page.goto(BASE + '/cgi/online.cgi?req=home', wait_until='domcontentloaded')
    page.wait_for_timeout(8000)
    txt = page.evaluate("document.body?document.body.innerText:''")
    print('АВТОРИЗАЦИЯ:', 'ОК' if ('Избранное' in txt and 'Журнал' in txt) else 'НЕТ')
    if 'Избранное' not in txt:
        shot(page, D, 'dbg_home')
        raise SystemExit('нужен вход')

    page.get_by_text('Избранное', exact=True).first.click()
    page.wait_for_timeout(6000)
    section(page, 'Папки')
    collapse(page)
    shot(page, D, '32_folders_all')

    for folder, name in [('Дистанционная торговля', '32_p4_folder'),
                         ('Уставный капитал АО', '32_p6_ao'),
                         ('Уставный капитал ООО', '32_p6_ooo')]:
        open_folder(page, folder)
        shot(page, D, name)
        print(folder, '->', page.evaluate("document.body.innerText")[:400].replace('\n', ' | '))
        page.go_back(); page.wait_for_timeout(4000)
        section(page, 'Папки'); collapse(page)

    section(page, 'Документы на контроле')
    collapse(page)
    shot(page, D, '32_p8_list')
    print('КОНТРОЛЬ:', page.evaluate("document.body.innerText")[:400].replace('\n', ' | '))
    ctx.close()
