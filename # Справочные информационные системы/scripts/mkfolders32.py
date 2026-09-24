# -*- coding: utf-8 -*-
"""Задание 3.2: папки для подборок (пункты 4 и 6)."""
from fav import *
S = shots_dir('s32')
NAMES = ['Уставный капитал АО', 'Уставный капитал ООО', 'Дистанционная торговля']
with sync_playwright() as pw:
    ctx, page = open_ctx(pw)
    for name in NAMES:
        page.goto(BASE + '/cgi/online.cgi?req=favorites', wait_until='domcontentloaded')
        page.wait_for_timeout(7000)
        # снимаем выделение, чтобы папка создалась в корне «Мои закладки»
        page.get_by_text('Мои закладки', exact=True).first.click()
        page.wait_for_timeout(1200)
        page.get_by_text('Создать папку', exact=True).first.click()
        page.wait_for_timeout(2500)
        inp = page.locator('input[type=text]:visible').last
        inp.click(); page.keyboard.press('Control+a'); page.keyboard.type(name, delay=35)
        page.keyboard.press('Enter'); page.wait_for_timeout(3500)
        print('создана папка:', name, flush=True)
    page.goto(BASE + '/cgi/online.cgi?req=favorites', wait_until='domcontentloaded')
    page.wait_for_timeout(7000)
    shot(page, S, '32_folders')
    ctx.close()
