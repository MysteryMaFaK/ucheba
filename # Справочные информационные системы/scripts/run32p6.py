# -*- coding: utf-8 -*-
"""Задание 3.2, пункты 4 и 6: наполнение подборок."""
from addfolder import *
S = shots_dir('s32')

PLAN = [
 ('Уставный капитал АО', 'уставный капитал акционерного общества', 0),
 ('Уставный капитал АО', 'гражданский кодекс часть первая уставный капитал хозяйственного общества', 0),
 ('Уставный капитал ООО', 'уставный капитал общества с ограниченной ответственностью', 0),
 ('Уставный капитал ООО', 'гражданский кодекс часть первая уставный капитал хозяйственного общества', 0),
 ('Дистанционная торговля', 'Правила продажи товаров при дистанционном способе продажи товара постановление 2463', 0),
 ('Дистанционная торговля', 'закон о защите прав потребителей дистанционный способ продажи товара', 0),
]
with sync_playwright() as pw:
    ctx, page = open_ctx(pw)
    for folder, q, idx in PLAN:
        quick_search(page, q)
        ls = doc_links(page, idx + 2)
        if not ls:
            print('!! нет результатов:', q[:50]); continue
        print(f'{folder} <- {ls[idx]["t"][:80]}', flush=True)
        open_doc(page, ls[idx]['h'])
        add_doc_to_folder(page, folder)
    page.goto(BASE + '/cgi/online.cgi?req=favorites', wait_until='domcontentloaded')
    page.wait_for_timeout(8000)
    shot(page, S, '32_folders_filled')
    ctx.close()
