# -*- coding: utf-8 -*-
"""3.2 п.4: можно ли продавать БАД дистанционным способом."""
from kpfree import *
import json

Q = 'можно ли продавать дистанционным способом биологически активные добавки'

with sync_playwright() as pw:
    br, page = browser(pw)
    quick_search(page, Q)
    shot(page, '32_p4_bad_list')
    items = page.evaluate("""() => [...document.querySelectorAll('a[href*="req=doc"]')]
        .map(a=>({t:(a.innerText||'').replace(/\s+/g,' ').trim(), h:a.href}))
        .filter(x=>x.t.length>25).slice(0,15)""")
    for i, it in enumerate(items):
        print(i, it['t'][:160])
    json.dump(items, open('p4_items.json', 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    br.close()
