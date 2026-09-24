# -*- coding: utf-8 -*-
from kpfree import *
import json, re
items = json.load(open('p4_law.json', encoding='utf-8'))
res = {}
with sync_playwright() as pw:
    br, page = browser(pw)
    for idx, tag in [(4, 'fz29'), (2, 'rpn768')]:
        page.goto(items[idx]['h'], wait_until='domcontentloaded'); page.wait_for_timeout(9000)
        shot(page, '32_p4_' + tag)
        txts = []
        for fr in page.frames:
            try: txts.append(fr.evaluate("document.body?document.body.innerText:''"))
            except Exception: pass
        t = max(txts, key=len)
        res[tag] = {'title': items[idx]['t'], 'url': items[idx]['h'], 'len': len(t), 'text': t}
        print('==', tag, 'LEN', len(t))
        for m in re.finditer(r'[^\n]*дистанцион[^\n]*', t, re.I):
            print('  >', m.group(0)[:300])
    json.dump(res, open('p4_docs.json','w',encoding='utf-8'), ensure_ascii=False, indent=1)
    br.close()
