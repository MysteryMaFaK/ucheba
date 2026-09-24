# -*- coding: utf-8 -*-
"""Пункт 4: документы о БАД в папку «Дистанционная торговля». Пункт 8: письмо ФНС на контроль."""
from fav import *
S = shots_dir('s32')

EXPAND = """(n)=>{
  const i=[...document.querySelectorAll("input[type=text]")]
    .find(e=>e.offsetParent && /поиск/i.test(e.placeholder||""));
  if(!i) return "no input";
  i.focus(); i.value=n; i.dispatchEvent(new Event("input",{bubbles:true}));
  let p=i.parentElement, btn=null;
  for(let k=0;k<4&&p;k++){
    btn=[...p.querySelectorAll("*")].find(e=>e.children.length===0&&e.textContent.trim()==="Найти");
    if(btn) break; p=p.parentElement;
  }
  if(!btn) return "no btn";
  btn.click(); return "ok";
}"""


def to_folder(page, folder):
    open_fav_dialog(page)
    page.wait_for_timeout(2500)
    page.get_by_text('Папки', exact=True).last.click()
    page.wait_for_timeout(3000)
    page.evaluate(EXPAND, folder)
    page.wait_for_timeout(3500)
    page.evaluate("""(n)=>{
      const els=[...document.querySelectorAll('*')]
        .filter(e=>e.children.length===0 && e.textContent.trim()===n);
      if(els.length) els[els.length-1].click();
    }""", folder)
    page.wait_for_timeout(1800)
    page.evaluate("""()=>{
      const b=[...document.querySelectorAll('*')]
        .filter(e=>e.children.length===0 && e.textContent.trim()==='Добавить');
      if(b[0]) b[0].click();
    }""")
    page.wait_for_timeout(4500)

PLAN = [
    ('Дистанционная торговля',
     'Федеральный закон о качестве и безопасности пищевых продуктов 29-ФЗ биологически активные добавки'),
    ('Дистанционная торговля',
     'Правила продажи товаров по договору розничной купли-продажи постановление 657'),
]

with sync_playwright() as pw:
    ctx, page = open_ctx(pw)
    for folder, q in PLAN:
        quick_search(page, q)
        ls = doc_links(page, 3)
        if not ls:
            print('!! пусто:', q[:60], flush=True); continue
        print(folder, '<-', ls[0]['t'][:90], flush=True)
        open_doc(page, ls[0]['h'])
        to_folder(page, folder)

    # контроль: документ ФНС о заполнении счетов-фактур
    quick_search(page, 'письмо ФНС России о порядке заполнения счетов-фактур')
    ls = doc_links(page, 5)
    for l in ls[:5]:
        print('КАНДИДАТ:', l['t'][:110], flush=True)
    if ls:
        open_doc(page, ls[0]['h'])
        shot(page, S, '32_p8_fns_doc')
        page.evaluate("[...document.querySelectorAll('[title=\"Еще\"]')][0].click()")
        page.wait_for_timeout(2500)
        shot(page, S, '32_p8_fns_menu')
        try:
            page.get_by_text('Поставить на контроль', exact=True).first.click()
            page.wait_for_timeout(5000)
            shot(page, S, '32_p8_fns_after')
            print('КОНТРОЛЬ:', page.evaluate("document.body.innerText")[:300].replace('\n', ' | '))
        except Exception as e:
            print('не удалось поставить на контроль:', str(e)[:150])
    ctx.close()
