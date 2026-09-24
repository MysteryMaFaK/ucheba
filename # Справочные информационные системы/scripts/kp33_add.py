# -*- coding: utf-8 -*-
"""Задание 3.3: добор документов по пунктам 2 (доп.), 5 (доп. фрагмент), 6, 7, 8."""
from kp33 import *

PLAN = [
 ('2b', 'Телеграмма Банка России о признаках определения платежности банковских билетов ветхие',
     ['НАДПИСИ', 'ВЕТХ']),
 ('6',  'задаток обеспечительный платеж налог на добавленную стоимость письмо Минфина России',
     ['задат']),
 ('7',  'реализацией товаров признается передача права собственности на безвозмездной основе НДС',
     ['на безвозмездной основе']),
 ('8',  'средняя численность работников за налоговый период не превышает человек упрощенная система налогообложения',
     ['средняя численность работников']),
 ('8b', 'среднесписочная численность работников исчисляется путем суммирования списочной численности за каждый календарный день',
     ['суммирования списочной численности']),
]

result = {}
with sync_playwright() as pw:
    br, page = browser(pw)
    for tag, query, keys in PLAN:
        print(f'--- {tag}')
        quick_search(page, query)
        try:
            page.get_by_text('Законодательство', exact=True).first.click()
            page.wait_for_timeout(6000)
        except Exception:
            pass
        items = page.evaluate("""() => [...document.querySelectorAll('a[href*="req=doc"]')]
            .map(a=>({t:(a.innerText||'').replace(/\\s+/g,' ').trim(), h:a.getAttribute('href')}))""")
        for i, it in enumerate(items[:5]):
            print(f'   {i}. {it["t"][:105]}')
        if not items:
            continue
        # берём первый документ, в тексте которого реально есть ключевая фраза
        best = None
        for it in items[:5]:
            page.goto('https://www.consultant.ru/cons/cgi/' + it['h'].replace('../cgi/', ''),
                      wait_until='domcontentloaded')
            page.wait_for_timeout(10000)
            texts = []
            for fr in page.frames:
                try:
                    texts.append(fr.evaluate("document.body ? document.body.innerText : ''"))
                except Exception:
                    pass
            txt = max(texts, key=len) if texts else ''
            low = txt.lower()
            hit = next((low.find(k.lower()) for k in keys if low.find(k.lower()) > 0), -1)
            if hit > 0 and len(txt) > 1500:
                best = (it, txt, hit)
                break
        if not best:
            print('   !! подходящий документ не найден')
            continue
        it, txt, hit = best
        shot(page, f'n{tag}_doc')
        result[tag] = {'query': query, 'title': it['t'][:220], 'url': page.url, 'len': len(txt),
                       'fragment': txt[max(0, hit - 900): hit + 2400]}
        print('   >>', it['t'][:100], '| len', len(txt))
    br.close()

with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'kp33_add.json'),
          'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=1)
print('SAVED')
