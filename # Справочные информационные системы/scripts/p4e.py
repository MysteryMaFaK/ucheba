# -*- coding: utf-8 -*-
"""Правила продажи (ПП 2463): раздел о дистанционном способе + упоминания БАД."""
from kpfree import *
import json, re
URL = json.load(open('res32a.json', encoding='utf-8'))['4']['url']
with sync_playwright() as pw:
    br, page = browser(pw)
    page.goto(URL, wait_until='domcontentloaded'); page.wait_for_timeout(11000)
    shot(page, '32_p4_pp2463')
    txts = []
    for fr in page.frames:
        try: txts.append(fr.evaluate("document.body?document.body.innerText:''"))
        except Exception: pass
    t = max(txts, key=len)
    print('LEN', len(t))
    open('pp2463.txt', 'w', encoding='utf-8').write(t)
    for m in re.finditer(r'[^\n]*(биологически активн|дистанционн)[^\n]*', t, re.I):
        s = m.group(0).strip()
        if s: print('>', s[:280])
    br.close()
