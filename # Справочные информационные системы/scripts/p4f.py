# -*- coding: utf-8 -*-
from kpfree import *
import json, re
with sync_playwright() as pw:
    br, page = browser(pw)
    quick_search(page, 'Постановление Правительства 657 правила продажи товаров по договору розничной купли-продажи 2026')
    shot(page, '32_p4_657_list')
    items = page.evaluate("""() => [...document.querySelectorAll('a[href*="req=doc"]')]
        .map(a=>({t:(a.innerText||'').replace(/\s+/g,' ').trim(), h:a.href}))
        .filter(x=>x.t.length>25).slice(0,10)""")
    for i, it in enumerate(items): print(i, it['t'][:200])
    json.dump(items, open('p4_657.json','w',encoding='utf-8'), ensure_ascii=False, indent=1)
    br.close()
