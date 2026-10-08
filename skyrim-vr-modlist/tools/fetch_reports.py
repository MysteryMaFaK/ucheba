"""Скачать отчёты (status.json) 27 популярных сборок Wabbajack в data/rep/. Нужны для whouses.py и cand.py.
Запуск: python tools/fetch_reports.py   (около 42 МБ, 1-2 минуты)"""
import os, sys, urllib.request, concurrent.futures

BASE = 'https://raw.githubusercontent.com/wabbajack-tools/mod-lists/master/reports/{}/status.json'
LISTS = [  # VR: Yggdrasil, Stormcrown, Librum VR, Panda's, Tahrovin, Tahrovin Grit, Spirit of Grit, Tempus, FUS
    'wj-featured/yggdrasil_vr', 'Stormcrown_VR/Stormcrown_VR', 'librum/librum_vr', 'VirtualPanda/PandasSovngarde', 'iAmModlist/tahrovin',
    'TahrovinGrit/tahrovingrit', 'TahrovinGrit/spiritofgrit', 'Januarysnow/TempusVR', 'wj-featured/fus',
    # плоские next-gen
    'GhoulifiedReality/NGVO', 'Cistern/CSVO', 'CSVP/CSVP', 'LoreRim/LoreRim', 'Geborgen/nordic-souls', 'SkrubbySkrubInAShrub/NordicSoulsPBR',
    'Elysium/elysium', 'Wunduniik/Wunduniik', 'True_North/TrueNorth', 'LostOutpost/morningstar', 'LostOutpost/windsofthenorth',
    'Skyrim25/Skyrim25', 'wj-featured/aldrnari', 'WakingDreams/apostasy', 'LostOutpost/lostlegacy', 'Scrolls_of_Schtevie/TomesOfTalos',
    'SkyrimUnificationProject/SkyrimUnificationProject', 'TNE/tne',
]
out = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'data', 'rep')
os.makedirs(out, exist_ok=True)


def get(p):
    dst = os.path.join(out, p.replace('/', '_') + '.json')
    if os.path.exists(dst) and os.path.getsize(dst) > 1000:
        return p, 'есть'
    try:
        with urllib.request.urlopen(BASE.format(p), timeout=90) as r, open(dst, 'wb') as f:
            f.write(r.read())
        return p, 'ok'
    except Exception as e:
        return p, f'ОШИБКА {e}'


with concurrent.futures.ThreadPoolExecutor(8) as ex:
    for p, st in ex.map(get, LISTS):
        print(f'{st:8} {p}')
