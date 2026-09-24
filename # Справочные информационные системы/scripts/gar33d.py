# -*- coding: utf-8 -*-
"""ГАРАНТ: добор вопросов 7 и 8 (клик по полю перехватывает подсказка — вводим через focus)."""
import os, sys, io, json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from playwright.sync_api import sync_playwright

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'shots33g')
UA = ('Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
      'Chrome/140.0.0.0 Safari/537.36 Edg/140.0.0.0')
Q = {7: 'передача права собственности на безвозмездной основе признается реализацией',
     8: 'средняя численность работников упрощенная система налогообложения'}
with sync_playwright() as pw:
    br = pw.chromium.launch(channel='msedge', headless=True)
    ctx = br.new_context(user_agent=UA, locale='ru-RU', viewport={'width': 1280, 'height': 800},
                         device_scale_factor=2)
    page = ctx.new_page(); page.set_default_timeout(60000)
    for num, q in Q.items():
        print('---', num)
        page.goto('https://ivo.garant.ru/', wait_until='domcontentloaded')
        page.wait_for_timeout(12000)
        page.evaluate("""(q) => {
          const i=[...document.querySelectorAll('input[type=text]')].find(x=>x.offsetParent);
          i.focus(); i.value=q;
          i.dispatchEvent(new Event('input',{bubbles:true}));
          i.dispatchEvent(new Event('change',{bubbles:true}));
        }""", q)
        page.wait_for_timeout(1500)
        page.keyboard.press('Enter')
        page.wait_for_timeout(15000)
        page.screenshot(path=os.path.join(OUT, f'g{num}_1_list.png'))
        print('   ', page.evaluate("document.body.innerText").replace('\n', ' ')[:250])
    br.close()
