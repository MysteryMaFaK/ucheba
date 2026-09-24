# -*- coding: utf-8 -*-
"""Работа с Избранным КонсультантПлюс: закладки, папки, документы на контроле."""
from kp2 import *


def open_fav_dialog(page):
    """Меню «Еще» → «Добавить в Избранное…»."""
    page.evaluate("[...document.querySelectorAll('[title=\"Еще\"]')][0].click()")
    page.wait_for_timeout(2000)
    page.get_by_text('Добавить в Избранное…', exact=True).first.click()
    page.wait_for_timeout(4000)


def fav_tab(page, name):
    """Переключение вкладки диалога: Закладки / Папки / Документы на контроле."""
    page.get_by_text(name, exact=True).last.click()
    page.wait_for_timeout(2500)


def set_bookmark_name(page, name, comment=None):
    page.evaluate("""([n, c]) => {
      const tas=[...document.querySelectorAll('textarea')].filter(e=>e.offsetParent);
      if(tas[0]){ tas[0].focus(); tas[0].value=n;
                  tas[0].dispatchEvent(new Event('input',{bubbles:true})); }
      if(c){
        const ins=[...document.querySelectorAll('input[type=text],textarea')]
          .filter(e=>e.offsetParent && /комментар/i.test(e.placeholder||''));
        if(ins[0]){ ins[0].focus(); ins[0].value=c;
                    ins[0].dispatchEvent(new Event('input',{bubbles:true})); }
      }
    }""", [name, comment])
    page.wait_for_timeout(1000)


def create_folder(page, name):
    """Кнопка с иконкой «новая папка» справа от строки поиска в диалоге."""
    page.evaluate("""() => {
      const btns=[...document.querySelectorAll('button,div,span,a')]
        .filter(e=>e.offsetParent && /folder|newfolder|add-folder/i.test(
            (e.className||'')+' '+(e.id||'')+' '+(e.getAttribute('title')||'')));
      if(btns[0]) btns[0].click();
    }""")
    page.wait_for_timeout(2500)
    page.evaluate("""(n) => {
      const ins=[...document.querySelectorAll('input[type=text]')].filter(e=>e.offsetParent);
      const i=ins[ins.length-1];
      if(i){ i.focus(); i.value=n; i.dispatchEvent(new Event('input',{bubbles:true})); }
    }""", name)
    page.wait_for_timeout(800)
    page.keyboard.press('Enter')
    page.wait_for_timeout(3000)


def fav_add(page):
    page.get_by_text('Добавить', exact=True).first.click()
    page.wait_for_timeout(4000)
