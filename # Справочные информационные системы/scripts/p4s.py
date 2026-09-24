# -*- coding: utf-8 -*-
"""Тот же вопрос в авторизованной версии «Студент»."""
from kp2 import *
D = shots_dir('s32')
with sync_playwright() as pw:
    ctx, page = open_ctx(pw)
    quick_search(page, 'можно ли продавать биологически активные добавки дистанционным способом')
    shot(page, D, '32_p4_stud_list')
    items = page.evaluate("""() => [...document.querySelectorAll('a[href*="req=doc"]')]
        .map(a=>({t:(a.innerText||'').replace(/\s+/g,' ').trim(), h:a.getAttribute('href')}))
        .filter(x=>x.t.length>25).slice(0,12)""")
    for i, it in enumerate(items):
        print(i, it['t'][:170])
    import json; json.dump(items, open('p4_stud.json','w',encoding='utf-8'), ensure_ascii=False, indent=1)
    ctx.close()
