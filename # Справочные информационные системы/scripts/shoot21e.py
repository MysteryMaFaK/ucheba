# -*- coding: utf-8 -*-
"""Страница УСЗН: скроллим к заголовку услуги, иначе он у нижней кромки."""
import sys, io, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from playwright.sync_api import sync_playwright

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'shots21')

with sync_playwright() as pw:
    br = pw.chromium.launch(channel='msedge', headless=True)
    ctx = br.new_context(viewport={'width': 1280, 'height': 800}, device_scale_factor=2, locale='ru-RU')
    page = ctx.new_page(); page.set_default_timeout(60000)
    page.goto('https://nnsovuszn.ru/?page_id=825', wait_until='domcontentloaded')
    page.wait_for_timeout(6000)
    page.evaluate("""() => {
      const h=[...document.querySelectorAll('h1,h2,h3,.entry-title')]
        .find(e=>/Оказание материальной помощи/i.test(e.textContent||''));
      if(h) h.scrollIntoView({block:'start'});
      window.scrollBy(0,-60);
    }""")
    page.wait_for_timeout(1500)
    page.screenshot(path=os.path.join(OUT, '06_uszn_tzs.png'))
    print('OK 06_uszn_tzs')
    br.close()
