# -*- coding: utf-8 -*-
"""Открываем раздел «Папки» Избранного кликом по иконке в левой колонке."""
from fav import *
S = shots_dir('s32')
with sync_playwright() as pw:
    ctx, page = open_ctx(pw)
    page.goto(BASE + '/cgi/online.cgi?req=favorites', wait_until='domcontentloaded')
    page.wait_for_timeout(8000)
    favorites_section(page, 'Папки')
    page.wait_for_timeout(5000)
    shot(page, S, 'dbg_folders_section')
    print(page.evaluate("document.body.innerText")[:500].replace('\n', ' | '))
    ctx.close()
