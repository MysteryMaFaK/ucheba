# Передача работы: облачная сессия → локальный Claude

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
| Данные проверки ядра | Готовы | `data/wf1.json` (подборка из 27 сборок), `data/wf2.json` (хайтек 2026) |
| Черновой манифест ядра | Готов | `data/kit/draft_manifest.json`, группы `data/kit/g*.json` |
| Системный промпт, навык, README | Готовы | `SYSTEM_PROMPT.md`, `.claude/skills/skyrim-vr-install/`, `README.md` |
| `INSTALL_GUIDE.md` | Черновик, места с ⚠ нужно сверить | в конце файла список проверок |
| Карточки установки (файл, FOMOD, требования, порядок) | **131 из 275** | блоки `g1a`, `g1b`, `g2` в `data/partial/` |
| `manifest.yaml`, `MODLIST.md`, `CONFLICTS.md`, `links/` | **Промежуточная сборка**: 275 модов, у 144 карточка с `confidence: low` и общими правилами | собираются `tools/build_kit.py` |
| Проверка процедуры (MO2, Root Builder, xEdit, DynDOLOD и т. д.) | **Не выполнена** | нужен агент `procedure` |
| Критик согласованности (недостающие требования, группы «одно из», порядок) | **Не выполнен** | нужен агент `critic` |
| «Other Mods 2026»: пробелы ядра, часть 1 (старт, спутники, навигация, управление, сохранения, снаряжение, голос) | Собрано 30 кандидатов, **не проверены** | `data/partial/other-mods__collect_gaps-1.json` |
| «Other Mods 2026»: русификация, CC, музыка, ниша; текстуры; внешний вид и мир | **Не начато** | пулы кандидатов готовы в `data/pools/` |

## Продолжение — по шагам (в порядке приоритета)

Везде команды из папки `skyrim-vr-modlist`. Нужен Python 3 с PyYAML (`pip install pyyaml`).

### Шаг 0. Данные сборок (один раз)

```
python tools/fetch_reports.py
```

Скачивает отчёты 27 сборок в `data/rep/` (около 42 МБ, в git не попадает). Они нужны для `tools/whouses.py <id или имя>`: показывает, в каких сборках стоит мод и **точные имена файлов** (по ним видно, какой вариант выбирают VR-сборки).

### Шаг 1. Дописать карточки установки ядра

Недостающие группы: `g3_vr_hitech_ui` (68 модов), `g4_anim_combat` (37), `g5_immersion_audio_ai` (39), затем `procedure` и `critic`.

**Если у вас есть инструмент Workflow (режим «ultracode»):** запустите скрипт `workflows/skyrim-vr-install-spec-wf_a8af17cf-37b.js`.

1. `args: {"only": ["g3_vr_hitech_ui", "g4_anim_combat", "g5_immersion_audio_ai", "procedure"]}`
2. `python tools/save_journal.py <Transcript dir из ответа Workflow> install-spec`
3. `python tools/merge_partials.py install-spec`
4. Критик: `args: {"only": ["critic"], "specsFile": "skyrim-vr-modlist/data/specs_merged.json"}`, затем снова `save_journal.py`, `merge_partials.py`.
5. `python tools/build_kit.py data/install_spec.json`

**Без Workflow:** для каждой группы возьмите `data/kit/<группа>.json` и заполните карточки по схеме, как в готовых `data/partial/install-spec__enrich_g1a_tools_base_frameworks.json` (поля `key, kind, install_target, files, fomod, requires, requires_missing, incompatible_with, choose_one_group, mo2_order, plugin_order, config, verify, risk, confidence, sources`). Не выдумывайте названия опций FOMOD: если не знаете, пишите «неизвестно — общие правила». Результат сохраните как `data/partial/install-spec__enrich_<группа>.json` (формат `{"items": [...], "group_notes": ""}`), потом шаги 3 и 5.

Что должен сделать критик: найти требования, которых нет в манифесте; пары «одно из» без группы; моды из списка «не ставить»; противоречия порядка; свести правила порядка в MO2 и плагинов в `CONFLICTS.md`.

Факты процедуры для агента `procedure` (проверить на страницах модов, а не по памяти): режим Root Builder для VR; аргумент xEdit/xLODGen/DynDOLOD для VR; путь `sksevr.log`; ключ `MaxStdio` в настройках Engine Fixes VR; папка `PrecacheGrass.txt` в VR; выбор игры в Synthesis; запуск Pandora из MO2; корневые файлы OpenComposite Unleashed. Полный перечень вопросов — в `workflows/skyrim-vr-install-spec-wf_a8af17cf-37b.js` (`PROCEDURE_PROMPT`) и в конце `INSTALL_GUIDE.md`.

### Шаг 2. Собрать «Skyrim VR Other Mods 2026»

Скрипт `workflows/skyrim-vr-other-mods-wf_25225427-efd.js`. Кандидаты по темам лежат в `data/pools/` (`other_world.txt`, `other_tex_nature.txt`, `other_tex_arch.txt`, `other_chars.txt`).

1. Сбор оставшихся агентов: `args: {"only": ["gaps-2", "tex-nature", "tex-arch", "chars-armor", "world-creatures"]}`.
2. `python tools/save_journal.py <Transcript dir> other-mods`, затем `python tools/merge_partials.py other-mods` → `data/other_picks.json` (кандидаты с ключами).
3. Проверка в двух проходах: `args: {"picksFile": "skyrim-vr-modlist/data/other_picks.json"}`. Агенты `verify:vr-compat` и `verify:value-perf` читают файл сами. Снова `save_journal.py`, `merge_partials.py other-mods` → `data/other_result.json`.
4. Страница и markdown: `python tools/build_other.py data/other_result.json site/skyrim-vr-other-mods-2026.html OTHER_MODS.md`.
5. Опубликуйте `site/skyrim-vr-other-mods-2026.html` инструментом Artifact (новая страница) и пришлите пользователю ссылку.
6. Для файлов установки второй подборки повторите шаг 1 на её модах (отдельный манифест `manifest_other.yaml`, по образцу первого).

Если Workflow нет, выполните то же вручную: пройдите пулы построчно, для каждого кандидата проверьте VR (`whouses.py`, страница мода: требования, файлы, баги с «VR»), отсейте дубли и запрещённые категории.

Критерии для текстур в VR: по умолчанию **2K** (видеопамять делится на два глаза), 4K только для того, что видно вплотную; PBR-ландшафты — только те, что работают с Open Shaders; одна группа «одно из» на конкурирующие пакеты ландшафта, городов и тел. После текстур в финальную генерацию входят PGPatcher, прекэш травы NGIO, xLODGen, TexGen, DynDOLOD.

### Шаг 3. Обновить публикации

- Ядро: если меняете список, правьте `tools/build_page.py` и `tools/additions.py`, затем `python tools/build_page.py site/skyrim-vr-core-2026.html` и опубликуйте тем же URL (инструмент Artifact, `url=https://claude.ai/artifact/CtFycL6Py2fC2TDY7NZgCa`).
- После правок списка ядра пересоберите черновой манифест: `python tools/make_draft_manifest.py`.
- Закоммитьте и запушьте всё в ветку.

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
