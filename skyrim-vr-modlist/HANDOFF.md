# Передача работы: облачная сессия → локальный Claude

> **Новый чат?** Сначала `NEW_CHAT_PROMPT.md` (что вставить в первое сообщение) и `CONTEXT_FOR_NEW_CHAT.md` (контекст, решения, ошибки). Индекс файлов — `FILES.md`. Скачать пакет на Windows: `tools/windows_setup.ps1`.

Состояние на 08.10.2026. Работа переносится на ваш компьютер, чтобы тратить токены подписки, а не облачной сессии.
Ветка репозитория: `claude/wizardly-brahmagupta-qj2sb4`. Откройте во вкладке Code папку **`skyrim-vr-modlist`** как проект (тогда подхватится навык `/skyrim-vr-install`).

## Что нужно знать сразу

- Пользователь играет в **Skyrim VR 1.4.15** (SKSEVR 2.0.12, MO2). Все решения — под VR. Язык общения — русский.
- Цель: подборка модов для next-gen сборки (по роликам вроде «Next Gen Skyrim 2026»), без конфликтов, с патчами, производительная. Затем — установка в MO2 по этому пакету.
- Источники: составы 27 популярных сборок Wabbajack 2025–2026 (9 VR, 18 плоских next-gen) и исходники модов. Каждый мод проверен дважды: совместимость с VR и избыточность.
- Правило пользователя: моды для обычной Skyrim SE подходят в VR, если нет жалоб на VR. Моя поправка: для модов с **DLL** этого мало, нужна VR-сборка (файл VR, страница VR или «SE/AE/VR» у автора). Моды без DLL работают почти всегда.
- Два списка: **ядро** (готово) и **«Other Mods 2026»** (пробелы ядра → текстуры → внешний вид и мир). Для второго пользователь исключил: квесты и новые земли, дома игрока, компаньонов-персонажей, крупные оверхолы сложности, пакеты заклинаний и криков, узкие части SimonRim (Aetherius, Scion, Manbeast, Pilgrim), NSFW.
- Порядок разделов второго списка (так просил пользователь): сначала **пробелы ядра**, потом **текстуры**, потом **внешний вид и мир** (тела, лица, броня, существа, меши городов, ReShade).
- В облачной сессии были закрыты nexusmods.com, modding.wiki и сайты Wabbajack CDN: данные брались из сниппетов поиска, GitHub и отчётов сборок. **Локально Nexus открывается** — используйте страницы модов напрямую, это точнее и дешевле поиска. Вход в аккаунт Nexus и ввод паролей агент не делает.

## Состояние

| Часть | Статус | Где |
|---|---|---|
| Страница ядра (275 модов) | **Готова, опубликована** | https://claude.ai/artifact/CtFycL6Py2fC2TDY7NZgCa · исходник `site/skyrim-vr-core-2026.html` |
| Манифест установки ядра | **Готов**: 287 модов, карточки у всех (275 подробных, 12 коротких у требований, найденных критиком) | `manifest.yaml`, `MODLIST.md`, `links/` |
| Группы «одно из», правила порядка в MO2 и плагинов, найденные противоречия, системные требования | **Готовы** (17 групп, 22 + 14 правил, 38 противоречий) | `CONFLICTS.md`, `manifest.yaml` |
| Проверка процедуры (MO2, Root Builder, SKSEVR, Engine Fixes, xEdit, DynDOLOD, NGIO, Synthesis) | **Выполнена**; низкая надёжность помечена **(проверить)** | `INSTALL_GUIDE.md`, `data/partial/install-spec__procedure_fact-check.json` |
| Системный промпт и навык `/skyrim-vr-install` | Готовы | `SYSTEM_PROMPT.md`, `.claude/skills/skyrim-vr-install/` |
| «Other Mods 2026» — список | **Готов, опубликован**: 128 модов + 23 запрета (из 178 кандидатов оставлено 151) | https://claude.ai/artifact/GRjZnT1B4zRCYUyV4UppH9 · `OTHER_MODS.md` · `site/skyrim-vr-other-mods-2026.html` |
| «Other Mods 2026» — файлы установки (файл, FOMOD, требования, порядок) | **Не сделаны** | см. шаг 2 ниже |

## Требования к окружению

- **Python 3** (на Windows команда `python`, на Linux и macOS `python3`; ниже везде `python`) и `pip install pyyaml` (нужен `build_kit.py`).
- Интернет к `raw.githubusercontent.com` (скачивание отчётов сборок). **Перед `whouses.py`, `cand.py`, `cats.py`, `union.py` обязателен шаг 0** (`fetch_reports.py`): без папки `data/rep/` они упадут.
- Git. Репозиторий приватный: при первом обращении Git попросит войти в GitHub.
- Для воркфлоу-скриптов — инструмент Workflow Claude Code (режим «ultracode» или явная просьба владельца). Без него те же шаги выполняются вручную (описано ниже).

## Где править (сгенерированные файлы)

Эти файлы **собираются скриптами**; правка вручную пропадёт при пересборке. Перед любой пересборкой сделайте коммит или копию.

| Сгенерированный файл | Что править |
|---|---|
| `site/skyrim-vr-core-2026.html` | `tools/build_page.py` (основной список) и `tools/additions.py` (добавления 08.10), затем `python tools/build_page.py site/skyrim-vr-core-2026.html` |
| `data/kit/draft_manifest.json` | не вручную: `python tools/make_draft_manifest.py` (читает `build_page.py` и `additions.py`) |
| `manifest.yaml`, `MODLIST.md`, `CONFLICTS.md`, `links/` | **карточки модов**: `data/partial/install-spec__enrich_*.json` (источник) либо точечно `data/kit/fixups.json` (`mod_patches` по ключу мода, `text_fixes` для замены текста, `key_aliases` для переименованных ключей); **группы, порядок, противоречия**: `data/partial/install-spec__critic_consistency.json`. Затем `python tools/merge_partials.py install-spec` и `python tools/build_kit.py data/install_spec.json` |
| `OTHER_MODS.md`, `site/skyrim-vr-other-mods-2026.html` | `data/partial/other-mods__*.json`, затем `merge_partials.py other-mods` и `build_other.py` (см. шаг 3) |

Закрывая метку «проверить» в карточке мода: поправьте поля в `data/partial/install-spec__enrich_<группа>.json` (источник; ключ карточки — поле `key`) или добавьте запись в `mod_patches` файла `fixups.json`, потом пересоберите. Правка прямо в `manifest.yaml` не переживёт пересборку.

## Как перезапустить часть агентов (инструмент Workflow)

Вызов: `Workflow({scriptPath: "<абсолютный путь к скрипту из workflows/>", args: {...}})`. Скрипты по умолчанию используют относительные пути `skyrim-vr-modlist/...`, то есть рассчитаны на запуск из папки, **содержащей** `skyrim-vr-modlist` (корень клона). Если рабочая папка чата — сама папка проекта, добавьте во **все** вызовы параметр `root` с абсолютным путём, например `"root": "E:/Modding/ucheba/skyrim-vr-modlist"`. Ответ инструмента содержит `Transcript dir`: он нужен для сохранения результатов.

| Скрипт | Параметры `args` |
|---|---|
| `skyrim-vr-install-spec-wf_*.js` | `{"only": ["g3_vr_hitech_ui","g4_anim_combat","g5_immersion_audio_ai","procedure"]}` — карточки и проверка процедуры; `{"only": ["critic"], "specsFile": "<абс. путь>/data/specs_merged.json"}` — критик. Группы: `g1a_tools_base_frameworks`, `g1b_fixes`, `g2_gfx_world_land`, `g3_vr_hitech_ui`, `g4_anim_combat`, `g5_immersion_audio_ai` |
| `skyrim-vr-other-mods-wf_*.js` | сбор: `{"only": ["gaps-1","gaps-2","tex-nature","tex-arch","chars-armor","world-creatures"]}`; проверка: `{"picksFile": "<абс. путь>/data/other_picks.json"}` |
| `skyrim-vr-core-additions-wf_*.js`, `skyrim-vr-hitech-2026-wf_*.js` | **без параметров** и перезапускать не нужно: их результаты уже в `data/wf1.json` и `data/wf2.json` |

После запуска: `python tools/save_journal.py "<Transcript dir>" <install-spec|other-mods>` (существующие файлы не перезаписывает; `--overwrite` заменяет с копией в `data/partial/_backup/`), затем `merge_partials.py`, затем `build_kit.py` / `build_other.py`. Это можно делать и фоном: `tools/autosave.sh <кампания>=<Transcript dir>` (с `--push` добавит коммит и пуш, только с разрешения владельца).

**Без Workflow:** прочитайте нужный скрипт, возьмите из него текст запроса агента (`CONTEXT`, `prompt`, схему результата) и выполните ту же работу самостоятельно, сохраняя результат в файл формата `data/partial/<кампания>__<метка>.json`.

## Что осталось

### Шаг 0. Данные сборок (нужны, если будете искать по сборкам)

```
python tools/fetch_reports.py
```

Скачивает отчёты 27 сборок в `data/rep/` (около 42 МБ, 2 секунды, в git не попадает). Дальше `python tools/whouses.py <id или имя>` показывает, в каких сборках стоит мод и **точные имена файлов**.

### Шаг 1. Закрыть метки «проверить» в ядре (ручная сверка на Nexus)

Локально Nexus открывается, поэтому агент читает страницы и правит карточки. Список — в конце `INSTALL_GUIDE.md` и в разделе «Найденные противоречия» файла `CONFLICTS.md` (пункты с «уточнить вручную»): зависимости SkyrimNet (Prisma UI, Media Keys Fix), Mantella (No NPC Greetings, World Encounter Hostility Fix), патч NPC Spell Variance для PLANCK, SkyUI Weapons Pack для Norden UI, DynamicShader Core, Tiny Light Placer Hub, ImGui Icons для SKSE Menu Framework. Все они относятся к модам с меткой `opt` или `try`: по умолчанию не ставятся.
Карточки 12 требований, добавленных критиком (SSE Terrain Tamriel, Simple Realistic Archery VR, Broken Feathers, Floating Subtitles, RaceMenu AE, FEC SE, Embers XD FEC Patch, Behavior Data Injector и Universal Support, ISC-SRDified, Seasons of Skyrim VR, Simple Offence Suppression SE) короткие: файл и выборы установщика берутся со страницы мода.

### Шаг 2. Файлы установки для «Other Mods 2026»

Для 151 мода второй подборки нужны карточки установки по образцу `manifest.yaml`. Процесс тот же, что был для ядра:

1. Список — `data/other_result.json` (поле `verified`, `keep: true`).
2. Разбейте на группы по 25–40 модов, для каждой заполните карточку (`key, kind, install_target, files, fomod, requires, requires_missing, incompatible_with, choose_one_group, mo2_order, plugin_order, config, verify, risk, confidence, sources`). Схема и образец — `data/partial/install-spec__enrich_g1a_tools_base_frameworks.json`. Не выдумывайте названия опций FOMOD: «неизвестно — общие правила».
3. Критик согласованности (как для ядра): недостающие требования, группы «одно из», противоречия, порядок. Особое внимание группам тел, лиц, ландшафта, городов; BodySlide и тела — до брони.
4. **Нужен новый скрипт** (например, `tools/build_kit_other.py`): `build_kit.py` привязан к ядру (фазы, `draft_manifest.json`, разделители). Вход: `data/other_result.json` (элементы `verified` с `keep: true`: `name, id, url, section, tag, choose_one_group, what, files, requires, note`) и карточки установки; выход: `manifest_other.yaml`, `MODLIST_OTHER.md`, `links_other/phase-*.txt`. Формат карточек и полей — как в `manifest.yaml`.

С Workflow: скрипт `workflows/skyrim-vr-install-spec-wf_a8af17cf-37b.js` написан под ядро (группы в `GROUPS`); для второго списка замените `GROUPS` и пути на `data/other_result.json`. Без Workflow — вручную по группам.

### Шаг 3. Публикации

- Ядро: правьте `tools/build_page.py` и `tools/additions.py`, затем `python tools/build_page.py site/skyrim-vr-core-2026.html` и публикуйте тем же URL (инструмент Artifact, `url=https://claude.ai/artifact/CtFycL6Py2fC2TDY7NZgCa`). После правок пересоберите манифест: `python tools/make_draft_manifest.py && python tools/build_kit.py data/install_spec.json`.
- Вторая подборка: `python tools/build_other.py data/other_result.json site/skyrim-vr-other-mods-2026.html OTHER_MODS.md`, URL `https://claude.ai/artifact/GRjZnT1B4zRCYUyV4UppH9`.
- Публикация страницы инструментом Artifact **перезаписывает опубликованную страницу**: делайте это только с явного «да» владельца. Запасной вариант без Artifact: отдать HTML-файл из `site/`.
- Коммит и пуш в ветку — тоже по просьбе владельца.

## Известные решения и оговорки

- Официальный Community Shaders с 1.7 не поддерживает VR; взят **Open Shaders 2.17** (альтернатива CSX). Один из двух.
- Не добавлены из-за расхождения оценок или отсутствия данных: Particle Wind (VR есть в исходниках шаблона, но требует Address Library для SE), Interior DALC Fix, Dynamic Interior Fog.
- Помечены `try` (VR заявлен, не обкатан): Dynamic Footprints SKSE, DynamicSnow, XPMF, Frostwalker, Bobbing Framework, Immersive NPC Dialogue VR, Palm Compass VR, RaceMenu VR 2, I5, Variadic Collision Dynamics, A-Pose Bug Fix, Native Water Light Stabilizer, Saving on Steed.
- У многих новинок 2026 года на Nexus стоит метка AI Assisted/Generated — это указано в описаниях.
- Замена в ядре: вместо VR Climbing (168553) стоит форк Aelove (170321).
- Пути A и B для мастеров/USSEP описаны в `INSTALL_GUIDE.md`; выбор — переменная `MASTERS_PATH` в `SYSTEM_PROMPT.md`.

## Как экономить токены локально

- Данные уже собраны: в `data/` лежат результаты проверки и пулы кандидатов, заново искать их не нужно.
- Читайте страницы модов на Nexus напрямую, а не через поисковые сниппеты.
- Карточки установки заполняйте по группам; для рутинных групп хватит модели поменьше.
- `tools/whouses.py` ничего не стоит по токенам и сразу показывает, какой файл выбирают VR-сборки.
