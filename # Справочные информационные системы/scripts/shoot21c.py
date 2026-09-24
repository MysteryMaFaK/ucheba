# -*- coding: utf-8 -*-
"""Пересъёмка карточки услуги на gu.nnov.ru: сначала закрыть модалку «Уточните услугу»."""
import sys, io, os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from playwright.sync_api import sync_playwright

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'shots21')
SERVICE = ('https://gu.nnov.ru/services/31c7f896-8ac6-4898-8e72-317b89c33ef7'
           '/targets/167c116a-d66e-4c73-8492-c983dc3235cc/?onlyOneTarget=Y')
TITLE = ('Оказание адресной государственной социальной поддержки малоимущим семьям '
         'или малоимущим одиноко проживающим гражданам в Нижегородской области')

CLEAN = """() => {
  document.querySelectorAll('div,section,aside').forEach(e=>{
    const t=(e.innerText||'');
    if(t.length<700 && /(cookie|куки|метаданные пользователя|Робот Макс|Чат бот)/i.test(t)) e.style.display='none';
  });
  document.body.style.overflow='auto';
}"""

PICK = """(title) => {
  // тот же заголовок есть в баннере сверху — берём вариант из списка «Уточните услугу» (ниже по странице)
  const els=[...document.querySelectorAll('*')].filter(e=>e.children.length===0 && e.textContent.trim()===title);
  const target=els.map(e=>[e, e.getBoundingClientRect()]).filter(([,r])=>r.top>300).sort((a,b)=>a[1].top-b[1].top)[0];
  if(target){ target[0].click(); return 'picked at y=' + Math.round(target[1].top); }
  return 'no-modal (' + els.length + ' matches)';
}"""

with sync_playwright() as pw:
    br = pw.chromium.launch(channel='msedge', headless=True)
    ctx = br.new_context(viewport={'width': 1280, 'height': 800}, device_scale_factor=2, locale='ru-RU')
    page = ctx.new_page(); page.set_default_timeout(60000)

    page.goto(SERVICE, wait_until='domcontentloaded')
    page.wait_for_timeout(8000)
    try:
        page.get_by_text('Оказание адресной государственной социальной поддержки малоимущим'
                         ).last.click(timeout=8000)
        print('picked')
    except Exception as e:
        print('pick failed:', type(e).__name__)
    page.wait_for_timeout(5000)
    page.evaluate(CLEAN)
    page.screenshot(path=os.path.join(OUT, '04_gu_service_about.png'))
    print('OK 04_gu_service_about')

    page.evaluate("""() => {
      const t=[...document.querySelectorAll('*')].find(e=>e.textContent.trim()==='Подробнее'&&e.children.length===0);
      if(t) t.click();
    }""")
    page.wait_for_timeout(4000)
    page.evaluate(CLEAN)
    page.screenshot(path=os.path.join(OUT, '05_gu_service_details.png'))
    print('OK 05_gu_service_details')
    br.close()
