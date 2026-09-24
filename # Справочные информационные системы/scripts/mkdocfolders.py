# -*- coding: utf-8 -*-
"""Создание папок документов в разделе «Папки» Избранного."""
from fav import *
S = shots_dir('s32')
NAMES = ['Уставный капитал АО', 'Уставный капитал ООО', 'Дистанционная торговля']
with sync_playwright() as pw:
    ctx, page = open_ctx(pw)
    for name in NAMES:
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
    shot(page, S, '32_docfolders')
    print(page.evaluate("document.body.innerText")[-400:].replace('\n', ' | '))
    ctx.close()
