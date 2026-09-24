# -*- coding: utf-8 -*-
"""Задание 3.3, пункт 7: письмо Минфина о НДС при безвозмездной передаче."""
from kp33 import *
result = {}
with sync_playwright() as pw:
    br, page = browser(pw)
    quick_search(page, 'безвозмездная передача права собственности на товары признается реализацией объект налогообложения НДС')
    page.get_by_text('Законодательство', exact=True).first.click()
    page.wait_for_timeout(6000)
    shot(page, 'n7_1_list')
    items = page.evaluate("""() => [...document.querySelectorAll('a[href*="req=doc"]')]
        .map(a=>({t:(a.innerText||'').replace(/\s+/g,' ').trim(), h:a.getAttribute('href')}))""")
    it = items[1]
    page.goto('https://www.consultant.ru/cons/cgi/' + it['h'].replace('../cgi/', ''), wait_until='domcontentloaded')
    page.wait_for_timeout(11000)
    shot(page, 'n7_2_doc')
    texts = []
    for fr in page.frames:
        try: texts.append(fr.evaluate("document.body ? document.body.innerText : ''"))
        except Exception: pass
    txt = max(texts, key=len) if texts else ''
    result['7'] = {'title': it['t'][:220], 'url': page.url, 'len': len(txt), 'fragment': txt[:3000]}
    print(it['t'][:110], '| len', len(txt))
    br.close()
with open('kp33_t7.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=1)
