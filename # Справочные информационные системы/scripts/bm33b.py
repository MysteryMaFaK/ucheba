# -*- coding: utf-8 -*-
"""Задание 3.3: закладки «задание N» для пунктов 4-8."""
from fav import *
S = shots_dir('s33')

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

PLAN = [
 (4, 'социальный вычет на обучение за границей дистанционное обучение', 1),
 (5, 'дни приезда и отъезда 183 дня налоговый резидент НДФЛ', 1),
 (6, 'НДС при получении задатка налоговая база', 0),
 (7, 'НДС передача подарков работникам безвозмездная передача', 1),
 (8, 'статья 346.12 налогоплательщики упрощенная система налогообложения', 1),
]
with sync_playwright() as pw:
    ctx, page = open_ctx(pw)
    for n, q, idx in PLAN:
        print('--- задание', n, flush=True)
        quick_search(page, q)
        ls = doc_links(page, idx + 2)
        print('   ', ls[idx]['t'][:95], flush=True)
        open_doc(page, ls[idx]['h'])
        shot(page, S, f'33_t{n}_doc')
        open_fav_dialog(page)
        set_bookmark_name(page, f'задание {n}')
        print('   expand:', page.evaluate(EXPAND, f'задание {n}'), flush=True)
        page.wait_for_timeout(3500)
        # мышиный клик попадает в фон диалога — жмём сам узел дерева
        page.evaluate("""(n)=>{
          const els=[...document.querySelectorAll('*')]
            .filter(e=>e.children.length===0 && e.textContent.trim()===n);
          const el=els[els.length-1];
          if(el) el.click();
        }""", f'задание {n}')
        page.wait_for_timeout(2000)
        shot(page, S, f'33_t{n}_dialog')
        page.evaluate("""()=>{
          const b=[...document.querySelectorAll('*')]
            .filter(e=>e.children.length===0 && e.textContent.trim()==='Добавить');
          if(b[0]) b[0].click();
        }""")
        page.wait_for_timeout(4500)
        print('   добавлено', flush=True)
    page.goto(BASE + '/cgi/online.cgi?req=favorites', wait_until='domcontentloaded')
    page.wait_for_timeout(8000)
    shot(page, S, '33_bookmarks_all')
    ctx.close()
