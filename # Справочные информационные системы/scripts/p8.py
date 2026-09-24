# -*- coding: utf-8 -*-
"""Задание 3.2, пункт 8: постановка документа по счетам-фактурам на контроль."""
from fav import *
S = shots_dir('s32')
with sync_playwright() as pw:
    ctx, page = open_ctx(pw)
    quick_search(page, 'постановление 1137 формы и правила заполнения счета-фактуры')
    ls = doc_links(page, 1)
    open_doc(page, ls[0]['h'])
    shot(page, S, '32_p8_doc')
    page.evaluate("[...document.querySelectorAll('[title=\"Еще\"]')][0].click()")
    page.wait_for_timeout(2500)
    shot(page, S, '32_p8_menu')
    page.get_by_text('Поставить на контроль', exact=True).first.click()
    page.wait_for_timeout(5000)
    shot(page, S, '32_p8_after')
    print(page.evaluate("document.body.innerText")[-400:].replace('\n', ' | '))
    ctx.close()
