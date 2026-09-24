# -*- coding: utf-8 -*-
"""Задание 3.3: добор статей НК РФ по пунктам 7 и 8 через раздел «Кодексы»."""
from kp33 import *

PLAN = [
 ('7', 'безвозмездная передача права собственности на товары признается реализацией объект налогообложения НДС',
       ['на безвозмездной основе, признается реализацией', 'признается реализацией товаров']),
 ('8', 'налогоплательщики упрощенной системы средняя численность работников превышает 130 человек',
       ['средняя численность работников']),
]
result = {}
with sync_playwright() as pw:
    br, page = browser(pw)
    for tag, query, keys in PLAN:
        print('---', tag)
        quick_search(page, query)
        try:
            page.get_by_text('Законодательство', exact=True).first.click()
            page.wait_for_timeout(6000)
        except Exception:
            pass
        shot(page, f'n{tag}_1_list')
        items = page.evaluate("""() => [...document.querySelectorAll('a[href*="req=doc"]')]
            .map(a=>({t:(a.innerText||'').replace(/\s+/g,' ').trim(), h:a.getAttribute('href')}))""")
        for i, it in enumerate(items[:4]):
            print(f'   {i}. {it["t"][:100]}')
        best = None
        for it in items[:4]:
            page.goto('https://www.consultant.ru/cons/cgi/' + it['h'].replace('../cgi/', ''),
                      wait_until='domcontentloaded')
            page.wait_for_timeout(11000)
            texts = []
            for fr in page.frames:
                try:
                    texts.append(fr.evaluate("document.body ? document.body.innerText : ''"))
                except Exception:
                    pass
            txt = max(texts, key=len) if texts else ''
            low = txt.lower()
            hit = next((low.find(k.lower()) for k in keys if low.find(k.lower()) > 0), -1)
            if hit > 0 and len(txt) > 2000 and 'Налоговый кодекс' in it['t']:
                best = (it, txt, hit); break
        if not best:
            print('   !! не найдено'); continue
        it, txt, hit = best
        shot(page, f'n{tag}_2_doc')
        result[tag] = {'query': query, 'title': it['t'][:220], 'url': page.url, 'len': len(txt),
                       'fragment': txt[max(0, hit-800): hit+2200]}
        print('   >>', it['t'][:90], '| len', len(txt))
    br.close()
with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'kp33_nk2.json'), 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=1)
print('SAVED')
