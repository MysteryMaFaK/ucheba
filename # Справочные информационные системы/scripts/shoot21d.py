# -*- coding: utf-8 -*-
"""Вкладка «Подробнее» — скроллим к блоку «Административная информация» (реестровый номер)."""
import sys, io, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from playwright.sync_api import sync_playwright

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'shots21')
SERVICE = ('https://gu.nnov.ru/services/31c7f896-8ac6-4898-8e72-317b89c33ef7'
           '/targets/167c116a-d66e-4c73-8492-c983dc3235cc/?onlyOneTarget=Y')

CLEAN = """() => {
  document.querySelectorAll('div,section,aside').forEach(e=>{
    const t=(e.innerText||'');
    if(t.length<700 && /(cookie|куки|метаданные пользователя|Робот Макс|Чат бот)/i.test(t)) e.style.display='none';
  });
}"""

with sync_playwright() as pw:
    br = pw.chromium.launch(channel='msedge', headless=True)
    ctx = br.new_context(viewport={'width': 1280, 'height': 800}, device_scale_factor=2, locale='ru-RU')
    page = ctx.new_page(); page.set_default_timeout(60000)
    page.goto(SERVICE, wait_until='domcontentloaded')
    page.wait_for_timeout(8000)
    try:
        page.get_by_text('Оказание адресной государственной социальной поддержки малоимущим').last.click(timeout=8000)
    except Exception:
        pass
    page.wait_for_timeout(5000)
    page.get_by_text('Подробнее', exact=True).first.click()
    page.wait_for_timeout(4000)
    page.evaluate(CLEAN)
    page.evaluate("""() => {
      const h=[...document.querySelectorAll('*')].find(e=>e.children.length===0
          && e.textContent.trim()==='Категория получателей');
      if(h) h.scrollIntoView({block:'start'});
      window.scrollBy(0,-100);
    }""")
    page.wait_for_timeout(1500)
    page.screenshot(path=os.path.join(OUT, '05_gu_service_details.png'))
    print('OK 05_gu_service_details')
    br.close()
