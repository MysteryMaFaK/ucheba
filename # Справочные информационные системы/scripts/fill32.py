# -*- coding: utf-8 -*-
"""Задание 3.2, пункты 4 и 6: раскладываем документы по папкам."""
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
 ('Уставный капитал АО', 'уставный капитал акционерного общества', 0),
 ('Уставный капитал АО', 'гражданский кодекс часть первая уставный капитал хозяйственного общества', 0),
 ('Уставный капитал ООО', 'уставный капитал общества с ограниченной ответственностью', 0),
 ('Уставный капитал ООО', 'гражданский кодекс часть первая уставный капитал хозяйственного общества', 0),
 ('Дистанционная торговля', 'Правила продажи товаров при дистанционном способе продажи товара постановление 2463', 0),
 ('Дистанционная торговля', 'закон о защите прав потребителей дистанционный способ продажи товара', 0),
]
with sync_playwright() as pw:
    ctx, page = open_ctx(pw)
    for folder, q, idx in PLAN:
        quick_search(page, q)
        ls = doc_links(page, idx + 2)
        if not ls:
            print('!! пусто:', q[:45]); continue
        print(f'{folder} <- {ls[idx]["t"][:75]}', flush=True)
        open_doc(page, ls[idx]['h'])
        to_folder(page, folder)
    page.goto(BASE + '/cgi/online.cgi?req=favorites', wait_until='domcontentloaded')
    page.wait_for_timeout(7000)
    page.mouse.click(32, 203); page.wait_for_timeout(4500)
    shot(page, S, '32_docfolders_filled')
    print(page.evaluate("document.body.innerText")[-330:].replace('\n', ' | '))
    ctx.close()
