# -*- coding: utf-8 -*-
"""Скриншоты содержимого папок Избранного и раздела «Документы на контроле»."""
from kp2 import *
D = shots_dir('s32')
FOLDERS = [('Дистанционная торговля', '32_p4_folder'),
           ('Уставный капитал АО', '32_p6_ao'),
           ('Уставный капитал ООО', '32_p6_ooo')]


def folders_page(page):
    page.goto(BASE + '/cgi/online.cgi?req=favorites', wait_until='domcontentloaded')
    page.wait_for_timeout(8000)
    favorites_section(page, 'Папки')            # раздел «Папки»
    page.wait_for_timeout(4000)


def collapse(page):
    page.evaluate("""()=>{const e=[...document.querySelectorAll('*')]
        .filter(x=>x.children.length===0 && x.textContent.trim()==='Свернуть');
        if(e.length) e[e.length-1].click();}""")
    page.wait_for_timeout(1500)


with sync_playwright() as pw:
    ctx, page = open_ctx(pw)
    for name, shotname in FOLDERS:
        folders_page(page)
        el = page.locator('.x-components-favorites-folder-text', has_text=name).first
        el.dblclick()
        page.wait_for_timeout(5000)
        collapse(page)
        shot(page, D, shotname)
        print(name, '->', page.evaluate("document.body.innerText")[:500].replace('\n', ' | '), flush=True)

    page.goto(BASE + '/cgi/online.cgi?req=favorites', wait_until='domcontentloaded')
    page.wait_for_timeout(8000)
    favorites_section(page, 'Документы на контроле')            # раздел «Документы на контроле»
    page.wait_for_timeout(5000)
    collapse(page)
    shot(page, D, '32_p8_list')
    print('КОНТРОЛЬ:', page.evaluate("document.body.innerText")[:500].replace('\n', ' | '))
    ctx.close()
