# -*- coding: utf-8 -*-
from kpfree import *
import json, re
URL = json.load(open('p4_657.json', encoding='utf-8'))[0]['h']
with sync_playwright() as pw:
    br, page = browser(pw)
    page.goto(URL, wait_until='domcontentloaded'); page.wait_for_timeout(11000)
    shot(page, '32_p4_657_doc')
    txts = []
    for fr in page.frames:
        try: txts.append(fr.evaluate("document.body?document.body.innerText:''"))
        except Exception: pass
    t = max(txts, key=len); open('pp657_p1.txt','w',encoding='utf-8').write(t)
    print('LEN', len(t))
    print(t[:700])
    # ссылки постраничной навигации
    nav = page.evaluate("""() => [...document.querySelectorAll('a')]
        .map(a=>({t:(a.innerText||'').replace(/\s+/g,' ').trim(), h:a.href}))
        .filter(x=>/страниц|дистанцион|Оглавление|далее|Правила прод/i.test(x.t)).slice(0,20)""")
    for n in nav: print('NAV', n['t'][:80], n['h'][:120])
    br.close()
