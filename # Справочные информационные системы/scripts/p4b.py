# -*- coding: utf-8 -*-
from kpfree import *
import json
items = json.load(open('p4_items.json', encoding='utf-8'))
with sync_playwright() as pw:
    br, page = browser(pw)
    page.goto(items[0]['h'], wait_until='domcontentloaded'); page.wait_for_timeout(9000)
    shot(page, '32_p4_bad_doc')
    txts = []
    for fr in page.frames:
        try: txts.append(fr.evaluate("document.body?document.body.innerText:''"))
        except Exception: pass
    t = max(txts, key=len)
    print('LEN', len(t)); print(t[:3000])
    br.close()
