# -*- coding: utf-8 -*-
"""Задание 3.3: закладки «задание N» в одноимённых папках."""
from fav import *
S = shots_dir('s33')

PLAN = [
 (2, 'признаки платежеспособности банкнот и монеты Банка России', 3),
 (4, 'социальный вычет на обучение за границей дистанционное обучение', 1),
 (5, 'дни приезда и отъезда 183 дня налоговый резидент НДФЛ', 1),
 (6, 'НДС при получении задатка налоговая база', 0),
 (7, 'НДС передача подарков работникам безвозмездная передача', 1),
 (8, 'статья 346.12 налогоплательщики упрощенная система налогообложения', 1),
]
with sync_playwright() as pw:
    ctx, page = open_ctx(pw)
    for n, q, idx in PLAN:
        print('--- задание', n, flush=True)
        quick_search(page, q)
        ls = doc_links(page, idx + 2)
        print('   ', ls[idx]['t'][:95], flush=True)
        open_doc(page, ls[idx]['h'])
        shot(page, S, f'33_t{n}_doc')
        open_fav_dialog(page)
        set_bookmark_name(page, f'задание {n}')
        # дерево папок свёрнуто — отбираем нужную через поиск внутри диалога
        page.evaluate("""(n) => {
          const i=[...document.querySelectorAll('input[type=text]')]
            .find(e=>e.offsetParent && /поиск/i.test(e.placeholder||''));
          if(i){ i.focus(); i.value=n; i.dispatchEvent(new Event('input',{bubbles:true})); }
        }""", f'задание {n}')
        page.wait_for_timeout(800)
        page.get_by_text('Найти', exact=True).last.click()
        page.wait_for_timeout(3000)
        page.get_by_text(f'задание {n}', exact=True).last.click()
        page.wait_for_timeout(1500)
        shot(page, S, f'33_t{n}_dialog')
        fav_add(page)
        page.wait_for_timeout(2500)
    page.goto(BASE + '/cgi/online.cgi?req=favorites', wait_until='domcontentloaded')
    page.wait_for_timeout(8000)
    shot(page, S, '33_bookmarks_all')
    print(page.evaluate('document.body.innerText')[-900:].replace('\n', ' | '))
    ctx.close()
