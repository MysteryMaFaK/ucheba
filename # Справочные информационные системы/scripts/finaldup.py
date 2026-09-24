# -*- coding: utf-8 -*-
"""Убрать дубликаты папок «задание N» в разделе «Папки».

Разделы Избранного переключаются кнопками .x-page-favorites-sidebar-button
(0 — Закладки, 1 — Папки, 2 — Документы на контроле); клик по координатам ненадёжен.
"""
from work32 import *
S33D = os.path.join(HERE, 's33')

TABS = {'Закладки': 0, 'Папки': 1, 'Документы на контроле': 2}


def goto_section(page, name, tries=3):
    for _ in range(tries):
        page.goto(BASE + '/cgi/online.cgi?req=favorites', wait_until='domcontentloaded')
        page.wait_for_timeout(7000)
        page.evaluate("""(i)=>{const b=document.querySelectorAll('.x-page-favorites-sidebar-button');
            if(b[i]) b[i].click();}""", TABS[name])
        page.wait_for_timeout(4000)
        title = page.evaluate("""()=>{const t=document.querySelector('.x-page-favorites-title-toolbar__title');
            return t?t.textContent.trim():'';}""")
        if title == name:
            return True
        print('  заголовок «%s» вместо «%s», повтор' % (title, name), flush=True)
    return False


def job(page):
    if not goto_section(page, 'Папки'):
        print('!! раздел «Папки» не открылся — ничего не трогаю', flush=True)
        return
    print('ПАПКИ СЕЙЧАС:', txt(page, 800), flush=True)
    shot(page, S33D, 'dbg_folders_now')

    marked = page.evaluate("""()=>{
      const rs=[...document.querySelectorAll('.x-list__row')];
      let n=0, seen=[];
      for(const r of rs){
        const t=(r.innerText||'').replace(/\\s+/g,' ').trim();
        seen.push(t.slice(0,50));
        if(/^задание \\d/.test(t) && /22\\.09\\.2026/.test(t)){
          const b=r.querySelector('input[type=checkbox]');
          if(b && !b.checked){ b.click(); n++; }
        }
      }
      return {n, seen};
    }""")
    print('строк:', marked['seen'], flush=True)
    print('отмечено:', marked['n'], flush=True)
    page.wait_for_timeout(1500)
    shot(page, S33D, 'dbg_dups_marked')
    if marked['n'] == 0 or marked['n'] > 8:
        print('НЕ УДАЛЯЮ — неожиданное количество', flush=True)
        return
    page.evaluate("""()=>{const t=[...document.querySelectorAll('*')]
        .find(e=>/trash|delete|basket|remove/i.test((e.className||'').toString()) && e.offsetParent);
        if(t) t.closest('a,button,div').click();}""")
    page.wait_for_timeout(3000)
    for label in ('Удалить', 'Да', 'ОК'):
        try:
            page.get_by_text(label, exact=True).last.click(timeout=4000)
            page.wait_for_timeout(3000)
            print('подтверждено:', label, flush=True)
            break
        except Exception:
            pass
    goto_section(page, 'Папки')
    shot(page, S33D, '33_docfolders_filled')
    print('ПАПКИ ИТОГ:', txt(page, 800), flush=True)
    goto_section(page, 'Закладки')
    shot(page, S33D, '33_folders')
    print('ЗАКЛАДКИ ИТОГ:', txt(page, 800), flush=True)


if __name__ == '__main__':
    run(job)
