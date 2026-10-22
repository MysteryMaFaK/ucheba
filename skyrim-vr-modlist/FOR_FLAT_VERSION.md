# Для плоской версии (Skyrim SE/AE)

Всё, что собрано и проверено для Skyrim VR, сохранено в этом репозитории. Здесь — что из этого брать для обычной (плоской) Skyrim SE/AE и что поменять. Данные на 22.10.2026.

## Главные файлы

| Файл | Что внутри |
|---|---|
| `data/export/mods_all.csv` | **Сводная таблица** — каждый мод Nexus из 27 популярных сборок (13 733) + не-Nexus позиции ядра: в каких сборках стоит, наше решение, раздел, метка, причина отказа. Открывается в Excel/LibreOffice (UTF-8, разделитель «;») |
| `data/export/flat_candidates.csv` | **Подборка для плоской версии** (1920 строк): основа SE/AE, моды, отсеянные только из-за VR, и популярные в SE-сборках, но не оценённые нами |
| `data/export/mods_all.json` | То же, что CSV, плюс все решения агентов по каждому моду (поле `decisions`) |
| `data/rep/` | Состав 27 сборок Wabbajack (18 плоских next-gen + 9 VR). В git не хранится: `python tools/fetch_reports.py` (~42 МБ) |
| `data/lists_extra/` | Ещё 4 выгрузки: **Frostbound** и **Thundercrown** (плоские, ~370 модов), Auriel's Dream VR, Curseadelica VR. Формат строки: `N <id> <название> <версия> [<файлы>]` |
| `MODLIST.md`, `manifest.yaml`, `CONFLICTS.md` | Ядро VR с карточками установки: файлы, выборы FOMOD, порядок, конфликты — большая часть применима и к плоской (см. ниже) |
| `OTHER_MODS.md`, `data/other_result.json` | Вторая подборка: текстуры, тела, лица, броня, существа, города — почти всё без DLL, переносится в плоскую |
| `VR_INTERACTION.md` | Взаимодействие в VR — для плоской не нужно, кроме раздела «Не ставить», где есть плоские аналоги |
| `data/other2/dispositions.json` | Решение и причина по каждому из 1573 кандидатов второго прохода |
| `data/other2/prefilter_skipped.tsv` | 799 модов, отсеянных без проверки, большинство — «только SE-сборки»: для плоской это **готовый пул кандидатов** |

## Как пользоваться таблицей

Поля `status` (наше решение) и `flat_hint` (подсказка для плоской):

- `flat_hint = flat_base` (20) — SE/AE-основа вместо VR-варианта из ядра: SKSE64, Address Library, SSE Engine Fixes, SkyUI, moreHUD SE, SPID, Base Object Swapper, Dual Casting Fix, DynDOLOD-файлы и др. **Ставить первыми.**
- `flat_hint = flat_candidate` (556) — отсеяны только из-за VR (нет VR-сборки DLL, «flat-only»): Bug Fixes SSE, Scrambled Bugs, Actor Limit Fix, TrueHUD, SmoothCam, Better Third Person Selection, Immersive Equipment Displays, Simple Dual Sheath, SkyHUD, Essential Favorites… В колонке `reason` — почему не подошло VR; для плоской эта причина снимается, но ценность стоит оценить.
- `flat_hint = se_popular_unreviewed` (1344) — стоят в 4+ плоских сборках, но нами не оценивались (VR их не рассматривал).
- `flat_hint = vr_only` (283) — VR-специфичные: в плоской не нужны или есть SE-аналог.
- `status = core / other_keep` — то, что мы взяли для VR; без DLL переносится как есть, с DLL — брать SE/AE-файл с той же страницы.
- `status = dropped / rejected` с причинами «covered_elsewhere», «low_value», «excluded_category» — эти причины к VR не относятся и для плоской обычно остаются в силе.

Удобные фильтры: `se_lists_n` ≥ 8 — «стандарт» плоских next-gen сборок; `newest_file` ≥ 2025 — свежее.

## Ядро: что заменить

| В VR-ядре | Для SE/AE |
|---|---|
| Skyrim Script Extender for VR (SKSEVR) | SKSE64 (#30379) |
| VR Address Library for SKSEVR | Address Library for SKSE Plugins (#32444) |
| Engine Fixes VR | SSE Engine Fixes (#17230) |
| SkyUI - VR | SkyUI (#12604) |
| moreHUD VR | moreHUD SE (#12688) |
| Spell Perk Item Distributor (SPID) VR | SPID (#36869) |
| Base Object Swapper VR | Base Object Swapper (#60805) |
| Dual Casting Fix VR | Dual Casting Fix (#92454) |
| Increase Actor Limit for VR | Actor Limit Fix (#32349) |
| Poached Bugs VR | Bug Fixes SSE (#33261) + Scrambled Bugs (#43532) |
| Essential Favorites VR | Essential Favorites (#42997) |
| Spell Wheel VR | Wheeler (#97345) или аналог |
| Open Shaders 2.17 (VR-форк) | Community Shaders — основная ветка для SE/AE (с PBR) |
| Skyrim VR ESL Support, патчи USSEP/Strings для VR | Не нужны: в SE/AE ESL встроен, USSEP ставится как есть |
| VRIK, HIGGS, PLANCK, Physical Collision VR, True Wield VR, Weapon Throw VR, VR Equip, Gift by Hand, VR Climbing, Interactive Activators/Waters VR, VR Keyboard, OpenComposite, VR FPS Stabilizer и прочие VR-механики | Не нужны. Вместо физического боя и камеры VR в плоских сборках стоят: True Directional Movement (#51614), TrueHUD (#62775), SmoothCam (#41252), Precision (#72347) — все есть в таблице |

Общее правило: у мода ядра с DLL берите SE/AE-файл с той же страницы (многие моды выпускают одну страницу на SE/AE/VR). Моды без DLL (меши, текстуры, плагины, конфиги, OAR-анимации) переносятся как есть.

## Что меняется в правилах отбора

- **Видеопамять:** в VR по умолчанию 2K (картинка на два глаза). В плоской 4K для крупных поверхностей допустим.
- **PBR:** на Open Shaders в VR не подтверждён ни одной VR-сборкой, поэтому PBR-пакеты в «Other Mods» помечены `try`. На Community Shaders в плоской PBR штатный (Nordic Souls PBR, Morning Star и др.) — такие пакеты можно поднимать до `rec`.
- **Процессор:** тяжёлые города и клаттер (JK's, Great Cities) в плоской бьют по кадрам меньше, чем в VR.
- **Камера и анимации:** в VR не имели смысла анимации от первого лица, камера третьего лица, HUD-моды — в плоской это важные разделы (ищите в `se_popular_unreviewed` и `flat_candidate`).
- **Правила владельца** (без квестового контента, спутников, крупных оверхолов сложности, пакетов заклинаний, узкого SimonRim, NSFW) — заданы для VR-сборки; для плоской решите заново. Отсеянное по ним — `data/other2/auto_excluded.tsv`.

## Инструменты (работают и для плоской)

- `python tools/fetch_reports.py` — состав 27 сборок; `python tools/whouses.py <id или имя>` — в каких сборках мод и какие файлы берут (`[SE]` — плоские).
- `python tools/export_all.py` — пересобрать сводную таблицу после новых решений.
- Лёгкий конвейер отбора (`tools/verify_chunks.py`, `workflows/skyrim-vr-verify-light.js`, `tools/consolidate_input.py`, `workflows/skyrim-vr-consolidate-light.js`) — переделать под плоскую: в текстах запросов заменить стек (SKSE64, Community Shaders) и убрать VR-чеклист. Правила экономии токенов — в `HANDOFF.md`, «Как экономить токены».
- `workflows/*.js` — все сценарии агентов, которыми собиралась VR-версия (в т. ч. тяжёлые — как образец постановки задач; запускать их заново не нужно).

## Что не сохранено

- `data/rep/` — скачивается заново одной командой.
- Клоны исходников модов с GitHub (~570 МБ), из которых проверялась поддержка VR: для плоской не нужны.
- Журналы агентов: сами результаты сохранены в `data/partial/` (по файлу на агента).
