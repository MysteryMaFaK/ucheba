# -*- coding: utf-8 -*-
"""Задание 3.2, этап 1: поиск документов и фрагментов в некоммерческой версии."""
from kpfree import *

PLAN = [
 ('1', 'Письмо ФНС России ГД-4-3/6915@ о порядке заполнения налоговой декларации по налогу на добавленную стоимость',
      0, ['1010823', 'код']),
 ('3', 'корреспонденция счетов удержание из заработной платы работника страховой премии по договору добровольного медицинского страхования',
      1, ['удержан']),
 ('4', 'Правила продажи товаров при дистанционном способе продажи товара постановление 2463',
      0, ['дистанционн']),
 ('5', 'Соглашение о взаимодействии между МВД России и ФНС России 2010',
      0, ['взаимодейств']),
 ('8', 'письмо ФНС о порядке заполнения счетов-фактур',
      0, ['счет-фактур', 'счетов-фактур']),
]
result = {}
with sync_playwright() as pw:
    br, page = browser(pw)
    for tag, q, idx, keys in PLAN:
        print('---', tag, flush=True)
        quick_search(page, q)
        shot(page, f'32_{tag}_list')
        items = page.evaluate("""() => [...document.querySelectorAll('a[href*="req=doc"]')]
            .map(a=>({t:(a.innerText||'').replace(/\s+/g,' ').trim(), h:a.getAttribute('href')}))""")
        if idx >= len(items):
            print('   !! мало результатов'); continue
        it = items[idx]
        page.goto('https://www.consultant.ru/cons/cgi/' + it['h'].replace('../cgi/', ''),
                  wait_until='domcontentloaded')
        page.wait_for_timeout(11000)
        shot(page, f'32_{tag}_doc')
        texts = []
        for fr in page.frames:
            try:
                texts.append(fr.evaluate("document.body ? document.body.innerText : ''"))
            except Exception:
                pass
        txt = max(texts, key=len) if texts else ''
        low = txt.lower()
        hit = next((low.find(k.lower()) for k in keys if low.find(k.lower()) > 0), -1)
        frag = txt[max(0, hit - 700): hit + 2200] if hit > 0 else txt[:2400]
        result[tag] = {'query': q, 'title': it['t'][:230], 'url': page.url,
                       'len': len(txt), 'fragment': frag}
        print('   ', it['t'][:100], '| len', len(txt), flush=True)
    br.close()
with open('res32a.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=1)
print('SAVED')
