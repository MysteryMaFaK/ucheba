# Индекс файлов

Папка `skyrim-vr-modlist` (репозиторий `MysteryMaFaK/ucheba`, ветка `claude/wizardly-brahmagupta-qj2sb4`).

## Сводка чисел

| Что | Число |
|---|---|
| Страница ядра | 275 позиций |
| `manifest.yaml` ядра | 287 модов = 275 + 12 требований, найденных проверкой согласованности |
| Группы «одно из» / правила порядка MO2 / правила порядка плагинов / разобранные противоречия | 17 / 22 / 14 / 38 |
| Вторая подборка | 178 кандидатов → 151 прошли обе проверки = **128 модов + 23 запрета «не ставить»** |
| Сборки Wabbajack в анализе | 27 = 9 VR + 18 плоских next-gen |

## Что генерируется

Не править вручную: `manifest.yaml`, `MODLIST.md`, `CONFLICTS.md`, `links/`, `OTHER_MODS.md`, `site/*.html`, `data/kit/draft_manifest.json`, `data/install_spec.json`, `data/specs_merged.json`, `data/other_picks.json`, `data/other_result.json`. Источники правок — `tools/build_page.py`, `tools/additions.py`, `data/partial/`, `data/kit/fixups.json` (подробно — `HANDOFF.md`, «Где править»).

## Читать в первую очередь

| Файл | Что внутри |
|---|---|
| `NEW_CHAT_PROMPT.md` | Короткий промпт для первого сообщения нового чата |
| `CONTEXT_FOR_NEW_CHAT.md` | Контекст проекта: цель, хронология запросов, решения, ошибки, открытые вопросы, состояние |
| `HANDOFF.md` | Состояние работы и точные команды продолжения |
| `README.md` | Краткое описание пакета и способы запуска установки |

## Пакет установки (читает агент-установщик)

| Файл | Что внутри |
|---|---|
| `SYSTEM_PROMPT.md` | Системный промпт: конфигурация, алгоритм установки мода, правила FOMOD, критичные правила MO2, контрольные запуски |
| `.claude/skills/skyrim-vr-install/SKILL.md` | Навык `/skyrim-vr-install` (запускает промпт) |
| `manifest.yaml` | Машиночитаемый манифест ядра: 287 модов с файлом, FOMOD, требованиями, конфликтами, порядком, настройками, проверкой |
| `MODLIST.md` | Тот же манифест в читаемом виде (карточка на мод) |
| `CONFLICTS.md` | Группы «одно из», системные требования, правила порядка в MO2 и плагинов, разобранные противоречия, список «не ставить в VR» |
| `INSTALL_GUIDE.md` | Подготовка, MO2, Root Builder, файлы профиля, инструменты, фазы 0–10, финальная генерация LOD |
| `links/phase-1..9.txt` | Ссылки на моды по фазам установки |

## Списки

| Файл | Что внутри |
|---|---|
| `site/skyrim-vr-core-2026.html` | Исходник опубликованной страницы ядра (275 позиций) |
| `site/skyrim-vr-other-mods-2026.html` | Исходник страницы «Other Mods 2026» (128 модов + 23 запрета) |
| `OTHER_MODS.md` | Вторая подборка в markdown |

## Данные (`data/`)

| Файл | Что внутри |
|---|---|
| `wf1.json`, `wf2.json` | Результаты двойной проверки модов ядра: подборка из 27 сборок и хайтек-новинки 2026 |
| `install_spec.json`, `specs_merged.json` | Карточки установки ядра и разбор критика (склеены из `partial/`) |
| `other_picks.json`, `other_result.json` | Кандидаты второй подборки и результат двойной проверки (151 из 178) |
| `partial/` | Результаты отдельных агентов по одному файлу: карточки установки, проверка процедуры, критик, сбор и проверка второй подборки |
| `kit/` | `draft_manifest.json` (275 модов ядра), группы для карточек, `fixups.json` (исправления текста и алиасы ключей) |
| `pools/` | Пулы кандидатов из составов сборок по темам (для сбора второй подборки) |
| `page_items.txt`, `page_ids.json`, `new2026_in_lists.txt` | Инвентарь страницы ядра и моды 2026 года, которые уже стоят в популярных сборках |
| `rep/` | Отчёты 27 сборок Wabbajack. **Не в git**: `python tools/fetch_reports.py` |

## Инструменты (`tools/`)

| Файл | Назначение |
|---|---|
| `fetch_reports.py` | Скачать отчёты 27 сборок в `data/rep/` |
| `whouses.py` | Какие сборки используют мод и какие файлы выбирают (`python tools/whouses.py <ID или имя>`) |
| `build_page.py`, `additions.py`, `template.html` | Исходник списка ядра и сборка страницы: `python tools/build_page.py site/skyrim-vr-core-2026.html` |
| `make_draft_manifest.py` | Пересобрать `data/kit/draft_manifest.json` после правки списка ядра |
| `merge_partials.py` | Склеить `data/partial/` в `install_spec.json` / `other_picks.json` / `other_result.json` |
| `build_kit.py` | Собрать `manifest.yaml`, `MODLIST.md`, `CONFLICTS.md`, `links/` |
| `build_other.py`, `template_other.html` | Собрать страницу и markdown второй подборки |
| `save_journal.py`, `autosave.sh` | Сохранить результаты агентов воркфлоу из журнала в `data/partial/` |
| `cand.py`, `cats.py`, `union.py`, `listdates.py`, `wjlist.py` | Вспомогательные скрипты анализа составов сборок |
| `windows_setup.ps1` | Клонирование только папки проекта на Windows: по умолчанию в `E:\Modding\ucheba\skyrim-vr-modlist` |

## Сценарии воркфлоу (`workflows/`)

Скрипты для инструмента Workflow (режим «ultracode»), пути в них относительные (`skyrim-vr-modlist/...`). Параметры `args` есть только у `install-spec` (`only`, `specsFile`) и `other-mods` (`only`, `picksFile`); `core-additions` и `hitech-2026` без параметров и уже отработали. Точные вызовы — `HANDOFF.md`, раздел «Как перезапустить часть агентов».

| Файл | Что делает |
|---|---|
| `skyrim-vr-core-additions-wf_*.js` | Добор модов ядра из составов сборок (6 категорий + свежие релизы) + двойная проверка |
| `skyrim-vr-hitech-2026-wf_*.js` | Проверка пяти примеров владельца и поиск хайтек-новинок 2026 |
| `skyrim-vr-install-spec-wf_*.js` | Карточки установки ядра (6 групп), проверка процедуры, критик согласованности |
| `skyrim-vr-other-mods-wf_*.js` | Сбор второй подборки (6 агентов) и двойная проверка |
