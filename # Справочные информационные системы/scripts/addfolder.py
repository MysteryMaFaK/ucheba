# -*- coding: utf-8 -*-
"""Добавление документа целиком в папку Избранного."""
from fav import *

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


def add_doc_to_folder(page, folder):
    """F8 → вкладка «Папки» → документ целиком → нужная папка → Добавить."""
    open_fav_dialog(page)
    page.wait_for_timeout(2000)
    page.get_by_text('Папки', exact=True).last.click()
    page.wait_for_timeout(2500)
    # отмечаем «Добавить документ целиком», если чекбокс есть
    page.evaluate("""()=>{
      const lab=[...document.querySelectorAll('*')]
        .find(e=>e.children.length===0 && e.textContent.trim()==='Добавить документ целиком');
      if(!lab) return;
      let row=lab.parentElement, cb=null;
      for(let i=0;i<4&&row;i++){ cb=row.querySelector('input[type=checkbox]'); if(cb) break; row=row.parentElement; }
      if(cb && !cb.checked) cb.click();
    }""")
    page.wait_for_timeout(1000)
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
