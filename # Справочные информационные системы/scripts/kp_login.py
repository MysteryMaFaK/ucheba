# -*- coding: utf-8 -*-
"""Разовый вход в КонсультантПлюс: открывает видимое окно, ждёт авторизации, сохраняет профиль."""
import os, sys, io, time
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
PROFILE = os.path.join(HERE, 'kpprofile')
os.makedirs(PROFILE, exist_ok=True)

with sync_playwright() as pw:
    ctx = pw.chromium.launch_persistent_context(
        PROFILE, channel='msedge', headless=False,
        viewport={'width': 1280, 'height': 800}, device_scale_factor=2, locale='ru-RU',
        args=['--window-size=1320,900'])
    page = ctx.pages[0] if ctx.pages else ctx.new_page()
    page.set_default_timeout(60000)
    page.goto('https://student2.consultant.ru/', wait_until='domcontentloaded')
    print('ОКНО ОТКРЫТО. Войдите в систему в этом окне.', flush=True)

    deadline = time.time() + 900          # ждём вход до 15 минут
    ok = False
    while time.time() < deadline:
        try:
            txt = page.evaluate("document.body ? document.body.innerText : ''")
            if 'Избранное' in txt and 'Журнал' in txt:
                ok = True
                break
        except Exception:
            pass
        time.sleep(3)

    print('АВТОРИЗОВАН' if ok else 'НЕ ДОЖДАЛСЯ ВХОДА', flush=True)
    page.wait_for_timeout(3000)
    ctx.close()
print('ПРОФИЛЬ СОХРАНЁН:', PROFILE)
