# -*- coding: utf-8 -*-
"""Пересъёмка поиска в ЭБС «Юрайт» с фильтром «Для вузов» (нужна ширина 1440 — иначе панель фильтров скрыта)."""
import sys, io, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from playwright.sync_api import sync_playwright

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'shots')
LVL = ''.join('edu_level_ids[]=%d&' % i for i in (62, 63, 64, 68, 65, 6, 7, 9))
URL = ('https://urait.ru/catalog?' + LVL +
       'query=%D0%B3%D0%BE%D1%81%D1%83%D0%B4%D0%B0%D1%80%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D0%BE%D0%B5'
       '+%D1%80%D0%B5%D0%B3%D1%83%D0%BB%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5'
       '+%D1%8D%D0%BA%D0%BE%D0%BD%D0%BE%D0%BC%D0%B8%D0%BA%D0%B8&sort=relevance')

with sync_playwright() as pw:
    br = pw.chromium.launch(channel='msedge', headless=True)
    ctx = br.new_context(viewport={'width': 1440, 'height': 900}, device_scale_factor=2, locale='ru-RU')
    page = ctx.new_page(); page.set_default_timeout(45000)
    # фильтр ставим кликом, чтобы в чекбоксе «Для вузов» стояла галка
    page.goto('https://urait.ru/search?words=%D0%B3%D0%BE%D1%81%D1%83%D0%B4%D0%B0%D1%80%D1%81%D1%82%D0%B2%D0%B5%D0%BD%D0%BD%D0%BE%D0%B5'
              '+%D1%80%D0%B5%D0%B3%D1%83%D0%BB%D0%B8%D1%80%D0%BE%D0%B2%D0%B0%D0%BD%D0%B8%D0%B5'
              '+%D1%8D%D0%BA%D0%BE%D0%BD%D0%BE%D0%BC%D0%B8%D0%BA%D0%B8', wait_until='domcontentloaded')
    page.wait_for_timeout(9000)
    page.evaluate("""() => {
      const e=[...document.querySelectorAll('*')].find(x=>x.textContent.trim()==='Для вузов'&&x.children.length===0);
      if(e) e.closest('.cursor-pointer').click();
    }""")
    page.wait_for_timeout(8000)
    page.evaluate("""() => {
      document.querySelectorAll('div,section,aside').forEach(e=>{
        const t=(e.innerText||'');
        if(t.length<600 && /cookie|куки|Отправьте нам сообщение/i.test(t)) e.style.display='none';
      });
    }""")
    page.screenshot(path=os.path.join(OUT, '06_urait_search.png'))
    print('OK 06_urait_search (фильтр «Для вузов»)')
    br.close()
