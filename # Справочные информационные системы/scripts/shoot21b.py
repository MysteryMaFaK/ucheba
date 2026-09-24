# -*- coding: utf-8 -*-
"""Перес]ъёмка: список найденных нотариусов (нужен скролл к блоку результатов)."""
import sys, io, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from playwright.sync_api import sync_playwright

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'shots21')
NOTARY = ('https://data.notariat.ru/directory/notary/?last_name=&first_name=&middle_name='
          '&chamber__region_id=52&address=%D0%9D%D0%B8%D0%B6%D0%BD%D0%B8%D0%B9+%D0%9D%D0%BE%D0%B2%D0%B3%D0%BE%D1%80%D0%BE%D0%B4')

with sync_playwright() as pw:
    br = pw.chromium.launch(channel='msedge', headless=True)
    ctx = br.new_context(viewport={'width': 1280, 'height': 800}, device_scale_factor=2, locale='ru-RU')
    page = ctx.new_page(); page.set_default_timeout(60000)
    page.goto(NOTARY, wait_until='domcontentloaded')
    page.wait_for_timeout(5000)
    page.evaluate("""() => {
      const h=[...document.querySelectorAll('*')].find(e=>e.textContent.trim()==='Нотариусы'&&e.children.length===0);
      if(h) h.scrollIntoView({block:'start'});
      window.scrollBy(0,-120);
    }""")
    page.wait_for_timeout(1500)
    page.screenshot(path=os.path.join(OUT, '09_notary_results.png'))
    print('OK 09_notary_results')
    br.close()
