# -*- coding: utf-8 -*-
"""Добор закладок «задание 4» и «задание 8»."""
from fav import *
S = shots_dir('s33')
EXPAND = open('bm33b.py', encoding='utf-8').read().split('EXPAND = """')[1].split('"""')[0]

PLAN = [
 (4, 'социальный вычет на обучение за границей дистанционное обучение', 1),
 (8, 'статья 346.12 налогоплательщики упрощенная система налогообложения', 1),
]
with sync_playwright() as pw:
    ctx, page = open_ctx(pw)
    for n, q, idx in PLAN:
        print('--- задание', n, flush=True)
        quick_search(page, q)
        ls = doc_links(page, idx + 2)
        print('   ', ls[idx]['t'][:90], flush=True)
        open_doc(page, ls[idx]['h'])
        open_fav_dialog(page)
        set_bookmark_name(page, f'задание {n}')
        print('   expand:', page.evaluate(EXPAND, f'задание {n}'), flush=True)
        page.wait_for_timeout(4000)
        clicked = page.evaluate("""(n)=>{
          const els=[...document.querySelectorAll('*')]
            .filter(e=>e.children.length===0 && e.textContent.trim()===n);
          if(!els.length) return 'no folder';
          els[els.length-1].click(); return 'folder ok';
        }""", f'задание {n}')
        print('   ', clicked, flush=True)
        page.wait_for_timeout(2000)
        shot(page, S, f'33_t{n}_dialog')
        page.evaluate("""()=>{
          const b=[...document.querySelectorAll('*')]
            .filter(e=>e.children.length===0 && e.textContent.trim()==='Добавить');
          if(b[0]) b[0].click();
        }""")
        page.wait_for_timeout(5000)
        print('   добавлено', flush=True)
    ctx.close()
