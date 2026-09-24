# -*- coding: utf-8 -*-
"""Папки документов «задание 1» … «задание 8» в разделе «Папки» (для задания 3.3)."""
from fav import *
S = shots_dir('s33')
NAMES = ['задание %d' % i for i in range(1, 9)]

with sync_playwright() as pw:
    ctx, page = open_ctx(pw)
    for name in NAMES:
        # перезагрузка снимает выделение предыдущей папки, иначе новая создаётся внутри неё
        page.goto(BASE + '/cgi/online.cgi?req=favorites', wait_until='domcontentloaded')
        page.wait_for_timeout(7000)
        favorites_section(page, 'Папки')          # раздел «Папки»
        page.wait_for_timeout(4000)
        page.get_by_text('Создать папку', exact=True).first.click()
        page.wait_for_timeout(2500)
        inp = page.locator('input[type=text]:visible').last
        inp.click(); page.keyboard.press('Control+a'); page.keyboard.type(name, delay=35)
        page.keyboard.press('Enter'); page.wait_for_timeout(3500)
        print('создана:', name, flush=True)

    page.goto(BASE + '/cgi/online.cgi?req=favorites', wait_until='domcontentloaded')
    page.wait_for_timeout(7000)
    favorites_section(page, 'Папки'); page.wait_for_timeout(4000)
    page.evaluate("""()=>{const e=[...document.querySelectorAll('*')]
        .filter(x=>x.children.length===0 && /Свернуть/.test(x.textContent.trim()));
        if(e.length) e[e.length-1].click();}""")
    page.wait_for_timeout(1500)
    shot(page, S, '33_docfolders')
    print(page.evaluate("document.body.innerText")[-600:].replace('\n', ' | '))
    ctx.close()
