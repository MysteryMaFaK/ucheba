# Skyrim VR Core 2026 — карточки модов

Тот же манифест в читаемом виде. Порядок карточек — порядок в левой панели MO2 сверху вниз внутри разделителя.
Метки: `core` — обязательно · `rec` — рекомендую · `opt` — по желанию · `alt` — выбор · `try` — проверить.

## Разделители
- [00 Инструменты и корень](#00-инструменты-и-корень) — 16
- [01 Мастера и USSEP](#01-мастера-и-ussep) — 8
- [02 SKSEVR и библиотеки](#02-sksevr-и-библиотеки) — 31
- [03 Фиксы движка](#03-фиксы-движка) — 36
- [04 Шейдеры и свет](#04-шейдеры-и-свет) — 6
- [05 VR-ядро](#05-vr-ядро) — 35
- [06 Хайтек 2026](#06-хайтек-2026) — 17
- [07 Интерфейс](#07-интерфейс) — 16
- [08 Звук](#08-звук) — 9
- [09 Свет, погода, вода, VFX](#09-свет-погода-вода-vfx) — 18
- [10 Ландшафт, трава, деревья](#10-ландшафт-трава-деревья) — 13
- [11 Анимации и физика](#11-анимации-и-физика) — 19
- [12 Бой и геймплей](#12-бой-и-геймплей) — 18
- [13 Мир, ИИ, погружение](#13-мир-ии-погружение) — 27
- [14 ИИ-NPC](#14-ии-npc) — 3
- [15 VR-рантайм и производительность](#15-vr-рантайм-и-производительность) — 3

## 00 Инструменты и корень

### Mod Organizer 2 — `core` [ссылка](https://github.com/ModOrganizer2/modorganizer/releases)
- Фаза 1 · тип `external_tool` · установка `manual_steps` · надёжность данных `high`
- Файл: Mod.Organizer-2.5.2.7z с GitHub (ModOrganizer2/modorganizer releases). Ту же версию ставят Stormcrown VR и Panda's Sovngarde.
- Установщик: нет установщика
- Настройки: Создать портативный инстанс в отдельной папке. Не класть его в Program Files и в папку Steam (например, C:\Modding\SkyrimVR). Игра — Skyrim VR. В профиле включить «Use profile-specific Game INI Files», локальные сохранения — по желанию. Папку downloads держать внутри инстанса. Разделители — по mo2_order манифеста.
- Проверка: В заголовке MO2 — Skyrim VR. На вкладке Plugins видны Skyrim.esm … SkyrimVR.esm.
- Заметка: Портативный инстанс в отдельной папке. Профиль с локальными INI — так настройки VR не смешаются с другими сборками.

### Root Builder — `core` [#31720](https://www.nexusmods.com/skyrimspecialedition/mods/31720)
- Фаза 1 · тип `mo2_plugin` · установка `mo2_plugins_folder` · надёжность данных `high`
- Файл: Root Builder 5.1.x (Stormcrown VR — Root Builder-31720-5-1-1). Panda's Sovngarde и Tempus VR — 5.0.5.
- Установщик: нет установщика: папку rootbuilder распаковать в <MO2>\plugins\rootbuilder
- Требует: Mod Organizer 2 (2.5.2)
- Порядок в MO2: Сам Root Builder — не мод. Моды с папкой Root ставить в разделе «Инструменты и корень».
- Настройки: Оставить настройки по умолчанию: copyfiles=** (режим Copy), autobuild=true, redirect=true, backup=true, cache=true. installer=false (по умолчанию), поэтому корневые файлы класть в папку Root вручную. Папка Root лежит рядом с содержимым Data, а не внутри Data. Папку Data в Root не класть — мод будет проигнорирован. Пока MO2 работает, не нажимать Unlock. После вылета игры: Tools → Root Builder → Clear, потом Clear Overwrite (так советует FUS).
- Проверка: При запуске через MO2 в папке игры появляются sksevr_loader.exe, DLL SKSEVR и Part 2 Engine Fixes. После закрытия игры они убираются.
- Заметка: Кладёт в корень игры загрузчик SKSEVR, Part 2 от Engine Fixes VR и DLL OpenComposite, не трогая папку Steam.

### SSEEdit (xEdit) — `core` [#164](https://www.nexusmods.com/skyrimspecialedition/mods/164)
- Фаза 1 · тип `external_tool` · установка `external_tool` · надёжность данных `high`
- Файл: SSEEdit/xEdit 4.1.5f (xEdit.4.1.5f.7z с GitHub TES5Edit или Nexus #164). Ставят Stormcrown VR, Tempus VR, FUS и Panda's Sovngarde.
- Установщик: нет установщика
- Настройки: Распаковать в <MO2>\tools\SSEEdit (не в mods и не в папку игры). Добавить exe из архива исполняемым в MO2 с аргументом -tes5vr. Запускать только из MO2. Результат правок попадает в Overwrite — переносить его в отдельный мод.
- Проверка: Окно открывается в режиме TES5VR, в списке есть SkyrimVR.esm.
- Заметка: Режим VR: аргумент -tes5vr. Чистка мастеров, просмотр конфликтов, ручные патчи.

### LOOT — `core` [ссылка](https://loot.github.io/)
- Фаза 1 · тип `external_tool` · установка `external_tool` · надёжность данных `medium`
- Файл: LOOT с GitHub (loot/loot releases), свежая версия. Panda's Sovngarde — loot_0.26.0-win64.7z.
- Установщик: нет установщика
- Порядок плагина: Сортировать после каждой порции модов. Свои правила добавлять только при подтверждённом конфликте.
- Настройки: Распаковать в tools и добавить исполняемым в MO2. Игра — Skyrim VR. После сортировки проверить конфликты в xEdit. Если LOOT помечает ESL как неподдерживаемые в VR — обновить LOOT. При стоящем Skyrim VR ESL Support это не ошибка игры.
- Проверка: LOOT видит SkyrimVR.esm, ошибок про отсутствующие мастера нет.
- Заметка: Сортировка плагинов, Skyrim VR поддерживается. После сортировки — ручная проверка конфликтов в xEdit.

### BethINI Pie + Skyrim VR Plugin for Bethini Pie — `core` [ссылка](https://www.nexusmods.com/site/mods/631)
- Также скачать: VR-плагин: https://www.nexusmods.com/skyrimspecialedition/mods/177465
- Фаза 1 · тип `external_tool` · установка `external_tool` · надёжность данных `medium`
- Файл: BethINI Pie (Nexus site/mods/631) и Skyrim VR Plugin for Bethini Pie (#177465). Старый BethINI Standalone 3.6.1 (стоит в Tahrovin и SoG) не брать.
- Установщик: неизвестно — общие правила: куда класть VR-плагин, смотреть в README/описании
- Требует: Skyrim VR Plugin for Bethini Pie (#177465)
- Не вместе с: BethINI Standalone (#4875)
- Настройки: Распаковать в tools и запускать из MO2. Указать INI профиля MO2 (SkyrimVR.ini и SkyrimPrefs.ini лежат в папке профиля). Взять низкий или средний пресет, затем точечно поправить под VR. Делать до тонкой настройки Open Shaders.
- Проверка: INI в папке профиля MO2 изменились, игра стартует с ними.
- Заметка: INI под VR. Плагин VR ещё и требование Skyrim VR Fixes for Latest USSEP.

### Pandora Behaviour Engine+ — `rec` [#133232](https://www.nexusmods.com/skyrimspecialedition/mods/133232)
- Фаза 1 · тип `external_tool` · установка `external_tool` · надёжность данных `medium`
- Файл: Pandora Behaviour Engine не старше 4.1.2-beta: в ней вернули поддержку SkyrimVR, Tahrovin ставит v4.1.2-beta. Последние — 4.4.0-beta и 5.0.0-beta (01.10). Если 5.0 не собирает, взять 4.4.0-beta.
- Установщик: нет установщика
- Не вместе с: Nemesis Unlimited Behavior Engine
- Группа «одно из»: `behavior-engine`
- Порядок в MO2: Мод с выводом (Pandora Output) — в самом низу, в блоке «Сгенерированное».
- Настройки: Распаковать в tools, добавить исполняемым в MO2. В GUI указать Game path и Output path. Output вести в отдельную папку мода, например mods\Pandora Output, и включить этот мод. С 4.4.0 Settings.json лежит в папке установки, поэтому настройки свои у каждого профиля. Пересобирать после каждого изменения поведенческих модов.
- Проверка: Сборка проходит без ошибок, в Pandora Output есть meshes. В игре нет T-позы у NPC.
- Заметка: Сборка поведений для OAR и анимаций. Поддержку Skyrim VR вернули в 4.1.2-beta. Если какой-то мод не собирается — запасной вариант Nemesis.

### Synthesis — `rec` [ссылка](https://github.com/Mutagen-Modding/Synthesis/releases)
- Фаза 1 · тип `external_tool` · установка `external_tool` · надёжность данных `medium`
- Файл: Synthesis.zip с GitHub (Mutagen-Modding/Synthesis releases). Panda's Sovngarde — 0.35.0.
- Установщик: нет установщика
- Порядок в MO2: Мод Synthesis Output — в самом низу, в блоке «Сгенерированное».
- Порядок плагина: Synthesis.esp — самым последним, без исключений (FUS).
- Настройки: Распаковать в tools и запускать из MO2. Цель — Skyrim VR. Вывод направить в отдельный мод. Перед повторным запуском отключить старый Synthesis.esp, после — включить. Перезапускать после каждой генерации LOD и после изменений погоды или ячеек (FUS). Нужен .NET SDK — версию Synthesis покажет сам.
- Проверка: Synthesis.esp создан и стоит последним в load order.
- Заметка: Патчеры в финале сборки. Запускается после всех модов, перед генерацией LOD.

### fpsVR или SteamVR Frame Timing — `rec` [ссылка](https://store.steampowered.com/app/908520/fpsVR/)
- Фаза 1 · тип `external_tool` · установка `external_tool` · надёжность данных `medium`
- Файл: fpsVR (платное приложение Steam) или бесплатный SteamVR → Advanced Frame Timing. В MO2 не ставится.
- Установщик: нет установщика
- Настройки: Смотреть время кадра CPU и GPU, а не загрузку видеокарты. С OpenComposite игра идёт мимо SteamVR, поэтому оверлей fpsVR в шлеме не появится — замеры делать на SteamVR или через встроенный счётчик Open Shaders.
- Проверка: Время кадра укладывается в бюджет частоты шлема.
- Заметка: Без замеров время кадра не настроить. Смотрите на CPU и GPU frametime, а не на загрузку видеокарты.

### DynDOLOD 3 + Resources SE 3 + DynDOLOD DLL NG — `core` [#68518](https://www.nexusmods.com/skyrimspecialedition/mods/68518)
- Также скачать: Resources: https://www.nexusmods.com/skyrimspecialedition/mods/52897; DLL NG: https://www.nexusmods.com/skyrimspecialedition/mods/97720
- Фаза 1 · тип `external_tool` · установка `external_tool` · надёжность данных `high`
- Файл: DynDOLOD 3.00 Alpha-210 или новее (Stormcrown VR, 20.08.2026; Morning Star — Alpha-212). Resources SE 3.00 Alpha-59 (#52897, Stormcrown). DynDOLOD DLL NG and Scripts 3.00 Alpha-43 (#97720, Stormcrown). Старую DynDOLOD DLL VR и DLL SE не брать.
- Установщик: DynDOLOD — нет установщика, распаковать в tools. Resources SE 3 и DLL NG — неизвестно, общие правила: читать установщик, если он есть.
- Требует: DynDOLOD Resources SE 3 (#52897); DynDOLOD DLL NG and Scripts (#97720); SKSEVR (#30457); VR Address Library for SKSEVR (#58101); Skyrim VR ESL Support (#106712); xLODGen (вывод рельефа)
- Не вместе с: DynDOLOD DLL VR (старая); DynDOLOD DLL SE
- Порядок в MO2: Resources SE 3 — высоко в списке (рано), чтобы моды с LOD-ассетами её перезаписывали. DLL NG — обычный мод в блоке фреймворков. TexGen_Output и DynDOLOD_Output — в самом низу: xLODGen → TexGen → DynDOLOD.
- Порядок плагина: DynDOLOD.esm и DynDOLOD.esp ставит LOOT. Если Synthesis перезапускали после DynDOLOD (так у FUS), Synthesis.esp идёт после них, самым последним.
- Настройки: Распаковать в <MO2>\tools\DynDOLOD. Исполняемые TexGenx64.exe и DynDOLODx64.exe — с аргументом -tes5vr. Руководство для VR — DynDOLOD_Manual_TES5VR в архиве. В TexGen для VR рекомендуется сжатие BC3 (FUS). Вывод каждого инструмента — в свой мод. Запуск — только на финальном этапе (gen_steps), после Grass Cache и xLODGen.
- Проверка: DynDOLOD завершается без ошибок. В игре дальние LOD на месте, при подходе ничего не мерцает. В sksevr.log загружена DLL NG.
- Заметка: Генератор дальних LOD. Режим TES5VR, DLL NG общая для SE/AE/VR, старую DLL VR не ставить. Запуск — на финальном этапе.

### xLODGen — `core` [ссылка](https://stepmodifications.org/forum/topic/13451-xlodgen/)
- Фаза 1 · тип `external_tool` · установка `external_tool` · надёжность данных `medium`
- Файл: xLODGen.132.7z с GitHub (sheson/xLODGen release v132), так в Stormcrown VR.
- Установщик: нет установщика
- Требует: SSE Terrain Tamriel (#54680)
- Порядок в MO2: xLODGen_Output — в самом низу, перед TexGen_Output и DynDOLOD_Output. SSE Terrain Tamriel включать как мод на время генерации.
- Порядок плагина: SSE Terrain Tamriel.esm (если есть) нужен только для генерации — после неё отключить, если его страница так велит.
- Настройки: Распаковать в tools, исполняемый xLODGenx64.exe — с аргументом -tes5vr. Генерировать только Terrain LOD по всем мирам (FUS). Вывод — в отдельный мод. Файл Terrain Tamriel: Librum и Yggdrasil берут «Full Extend», Tempus — «Extend».
- Проверка: Рельеф вдали без дыр и чужих текстур.
- Заметка: LOD рельефа перед DynDOLOD. Ресурс SSE Terrain Tamriel — в блоке финальной генерации.

### MCM Memory — `rec` [#189722](https://www.nexusmods.com/skyrimspecialedition/mods/189722)
- Фаза 1 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: MCM Memory 1.5.3 или новее: в 1.5.3 исправлено автовосстановление в VR. Stormcrown VR — 1.5.3.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101); SkyUI VR (#91535); SKSE Menu Framework (#120352)
- Не вместе с: MCM Recorder (#61719); MCM Bridge
- Группа «одно из»: `mcm-backup`
- Настройки: Свой интерфейс открывается через SKSE Menu Framework. Совместим с MCM Helper и MCM Unlocked.
- Проверка: В sksevr.log DLL загружена. В новой игре настройки MCM восстанавливаются сами.
- Заметка: Сохраняет настройки всех MCM и сам восстанавливает их в новой игре. Преемник MCM Recorder, VR-фикс в 1.5.3. Стоит в Stormcrown VR.

### More Informative Console — `opt` [#19250](https://www.nexusmods.com/skyrimspecialedition/mods/19250)
- Фаза 1 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `high`
- Файл: Универсальный 1.2.2 (FUS, Panda, Tempus VR, Librum VR). Запасной — файл «More Informative Console 1.0.1 VR» (Tahrovin, SoG).
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Настройки: Работает вместе с ConsoleUtilVR и VR Console Selection Fix.
- Проверка: В консоли выбрать объект — сбоку панель с плагином-источником и перезаписями.
- Заметка: Консоль показывает плагин-источник, перезаписи, меши — главный инструмент отладки. Есть VR-файл.

### Lights Conflict Resolver — `opt` [#175086](https://www.nexusmods.com/skyrimspecialedition/mods/175086)
- Фаза 1 · тип `external_tool` · установка `external_tool` · надёжность данных `medium`
- Файл: Последняя версия (Tahrovin — 0.2.6, Tempus VR — 0.2.5).
- Установщик: неизвестно — общие правила
- Требует: Light Placer + Light Placer VR (#127557, #135822)
- Порядок в MO2: Если инструмент создаёт файлы — вывод в отдельный мод ниже всех конфигов света.
- Настройки: Запускать из MO2 после установки всех конфигов Light Placer, CS Light, Lux и Tiny Light Placer Hub. Формат вывода — неизвестно, читать описание.
- Проверка: В интерьерах Lux нет удвоенного света от одного источника.
- Заметка: Находит дубли в конфигах Light Placer, чтобы свет не удваивался. Свет у нас из Light Placer, CS Light и Lux — дубли реальны.

### VR Keyboard — `opt` [#64319](https://www.nexusmods.com/skyrimspecialedition/mods/64319)
- Фаза 1 · тип `mixed` · установка `mo2_mod` · надёжность данных `low`
- Файл: VR Keyboard-64319-1-0-1 (единственный файл, 5 VR-списков).
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457)
- Настройки: Проверить, нужен ли он вообще. По заметке куратора к OpenComposite Unleashed, в этой сборке виртуальная клавиатура уже работает. Если ввод имени там работает — не ставить.
- Проверка: При вводе имени персонажа появляется виртуальная клавиатура.
- Заметка: Виртуальная клавиатура для имён и поиска — с OpenComposite оверлея SteamVR нет.

### PGPatcher (бывш. ParallaxGen) — `opt` [#120946](https://www.nexusmods.com/skyrimspecialedition/mods/120946)
- Фаза 1 · тип `external_tool` · установка `external_tool` · надёжность данных `medium`
- Файл: PGPatcher 2.0.x (Stormcrown — 2.0.0, True North — 2.1.1).
- Установщик: нет установщика
- Порядок в MO2: Вывод — в отдельный мод в блоке «Сгенерированное», выше Synthesis и LOD-вывода.
- Настройки: Только на этапе текстур (gen_steps, шаг 2), если стоят PBR или parallax-текстуры. Запуск из MO2.
- Проверка: Без фиолетовых или блестящих мешей на объектах с parallax и PBR.
- Заметка: Патчер мешей под parallax и PBR. Понадобится на этапе текстур.

### NIF Preview for MO2 — `opt` [#137741](https://www.nexusmods.com/skyrimspecialedition/mods/137741)
- Фаза 1 · тип `mo2_plugin` · установка `mo2_plugins_folder` · надёжность данных `medium`
- Файл: Вариант под MO2 2.5.2 — «NIF Preview MO2-2.5.2» 0.5.1 (Stormcrown VR). Panda — 0.4.3.
- Установщик: нет установщика: распаковать в <MO2>\plugins и проверить, что не вышло plugins\plugins
- Требует: Mod Organizer 2 (2.5.2)
- Проверка: В окне информации о моде превью .nif показывает 3D-модель.
- Заметка: 3D-превью мешей прямо в окне конфликтов MO2 2.5.x.

## 01 Мастера и USSEP

### Путь A. Обновлённые мастера SSE 1.6.1170 + 4 бесплатных CC — `alt` [ссылка](https://www.nexusmods.com/skyrimspecialedition/articles/6529)
- Также скачать: гайд по мастерам: https://www.nexusmods.com/skyrimspecialedition/articles/6642
- Фаза 1 · тип `guide_steps` · установка `manual_steps` · надёжность данных `medium`
- Файл: Мастера из купленной SE/AE 1.6.1170 (Steam/GOG): Skyrim.esm, Update.esm, Dawnguard.esm, HearthFires.esm, Dragonborn.esm. Плюс 4 бесплатных CC с их BSA: Survival Mode, Saints & Seducers, Rare Curios, Fishing. Точный список файлов — по гайду.
- Установщик: нет установщика: собрать вручную по гайду infernalryan (статья 6642)
- Требует: Skyrim VR ESL Support (#106712); Skyrim VR Strings Fix for Updated SSE Master Files (#176040); USSEP 4.3.x (#266); Survival Mode Prompt Removed (#59049); Skyrim VR Survival Text Removed (#177398); Engine Fixes VR (#62089)
- Не вместе с: Путь B: USSEP 4.2.5b + Skyrim VR USSEP patch (#91475)
- Группа «одно из»: `masters-path`
- Порядок в MO2: Мод «Updated Masters» — первым после раздела инструментов. Ниже — Strings Fix, ещё ниже — USSEP.
- Порядок плагина: Порядок мастеров и CC — по LOOT. CC-плагин Survival Mode оставить включённым.
- Настройки: Идти строго по гайду infernalryan (обновлён 23.07.2026). SkyrimVR.esm остаётся из игры. Часть CC — ESL, поэтому без Skyrim VR ESL Support путь A не работает. Если копии SE/AE нет — выбрать путь B.
- Проверка: В игре есть контент Rare Curios и Fishing, предложения Survival нет, тексты на месте, отмычки поднимаются.
- Заметка: По гайду infernalryan (обновлён 23.07.2026): Skyrim.esm, Update.esm, DLC и CC Survival Mode, Saints & Seducers, Rare Curios, Fishing из SE/AE переносятся в VR отдельным модом.

### USSEP (последний, 4.3.x) — `alt` [#266](https://www.nexusmods.com/skyrimspecialedition/mods/266)
- Фаза 1 · тип `plugin_only` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Основной файл последней версии (4.3.x; в Tempus VR — 4.3.2). Только для пути A.
- Установщик: нет установщика
- Требует: Путь A — обновлённые мастера (base-0); Survival Mode Prompt Removed (#59049)
- Не вместе с: USSEP 4.2.5b и Skyrim VR USSEP patch (путь B, #91475)
- Порядок в MO2: Ниже мода с мастерами и Strings Fix.
- Порядок плагина: Сразу после мастеров и CC, по LOOT.
- Настройки: Предупреждение страницы про SSE 1.6.1130+ закрывают мастера из пути A.
- Проверка: Игра стартует, xEdit не ругается на отсутствующие мастера USSEP.
- Заметка: Только для пути A. Предупреждение на странице о версии SSE 1.6.1130+ закрывают подготовленные по гайду файлы.

### Skyrim VR Strings Fix for Updated SSE Master Files — `alt` [#176040](https://www.nexusmods.com/skyrimspecialedition/mods/176040)
- Фаза 1 · тип `assets_only` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Версия 2.0 поддерживает обновлённые мастера 1.6.1170 и 1.5.97. Проверить, что в архиве есть строки для вашего языка игры.
- Установщик: неизвестно — общие правила
- Требует: Путь A — обновлённые мастера (base-0)
- Не вместе с: Путь B (#91475)
- Порядок в MO2: Ниже мода с обновлёнными мастерами: он перезаписывает ванильные строки VR.
- Проверка: Нет пустых названий и диалогов, отмычки подбираются и не пропадают.
- Заметка: Без него пропадает текст, а отмычки могут не подниматься. Проверьте, что в архиве есть строки для языка, на котором вы играете.

### Survival Mode Prompt Removed (Disable Permanently) — `alt` [#59049](https://www.nexusmods.com/skyrimspecialedition/mods/59049)
- Фаза 1 · тип `plugin_only` · установка `mo2_mod` · надёжность данных `high`
- Файл: Survival Mode - Disable Permanently 1.0.0 (Tempus VR).
- Установщик: нет установщика
- Требует: Путь A — обновлённые мастера (base-0)
- Не вместе с: Путь B (#91475)
- Порядок плагина: CC-плагин Survival Mode оставить включённым: его требует свежий USSEP.
- Проверка: Предложение включить режим выживания не появляется.
- Заметка: Плагин Survival Mode остаётся включённым (его требует свежий USSEP), но режим выживания не предлагается.

### Skyrim VR Survival Text Removed — `alt` [#177398](https://www.nexusmods.com/skyrimspecialedition/mods/177398)
- Фаза 1 · тип `mixed` · установка `mo2_mod` · надёжность данных `low`
- Файл: Основной файл.
- Установщик: неизвестно — общие правила
- Требует: Путь A — обновлённые мастера (base-0)
- Не вместе с: Путь B (#91475)
- Порядок в MO2: Ниже Strings Fix, если правит те же строки.
- Проверка: В карточках предметов нет «SURV=…».
- Заметка: Убирает «SURV=…» из карточек предметов.

### Skyrim VR Fixes for Latest USSEP — `opt` [#177650](https://www.nexusmods.com/skyrimspecialedition/mods/177650)
- Фаза 1 · тип `plugin_only` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Основной файл (ESL-мастер).
- Установщик: неизвестно — общие правила
- Требует: USSEP 4.3.x (#266); Skyrim VR ESL Support (#106712); Skyrim VR Plugin for Bethini Pie (#177465)
- Не вместе с: Путь B (#91475)
- Порядок плагина: Сразу после USSEP.
- Настройки: Ставить, только если в Playroom или в мире видны белые деревья. С Open Shaders и другими шейдерами семейства CS обычно не нужен.
- Проверка: Белых деревьев нет.
- Заметка: Ставить, если видите белые деревья в Playroom или в мире. ESL-мастер сразу после USSEP. С шейдерами семейства CS обычно не нужен — шаг убран из гайда.

### Путь B. USSEP 4.2.5b + Skyrim VR USSEP patch for 4.2.5b — `alt` [#91475](https://www.nexusmods.com/skyrimspecialedition/mods/91475)
- Фаза 1 · тип `plugin_only` · установка `mo2_mod` · надёжность данных `high`
- Файл: USSEP 4.2.5b из Old files страницы 266 (Unofficial Skyrim Special Edition Patch-266-4-2-5b, есть во всех 9 VR-списках). Плюс SkyrimVR USSEP 4.2.5b Compatibility Patch 1.0 (#91475; Stormcrown VR, Panda).
- Установщик: неизвестно — общие правила
- Требует: USSEP 4.2.5b (#266, Old files)
- Не вместе с: Путь A (base-0); USSEP 4.3.x; Skyrim VR Strings Fix (#176040); Skyrim VR Fixes for Latest USSEP (#177650)
- Группа «одно из»: `masters-path`
- Порядок в MO2: USSEP 4.2.5b — сразу после инструментов. Патч совместимости — ниже USSEP.
- Порядок плагина: По LOOT.
- Настройки: Путь для тех, у кого нет SE/AE. Моды, которым нужен свежий USSEP, проверять вручную в xEdit.
- Проверка: Игра стартует, в xEdit нет ошибок мастеров.
- Заметка: Если SE/AE нет. USSEP 4.2.5b берётся из старых файлов страницы 266. Так собран Stormcrown VR (сентябрь 2026). Моды, требующие свежий USSEP, проверять вручную.

### Чистка мастеров в SSEEdit — `rec` [ссылка](https://www.nexusmods.com/skyrimspecialedition/mods/113681)
- Фаза 1 · тип `guide_steps` · установка `manual_steps` · надёжность данных `medium`
- Файл: Своих файлов нет: нужен SSEEdit 4.1.5f.
- Установщик: нет установщика
- Требует: SSEEdit (xEdit) (#164)
- Порядок в MO2: Мод «Cleaned Masters» (из Overwrite) — сразу ниже модов с мастерами и патчем пути A или B, чтобы выигрывал.
- Настройки: Quick Auto Clean по очереди: Update.esm, Dawnguard.esm, HearthFires.esm, Dragonborn.esm (аргументы -tes5vr -qac -autoexit -autoload <файл>). Чистить ту версию, что сейчас выигрывает в MO2, то есть после установки пути A или B. Skyrim.esm и SkyrimVR.esm не трогать. Результат перенести из Overwrite в мод «Cleaned Masters» — так это сделано у Stormcrown VR.
- Проверка: Повторный QAC ничего не находит, DynDOLOD не пишет про удалённые большие референсы.
- Заметка: Quick Auto Clean для Update, Dawnguard, HearthFires, Dragonborn. DynDOLOD потом не ругается на удалённые большие референсы.

## 02 SKSEVR и библиотеки

### SKSEVR — `core` [#30457](https://www.nexusmods.com/skyrimspecialedition/mods/30457)
- Фаза 2 · тип `mixed` · установка `root_builder` · надёжность данных `high`
- Файл: SKSEVR 2.0.12: sksevr_2_00_12.7z с сайта SKSE (Tempus, FUS, Ygg и др.) или файл Nexus #30457 (Stormcrown, Panda). Других версий нет.
- Установщик: нет установщика
- Требует: Root Builder (#31720)
- Не вместе с: SKSE64
- Порядок в MO2: Первый мод, раздел «Инструменты и корень». Скрипты SKSEVR должны выигрывать любые конфликты.
- Настройки: В окне установки MO2 создать папку Root рядом с Data. Перенести туда exe и dll SKSEVR из корня архива: sksevr_loader.exe и sksevr_*.dll. txt и src не нужны. Папку Data со скриптами назначить как <data>. Добавить исполняемый <MO2>\mods\SKSEVR\Root\sksevr_loader.exe — при redirect=true он запускается из папки игры. Игру запускать только так.
- Проверка: Создаётся Documents\My Games\Skyrim VR\SKSE\sksevr.log. Консольная команда GetSKSEVersion возвращает 2.0.12.
- Заметка: Загрузчик и DLL — в корень через Root Builder, скрипты — как обычный мод. Игра запускается только через sksevr_loader.exe.

### VR Address Library for SKSEVR — `core` [#58101](https://www.nexusmods.com/skyrimspecialedition/mods/58101)
- Фаза 2 · тип `assets_only` · установка `mo2_mod` · надёжность данных `high`
- Файл: Последняя версия: Stormcrown — 0.270.0, Yggdrasil VR — 0.275.0 (30.09.2026).
- Установщик: нет установщика
- Требует: SKSEVR (#30457)
- Не вместе с: Address Library for SKSE Plugins (SE/AE, #32444)
- Порядок в MO2: Сразу после SKSEVR.
- Настройки: Обновлять вместе с каждым SKSE-плагином: новые версии плагинов просят новые адреса.
- Проверка: В sksevr.log и логах плагинов нет ошибок про отсутствующие адреса или Address Library.
- Заметка: Обновлять вместе с каждым SKSE-плагином: новые версии плагинов просят новые адреса.

### Engine Fixes VR — `core` [#62089](https://www.nexusmods.com/skyrimspecialedition/mods/62089)
- Фаза 2 · тип `mixed` · установка `root_builder` · надёжность данных `medium`
- Файл: Part 1 — основной файл 7.x: 7.10.0 от 03.10.2026, Stormcrown и Ygg ставят 7.9.0. Part 2 — файл «Part 2 Engine Fixes VR v1.26»/«v1.26a» с той же страницы: Stormcrown ставит его в пару к 7.9.0.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101); Root Builder (#31720)
- Не вместе с: SSE Engine Fixes (#17230); Engine Fixes VR ObjectLOD and Shadow Map Crash Fix (#188237)
- Порядок в MO2: Part 1 — обычный мод в разделе фреймворков. Part 2 — отдельный мод «Engine Fixes VR Part 2», все файлы в Root, раздел «Инструменты и корень».
- Настройки: В конфиге Part 1 (EngineFixes.toml в 7.x), секция [Patches]: MaxStdio = 8192. Страница ESL Support требует MaxStdio — true в старых версиях или 4096 в новых. Отдельный ObjectLOD/Shadow Map fix не ставить: он встроен с 7.4.9, а если стоит — удалить.
- Проверка: В sksevr.log Engine Fixes загружен. В логе ESL Support нет предупреждения про MaxStdio. При неправильно поставленном Part 2 плагин не грузится.
- Заметка: Part 1 — мод, Part 2 — в корень. В EngineFixes.toml поставить MaxStdio = 8192: это требование Skyrim VR ESL Support. Старый отдельный ObjectLOD/Shadow Map fix не ставить — он уже внутри с 7.4.9.

### Skyrim VR ESL Support — `core` [#106712](https://www.nexusmods.com/skyrimspecialedition/mods/106712)
- Фаза 2 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `high`
- Файл: Основной «Skyrim VR ESL» 1.3.2 (Stormcrown, Librum, Ygg). С той же страницы: «PapyrusUtil ESL Patch» 1.1 — ставить обязательно, он есть в 7 VR-списках, включая Stormcrown. «RaceMenu ESL Patch» 1.0 — только для старого RaceMenu VR 0.4.14 (#19080, так в Panda). Со RacemenuVR 0.5 (#156898) VR-списки его не ставят.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101); Engine Fixes VR (#62089)
- Не вместе с: Backported Extended ESL Support
- Порядок в MO2: PapyrusUtil ESL Patch — ниже PapyrusUtil VR, чтобы его перезаписать.
- Настройки: Работает только с официальным SKSEVR 2.0.12. Нужен MaxStdio в Engine Fixes VR. Ставить до запуска xEdit, LOOT и DynDOLOD. После включения ESL лучше начать новую игру.
- Проверка: В логе ESL Support (Documents\My Games\Skyrim VR\SKSE) нет предупреждения про MaxStdio. ESL-плагины (например, CC пути A) работают в игре.
- Заметка: ESL и ESPFE в VR, включая расширенный диапазон 1.6.1130. Работает только с официальным SKSEVR 2.0.12. Должен стоять до запуска DynDOLOD.

### Crash Logger SSE AE VR — `core` [#59818](https://www.nexusmods.com/skyrimspecialedition/mods/59818)
- Фаза 2 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `high`
- Файл: CrashLogger 1.25.0 — универсальный файл (Stormcrown, Ygg). Опционально с той же страницы «Skyrim PDBs» 2026.08.23 — для имён функций в логах.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Не вместе с: Другие логгеры вылетов (Trainwreck и т. п.)
- Проверка: При вылете в Documents\My Games\Skyrim VR\SKSE появляется crash-*.log.
- Заметка: Логи вылетов. Без него конфликт в 300 модах не найти.

### Skyrim VR Tools — `core` [#27782](https://www.nexusmods.com/skyrimspecialedition/mods/27782)
- Фаза 2 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `high`
- Файл: SkyrimVRTools 2.3 BETA — единственный файл, во всех VR-списках.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457)
- Проверка: В sksevr.log SkyrimVRTools загружен. VR Climbing и Spellsiphon работают.
- Заметка: Основа для многих VR-модов: VR Climbing, Spellsiphon и других.

### PapyrusUtil VR — `core` [#13048](https://www.nexusmods.com/skyrimspecialedition/mods/13048)
- Фаза 2 · тип `mixed` · установка `mo2_mod` · надёжность данных `high`
- Файл: Файл «PapyrusUtil VR - Scripting Utility Functions» 3.6b — во всех VR-списках. AE/SE-файлы не брать.
- Установщик: нет установщика
- Требует: SKSEVR (#30457); PapyrusUtil ESL Patch (со страницы #106712)
- Не вместе с: PapyrusUtil AE SE
- Порядок в MO2: PapyrusUtil ESL Patch — ниже, перезаписывает.
- Проверка: В sksevr.log PapyrusUtil загружен. Моды на нём работают.
- Заметка: Файл с пометкой VR.

### JContainers VR — `core` [#16495](https://www.nexusmods.com/skyrimspecialedition/mods/16495)
- Фаза 2 · тип `mixed` · установка `mo2_mod` · надёжность данных `high`
- Файл: Файл «JContainers VR», новейший 4.3.x (Ygg — 4.3.2, 09.2026). Stormcrown, Panda, Tempus, FUS — 4.2.11. JContainers SE не брать.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457)
- Не вместе с: JContainers SE
- Проверка: В sksevr.log JContainers загружен без ошибок.
- Заметка: Файл с пометкой VR.

### powerofthree's Papyrus Extender + Papyrus Extender VR — `core` [#22854](https://www.nexusmods.com/skyrimspecialedition/mods/22854)
- Также скачать: VR-DLL: https://www.nexusmods.com/skyrimspecialedition/mods/58296
- Фаза 2 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `high`
- Файл: Основной Papyrus Extender (скрипты) и Papyrus Extender VR (#58296) одной версии. Stormcrown и Ygg ставят обе 6.5.2.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Порядок в MO2: Мод с VR-DLL — ниже основного, его DLL выигрывает. SE/AE-DLL основного мода можно скрыть.
- Настройки: Обновлять обе части вместе, до одной версии.
- Проверка: В sksevr.log po3_PapyrusExtender загружен, версия совпадает с VR-файлом.
- Заметка: Сначала основной мод, поверх DLL со страницы VR.

### powerofthree's Tweaks + po3 Tweaks VR — `core` [#51073](https://www.nexusmods.com/skyrimspecialedition/mods/51073)
- Также скачать: VR-DLL: https://www.nexusmods.com/skyrimspecialedition/mods/59510
- Фаза 2 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `high`
- Файл: Основной po3 Tweaks (INI) и po3 Tweaks VR (#59510) одной версии. Stormcrown, Panda, Librum, Tempus — 1.15.1 + VR 1.15.1.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Порядок в MO2: VR-мод ниже основного: DLL берётся из VR, INI — из основного.
- Настройки: Твики включать в po3_Tweaks.ini основного мода.
- Проверка: В sksevr.log po3_Tweaks загружен.
- Заметка: INI из основного мода, DLL из VR-версии.

### Spell Perk Item Distributor VR — `core` [#59121](https://www.nexusmods.com/skyrimspecialedition/mods/59121)
- Фаза 2 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `high`
- Файл: Spell Perk Item Distributor VR 7.3.0 — отдельная страница (Stormcrown, Ygg).
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Не вместе с: Spell Perk Item Distributor SE/AE (#36869)
- Проверка: Лог SPID в Documents\My Games\Skyrim VR\SKSE без ошибок, правила *_DISTR.ini применяются.

### Keyword Item Distributor — `core` [#55728](https://www.nexusmods.com/skyrimspecialedition/mods/55728)
- Фаза 2 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `high`
- Файл: Файл «Keyword Item Distributor (VR)» 4.1.0 со страницы 55728 (Stormcrown, Ygg). Старые VR-списки ставили универсальный 3.4.0.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Проверка: Лог KID без ошибок, правила *_KID.ini применяются.

### Base Object Swapper VR — `core` [#61734](https://www.nexusmods.com/skyrimspecialedition/mods/61734)
- Фаза 2 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `high`
- Файл: Base Object Swapper VR 3.4.1 — отдельная страница (Stormcrown, Panda, Librum, FUS, Ygg).
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Не вместе с: Base Object Swapper SE/AE (#60805)
- Проверка: Лог BOS без ошибок, замены *_SWAP.ini видны в мире.

### SkyPatcher — `core` [#106659](https://www.nexusmods.com/skyrimspecialedition/mods/106659)
- Фаза 2 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `high`
- Файл: Файл «SkyPatcher - VR» 7.1.0 (Stormcrown). Panda — 5.0.3, Tempus — 6.3.1.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Проверка: Лог SkyPatcher без ошибок, INI-патчи применяются.

### MCM Helper — `core` [#53000](https://www.nexusmods.com/skyrimspecialedition/mods/53000)
- Фаза 2 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `high`
- Файл: Основной универсальный файл последней версии (Stormcrown — 1.6.2, Ygg — 1.6.3). Старый «MCM Helper VR» 1.4.0 не брать.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101); SkyUI VR (#91535)
- Проверка: MCM модов на MCM Helper открываются, настройки сохраняются.

### SkyUI VR — `core` [#91535](https://www.nexusmods.com/skyrimspecialedition/mods/91535)
- Фаза 2 · тип `mixed` · установка `mo2_mod` · надёжность данных `high`
- Файл: SkyUI VR 1.2.2 с Nexus #91535 (Stormcrown, Panda, FUS, Ygg). Старую GitHub-бету SkyUI-VR v1.0-beta не брать.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457)
- Не вместе с: SkyUI (SE)
- Проверка: В меню паузы есть «Настройки модов» (MCM).
- Заметка: Меню настроек модов (MCM) в VR.

### Container Distribution Framework + VR — `rec` [#120152](https://www.nexusmods.com/skyrimspecialedition/mods/120152)
- Также скачать: VR-DLL: https://www.nexusmods.com/skyrimspecialedition/mods/139051
- Фаза 2 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `high`
- Файл: Основной CDF 3.0.2 и Container Distribution Framework VR 3.0.2 (#139051). Stormcrown и Ygg ставят пару.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Порядок в MO2: VR-мод ниже основного, его DLL выигрывает.
- Проверка: В sksevr.log CDF загружен, конфиги распределения в контейнерах срабатывают.

### FormList Manipulator — `rec` [#74037](https://www.nexusmods.com/skyrimspecialedition/mods/74037)
- Фаза 2 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `high`
- Файл: FormList Manipulator - FLM 1.8.1 — общий файл (Tempus, Stormcrown, Panda, Librum).
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Проверка: В sksevr.log FLM загружен.

### Description Framework — `rec` [#105799](https://www.nexusmods.com/skyrimspecialedition/mods/105799)
- Фаза 2 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: 2.1.2 (Stormcrown, Tempus) или 3.0.0 (Yggdrasil VR, 28.09.2026). Опционально «Description Framework User INI settings» (Tahrovin).
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101); SkyUI VR (#91535)
- Проверка: В карточках предметов видны описания из *_DESC.ini.

### Inventory Interface Information Injector — `rec` [#85702](https://www.nexusmods.com/skyrimspecialedition/mods/85702)
- Фаза 2 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `high`
- Файл: Файл «Inventory Interface Information Injector (VR)» 1.1.0 (Tempus, Stormcrown, Panda, Tahrovin). SE-файл не брать.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101); SkyUI VR (#91535)
- Не вместе с: I5 — Information Injector Improved (ui-192976)
- Группа «одно из»: `item-info`
- Порядок в MO2: Иконочные паки и патчи I4 — ниже I4.
- Проверка: В инвентаре SkyUI VR у предметов появились иконки I4.

### Sound Record Distributor — `rec` [#77815](https://www.nexusmods.com/skyrimspecialedition/mods/77815)
- Фаза 2 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `high`
- Файл: Sound Record Distributor 1.5.4 — общий файл (Stormcrown). Tempus и Panda — 1.5.0, Librum — 1.5.3.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Проверка: В sksevr.log SRD загружен, звуки модов раздела «Звук» играют.
- Заметка: Нужен звуковым модам из раздела «Звук».

### ConsoleUtilVR — `rec` [#47189](https://www.nexusmods.com/skyrimspecialedition/mods/47189)
- Фаза 2 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `high`
- Файл: ConsoleUtilVR 1.3 — единственный файл (6 VR-списков).
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457)
- Не вместе с: ConsoleUtilSSE
- Проверка: В sksevr.log ConsoleUtilVR загружен. Моды, вызывающие консольные команды, работают.

### SKSE Menu Framework + ImGui VR Helper — `rec` [#120352](https://www.nexusmods.com/skyrimspecialedition/mods/120352)
- Также скачать: ImGui VR Helper: https://www.nexusmods.com/skyrimspecialedition/mods/183466
- Фаза 2 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `high`
- Файл: SKSE Menu Framework 3.18 (Stormcrown) и ImGui VR Helper (#183466): 1.9.4 в Ygg, 1.9.3 в Stormcrown.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Порядок в MO2: ImGui VR Helper — ниже SKSE Menu Framework.
- Проверка: Меню Open Shaders и MCM Memory открывается и управляется в шлеме.
- Заметка: Меню Open Shaders и других ImGui-модов прямо в шлеме, без снятия гарнитуры.

### MFG Fix NG — `rec` [#133568](https://www.nexusmods.com/skyrimspecialedition/mods/133568)
- Фаза 2 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `high`
- Файл: MfgFix NG последней версии (Tempus VR — 1.0.4, Panda — 1.0.3).
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Не вместе с: MfgFix-vr 1.0 (старый)
- Проверка: У NPC при разговоре двигаются губы и меняется мимика.
- Заметка: Мимика и липсинк. Требование SkyrimNet. Старый MfgFix-vr 1.0 вместе не ставить.

### Skyrim VR Refocused — `rec` [#32737](https://www.nexusmods.com/skyrimspecialedition/mods/32737)
- Фаза 2 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `high`
- Файл: Skyrim VR Refocused 1.0.2 — единственный файл (5 VR-списков).
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457)
- Настройки: Ищет окно с заголовком «Skyrim VR» — не переименовывать окно игры.
- Проверка: Моды, эмулирующие нажатия, срабатывают, даже если фокус был на другом окне.
- Заметка: Возвращает фокус окну игры. Нужен модам, которые эмулируют нажатия. Ищет окно с заголовком «Skyrim VR».

### Scaleform Translation Plus Plus VR — `rec` [#60210](https://www.nexusmods.com/skyrimspecialedition/mods/60210)
- Фаза 2 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `high`
- Файл: ScaleformTranslationPP VR 1.4.1 (Tempus, Panda, Tahrovin, Ygg).
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); SkyUI VR (#91535)
- Проверка: В MCM на русском нет сырых ключей $KEY.
- Заметка: Для игры на русском: вложенные переводы SkyUI и запасной английский, в MCM не будет сырых $KEY. Стоит в 4 VR-сборках.

### UIExtensions — `opt` [#17561](https://www.nexusmods.com/skyrimspecialedition/mods/17561)
- Фаза 2 · тип `mixed` · установка `mo2_mod` · надёжность данных `high`
- Файл: UIExtensions 1.2.0 (5 VR-списков).
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457)
- Настройки: Ставить, только когда его потребует мод.
- Проверка: Меню мода-потребителя открывается.
- Заметка: Библиотека меню, без DLL. Ставить, когда её потребует мод.

### Object Categorization Framework — `opt` [#81469](https://www.nexusmods.com/skyrimspecialedition/mods/81469)
- Фаза 2 · тип `plugin_only` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Object Categorization Framework 6.1.0 (Stormcrown). Tempus — 6.0.2.
- Установщик: неизвестно — общие правила
- Требует: Keyword Item Distributor (#55728)
- Настройки: Своей DLL нет. Иконки показываются через I4.
- Проверка: Предметы получили ключевые слова OCF, в I4 видны иконки категорий.
- Заметка: Разметка предметов через KID для сортировки и иконок I4.

### Dynamic String Distributor — `opt` [#107676](https://www.nexusmods.com/skyrimspecialedition/mods/107676)
- Фаза 2 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Dynamic String Distributor 1.3.1 (Panda). Tempus — 1.2.5.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Настройки: Один и тот же текст править в одном месте: либо DSD, либо ESP-перевод.
- Проверка: В sksevr.log DSD загружен, тексты из JSON заменены в игре.
- Заметка: Правит тексты на лету по JSON — удобно для русификации без ESP-переводов. VR-пресет в исходниках.

### MCM Unlocked — `opt` [#180186](https://www.nexusmods.com/skyrimspecialedition/mods/180186)
- Фаза 2 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: MCM Unlocked 2.1.6 (Stormcrown VR).
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101); SkyUI VR (#91535)
- Не вместе с: MCM super SEEDED; Menu Maid 2
- Проверка: Видны все MCM, даже если их больше 128.
- Заметка: Снимает лимит SkyUI в 128 MCM и ускоряет меню. VR заявлен, стоит в Stormcrown VR. Метка AI-Generated.

### Dynamic Leveled Lists + Dynamic Container Loot — `opt` [#172083](https://www.nexusmods.com/skyrimspecialedition/mods/172083)
- Также скачать: DCL: https://www.nexusmods.com/skyrimspecialedition/mods/172018
- Фаза 2 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: VR-файлы: «Dynamic Leveled Lists VR (SKSE)» 0.4.3a и «Dynamic Container Loot VR (SKSE)» 0.4a (#172018), так в Panda. Если на странице один файл с установщиком — выбрать VR. Предпочесть 0.5.2+: в ней исправлены вылеты.
- Установщик: Если установщик есть — выбрать вариант VR (сниппет: «choose Skyrim 1.5.97, 1.6.x, 1.7.104 or VR»). Иначе — VR-файл.
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Настройки: Те же левел-листы не сливать ещё и в Bashed Patch или Synthesis-патчере.
- Проверка: В sksevr.log обе DLL загружены, лут из нескольких модов смешивается.
- Заметка: Сливает конфликтующие левел-листы прямо в игре. В установщике выбрать VR. Те же списки не сливать ещё и Bashed Patch.

## 03 Фиксы движка

### Poached Bugs VR — `core` [#107053](https://www.nexusmods.com/skyrimspecialedition/mods/107053)
- Фаза 2 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `high`
- Файл: Main: «Poached Bugs VR Core File» последней версии (0.6.0 — так в Stormcrown VR, Librum VR, Yggdrasil VR). Отдельным модом — «Simonrim Choice Config» той же версии (0.6.0), потому что в сборке Adamant и Mysticism (SimonRim). Версии Core и Simonrim Config должны совпадать.
- Установщик: нет установщика (по именам архивов — два отдельных файла: Core и Simonrim Choice Config); точную структуру проверить при установке
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Не вместе с: Scrambled Bugs (SE/AE, в VR не работает)
- Порядок в MO2: Simonrim Choice Config — сразу НИЖЕ Core (должен перезаписать его конфиг). Оба — в разделе «03 Фиксы движка», после Engine Fixes VR.
- Настройки: Фиксы включены по умолчанию — не трогать. Твики оставить по умолчанию; Simonrim Choice Config сам выставляет значения под Adamant/Mysticism. Имя конфига не придумывать — смотреть в архиве.
- Проверка: В sksevr.log DLL Poached Bugs загружена без ошибки. В MO2 на вкладке конфликтов Simonrim Config побеждает Core.
- Заметка: Порт фиксов Scrambled Bugs (сам Scrambled Bugs в VR не работает). Файл Simonrim Choice Config — если ставите моды SimonRim.

### Papyrus Tweaks NG — `core` [#77779](https://www.nexusmods.com/skyrimspecialedition/mods/77779)
- Фаза 2 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `high`
- Файл: Main: «Papyrus Tweaks» последней версии (4.2.1 — Yggdrasil VR, 2026-09; 4.1.1 — Stormcrown VR). Файл «INI file for reference» — не ставить, это образец INI.
- Установщик: нет установщика (по именам архивов); проверить структуру при установке
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Порядок в MO2: Раздел «03 Фиксы движка». Конфликтов файлов не ожидается.
- Настройки: INI по умолчанию. Не включать экспериментальные/рискованные опции без причины.
- Проверка: В sksevr.log DLL Papyrus Tweaks загружена без ошибки. В Papyrus-логе нет ошибок от неё.

### Skyrim freeze fix NG — `rec` [#160704](https://www.nexusmods.com/skyrimspecialedition/mods/160704)
- Фаза 2 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Main: «skyrim-freeze-fix» последней версии (0.0.5 — Stormcrown VR, 2026-08; 0.0.3 — Tempus Maledictum VR). Отдельного VR-файла нет.
- Установщик: нет установщика (по именам архивов)
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Порядок в MO2: Раздел «03 Фиксы движка».
- Проверка: Обязательно: в sksevr.log DLL загружена, нет «incompatible»/«failed». Если не грузится — удалить мод (в описании заявлены только SE и AE).

### Disabled Reference Integrity Fix (VR) — `rec` [#175062](https://www.nexusmods.com/skyrimspecialedition/mods/175062)
- Фаза 2 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `high`
- Файл: Брать VR-файл: «Disabled Reference Integrity Fix VR (SKSE)» (1.5.0 — Stormcrown VR, 2026-09). Файл «…AE (SKSE)» не брать.
- Установщик: нет установщика (по именам архивов)
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Порядок в MO2: Раздел «03 Фиксы движка».
- Настройки: Настраивается (по описанию «Highly configurable»). Оставить по умолчанию.
- Проверка: В sksevr.log VR-DLL загружена. Если у мода есть лог — проверить, что при загрузке ячеек он сканирует их без ошибок.

### Block Condition Freeze CTD Fix — `rec` [#193168](https://www.nexusmods.com/skyrimspecialedition/mods/193168)
- Фаза 2 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `low`
- Файл: Main: «Block Condition Freeze CTD Fix» 1.0 (так в Yggdrasil VR, 2026-09-26). Отдельного VR-файла не видно.
- Установщик: нет установщика (по имени архива; «SKSE and no esp»)
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Порядок в MO2: Раздел «03 Фиксы движка».
- Проверка: Обязательно: в sksevr.log DLL загружена без ошибки. Проверить блок щитом/оружием в бою (PLANCK/HIGGS): нет фризов, блок работает. Если DLL не грузится — удалить.
- Заметка: Свежий, сентябрь 2026.

### NPC AI Process Position Fix NG — `rec` [#69326](https://www.nexusmods.com/skyrimspecialedition/mods/69326)
- Фаза 2 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `high`
- Файл: Main: «NPC AI Process Position Fix - NG» последней версии (1.1.3 — Stormcrown VR, 2026-08; 1.1.1 — Yggdrasil VR, Panda's). Одна DLL на SE/AE/VR.
- Установщик: нет установщика (по именам архивов)
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Не вместе с: Старая не-NG версия NPC AI Process Position Fix
- Порядок в MO2: Раздел «03 Фиксы движка».
- Проверка: В sksevr.log DLL загружена без ошибки.

### Animated Static Reload Fix NG — `rec` [#69331](https://www.nexusmods.com/skyrimspecialedition/mods/69331)
- Фаза 2 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `high`
- Файл: Main: «Animated Static Reload Fix - NG» последней версии (1.0.4 — Stormcrown VR, Yggdrasil VR). Одна DLL на SE/AE/VR.
- Установщик: нет установщика (по именам архивов)
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Не вместе с: Старая не-NG версия Animated Static Reload Fix
- Порядок в MO2: Раздел «03 Фиксы движка».
- Проверка: В sksevr.log DLL загружена без ошибки.

### Stagger Effect Fix — `rec` [#110508](https://www.nexusmods.com/skyrimspecialedition/mods/110508)
- Фаза 2 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `high`
- Файл: Main: «Stagger Effect Fix» последней версии (1.0.4 — Stormcrown VR, Yggdrasil VR).
- Установщик: нет установщика (по именам архивов)
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Порядок в MO2: Раздел «03 Фиксы движка».
- Проверка: В sksevr.log DLL загружена. В игре: шокирующая магия/крик отталкивает цель от заклинателя, а не к нему.

### Animation Queue Fix — `rec` [#82395](https://www.nexusmods.com/skyrimspecialedition/mods/82395)
- Фаза 2 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `high`
- Файл: Main: «Animation Queue Fix» последней версии (1.0.2 — Yggdrasil VR, 2026-08; 1.0.1 — ещё 6 VR-списков).
- Установщик: нет установщика (по именам архивов)
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Порядок в MO2: Раздел «03 Фиксы движка».
- Проверка: В sksevr.log DLL загружена без ошибки. В людных местах (Вайтран) нет застывших NPC в T-позе.

### Seamless Saving VR — `rec` [#174106](https://www.nexusmods.com/skyrimspecialedition/mods/174106)
- Фаза 2 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `high`
- Файл: Main: «SeamlessSaving» v1.0.7 (Stormcrown VR, Librum VR, Tempus VR). Мод только для VR.
- Установщик: нет установщика (по именам архивов)
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Порядок в MO2: Раздел «03 Фиксы движка».
- Проверка: В sksevr.log DLL загружена. Автосейв и быстрое сохранение проходят без заметного фриза. Сохранение затем загружается (проверить 2–3 раза).
- Заметка: Ускоряет сохранение — меньше подвисаний на автосейвах.

### Faster Decompression — `rec` [#174643](https://www.nexusmods.com/skyrimspecialedition/mods/174643)
- Фаза 2 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Main: «Fast Decompress» последней версии (1.4.2 — Stormcrown VR, 2026-09). Универсальная DLL для AE и VR.
- Установщик: нет установщика (по именам архивов)
- Требует: SKSEVR (#30457)
- Порядок в MO2: Раздел «03 Фиксы движка».
- Проверка: В sksevr.log DLL загружена без ошибки. Нужна ли VR Address Library, сверить со вкладкой Requirements; если в логе ошибка адресов — поставить/обновить её.

### Disk Cache Enabler — `rec` [#100975](https://www.nexusmods.com/skyrimspecialedition/mods/100975)
- Фаза 2 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Для VR брать вариант «Universal» (DiskCacheEnabler-Universal; так в Librum VR, Spirit of Grit, Tahrovin, Grit). Вариант «Main» по цитате описания — memory patch для AE. Файл «1.2» стоит в FUS/Stormcrown/Yggdrasil/Panda's/Tempus — брать его, только если в описании файла на вкладке Files прямо указан VR/universal.
- Установщик: нет установщика (по именам архивов)
- Требует: SKSEVR (#30457)
- Порядок в MO2: Раздел «03 Фиксы движка». Проверить структуру архива: DLL должна оказаться в Data/SKSE/Plugins.
- Проверка: В sksevr.log DLL загружена без ошибки.

### PrivateProfileRedirector — `rec` [#18860](https://www.nexusmods.com/skyrimspecialedition/mods/18860)
- Фаза 2 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `high`
- Файл: Только VR-файл: «PrivateProfileRedirector VR 0.6.2 (Runtime 1.4.15)» (так во всех 5 VR-списках: Stormcrown, Panda's, Tahrovin, FUS, Yggdrasil). Не брать SE-файлы 0.5.x/0.6.x.
- Установщик: нет установщика (по именам архивов). Если в архиве верхний уровень — папка Data, MO2 возьмёт её как корень мода
- Требует: SKSEVR (#30457)
- Не вместе с: PrivateProfileRedirector 0.5.x и старее (зависание на старте с шейдерами семейства CS)
- Порядок в MO2: Раздел «03 Фиксы движка». DLL и INI — в Data/SKSE/Plugins.
- Настройки: PrivateProfileRedirector.ini — по умолчанию.
- Проверка: В sksevr.log DLL загружена. Игра стартует быстрее. Open Shaders создаёт свой JSON нормально, на старте нет зависания.
- Заметка: Быстрее старт игры.

### Skyrim Priority SE AE VR — `rec` [#50129](https://www.nexusmods.com/skyrimspecialedition/mods/50129)
- Фаза 2 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Main: «Skyrim Priority SE AE» 3.4.0 (так в Stormcrown VR, Tempus VR, Panda's). Отдельного VR-файла нет.
- Установщик: нет установщика (по именам архивов)
- Требует: SKSEVR (#30457)
- Не вместе с: Другие моды и утилиты, меняющие приоритет процесса (Fallrim Priority / PriorityMod) — оставить один
- Порядок в MO2: Раздел «03 Фиксы движка».
- Настройки: По умолчанию. Не ставить Realtime-приоритет.
- Проверка: В sksevr.log DLL загружена. В диспетчере задач у SkyrimVR.exe приоритет «Высокий».

### SCROTE — Simply Optimized Scripts — `rec` [#97155](https://www.nexusmods.com/skyrimspecialedition/mods/97155)
- Фаза 2 · тип `assets_only` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Брать «SCROTE Loose Files Version» последней версии (1.0.3 — Stormcrown VR, 2026-09). BSA-версию не брать: все VR-списки берут Loose Files.
- Установщик: неизвестно — общие правила
- Порядок в MO2: Сразу ниже USSEP (должен перезаписать его скрипты). Ниже SCROTE — моды, которые правят те же скрипты точечно: Dragonactorscript Infinite Loop Fix, CritterSpawn Congestion Fix. Конфликты .pex смотреть на вкладке конфликтов MO2.
- Порядок плагина: Если в версии есть плагин — LOOT, сразу после USSEP.
- Проверка: В MO2 SCROTE побеждает USSEP по общим .pex; Dragonactorscript Fix и CritterSpawn Fix побеждают SCROTE.

### eFPS — Exterior FPS boost + Patch Hub — `rec` [#54907](https://www.nexusmods.com/skyrimspecialedition/mods/54907)
- Также скачать: Patch Hub: https://www.nexusmods.com/skyrimspecialedition/mods/54998
- Фаза 2 · тип `plugin_only` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Main: «eFPS - Exterior FPS boost» 2.4.2. Отдельно «eFPS - Official Patch Hub» 1.7a (страница 54998) — только патчи для установленных модов. Так в Tempus VR, Yggdrasil VR, Stormcrown VR.
- Установщик: неизвестно — общие правила; в Patch Hub отметить только патчи для модов, которые реально стоят (сверить с Lux Orbis, Lux Via, городскими модами)
- Не вместе с: Open Cities; JK's Skyrim и др. моды, перестраивающие города, — без патча из Patch Hub
- Порядок в MO2: Patch Hub — ниже eFPS и ниже модов, которые он патчит.
- Порядок плагина: eFPS — по LOOT. Патчи Patch Hub — ниже eFPS и модов, к которым они.
- Проверка: В xEdit нет конфликтов eFPS с модами городов без патча. В Вайтране и Рифтене нет «дыр» и исчезающих зданий.
- Заметка: Плоскости окклюзии в экстерьерах — меньше объектов в кадре, прямая экономия CPU.

### Lightened Skyrim — BOS edition — `rec` [#111475](https://www.nexusmods.com/skyrimspecialedition/mods/111475)
- Фаза 2 · тип `mixed` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Main: «Lightened Skyrim» на странице 111475 — версия для Base Object Swapper (1.10 — Stormcrown VR). ESP-версию со страницы 50755 вместе с ней не ставить.
- Установщик: неизвестно — общие правила
- Требует: Base Object Swapper VR (#61734)
- Не вместе с: Lightened Skyrim (ESP-версия, #50755)
- Порядок в MO2: Раздел «03 Фиксы движка» (или «Производительность»), ниже Base Object Swapper VR.
- Проверка: В логе Base Object Swapper видны SWAP-файлы Lightened Skyrim. Время кадра в экстерьере (fpsVR) не хуже, чем без мода.
- Заметка: В тестах FUS давал 1–2 мс на кадр.

### Inertia (Floating Gear Fix) — `rec` [#148746](https://www.nexusmods.com/skyrimspecialedition/mods/148746)
- Фаза 2 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Main: «Inertia - Latest Version» (1.1.1 — Yggdrasil VR, 2026-09; 1.1.0 — Stormcrown VR).
- Установщик: нет установщика (по именам архивов)
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Порядок в MO2: Раздел «03 Фиксы движка».
- Настройки: Длительность «инерции» настраивается — оставить по умолчанию.
- Проверка: В sksevr.log DLL загружена. Убить NPC: снаряжение падает вместе с телом, не висит в воздухе.

### Assorted Mesh Fixes — `rec` [#32117](https://www.nexusmods.com/skyrimspecialedition/mods/32117)
- Фаза 2 · тип `assets_only` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Main: «Assorted Mesh Fixes» последней версии (0.144 — Stormcrown VR, 2026-09-26). Файл «parallax shit (unsupported)» — не ставить, пока нет parallax-текстур (решить на этапе текстур).
- Установщик: неизвестно — общие правила
- Порядок в MO2: Рано в разделе фиксов мешей. Выше Unofficial Material Fix и Fixed Mesh Lighting. Более поздние меш-реплейсеры и патчи могут его перезаписывать.
- Порядок плагина: Если есть ESP — по LOOT.
- Проверка: MO2: конфликты с UMF/Fixed Mesh Lighting осознанные (UMF ставить патч для AMF, если есть).

### Unofficial Material Fix — `rec` [#21027](https://www.nexusmods.com/skyrimspecialedition/mods/21027)
- Фаза 2 · тип `assets_only` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Main: «Unofficial Material Fix» 1.18.0 (Stormcrown VR, Panda's).
- Установщик: неизвестно — общие правила. По словам пользователя STEP, сейчас один файл с FOMOD и патчами (Assorted Mesh Fixes, ELFX, SMIM). Отметить патч для Assorted Mesh Fixes, если он есть, и не отмечать патчи для неустановленных модов
- Порядок в MO2: Ниже Assorted Mesh Fixes.
- Проверка: MO2: UMF побеждает AMF по общим мешам (если выбран патч под AMF).

### Skyrim Landscape and Water Fixes — `rec` [#26138](https://www.nexusmods.com/skyrimspecialedition/mods/26138)
- Фаза 2 · тип `mixed` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Main: «Skyrim Landscape and Water Fixes - FOMOD» последней версии (v10.x; Panda's v10.0.2, Tempus v9.9.1A, SE до v10.6).
- Установщик: Есть FOMOD. По гайду STEP (старая версия): основной плагин, патчи (ELFX, Relighting Skyrim, CACO, Landscape Fixes For Grass Mods), Walkway Wall fix, Missing Lights Fix. Отметить патч для Landscape Fixes For Grass Mods (он в сборке), остальные патчи — только для установленных модов. Точные названия опций — читать в установщике
- Порядок в MO2: Ниже Landscape Fixes For Grass Mods (если выбран патч к нему).
- Порядок плагина: По LOOT. Патч к LFfGM — после обоих модов.
- Проверка: В xEdit нет перезаписи ландшафта SLaWF без патча модами ландшафта/городов. У Ривервуда и у рек нет дыр и висящей воды.

### Navigator — Navmesh Fixes — `rec` [#52641](https://www.nexusmods.com/skyrimspecialedition/mods/52641)
- Фаза 2 · тип `plugin_only` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Main: «Navigator - Navmesh Fixes» последней версии (1.8.3 — Stormcrown VR, 2026-07).
- Установщик: Есть FOMOD. По гайду STEP: выбрать All-In-One ESL; патчи (Interesting NPCs, Skyrim Sewers, Sunder and Wraithguard) — только если эти моды стоят. Точные названия — читать в установщике
- Требует: Skyrim VR ESL Support (#106712)
- Порядок плагина: Высоко в порядке загрузки (автор советует, если LOOT не поставил сам). НЕ чистить в xEdit — «грязные» записи намеренные.
- Проверка: Плагин ESL активен (VR ESL Support в sksevr.log работает). В подземельях компаньоны не застревают в дверях.

### Increase Actor Limit for VR — `opt` [#37440](https://www.nexusmods.com/skyrimspecialedition/mods/37440)
- Фаза 2 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Main: «Increase Actor Limit VR» v1.0 (единственный файл, во всех 8 VR-списках).
- Установщик: нет установщика (по имени архива)
- Требует: SKSEVR (#30457)
- Не вместе с: Actor Limit Fix (SE, #32349) — не для VR
- Порядок в MO2: Раздел «03 Фиксы движка».
- Проверка: В sksevr.log DLL загружена. В больших боях/толпах нет NPC, «плывущих» без анимации.

### Save Unbaker VR — `rec` [#86265](https://www.nexusmods.com/skyrimspecialedition/mods/86265)
- Фаза 2 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `high`
- Файл: Main: «Save Unbaker VR» 1.0.4 (Panda's, Tahrovin, Librum VR, Yggdrasil VR). SE-версию 85565 не брать.
- Установщик: нет установщика (по имени архива)
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Не вместе с: Save Unbaker SE/AE (#85565)
- Порядок в MO2: Раздел «03 Фиксы движка».
- Проверка: В sksevr.log DLL загружена без ошибки.
- Заметка: Часть данных берётся из плагинов, а не из сохранения — меньше поломок при смене модов. Во всех крупных VR-сборках 2025–2026.

### Dragonactorscript Infinite Loop Fix — `rec` [#87940](https://www.nexusmods.com/skyrimspecialedition/mods/87940)
- Фаза 2 · тип `assets_only` · установка `mo2_mod` · надёжность данных `high`
- Файл: Main: «Dragonactorscript Infinite Loop Fix - FOMOD» 1.4.2 (Spirit of Grit, Tahrovin-Grit, Yggdrasil VR).
- Установщик: Есть FOMOD с двумя вариантами (по описанию): основной («fail silently» — цикл завершается, когда ячейка дракона выгружена; душу недоступного трупа не получить) и альтернативный («absorb anywhere» — душа поглощается через ~5 минут где угодно; конфликтует с анимацией поглощения у модов вроде Cinematic Dragon Soul Absorption). Брать основной. Отдельной опции «под USSEP» нет: правки USSEP уже включены, USSEP не обязателен. Точные надписи — читать в установщике
- Порядок в MO2: Ниже USSEP, SCROTE и любых модов драконов с dragonactorscript.pex — этот мод должен победить в конфликте.
- Проверка: MO2: dragonactorscript.pex приходит из этого мода (вкладка конфликтов).
- Заметка: Чинит бесконечный цикл в скрипте драконов, который забивает Papyrus. Вариант под USSEP.

### Telekinesis Aim Fix VR — `rec` [#191729](https://www.nexusmods.com/skyrimspecialedition/mods/191729)
- Фаза 2 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Main: «Telekinesis Aim Fix VR», версия «1» (2026-09-13; Yggdrasil VR, Tahrovin-Grit). Мод только для VR.
- Установщик: нет установщика (по имени архива)
- Требует: SKSEVR (#30457)
- Порядок в MO2: Раздел «03 Фиксы движка» или «VR-ядро».
- Проверка: В sksevr.log DLL загружена. Телекинез бросает предмет туда, куда направлена рука. Нужна ли VR Address Library — сверить с Requirements.
- Заметка: Телекинез бросает туда, куда указывает рука. Стоит в Yggdrasil VR и Tahrovin — Grit.

### Collision Sentinel — `opt` [#181445](https://www.nexusmods.com/skyrimspecialedition/mods/181445)
- Фаза 2 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Main: «CollisionSentinel» последней версии (2.1.0 — Spirit of Grit, Tahrovin-Grit, 2026-07).
- Установщик: нет установщика (по имени архива)
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Порядок в MO2: Раздел «03 Фиксы движка».
- Настройки: По умолчанию. Свой лог с виновником (NIF, FormID) — читать при вылетах.
- Проверка: В sksevr.log DLL загружена. Проверить, что в EngineFixes.toml защита Havok-материалов и Collision Sentinel не дают двойных срабатываний. Пройти мост у Ивастеда (жалоба на зависание вместе с Water Collision Crash Fix).
- Заметка: Защищает от вылетов из-за битой коллизии в модовых мешах и пишет виновника в лог. VR 1.4.15 в списке поддержки, стоит в Grit-сборках. Метка AI-Generated.

### Recursion Monitor — `opt` [#76867](https://www.nexusmods.com/skyrimspecialedition/mods/76867)
- Фаза 2 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `high`
- Файл: Main: «Recursion Fix» 1.2 (единственный файл; 5 VR-списков).
- Установщик: нет установщика (по имени архива)
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Порядок в MO2: Раздел «03 Фиксы движка».
- Проверка: В sksevr.log DLL загружена без ошибки.
- Заметка: Обрывает зацикленную Papyrus-рекурсию до того, как она обрушит FPS.

### Combat Music Fix NG — `opt` [#110459](https://www.nexusmods.com/skyrimspecialedition/mods/110459)
- Фаза 2 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Main: «Combat Music Fix NG» 2.0.0 (Stormcrown VR, 2026-09). Вариант «Only At Save Load» не брать (он только в SE-списке Nordic Souls PBR).
- Установщик: нет установщика (по именам архивов)
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Не вместе с: Combat Music Fix (старый, dTry, #67015); Старые ESP-фиксы боевой музыки
- Порядок в MO2: Раздел «03 Фиксы движка».
- Проверка: Обязательно: в sksevr.log DLL загружена без ошибки (VR-файла нет). Сохранения загружаются без вылета: есть жалоба SE-пользователя на вылет при загрузке. После боя музыка стихает.
- Заметка: Боевая музыка выключается после боя. Проверить загрузку в sksevr.log.

### Fixed Mesh Lighting — `opt` [#53653](https://www.nexusmods.com/skyrimspecialedition/mods/53653)
- Фаза 2 · тип `assets_only` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Main: «Fixed Mesh Lighting» 1.9.1 (Librum VR, FUS).
- Установщик: неизвестно — общие правила. В описании «Patches for popular mods included» — отметить патчи только для установленных модов
- Порядок в MO2: Ниже Assorted Mesh Fixes и Unofficial Material Fix. Конфликты мешей смотреть в MO2.
- Проверка: MO2: конфликты с AMF/UMF осознанные. Днём в тени предметы не светятся.
- Заметка: Предметы перестают светиться в темноте.

### Aurora Fix + Sky Reflection Fix — `opt` [#77834](https://www.nexusmods.com/skyrimspecialedition/mods/77834)
- Также скачать: Sky Reflection Fix: https://www.nexusmods.com/skyrimspecialedition/mods/110604
- Фаза 2 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Два мода: «Aurora Fix» 1.0.1 (77834) и «Sky Reflection Fix» 1.0.1 (110604). Отдельных VR-файлов нет.
- Установщик: нет установщика (по именам архивов)
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Порядок в MO2: Раздел «03 Фиксы движка». Ставить как два отдельных мода.
- Проверка: В sksevr.log загружены обе DLL. После Апокрифа/Солстейма в небе Скайрима нет чужого сияния. Отражения неба в воде не съезжают при поворотах головы.
- Заметка: Сияние не застревает при смене мира; отражение неба привязано к камере — вода и кубмапы отражают правильно. Обе DLL общие для SE/AE/VR.

### Water Effects Brightness and Reflection Fix — `opt` [#63862](https://www.nexusmods.com/skyrimspecialedition/mods/63862)
- Фаза 2 · тип `assets_only` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Main: «Water Effects Brightness and Reflection Fix» 0.5 (FUS, Panda's, Tempus).
- Установщик: неизвестно — общие правила
- Порядок в MO2: Выше Splashes of Skyrim / Splashes of Storms и водного мода (Simplicity of Sea). Где они пересекаются по мешам, должны побеждать они. Решить по вкладке конфликтов MO2.
- Проверка: MO2: проверить конфликты с водными модами. Ночью пена и водопады не светятся неоном.
- Заметка: Убирает пересвеченные брызги, пену и водопады.

### Unaggressive Dragon Priests Fix + Dwemer Gates Don't Reset — `opt` [#69026](https://www.nexusmods.com/skyrimspecialedition/mods/69026)
- Также скачать: Dwemer Gates: https://www.nexusmods.com/skyrimspecialedition/mods/26331
- Фаза 2 · тип `plugin_only` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Два мода. 1) «Unaggressive Dragon Priests Fix» 1.3.1 (FUS, Librum, Panda's, Tempus); патчи Beyond Reach / Wyrmstooth — только если стоят эти моды. 2) «Dwemer Gates Don't Reset» 1.3.7 (Tempus).
- Установщик: Dwemer Gates Don't Reset: по описанию есть версии «Dwemer-only» и «complete» и форматы .esl / ESM / ESP-FE / ESP. Брать «complete» в формате ESP-FE или ESL (VR ESL Support стоит). Точные надписи — читать в установщике/файлах. Unaggressive Dragon Priests Fix — неизвестно — общие правила
- Требует: USSEP (#266) — для Dwemer Gates Don't Reset; Skyrim VR ESL Support (#106712) — если выбран ESL/ESP-FE
- Порядок плагина: Оба — после USSEP (LOOT).
- Проверка: В xEdit Dwemer Gates видит USSEP мастером. В Блэкрич/Мзинчалефт ворота остаются открытыми после сброса ячейки; жрецы-драконы атакуют сразу.
- Заметка: Два мелких фикса логики, которых нет в USSEP.

### CritterSpawn Congestion Fix — `opt` [#67276](https://www.nexusmods.com/skyrimspecialedition/mods/67276)
- Фаза 2 · тип `mixed` · установка `mo2_mod` · надёжность данных `low`
- Файл: Main: «CritterSpawn Congestion Fix» 1.54 (Panda's Sovngarde).
- Установщик: неизвестно — общие правила
- Порядок в MO2: Ниже SCROTE и USSEP. Если MO2 показывает конфликт по скриптам спавна живности — победителем оставить CritterSpawn Congestion Fix (это его единственная цель).
- Порядок плагина: Если есть ESP — по LOOT, после USSEP.
- Проверка: MO2: скрипт спавна живности приходит из этого мода. В Papyrus-логе нет спама от critter-скриптов.
- Заметка: Снимает затор скриптов спавна бабочек и рыб.

### Unofficial Skyrim Modder's Patch (USMP) — `opt` [#49616](https://www.nexusmods.com/skyrimspecialedition/mods/49616)
- Фаза 2 · тип `mixed` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Версию брать под путь USSEP. Путь A (свежий USSEP 4.3.x) — последняя USMP (2.6.8b, июль 2026). Путь B (USSEP 4.2.5b) — 2.6.6 (Tahrovin так и стоит на 4.2.5b; Tempus — 2.6.2b). «USMP Patch Emporium» (50813) — только при конфликтах с NPC-модами.
- Установщик: неизвестно — общие правила
- Требует: USSEP (#266, путь A) или USSEP 4.2.5b + Skyrim VR USSEP patch (#91475, путь B)
- Порядок в MO2: Ниже USSEP.
- Порядок плагина: Сразу после USSEP и VR-патчей USSEP (LOOT).
- Проверка: В xEdit USMP загружается без ошибок мастеров. Нет перезаписи VR-правок USSEP-патча (сравнить записи в xEdit).
- Заметка: Фиксы поверх USSEP: ассеты, AI-пакеты, навмеши. Версию подбирать под выбранный путь USSEP.

### Saving on Steed — Horse Save Load Fix — `try` [#173629](https://www.nexusmods.com/skyrimspecialedition/mods/173629)
- Фаза 2 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `low`
- Файл: Только 0.1.2 («Saving on Steed - Horse Save Load Fix SKSE»; Librum VR, Panda's). Ветку 0.2.x не брать.
- Установщик: нет установщика (по имени архива)
- Требует: SKSEVR (#30457)
- Не вместе с: Horse Save Load Fix (скриптовый, #132110)
- Порядок в MO2: Раздел «03 Фиксы движка».
- Проверка: Обязательно: в sksevr.log DLL загружена без ошибки (VR автор не заявлял). Сохраниться верхом и загрузиться — лошадь и игрок на месте. Если DLL не грузится — удалить.
- Заметка: Чинит выброс в небо после загрузки сейва верхом. Две VR-сборки ставят 0.1.2, но VR автор не заявлял. Ветку 0.2 не брать.

## 04 Шейдеры и свет

### Open Shaders — `core` [#180419](https://www.nexusmods.com/skyrimspecialedition/mods/180419)
- Фаза 3 · тип `mixed` · установка `mo2_mod` · надёжность данных `high`
- Файл: Main file «Open Shaders» 2.17.0, один архив (Yggdrasil VR: «Open Shaders 180419 2.17.0»). Не брать пре-релизы GitHub (v2.17.0-prNNN, dev-latest) и форк «Open Shaders With DLSS5 Neural Rendering». Отдельные аддоны фич CS (Grass Lighting, Light Limit Fix, Dynamic Cubemaps и т. п.) не ставить: по заметке куратора они уже в архиве.
- Установщик: неизвестно — общие правила. Если установщик предлагает альтернативную DLL (clang-cl), оставить вариант по умолчанию. Фичи включать и выключать в меню игры, а не в установщике.
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Не вместе с: Community Shaders Expanded (CSX) (#166950); Community Shaders 1.7+ (#86492); ENB; Skyrim Upscaler / vrperfkit; Intellightent; Open Shaders With DLSS5 Neural Rendering; ENB Light / Particle Lights for ENB
- Группа «одно из»: `shaders`
- Порядок в MO2: Сепаратор «Open Shaders, Light Placer», ниже фреймворков и фиксов. Сразу под ним поставить отдельный мод «Open Shaders — настройки» с SettingsUser.json. Моды с файлами под CS (Azurite III HDR, Map Weather — CS, Parallax Spell Impacts) — ниже Open Shaders.
- Настройки: Первый запуск долго компилирует шейдеры — не прерывать. Меню открывается клавишей END в окне игры на ПК: виртуальная клавиатура в шлеме его не вызывает. После настройки перенести SKSE\Plugins\CommunityShaders\SettingsUser.json из Overwrite в мод «Open Shaders — настройки». Для параллакса рельефа нужен bLandSpecular=1 в SkyrimVR.ini (по FAQ). Апскейл DLSS/DLAA/FSR — только встроенный. После смены фич очистить Overwrite от кэша шейдеров.
- Проверка: В sksevr.log DLL Open Shaders загружена без ошибки версии (внутреннее имя осталось CommunityShaders). Есть лог My Games\Skyrim VR\SKSE\CommunityShaders.log без ошибок. END в окне ПК открывает меню.
- Заметка: Форк Community Shaders от alandtse, всё в одном архиве: DLSS/DLAA/FSR для VR, фовеальный рендеринг, Skylighting, Light Limit Fix, Grass Lighting, Dynamic Cubemaps, тени облаков и рельефа, Wetness. Ставится вместо CS: те же файлы и папка настроек. Так собран Yggdrasil VR.

### Community Shaders Expanded (CSX), VR-сборка — `alt` [#166950](https://www.nexusmods.com/skyrimspecialedition/mods/166950)
- Фаза 3 · тип `mixed` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Main «Community Shaders Expanded (CSX)» csx3.19.1-VR (Stormcrown VR, 2026-09-23) плюс ОДИН пресет: «CSX Balanced Preset», «CSX Perform. Preset» или «CSX Quality Preset» (- Press END On PC To Customize). Старую линейку «Community Shaders Particle Lights VR» (PL3.x) с той же страницы не брать.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Не вместе с: Open Shaders (#180419); Community Shaders 1.7+ (#86492); ENB
- Группа «одно из»: `shaders`
- Порядок в MO2: Встаёт вместо Open Shaders в том же сепараторе. Пресет — ниже основного архива CSX.
- Настройки: Пресет — это стартовые настройки, донастраивать клавишей END на ПК. В CSX работают Particle Lights: ENB Particle Lights-моды допустимы только с CSX. Не вешать на одни и те же объекты свет и частицами, и конфигами Light Placer — свет удвоится.
- Проверка: В sksevr.log DLL загружена. Есть лог CommunityShaders.log. END открывает меню CSX.
- Заметка: Альтернатива Open Shaders: вернул Particle Lights и Screen Space Shadows в VR, упор на стабильность. Так собраны Stormcrown VR и MGO 4.0.

### Light Placer + Light Placer VR — `core` [#127557](https://www.nexusmods.com/skyrimspecialedition/mods/127557)
- Также скачать: VR-DLL: https://www.nexusmods.com/skyrimspecialedition/mods/135822
- Фаза 3 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `high`
- Файл: Основной 127557 и VR-DLL 135822 из одной линейки: Light Placer 4.2.x + «Light Placer VR» 4.2.0 (так Panda's, Stormcrown и Tempus VR). Основной 5.0.0 брать, только если на VR-странице вышла 5.x.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Не вместе с: ENB Light; Particle Lights for ENB (с Open Shaders не работают)
- Порядок в MO2: Light Placer VR — ниже основного Light Placer: его DLL должна перекрыть DLL основного. Конфиг-моды (CS Light и др.) — ниже обоих.
- Настройки: JSON-конфиги лежат в Data\LightPlacer\. Пересечения огней проверить Lights Conflict Resolver (есть в манифесте).
- Проверка: В sksevr.log Light Placer загружен без ошибки версии. Свечи и жаровни из конфигов CS Light дают свет.
- Заметка: Огни на мешах и эффектах через JSON. ENB Light в CS 1.4+ не работает, его заменяет Light Placer. Основной мод — конфиги, VR-страница — DLL.

### CS Light — `rec` [#138443](https://www.nexusmods.com/skyrimspecialedition/mods/138443)
- Фаза 3 · тип `mixed` · установка `mo2_mod` · надёжность данных `medium`
- Файл: CS Light 2.0.1 (Stormcrown VR, Nordic Souls PBR) — последний.
- Установщик: Первый шаг (по комментарию автора): три группы — Lux, Embers XD, Vanilla. С Lux выбирать только группу Lux: её конфиги подходят и для Embers XD. По FOMOD из репозитория InTheBottle/CS-Light: «Furniture» при Lux не брать; «Deathbell» не брать при Cathedral 3D Deathbell; Potions — одно из Dim, Bright или Legacy; «CS Light» (esp: ISL для магии в руках и снарядов) — брать. «Magic FX» и «Bound Weapons» — по желанию; «Mysticsm» — только вместе с Mysticism. «Interior Window Lights» требует включённой фичи Inverse Square Lighting. Патчи (Wyrmstooth, Nirn Necessities и т. п.) — только для установленных модов. Версия FOMOD на Nexus может отличаться: читать установщик.
- Требует: Light Placer + Light Placer VR (#127557, #135822); Open Shaders (#180419) или CSX (#166950)
- Не вместе с: ENB Lights For Effect Shaders вместе с опцией Magic FX (двойной свет)
- Порядок в MO2: Ниже Light Placer, Lux и Embers XD.
- Порядок плагина: CS Light.esp — после True Light и Window Shadows Ultimate, если они есть. Автор советует грузить его поздно.
- Проверка: Магия в руке и снаряды светят. Свечи и факелы без двойного свечения. У Light Placer нет ошибок в логе.
- Заметка: Конфиги Light Placer для свечей, факелов, эффектов. Не включайте одновременно опции «ENB lights for effect shaders» и «Magic FX lights» — свет удвоится.

### Rim Lighting Removed — `opt` [#164488](https://www.nexusmods.com/skyrimspecialedition/mods/164488)
- Фаза 3 · тип `mixed` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Rim Lighting Removed 1.1.0 (Panda's Sovngarde VR) или 1.1.1 (TNE, 2026-08). Состав архива неизвестен.
- Установщик: неизвестно — общие правила
- Проверка: Ореол по краям объектов и персонажей пропал. Нет вылетов при загрузке.
- Заметка: Убирает ванильную ореольную подсветку объектов. Дело вкуса, стоит в Panda's Sovngarde.

### Native Water Light Stabilizer — `try` [#186700](https://www.nexusmods.com/skyrimspecialedition/mods/186700)
- Фаза 3 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: NativeWaterLightStabilizer 1.3 (TNE, 2026-08-23), последний известный. В VR-сборках не встречается.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457)
- Настройки: Ставить последним и только после того, как Open Shaders уже стабильно работает. Если Open Shaders перестал грузиться — выключить этот мод первым.
- Проверка: В sksevr.log плагин загружен, Open Shaders тоже загружен. Блики на воде мерцают меньше.
- Заметка: Меньше мерцания бликов на воде. VR заявлен, но один пользователь писал, что с ним не грузится Open Shaders — проверять только вместе с OS 2.17.

## 05 VR-ядро

### VRIK Player Avatar — `core` [#23416](https://www.nexusmods.com/skyrimspecialedition/mods/23416)
- Фаза 3 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Тело игрока, холстеры, жесты.

### HIGGS — Enhanced VR Interaction — `core` [#43930](https://www.nexusmods.com/skyrimspecialedition/mods/43930)
- Фаза 3 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Коллизии рук, хват двумя руками, гравиперчатки.

### PLANCK — `core` [#66025](https://www.nexusmods.com/skyrimspecialedition/mods/66025)
- Фаза 3 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Физические удары и реакции NPC. Требует HIGGS 1.6.0+ и SKSEVR 2.0.12.

### Physical Collision VR — `rec` [#186335](https://www.nexusmods.com/skyrimspecialedition/mods/186335)
- Фаза 3 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Руки и оружие упираются в стены, столы и щит. Требует HIGGS, PLANCK, VRIK. Не совмещать с другими модами коллизии оружия вроде Pseudo Physical Weapon Collision and Parry — они делают одно и то же.

### True Wield VR — `rec` [#191123](https://www.nexusmods.com/skyrimspecialedition/mods/191123)
- Фаза 3 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Масса оружия и хват в любой точке рукояти. Требует Physical Collision VR, MCM Helper, SkyUI VR.

### Immersive Weapon Penetration VR — `rec` [#184223](https://www.nexusmods.com/skyrimspecialedition/mods/184223)
- Фаза 3 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Колющий удар входит в тело и застревает. Требует HIGGS, PLANCK, VRIK.

### Swap Drop and Hold Redux — VR — `rec` [#185816](https://www.nexusmods.com/skyrimspecialedition/mods/185816)
- Фаза 3 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Смена, бросание и удержание предметов в руке.

### Spell Wheel VR — `core` [#47630](https://www.nexusmods.com/skyrimspecialedition/mods/47630)
- Фаза 3 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Выбор заклинаний и предметов жестом, без меню.

### Weapon Throw VR — `rec` [#31374](https://www.nexusmods.com/skyrimspecialedition/mods/31374)
- Фаза 3 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила

### Interactive Activators VR — `rec` [#161676](https://www.nexusmods.com/skyrimspecialedition/mods/161676)
- Фаза 3 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Физические рычаги, цепи и кнопки. Заменил Interactive Pullchains VR.

### Instant Equip VR — `rec` [#44571](https://www.nexusmods.com/skyrimspecialedition/mods/44571)
- Фаза 3 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила

### Dialogue Movement Enabler VR — `rec` [#59816](https://www.nexusmods.com/skyrimspecialedition/mods/59816)
- Фаза 3 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила

### Stop Trigger Unsheathing For VR — `rec` [#55962](https://www.nexusmods.com/skyrimspecialedition/mods/55962)
- Фаза 3 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила

### Dual Casting Fix VR — `rec` [#92804](https://www.nexusmods.com/skyrimspecialedition/mods/92804)
- Фаза 3 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила

### Haptic Skyrim VR — `rec` [#20364](https://www.nexusmods.com/skyrimspecialedition/mods/20364)
- Фаза 3 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Отдача в контроллеры от лука, магии и ударов.

### Seamless Arrow Nocking VR + Immersive Crossbow Reload VR — `rec` [#117254](https://www.nexusmods.com/skyrimspecialedition/mods/117254)
- Также скачать: Crossbow Reload: https://www.nexusmods.com/skyrimspecialedition/mods/139152
- Фаза 3 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила

### Magic Improvements for Skyrim VR — `rec` [#55751](https://www.nexusmods.com/skyrimspecialedition/mods/55751)
- Фаза 3 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила

### Lethal Unarmed VR — `opt` [#191124](https://www.nexusmods.com/skyrimspecialedition/mods/191124)
- Фаза 3 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Захваты: схватить за руку, бросить, придушить.

### VR Climbing — Aelove Ver — `opt` [#170321](https://www.nexusmods.com/skyrimspecialedition/mods/170321)
- Фаза 3 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Форк VR Climbing с доп. настройками, свежие VR-сборки перешли на него. Ставить вместо оригинала 168553. Нужны HIGGS и Skyrim VR Tools. Метка AI-generated.

### Spellsiphon — `opt` [#26627](https://www.nexusmods.com/skyrimspecialedition/mods/26627)
- Фаза 3 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Жестовая магия.

### To Your Face — `opt` [#24720](https://www.nexusmods.com/skyrimspecialedition/mods/24720)
- Фаза 3 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: VR-файл: VR
- Установщик: неизвестно — общие правила

### Sprint Jump VR — `opt` [#28354](https://www.nexusmods.com/skyrimspecialedition/mods/28354)
- Фаза 3 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила

### Arctal's VRIK Tweaks — `rec` [#63663](https://www.nexusmods.com/skyrimspecialedition/mods/63663)
- Фаза 3 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Быстрые жесты для заклинаний и криков, правка ragdoll, fNearDistance против мерцания снега. 8 VR-сборок, есть русификация.

### No Stagger Mod — `rec` [#16335](https://www.nexusmods.com/skyrimspecialedition/mods/16335)
- Фаза 3 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Убирает пошатывание игрока — в VR оно дёргает камеру и укачивает. Во всех 9 VR-сборках.

### Neutral VR Animations for VRIK — `opt` [#28831](https://www.nexusmods.com/skyrimspecialedition/mods/28831)
- Фаза 3 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Тело VRIK не принимает боевые стойки.

### SKSEVR Perk Extender — `opt` [#16330](https://www.nexusmods.com/skyrimspecialedition/mods/16330)
- Фаза 3 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Без него большие перк-моды вылетают при входе в дерево. Его statsmenu.swf не давать перезаписать.

### Smooth Carriage Ride VR + Im Walkin' Here VR — `opt` [#129594](https://www.nexusmods.com/skyrimspecialedition/mods/129594)
- Также скачать: Im Walkin' Here: https://www.nexusmods.com/skyrimspecialedition/mods/39433
- Фаза 3 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Комфорт: карета не трясёт камеру, NPC не сдвигают игрока толчками.

### No more werewolf hat — `opt` [#104975](https://www.nexusmods.com/skyrimspecialedition/mods/104975)
- Фаза 3 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Голова вервольфа больше не закрывает обзор.

### VR Equip — `opt` [#83092](https://www.nexusmods.com/skyrimspecialedition/mods/83092)
- Фаза 3 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Поднёс вещь к телу — надел, ко рту — съел.

### Auto Sneak and Jump VR — `opt` [#23649](https://www.nexusmods.com/skyrimspecialedition/mods/23649)
- Фаза 3 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Скрытность — когда реально приседаете, прыжок — когда подпрыгиваете. Со Sprint Jump VR выбрать одну схему.

### Spell Auto-Aim VR — `opt` [#119689](https://www.nexusmods.com/skyrimspecialedition/mods/119689)
- Фаза 3 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Мягкое автонаведение заклинаний. Не совместим со SpellBender VR.

### Durability VR + Immersive Smithing — `opt` [#76830](https://www.nexusmods.com/skyrimspecialedition/mods/76830)
- Также скачать: Immersive Smithing: https://www.nexusmods.com/skyrimspecialedition/mods/72298
- Фаза 3 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Износ снаряжения с полосками на запястье и физическая кузня с молотом.

### PLANCK VR Stability Patch — `opt` [#188233](https://www.nexusmods.com/skyrimspecialedition/mods/188233)
- Фаза 3 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Неофициальная пересборка DLL PLANCK 0.8.1. Ставить, если PLANCK вылетает. Перезаписывает activeragdoll.dll.

### VRIK Closed Fist — `opt` [#182410](https://www.nexusmods.com/skyrimspecialedition/mods/182410)
- Фаза 3 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Свободные руки сжимаются в кулак. Пара к Lethal Unarmed VR.

### Steeds of Ultima — VR Mounted Combat — `opt` [#81220](https://www.nexusmods.com/skyrimspecialedition/mods/81220)
- Фаза 3 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Магия, крики и посохи с седла. Nemesis-патч собрать через Pandora.

## 06 Хайтек 2026

### Smooth Terrain — `rec` [#186875](https://www.nexusmods.com/skyrimspecialedition/mods/186875)
- Фаза 8 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Ваш пример. На лету дробит меши ландшафта вокруг игрока: холмы без углов, коллизия и сейвы не меняются. Одна DLL на SE/AE/VR (видно в исходниках), стоит в Yggdrasil VR рядом с Open Shaders. Метка AI Assisted. Начните с настроек по умолчанию и сверьте время кадра.

### Helios + MMSF, Luma Utility, XEMI Utility — `opt` [#181533](https://www.nexusmods.com/skyrimspecialedition/mods/181533)
- Также скачать: MMSF: https://www.nexusmods.com/skyrimspecialedition/mods/183073; Luma: https://www.nexusmods.com/skyrimspecialedition/mods/177961; XEMI: https://www.nexusmods.com/skyrimspecialedition/mods/159084
- Фаза 8 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Ваш пример, преемник DIAL: свет в интерьерах с окнами следует за погодой и временем суток. Набор версий как в Stormcrown VR: Helios 1.01, Luma 1.7, MMSF 1.1, XEMI 1.6. Luma и MMSF 2.x с ним несовместимы. С интерьерным светом Lux связку никто не проверял.

### Inventory Selfie VR — Redux — `rec` [#190704](https://www.nexusmods.com/skyrimspecialedition/mods/190704)
- Фаза 8 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: VR-замена Show Player In Inventory: в меню видно настоящее тело VRIK, без клона. Нужен VRIK 0.8.7+. Берите 1.3 — в ней исправлен вылет с HDT-SMP. Стоит в Tahrovin — Grit. Со старым View Yourself VR вместе не ставить.

### Pull Arrows VR — Immersive Extraction — `rec` [#169833](https://www.nexusmods.com/skyrimspecialedition/mods/169833)
- Фаза 8 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Стрелы, болты и брошенное оружие вытаскиваются из тел рукой: с сопротивлением, звуком и кровью. Нужны HIGGS, Weapon Throw VR и Broken Feathers. Есть в трёх VR-сборках.

### Cold Breath NG — `rec` [#174838](https://www.nexusmods.com/skyrimspecialedition/mods/174838)
- Фаза 8 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Пар изо рта на холоде у игрока, NPC и существ, без скриптов. Автор прямо пишет «для 1.5.97/1.6/VR». Старые скриптовые моды пара убрать. Проверка: у NPC в Винтерхолде идёт пар, в sksevr.log нет ошибок.

### Interactive Waters — VR (beta) — `opt` [#166560](https://www.nexusmods.com/skyrimspecialedition/mods/166560)
- Фаза 8 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Руки поднимают на воде рябь, волны и брызги, эффект зависит от скорости и силы удара. Только VR, стоит в Librum VR и Panda's Sovngarde. Бета.

### Immersive Harvesting VR — `opt` [#186754](https://www.nexusmods.com/skyrimspecialedition/mods/186754)
- Фаза 8 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Растения срываются рукой через HIGGS, ингредиент сразу в ладони. Стоит в Yggdrasil VR. Метка AI-Generated. С автосбором не совмещать.

### ISPVR — Immersive Spellcasting VR — `opt` [#164183](https://www.nexusmods.com/skyrimspecialedition/mods/164183)
- Фаза 8 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Магия кистью: сжал — заряд, вибрация — готово, раскрыл ладонь — выстрел. В VRIK выключить Open Hand Casting. Стоит в Panda's Sovngarde.

### Steeds of Omega VR — NPC Mounted Combat — `opt` [#169221](https://www.nexusmods.com/skyrimspecialedition/mods/169221)
- Фаза 8 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Конные NPC в бою атакуют, отходят и не падают с лошадей; всадника можно стащить через HIGGS. Пара к Steeds of Ultima VR. Стоит в Tempus VR.

### Dynamic Footprints SKSE — `try` [#175254](https://www.nexusmods.com/skyrimspecialedition/mods/175254)
- Фаза 8 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Работающая в VR часть идеи Dynamic Terrain Deformation: следы игрока, NPC и существ на снегу, пепле и песке. Автор: «рассчитан на SE, AE и VR, VR проверить не могу», есть отзыв о работе в VR. Вместо старых Footprints, не вместе.

### DynamicShader — DynamicSnow — `try` [#189713](https://www.nexusmods.com/skyrimspecialedition/mods/189713)
- Фаза 8 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Настоящая деформация вершин ландшафта поверх Smooth Terrain: колеи в снегу, песке и грязи. В README только SE/AE, VR не подтверждён. Только для эксперимента на отдельном сохранении, не вместе с Dynamic Footprints.

### XPMF — Extended Projected Materials Framework — `try` [#192698](https://www.nexusmods.com/skyrimspecialedition/mods/192698)
- Фаза 8 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Проецируемый снег и пепел на объектах: текстура как у земли, под крышами чисто, учитывает Seasons of Skyrim. VR заявлен, нужен VR Address Library 0.266+. Версия 0.x.

### Frostwalker — `try` [#184628](https://www.nexusmods.com/skyrimspecialedition/mods/184628)
- Фаза 8 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Морозная магия превращает воду в льдины, по которым можно идти. В исходниках есть отдельные VR-адреса. Проверка: заморозить воду морозным заклинанием.

### Bobbing Framework — `try` [#186081](https://www.nexusmods.com/skyrimspecialedition/mods/186081)
- Фаза 8 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Лодки и плавучие предметы покачиваются на воде без замены мешей. В VR автор отключил хук отрисовки из-за вылетов. Проверка: лодки у Рифтена.

### Immersive NPC Dialogue — VR — `try` [#184804](https://www.nexusmods.com/skyrimspecialedition/mods/184804)
- Фаза 8 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Разговор начинается взмахом руки в сторону NPC, варианты ответа — на запястье. Только SKSEVR, автор Interactive Waters. Ни в одной сборке пока нет.

### Palm Compass VR — `try` [#189452](https://www.nexusmods.com/skyrimspecialedition/mods/189452)
- Фаза 8 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Компас уходит с HUD на ладонь: подняли раскрытую руку — компас над ней. Нужны VRIK и HIGGS. Метка AI-Generated.

### Horizon Fix — `opt` [#184607](https://www.nexusmods.com/skyrimspecialedition/mods/184607)
- Фаза 8 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Убирает разрыв на горизонте: полоса перехода к небу и водная «юбка» до горизонта. В коде есть отдельная VR-ветка, в Open Shaders — фича-компаньон. В VR работает урезанно.

## 07 Интерфейс

### moreHUD VR — `rec` [#33215](https://www.nexusmods.com/skyrimspecialedition/mods/33215)
- Фаза 4 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила

### QuickLoot IE — `rec` [#120075](https://www.nexusmods.com/skyrimspecialedition/mods/120075)
- Фаза 4 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Быстрый лут. Работает в VR — стоит в Yggdrasil VR и Stormcrown VR.

### VR Console Selection Fix — `rec` [#140752](https://www.nexusmods.com/skyrimspecialedition/mods/140752)
- Фаза 4 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила

### No Menu Fade Out VR — `opt` [#185197](https://www.nexusmods.com/skyrimspecialedition/mods/185197)
- Фаза 4 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила

### Norden UI — VR Edition — `opt` [#169537](https://www.nexusmods.com/skyrimspecialedition/mods/169537)
- Фаза 4 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Тема интерфейса.

### Essential Favorites VR + Favorite Misc Items — `rec` [#59554](https://www.nexusmods.com/skyrimspecialedition/mods/59554)
- Также скачать: Favorite Misc Items: https://www.nexusmods.com/skyrimspecialedition/mods/42750
- Фаза 4 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Избранное нельзя случайно продать или выронить — с HIGGS это частая беда. Favorite Misc Items добавляет в Избранное факелы и кирки, VR-файл.

### VR Menu Mouse Fix — `opt` [#33414](https://www.nexusmods.com/skyrimspecialedition/mods/33414)
- Фаза 4 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Курсор от контроллера в MCM, поиске SkyUI, назначении клавиш.

### Crafting Categories for SkyUI VR (COCKS) — `opt` [#81409](https://www.nexusmods.com/skyrimspecialedition/mods/81409)
- Фаза 4 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: VR-файл: VR
- Установщик: неизвестно — общие правила
- Заметка: Категории в меню кузницы вместо одного длинного списка.

### Floating Subtitles VR — `opt` [#183714](https://www.nexusmods.com/skyrimspecialedition/mods/183714)
- Фаза 4 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Субтитры висят над говорящим NPC. Нужен ImGui VR Helper. Метка AI-Generated.

### Floating Damage NG — `opt` [#184159](https://www.nexusmods.com/skyrimspecialedition/mods/184159)
- Фаза 4 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Числа урона висят в 3D у цели. Нужен ImGui VR Helper 1.5.4+.

### Clear HUD VR + Clean Menu — `opt` [#49657](https://www.nexusmods.com/skyrimspecialedition/mods/49657)
- Также скачать: Clean Menu: https://www.nexusmods.com/skyrimspecialedition/mods/53524
- Фаза 4 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Чистый HUD и главное меню. Unobtrusive HUD не нужен — дублирует Clear HUD.

### Minimal Enemy Healthbar VR — `opt` [#17812](https://www.nexusmods.com/skyrimspecialedition/mods/17812)
- Фаза 4 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила

### Dynamic Location Pop-ups (VR) — `opt` [#155978](https://www.nexusmods.com/skyrimspecialedition/mods/155978)
- Также скачать: основной: https://www.nexusmods.com/skyrimspecialedition/mods/153122
- Фаза 4 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Название локации при каждом входе.

### RacemenuVR — `opt` [#156898](https://www.nexusmods.com/skyrimspecialedition/mods/156898)
- Фаза 4 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Редактор персонажа. Проверенный вариант из 4 VR-сборок.

### RaceMenu VR 2 — `try` [#192158](https://www.nexusmods.com/skyrimspecialedition/mods/192158)
- Фаза 4 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Новая надстройка: стабильный вид лица, Sculpt с undo, своя клавиатура. Бета, вместо RacemenuVR.

### I5 — Information Injector Improved — `try` [#192976](https://www.nexusmods.com/skyrimspecialedition/mods/192976)
- Фаза 4 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Преемник I4: меню не тормозит при каждом обновлении. VR включён в 0.3. Если I4 не вылетает — оставить I4.

## 08 Звук

### Audio Overhaul for Skyrim — `rec` [#12466](https://www.nexusmods.com/skyrimspecialedition/mods/12466)
- Фаза 4 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила

### Regional Sounds Expansion + Reverb Interior Sounds Expansion — `rec` [#77829](https://www.nexusmods.com/skyrimspecialedition/mods/77829)
- Также скачать: Reverb Interior: https://www.nexusmods.com/skyrimspecialedition/mods/77947
- Фаза 4 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила

### Acoustic Space Improvement Fixes — `rec` [#78992](https://www.nexusmods.com/skyrimspecialedition/mods/78992)
- Фаза 4 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила

### Immersive Sounds Compendium + AOS–ISC patch — `alt` [#523](https://www.nexusmods.com/skyrimspecialedition/mods/523)
- Также скачать: патч: https://www.nexusmods.com/skyrimspecialedition/mods/36761
- Фаза 4 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила

### True 3D Sound for Headphones — `rec` [#1897](https://www.nexusmods.com/skyrimspecialedition/mods/1897)
- Фаза 4 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: HRTF-позиционирование для наушников гарнитуры.

### UHDAP — Music HQ — `opt` [#18115](https://www.nexusmods.com/skyrimspecialedition/mods/18115)
- Фаза 4 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Ванильная музыка без артефактов. Голоса EN — только при английской озвучке.

### Wildwood Echoes + Murmurs and Mead — `opt` [#112008](https://www.nexusmods.com/skyrimspecialedition/mods/112008)
- Также скачать: Murmurs and Mead: https://www.nexusmods.com/skyrimspecialedition/mods/114716
- Фаза 4 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Звуки леса и 18 вариантов шума таверн.

### Haunting Harmonies of Hjaalmarch + Whispers of the Daedric Princes — `opt` [#125873](https://www.nexusmods.com/skyrimspecialedition/mods/125873)
- Также скачать: Whispers: https://www.nexusmods.com/skyrimspecialedition/mods/141931
- Фаза 4 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Атмосфера болот Морфала и шёпот у святилищ. Позиционный звук в шлеме.

### Immersive Draw Sheathe Sounds VR — `opt` [#44992](https://www.nexusmods.com/skyrimspecialedition/mods/44992)
- Фаза 4 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила

## 09 Свет, погода, вода, VFX

### Lux + Lux Patch Hub — `core` [#43158](https://www.nexusmods.com/skyrimspecialedition/mods/43158)
- Также скачать: Patch Hub: https://www.nexusmods.com/skyrimspecialedition/mods/113002
- Фаза 5 · тип `mixed` · установка `mo2_mod` · надёжность данных `medium`
- Файл: «Lux (main)» 7.0 и «Lux (main plugin update)» 7.1 с той же страницы: так в 12 SE-списках, Tempus VR и Panda's берут 7.0. Patch Hub 113002 — «Lux (patch hub)» 7.1.
- Установщик: Опции разделённых мешей (split meshes) НЕ выбирать: с Light Limit Fix они не нужны и добавляют draw calls. Меши с префиксом Lux_ оставить. Остальные опции — неизвестно, общие правила. В Patch Hub отмечать только патчи для установленных модов (Embers XD и др.).
- Не вместе с: Разделённые меши Lux; ENB Light
- Порядок в MO2: Patch Hub — ниже Lux и ниже патчируемых модов. Lux — выше CS Light.
- Порядок плагина: Патчи из Patch Hub — после Lux и патчируемых плагинов (LOOT обычно справляется).
- Проверка: В интерьерах нет чёрных мешей и мерцания света. В xEdit у патчей нет пропавших мастеров.
- Заметка: В установщике не выбирайте split meshes. Меши с префиксом Lux_ оставьте — они заменяют модели, а не режут их.

### Lux Via + Patch Hub — `rec` [#63588](https://www.nexusmods.com/skyrimspecialedition/mods/63588)
- Также скачать: Patch Hub: https://www.nexusmods.com/skyrimspecialedition/mods/116722
- Фаза 5 · тип `mixed` · установка `mo2_mod` · надёжность данных `medium`
- Файл: «Lux Via (main)» 2.2, «Lux Via main plugin update», «Lux Via meshes update», «Updated Lux - Resources plugin» — так Tempus VR. Если нужен Resource pack, то вариант «Optional Lux Resource pack (No ENB light)», как в CS-сборках CSVO и Morning Star; «(ENB light)» не брать. Patch Hub 116722 — «Lux Via (patch hub)» 2.2.
- Установщик: неизвестно — общие правила; патчи — только для установленных модов
- Не вместе с: Lux Via Resource pack (ENB light) при Open Shaders
- Порядок в MO2: Обновления (plugin/meshes update) — ниже основного Lux Via. Patch Hub — ниже патчируемых модов.
- Проверка: Фонари на дорогах и мостах светят. В xEdit нет пропавших мастеров.
- Заметка: Свет на дорогах и мостах.

### Lux Orbis + Patch Hub — `opt` [#56095](https://www.nexusmods.com/skyrimspecialedition/mods/56095)
- Также скачать: Patch Hub: https://www.nexusmods.com/skyrimspecialedition/mods/114169
- Фаза 5 · тип `mixed` · установка `mo2_mod` · надёжность данных `high`
- Файл: «Lux Orbis (main)» 4.5 (Tempus VR, Panda's, Tahrovin) + «Lux Orbis - Patch Hub» 4.7 (Tahrovin, SE-списки).
- Установщик: неизвестно — общие правила; патчи — только для установленных модов
- Порядок в MO2: Patch Hub — ниже Lux Orbis и патчируемых модов.
- Настройки: Мод дорогой по кадру. Включать, если есть запас по времени кадра.
- Проверка: Уличные фонари в городах светят. Время кадра в Вайтране в норме.
- Заметка: Больше уличных огней. Красиво, но дороже — включать при запасе по времени кадра.

### Azurite Weathers III + MCM + Azurite III HDR — `core` [#42731](https://www.nexusmods.com/skyrimspecialedition/mods/42731)
- Также скачать: MCM: https://www.nexusmods.com/skyrimspecialedition/mods/139858; HDR: https://www.nexusmods.com/skyrimspecialedition/mods/138991
- Фаза 5 · тип `mixed` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Azurite Weathers III 3.35 (Stormcrown VR, 2026). MCM: «Azurite Weathers - MCM and Settings Loader» 1.2.1 (Stormcrown, Panda's). HDR: «Azurite III - HDR» 1.0.1 (Stormcrown VR). По желанию, как у Panda's Sovngarde: Alluring Sunsets and Sunrises 3 (#119148), Azurite Weathers III - Enhanced (#150269); Seasonal Weathers Framework (#63562) — только с Seasons of Skyrim.
- Установщик: неизвестно — общие правила
- Требует: Open Shaders (#180419) или CSX (#166950) — для HDR
- Не вместе с: Volumetric Mists; другие погодные моды
- Порядок в MO2: MCM и HDR — ниже основного Azurite. Storm Lightning — ниже погоды.
- Настройки: HDR, по странице мода: [Display] bUseFilmicCurve=1 и fFilmicWhiteScale=10. В какой именно ini это задаётся — сверить со страницей, без этого тонмаппинг не работает. Проверить, не дублирует ли HDR встроенный HDR или Post-Processing Open Shaders. Настройки погоды — через MCM.
- Проверка: В MCM есть меню Azurite. Небо и погода меняются, нет пересвета. В логах Papyrus нет ошибок Azurite.
- Заметка: FUS перешёл на III как на более оптимизированную для VR, особенно небо. Volumetric Mists к ней не ставят.

### Splashes of Storms + VR — `rec` [#72115](https://www.nexusmods.com/skyrimspecialedition/mods/72115)
- Также скачать: VR-DLL: https://www.nexusmods.com/skyrimspecialedition/mods/73111
- Фаза 5 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Основной 72115 + VR-DLL 73111. Брать одну из двух проверенных пар: основной 1.3.1 + «Splashes of Storms VR» 1.3.0 (FUS, Panda's, Tempus VR) или основной 1.4.0 + VR 1.3.1 (Yggdrasil VR, 2026).
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Порядок в MO2: VR-мод — ниже основного, его DLL должна победить.
- Настройки: Настройки — в po3_SplashesOfStorms.toml.
- Проверка: В sksevr.log DLL Splashes of Storms загружена без ошибки версии. В дождь видны брызги.

### Splashes of Skyrim + VR — `rec` [#47710](https://www.nexusmods.com/skyrimspecialedition/mods/47710)
- Также скачать: VR-DLL: https://www.nexusmods.com/skyrimspecialedition/mods/58104
- Фаза 5 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Основной 47710 + VR-DLL 58104. Пары: основной 1.4.0 + «Splashes of Skyrim VR» 1.4.0 (FUS, Panda's) или основной 1.6.0 + VR 1.5.0 (Yggdrasil VR, 2026). Старый VR 1.6.0.2 от 2021 года (Librum) не брать.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Порядок в MO2: VR-мод — ниже основного.
- Проверка: В sksevr.log DLL загружена. Стрела или заклинание в воде дают брызги и круги, под водой — взрывы.

### Dynamic Wind Framework + Dynamic Wind — Skyrim — `rec` [#177023](https://www.nexusmods.com/skyrimspecialedition/mods/177023)
- Также скачать: Dynamic Wind — Skyrim: https://www.nexusmods.com/skyrimspecialedition/mods/177024
- Фаза 5 · тип `mixed` · установка `mo2_mod` · надёжность данных `low`
- Файл: Dynamic Wind Framework 1.4 + «DynamicWindSkyrim» 1 (#177024) — так Stormcrown VR.
- Установщик: неизвестно — общие правила
- Требует: Dynamic Wind Framework (#177023) — для Dynamic Wind — Skyrim; SKSEVR (#30457)
- Порядок в MO2: Dynamic Wind — Skyrim — ниже фреймворка.
- Настройки: Если в архиве есть DLL — нужна VR Address Library (общее правило).
- Проверка: В sksevr.log фреймворк загружен без ошибки. Деревья и трава качаются по ветру. Время кадра не просело.
- Заметка: Ветер для растительности, 2026 год, есть в Stormcrown VR.

### Simplicity of Sea — `rec` [#56520](https://www.nexusmods.com/skyrimspecialedition/mods/56520)
- Фаза 5 · тип `mixed` · установка `mo2_mod` · надёжность данных `high`
- Файл: «Water Mod» 0.8 (Stormcrown VR, Spirit of Grit, SE-списки). По желанию — «Simplicity of Sea - Water Color Tweaks» (#148761, Stormcrown VR).
- Установщик: неизвестно — общие правила
- Не вместе с: Water for ENB (#37061)
- Группа «одно из»: `water`
- Порядок в MO2: Color Tweaks — ниже основного.
- Проверка: Вода в реках и море меняет вид. Нет швов и прозрачных пятен на стыках ячеек.
- Заметка: Вода под шейдерные эффекты воды. Стоит в Stormcrown VR и MGO 4.0. Ставится один водный мод.

### Water for ENB — `alt` [#37061](https://www.nexusmods.com/skyrimspecialedition/mods/37061)
- Фаза 5 · тип `mixed` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Water for ENB: 2.15 (Tempus VR) или последний 2.21 (Morning Star, SUP).
- Установщик: неизвестно — общие правила
- Не вместе с: Simplicity of Sea (#56520)
- Группа «одно из»: `water`
- Проверка: Вода меняет вид. Нет швов на стыках ячеек.
- Заметка: Альтернатива Simplicity of Sea, вариант Tempus VR.

### Map Weather — CS — `opt` [#170955](https://www.nexusmods.com/skyrimspecialedition/mods/170955)
- Фаза 5 · тип `mixed` · установка `mo2_mod` · надёжность данных `low`
- Файл: «Map - CS» 1.0.0 (Stormcrown VR, CSVO, Morning Star).
- Установщик: неизвестно — общие правила
- Требует: Open Shaders (#180419) или CSX (#166950)
- Порядок в MO2: Ниже Open Shaders или CSX.
- Проверка: На карте мира видна погода. Карта открывается без вылета.

### Embers XD — `rec` [#37085](https://www.nexusmods.com/skyrimspecialedition/mods/37085)
- Фаза 5 · тип `mixed` · установка `mo2_mod` · надёжность данных `medium`
- Файл: «Embers XD 2K» 3.2.8 (Stormcrown VR, 2026-09) или 1K. Для слабых ПК по желанию — «Embers XD (Less Poly)» (#164369, Panda's).
- Установщик: По треду Step, в установщике есть качество частиц: для VR выбрать Optimized. С Open Shaders опции ENB/Complex Particle Lights не брать — свет даст CS Light (группа Embers XD или Lux). С CSX — либо частицы Embers, либо конфиги CS Light, не оба. Точные названия опций — читать установщик.
- Не вместе с: Embers HD
- Порядок в MO2: Патчи Lux для Embers XD из Lux Patch Hub — ниже обоих модов. CS Light — ниже.
- Проверка: У костров видны дым и искры. Свет не двоится. FPS у костров в норме.
- Заметка: Объёмный огонь, искры и дым у костров, факелов и свечей. В CS Light выбрать опцию под Embers XD. 7 VR-сборок.

### Moons and Stars + SKSEVR DLL — `rec` [#73336](https://www.nexusmods.com/skyrimspecialedition/mods/73336)
- Также скачать: SKSEVR DLL: https://www.nexusmods.com/skyrimspecialedition/mods/73667
- Фаза 5 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `high`
- Файл: «Moons And Stars - Sky Overhaul SKSE» 2.0.2 (73336) + «Moons and Stars - Sky Overhaul SKSEVR» 2.0.0 (73667). Версию 2.1.0 не брать: под неё нет VR-DLL.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Не вместе с: Moons and Stars 2.1.x; другие моды, меняющие меши звёзд и лун
- Порядок в MO2: Мод с SKSEVR-DLL — ниже основного 2.0.2: VR-DLL должна победить.
- Настройки: Текстуры галактики совместимость не ломают: Stormcrown VR ставит Realistic Galaxy вместе с M&S.
- Проверка: В sksevr.log DLL Moons and Stars загружена без ошибки версии. Ночью видны фазы лун и вращение неба.
- Заметка: Реальные звёзды, фазы лун, вращение неба. Держаться 2.0.2 — у 2.1 нет VR-DLL.

### Storm Lightning for SSE and VR — `rec` [#29243](https://www.nexusmods.com/skyrimspecialedition/mods/29243)
- Фаза 5 · тип `mixed` · установка `mo2_mod` · надёжность данных `medium`
- Файл: «Storm Lightning for SSE and VR - Fomod Installer»: последний 1.4.25 (TNE, 2026-08) или 1.4.22–1.4.23 (FUS, Tahrovin).
- Установщик: В установщике выбрать вариант для VR, если он есть. Остальное — неизвестно, общие правила.
- Порядок в MO2: Ниже Azurite Weathers III.
- Порядок плагина: После Azurite (LOOT).
- Проверка: В грозу видны разряды в землю и синхронный гром.
- Заметка: Разряды в землю, синхронный гром, вспышки. Дополняет грозы Azurite.

### Natural Waterfalls — `opt` [#87261](https://www.nexusmods.com/skyrimspecialedition/mods/87261)
- Фаза 5 · тип `mixed` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Natural Waterfalls 3.7 (последний, SE-списки). В VR-сборках: Panda's — 3.2, Tempus VR — 3.0.
- Установщик: неизвестно — общие правила
- Не вместе с: WAVY Waterfalls Effect (#126073) — проверить, оба меняют водопады
- Порядок в MO2: Ниже Simplicity of Sea или Water for ENB.
- Проверка: У водопадов есть брызги, пена и туман. В xEdit нет конфликта с водным модом.
- Заметка: Брызги, пена и туман вместо ванильных полотен водопадов.

### KittyVFX — Frost, Fire, Lightning, Dragon Breath, Healing, Portals — `opt` [#112509](https://www.nexusmods.com/skyrimspecialedition/mods/112509)
- Фаза 5 · тип `mixed` · установка `mo2_mod` · надёжность данных `high`
- Файл: Каждый модуль — отдельная страница: Frost (112509) 1.2, Fire (109414) 1.23 (по желанию вариант «Yellow Fire»), Lightning (124520) 1.3, Dragon Breath (118431) 1.32, Healing (133774) 1.3, Portals (135614) 1.03. Так Tempus VR.
- Установщик: неизвестно — общие правила
- Не вместе с: другие замены визуала магии тех же школ
- Проверка: Огонь, мороз и молния выглядят по-новому. В шлеме эффект не закрывает обзор.
- Заметка: Серия новых эффектов магии, без DLL. Магия кастуется прямо перед глазами.

### Deadly Spell Impacts + Parallax Spell Impacts — `opt` [#12939](https://www.nexusmods.com/skyrimspecialedition/mods/12939)
- Также скачать: Parallax: https://www.nexusmods.com/skyrimspecialedition/mods/83935
- Фаза 5 · тип `mixed` · установка `mo2_mod` · надёжность данных `high`
- Файл: Deadly Spell Impacts v1.70 (6 VR-списков) или v1.9 (Panda's). Parallax Spell Impacts 83935 — 2.1, по желанию «Thunderbolt HD» (Panda's).
- Установщик: неизвестно — общие правила
- Требует: Deadly Spell Impacts (#12939) — для PSI; Open Shaders (#180419) — параллакс PSI
- Порядок в MO2: PSI — ниже DSI.
- Проверка: На земле остаются следы заклинаний. С PSI у следов есть рельеф.
- Заметка: Выжженные и обледенелые следы заклинаний на поверхностях.

### slightly Better Dust + Improved Sparks — `opt` [#133368](https://www.nexusmods.com/skyrimspecialedition/mods/133368)
- Также скачать: Improved Sparks: https://www.nexusmods.com/skyrimspecialedition/mods/19831
- Фаза 5 · тип `mixed` · установка `mo2_mod` · надёжность данных `medium`
- Файл: «slightly Better Dust» 1.0 (Stormcrown VR, Tempus VR). Improved Sparks 19831: файлы «Grindstones - 10X Sparks» и «Impact Effects - Vanilla Sparks» (Yggdrasil VR); какой из них основной — неизвестно, смотреть страницу.
- Установщик: неизвестно — общие правила
- Проверка: Пыль от ударов мелкая. Искры от оружия и точила видны.
- Заметка: Мелкая пыль вместо облаков, настоящие искры от ударов.

### Volcanic Tundra — Heat Wave Effects — `opt` [#13749](https://www.nexusmods.com/skyrimspecialedition/mods/13749)
- Фаза 5 · тип `mixed` · установка `mo2_mod` · надёжность данных `high`
- Файл: «VolcanicHeatHaze-by-fadingsignal» 1.0 — единственный файл.
- Установщик: нет установщика
- Настройки: Если марево в шлеме неприятно — выключить мод.
- Проверка: Над горячими источниками Истмарка видно марево.
- Заметка: Марево над горячими источниками. Если в шлеме мешает — выключить.

## 10 Ландшафт, трава, деревья

### No Grass In Objects NG — `core` [#42161](https://www.nexusmods.com/skyrimspecialedition/mods/42161)
- Фаза 5 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `high`
- Файл: «NGIO - NG (1.6.14)» — общая сборка, VR поддерживается (так Stormcrown VR). Старый «NGIO - VR (1.4.15)» 1.1.0 не брать. С той же страницы по желанию: «Config INI - GrassControl.ini» отдельным модом и «Grass Generation MO2 Plugin v2» — плагин MO2 «Precache Grass» в папку plugins MO2 (так Tempus VR).
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Не вместе с: NGIO .NET Framework-версия
- Порядок в MO2: Сгенерированный кэш (папка Grass из Overwrite) — отдельный мод «Grass Cache» в самом низу, в сепараторе «Сгенерированное».
- Настройки: SKSE\Plugins\GrassControl.ini (дефисные ключи, как в GrassControl.toml из репо). Задать: Use-grass-cache = true; Only-load-from-cache = true; Ray-cast-enabled = true (основная функция — трава не растёт в камнях и дорогах); DynDOLOD-Grass-Mode = 1 (Grass Cache Helper NG работает только с 1, и так дешевле для VR); Extend-grass-distance = false (при Mode 1); Super-dense-grass = false; Overwrite-min-grass-size = -1 (брать из ini). iMinGrassSize в SkyrimVR.ini [Grass] задать ДО прекэша: он запекается в кэш, FUS советует 60–100, больше — реже трава. Прекэш: в Root Builder добавить исключение для PrecacheGrass.txt; создать PrecacheGrass.txt в корне игры или запустить «Precache Grass» из меню Tools MO2. Вылеты во время генерации — норма, перезапускать. После любых изменений травы, ландшафта или ini — удалить кэш и сгенерировать заново. В DynDOLOD Advanced тоже выставить Grass LOD Mode 1.
- Проверка: В sksevr.log GrassControl загружен. После прекэша в моде Grass Cache есть Grass\*.cgid. В игре трава не растёт сквозь камни и дороги, FPS на открытой местности выше.
- Заметка: Прекэш травы: большой выигрыш в VR и основа для Grass LOD в DynDOLOD. После смены травы или iMinGrassSize кэш генерируется заново.

### Grass Cache Helper NG — `core` [#101095](https://www.nexusmods.com/skyrimspecialedition/mods/101095)
- Фаза 5 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `high`
- Файл: Grass Cache Helper NG 1.0.2 (Stormcrown VR).
- Установщик: неизвестно — общие правила
- Требует: No Grass In Objects NG (#42161); SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Настройки: Работает только с DynDOLOD-Grass-Mode = 1. Подменяет загрузку .GID на .CGID — кэш NGIO переименовывать не нужно. Видит PrecacheGrass.txt и на время прекэша сам выставляет ini игры. С Seasons of Skyrim 1.8+ сам грузит сезонный кэш (.SPR/.SUM/.AUT/.WIN.CGID).
- Проверка: В sksevr.log плагин загружен. Трава из кэша видна. Нет пустых квадратов травы.

### Landscape Fixes For Grass Mods — `core` [#9005](https://www.nexusmods.com/skyrimspecialedition/mods/9005)
- Фаза 5 · тип `plugin_only` · установка `mo2_mod` · надёжность данных `high`
- Файл: Landscape Fixes For Grass Mods 5.8 (Tempus VR, Stormcrown VR, Panda's). Доп. патчи с той же страницы (Arthmoor's Town add-ons, Great Cities, Helgen Reborn и т. п.) — только если стоят эти моды.
- Установщик: нет установщика
- Порядок плагина: Как ставит LOOT, до генерации кэша травы.
- Настройки: Ставить до прекэша травы.
- Проверка: У дорог и стен нет торчащей травы.

### Merethic Grasslands — `rec` [#164058](https://www.nexusmods.com/skyrimspecialedition/mods/164058)
- Фаза 5 · тип `mixed` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Merethic Grasslands, один вариант под ландшафтные текстуры: Vanilla, Faultier's, Vanaheimr или Exist (бывший «Vanilla Plus»). Stormcrown VR ставит «Merethic Grass - Exist Variant» Ex1.68. Пока текстуры ванильные — брать Vanilla. На этапе текстур пересмотреть вариант и перегенерировать кэш.
- Установщик: неизвестно — общие правила; вариант выбирать по ландшафтным текстурам
- Требует: DrJacopo's 3D Grass Library — только файл Meshes (#80687); Open Shaders (#180419) — Grass Lighting
- Не вместе с: другие травяные оверхолы
- Группа «одно из»: `grass`
- Порядок в MO2: Ниже 3D Grass Library Meshes: Merethic должен перекрыть её файлы.
- Настройки: Landscape Fixes For Grass Mods рекомендован. Перед прекэшем NGIO выставить iMinGrassSize.
- Проверка: Трава ванильного стиля, без парящей травы. Время кадра на открытой местности в норме.
- Заметка: Трава в ванильном стиле. Выбрана в Stormcrown VR, где упор на производительность.

### Cathedral 3D Grass Library + 3D-растения — `alt` [#80687](https://www.nexusmods.com/skyrimspecialedition/mods/80687)
- Фаза 5 · тип `assets_only` · установка `mo2_mod` · надёжность данных `medium`
- Файл: «DrJacopo's - 3D Grass Library - Meshes» 16.53 (Stormcrown, Panda's). Этот файл ставить ВСЕГДА: он нужен и Merethic. «Resource Textures» и травяной сет на базе Cathedral (Panda's и Tempus VR ставят Freak's Floral Fields) — только если вместо Merethic выбран Cathedral-сет. 3D-растения (Cathedral 3D Tundra Shrubs, 3D Stonecrop) Stormcrown ставит вместе с Merethic.
- Установщик: неизвестно — общие правила
- Требует: Open Shaders (#180419) — Grass Lighting
- Группа «одно из»: `grass`
- Порядок в MO2: Выше Merethic или выше травяного сета Cathedral.
- Настройки: Как альтернатива Merethic — один травяной сет. Meshes — общая зависимость, не конфликт.
- Проверка: Нет невидимой и парящей травы. Время кадра в норме.
- Заметка: Плотнее и красивее, но тяжелее.

### Happy Little Trees + DynDOLOD 3 Add-On — `rec` [#50961](https://www.nexusmods.com/skyrimspecialedition/mods/50961)
- Также скачать: LOD add-on: https://www.nexusmods.com/skyrimspecialedition/mods/56907
- Фаза 5 · тип `mixed` · установка `mo2_mod` · надёжность данных `high`
- Файл: Happy Little Trees 2.03 + «Happy Little Trees 3D LOD - Performance» 2.02 (5 VR-списков). Quality — только на мощной видеокарте. Как у FUS, по желанию: «Performance - dlc1 pine fix» и «Solstheim Broken Pines 3D LOD Fix» с той же страницы 56907.
- Установщик: неизвестно — общие правила
- Требует: DynDOLOD 3 + Resources SE 3 + DynDOLOD DLL NG (#68518) — для LOD-аддона
- Не вместе с: другие оверхолы деревьев
- Порядок в MO2: LOD-аддон — ниже HLT и ниже DynDOLOD Resources.
- Настройки: В DynDOLOD выбрать 3D tree LOD (FUS по умолчанию берёт Performance и средний пресет).
- Проверка: Деревья заменены. После DynDOLOD дальние деревья совпадают с ближними.
- Заметка: Лёгкие деревья с хорошими LOD.

### Seasons of Skyrim — `opt` [ссылка](https://www.nexusmods.com/skyrimspecialedition/search/?gsearch=Seasons%20of%20Skyrim)
- Фаза 5 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: «Seasons of Skyrim» (62861) 1.8.6 + «Seasons of Skyrim VR» (63593) 1.8.6 — так Panda's Sovngarde. Версию 1.9.0 не брать: VR-DLL под неё не видно. По желанию — «Four Seasons - Faster Seasons of Skyrim» (#64286; Panda's, Librum VR).
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Порядок в MO2: VR-мод — ниже основного. Сезонные патчи — ниже.
- Настройки: Кэш травы и LOD — на каждый сезон: 4 прогона прекэша NGIO, Grass Cache Helper NG сам грузит нужный сезонный кэш (нужна SoS 1.8+). Для Azurite — по желанию Seasonal Weathers Framework (#63562).
- Проверка: В sksevr.log VR-DLL загружена. Зимой летние регионы в снегу. Трава сезона без парящей травы.
- Заметка: Работает в VR (есть в MGO), но кэш травы и LOD придётся генерировать на каждый сезон.

### LOD Model Library for DynDOLOD — `rec` [#87521](https://www.nexusmods.com/skyrimspecialedition/mods/87521)
- Фаза 5 · тип `assets_only` · установка `mo2_mod` · надёжность данных `high`
- Файл: LOD Model Library: последний 1.8.3 (CSVO, NGVO, 2026-06). В VR только Panda's — «LOD Model Library - FOMOD» 1.6.
- Установщик: неизвестно — общие правила
- Требует: DynDOLOD 3 + Resources SE 3 + DynDOLOD DLL NG (#68518)
- Порядок в MO2: Ниже DynDOLOD Resources SE 3.
- Настройки: Нужен только при генерации DynDOLOD. Держать включённым до и во время запуска TexGen и DynDOLOD.
- Проверка: После DynDOLOD дальние скалы, руины и постройки детальнее.
- Заметка: Качественные дальние скалы, руины и постройки для DynDOLOD 3. Стандарт next-gen сборок 2026.

### No Grass In Caves — `opt` [#12431](https://www.nexusmods.com/skyrimspecialedition/mods/12431)
- Фаза 5 · тип `plugin_only` · установка `mo2_mod` · надёжность данных `high`
- Файл: No Grass In Caves: 1.2 (FUS, Yggdrasil VR) или 1.3 (последний, SE).
- Установщик: нет установщика
- Настройки: Ставить до прекэша травы.
- Проверка: В пещерах нет травы.

### Better Dynamic Snow + Better Dynamic Ash — `opt` [#9121](https://www.nexusmods.com/skyrimspecialedition/mods/9121)
- Также скачать: BDA: https://www.nexusmods.com/skyrimspecialedition/mods/54754
- Фаза 5 · тип `mixed` · установка `mo2_mod` · надёжность данных `high`
- Файл: Better Dynamic Snow SE 3.6.0 (Stormcrown, Tempus, Panda's) + Better Dynamic Ash SE 2.1.1 (54754). На этапе параллакса по желанию — «Better Dynamic Snow - Complex Parallax Materials» (#115401, Tempus VR).
- Установщик: неизвестно — общие правила
- Настройки: Возможно пересечение с DynamicShader — DynamicSnow (try): проверить снег на объектах вместе, при двойном снеге оставить одно.
- Проверка: Снег и пепел лежат сверху объектов по геометрии.
- Заметка: Снег и пепел на объектах по геометрии.

### Simple Snow Improvements (BOS) — `opt` [#78702](https://www.nexusmods.com/skyrimspecialedition/mods/78702)
- Фаза 5 · тип `mixed` · установка `mo2_mod` · надёжность данных `high`
- Файл: «Simple Snow Improvements - Skyrim Fixes» 2.3 (Panda's) или 2.4 (SE). По желанию аддоны SSI, как у Panda's: Snow Forts (#85413), Giant Obelisks (#75251), Solstheim Ruins (#96532).
- Установщик: неизвестно — общие правила
- Требует: Base Object Swapper VR (#61734)
- Проверка: Снег на скалах и постройках без лишнего блеска и швов. У BOS нет ошибок в логе.
- Заметка: Чинит блеск и швы снега через BOS VR.

### Footprints + SPID for Footprints — `opt` [#3808](https://www.nexusmods.com/skyrimspecialedition/mods/3808)
- Также скачать: SPID for Footprints: https://www.nexusmods.com/skyrimspecialedition/mods/54924
- Фаза 5 · тип `mixed` · установка `mo2_mod` · надёжность данных `high`
- Файл: Footprints 1.6.1 + SPID for Footprints 3.4 (54924) — так Tempus VR и Panda's. По желанию: «SPIDforFootprintUltimateFix» 1.03 (#96086; Tempus, Panda's) и «Footprints - Alternative Design» (#109544).
- Установщик: неизвестно — общие правила
- Требует: Spell Perk Item Distributor VR (#59121)
- Не вместе с: Dynamic Footprints SKSE (#175254)
- Группа «одно из»: `footprints`
- Порядок в MO2: SPID for Footprints — ниже Footprints. Фиксы — ниже SPID for Footprints.
- Проверка: На снегу и песке остаются следы игрока и NPC. В логе SPID раздача прошла без ошибок.
- Заметка: Проверенные следы на снегу и песке. Или Dynamic Footprints SKSE из хайтек-раздела — одно из двух.

### Auto Parallax — `opt` [#79473](https://www.nexusmods.com/skyrimspecialedition/mods/79473)
- Фаза 5 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `high`
- Файл: Auto Parallax 1.0.27 (FUS, Panda's, Tahrovin), одна NG-DLL.
- Установщик: нет установщика
- Требует: VR Address Library for SKSEVR (#58101) 0.65.0+; Engine Fixes VR (#62089); SKSEVR (#30457)
- Настройки: Экспериментальное автовключение параллакса в INI оставить выключенным. Нужен на этапе parallax-текстур.
- Проверка: В sksevr.log Auto Parallax загружен. Нет растянутых и «плывущих» текстур на мешах без карты высот.
- Заметка: Отключает параллакс на мешах без карты высот. Нужен на этапе parallax-текстур.

## 11 Анимации и физика

### Open Animation Replacer — `core` [#92109](https://www.nexusmods.com/skyrimspecialedition/mods/92109)
- Фаза 6 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Официально поддерживает SE, AE и VR.

### Paired Animation Improvements — `rec` [#99621](https://www.nexusmods.com/skyrimspecialedition/mods/99621)
- Фаза 6 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила

### Mu Joint Fix (DLL) — `rec` [#61479](https://www.nexusmods.com/skyrimspecialedition/mods/61479)
- Фаза 6 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила

### FSMP — Faster HDT-SMP — `opt` [#57339](https://www.nexusmods.com/skyrimspecialedition/mods/57339)
- Фаза 6 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Только если будут SMP-волосы или одежда. Проверьте VR-вариант в установщике. Нужен XPMSSE с VR-фиксом.

### Dynamic Armor Physics — `opt` [#186346](https://www.nexusmods.com/skyrimspecialedition/mods/186346)
- Фаза 6 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: 2026 год, есть в Stormcrown VR.

### XPMSSE + XP32 First Person Skeleton CTD Bugfix for VR — `core` [#1988](https://www.nexusmods.com/skyrimspecialedition/mods/1988)
- Также скачать: VR-фикс: https://www.nexusmods.com/skyrimspecialedition/mods/34301
- Фаза 6 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Расширенный скелет — база для FSMP и многих анимаций. Без VR-фикса поверх SE-скелет в VR даёт вылеты.

### NPC Animation Remix + Gesture Animation Remix (OAR) — `rec` [#63471](https://www.nexusmods.com/skyrimspecialedition/mods/63471)
- Также скачать: Gesture Remix: https://www.nexusmods.com/skyrimspecialedition/mods/64420
- Фаза 6 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Стойки, ходьба и жесты NPC в диалогах. В VR собеседник в метре от вас — деревянные позы видно сразу.

### Expressive Facial Animation — Male + Female — `rec` [#19532](https://www.nexusmods.com/skyrimspecialedition/mods/19532)
- Также скачать: Female: https://www.nexusmods.com/skyrimspecialedition/mods/19181
- Фаза 6 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Мимика и моргание NPC. Дополняет MFG Fix NG и ИИ-NPC.

### Pristine Vanilla Movement — `opt` [#66635](https://www.nexusmods.com/skyrimspecialedition/mods/66635)
- Фаза 6 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Исправленные ванильные анимации передвижения — база под OAR-пакеты.

### Arm Movement Animations (OAR) — `opt` [#62849](https://www.nexusmods.com/skyrimspecialedition/mods/62849)
- Фаза 6 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: NPC при ходьбе держат руки естественно.

### Take a Seat + Improved Table Transitions — `opt` [#54193](https://www.nexusmods.com/skyrimspecialedition/mods/54193)
- Также скачать: Table Transitions: https://www.nexusmods.com/skyrimspecialedition/mods/84160
- Фаза 6 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Позы сидения и плавный вход за стол без телепорта.

### Lively Children Animations (OAR) — `opt` [#67557](https://www.nexusmods.com/skyrimspecialedition/mods/67557)
- Фаза 6 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила

### EVG Conditional Idles — `opt` [#34006](https://www.nexusmods.com/skyrimspecialedition/mods/34006)
- Фаза 6 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: NPC мёрзнет, устал, ранен. Animation Variance не брать — дублирует Remix.

### Goetia Animations — Spell Casting + Conditional Shouts — `opt` [#70204](https://www.nexusmods.com/skyrimspecialedition/mods/70204)
- Также скачать: Shouts: https://www.nexusmods.com/skyrimspecialedition/mods/76388
- Фаза 6 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Каст и крики у NPC-магов. У игрока в VR не видны.

### Leviathan / Vanargand Animations (стойки и атаки NPC) — `opt` [#47092](https://www.nexusmods.com/skyrimspecialedition/mods/47092)
- Фаза 6 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Разнообразие врагов в ближнем бою. Sneak-пакеты для игрока не брать.

### Conditional Tavern Cheering (OAR) — `opt` [#63029](https://www.nexusmods.com/skyrimspecialedition/mods/63029)
- Фаза 6 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила

### Super Fast Get Up Animation — `opt` [#46714](https://www.nexusmods.com/skyrimspecialedition/mods/46714)
- Фаза 6 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: С PLANCK враги падают часто — быстрый подъём не тормозит бой.

### Variadic Collision Dynamics — `try` [#183892](https://www.nexusmods.com/skyrimspecialedition/mods/183892)
- Также скачать: Resources: https://www.nexusmods.com/skyrimspecialedition/mods/184110
- Фаза 6 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Капсула коллизии меняется по позе — меньше застреваний. Капсула игрока в VR — зона PLANCK, конфликт вероятен.

### A-Pose Bug Fix — `try` [#168903](https://www.nexusmods.com/skyrimspecialedition/mods/168903)
- Фаза 6 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Только как лекарство, если появится A-поза. VR не подтверждён.

## 12 Бой и геймплей

### Blade and Blunt + Blade and Blunt VR — `rec` [#34549](https://www.nexusmods.com/skyrimspecialedition/mods/34549)
- Также скачать: VR: https://www.nexusmods.com/skyrimspecialedition/mods/120494
- Фаза 7 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила

### Adamant + Adamant — VR Tweaks — `rec` [#30191](https://www.nexusmods.com/skyrimspecialedition/mods/30191)
- Также скачать: VR Tweaks: https://www.nexusmods.com/skyrimspecialedition/mods/190589
- Фаза 7 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила

### Accuracy — Localized Combat Damage — `opt` [#187578](https://www.nexusmods.com/skyrimspecialedition/mods/187578)
- Фаза 7 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Урон по зонам попадания, 2026 год.

### Core Impact Framework — `opt` [#146873](https://www.nexusmods.com/skyrimspecialedition/mods/146873)
- Фаза 7 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила

### Ricochet — Arrow Physics Framework — `opt` [#160603](https://www.nexusmods.com/skyrimspecialedition/mods/160603)
- Фаза 7 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила

### Dismembering Framework — `opt` [#126203](https://www.nexusmods.com/skyrimspecialedition/mods/126203)
- Фаза 7 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила

### NPCs Take Cover — `opt` [#111890](https://www.nexusmods.com/skyrimspecialedition/mods/111890)
- Фаза 7 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила

### Enemy Friendly Fire — `opt` [#50483](https://www.nexusmods.com/skyrimspecialedition/mods/50483)
- Фаза 7 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: VR-файл: VR
- Установщик: неизвестно — общие правила

### Simple Offence Suppression (VR) — `rec` [#59508](https://www.nexusmods.com/skyrimspecialedition/mods/59508)
- Фаза 7 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Спутники и нейтралы не становятся врагами от случайного удара — с физическим боем это обычное дело.

### Mysticism — A Magic Overhaul — `rec` [#27839](https://www.nexusmods.com/skyrimspecialedition/mods/27839)
- Фаза 7 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Переработка всей магии, пара к Adamant. Без DLL, 7 VR-сборок.

### Thaumaturgy + Apothecary + Mundus — `opt` [#57138](https://www.nexusmods.com/skyrimspecialedition/mods/57138)
- Также скачать: Apothecary: https://www.nexusmods.com/skyrimspecialedition/mods/52130; Mundus: https://www.nexusmods.com/skyrimspecialedition/mods/33411
- Фаза 7 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Зачарование, алхимия и камни-хранители из набора SimonRim. Опциональную DLL Enchantment XP Tweak не ставить без проверки.

### Experience — `opt` [#17751](https://www.nexusmods.com/skyrimspecialedition/mods/17751)
- Фаза 7 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Уровень за квесты и исследование. DLL с VR Address Library, стоит в Stormcrown VR.

### Death Drop Overhaul — `opt` [#151590](https://www.nexusmods.com/skyrimspecialedition/mods/151590)
- Фаза 7 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Оружие убитых падает с инерцией, его можно поднять HIGGS.

### Magic Sneak Attacks VR + Physical Dodge VR — `opt` [#68028](https://www.nexusmods.com/skyrimspecialedition/mods/68028)
- Также скачать: Physical Dodge: https://www.nexusmods.com/skyrimspecialedition/mods/58605
- Фаза 7 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Скрытые атаки магией; уклонение рывком корпуса.

### Throat Slit — VR — `opt` [#184140](https://www.nexusmods.com/skyrimspecialedition/mods/184140)
- Фаза 7 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Горло перерезают движением руки с кинжалом.

### Dynamic Bloodpool Framework — `opt` [#172080](https://www.nexusmods.com/skyrimspecialedition/mods/172080)
- Фаза 7 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Лужи крови растекаются по рельефу. VR Address Library в требованиях, стоит в Panda's Sovngarde.

### DF Asset Packs + Next-Gen Decapitations — `opt` [#126328](https://www.nexusmods.com/skyrimspecialedition/mods/126328)
- Также скачать: Humanoid: https://www.nexusmods.com/skyrimspecialedition/mods/126327; Decapitations: https://www.nexusmods.com/skyrimspecialedition/mods/135254
- Фаза 7 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Нужны, если стоит Dismembering Framework.

### Sanguine Symphony — `opt` [#148388](https://www.nexusmods.com/skyrimspecialedition/mods/148388)
- Фаза 7 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Конфиги Core Impact Framework: отклик зависит от брони и места удара.

## 13 Мир, ИИ, погружение

### Locational Encounter Zones — `rec` [#85212](https://www.nexusmods.com/skyrimspecialedition/mods/85212)
- Фаза 7 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Стража у входа в подземелье того же уровня, что и враги внутри. Одна DLL с VR-пресетом, 6 VR-сборок.

### Don't Stay in The Water — NPC Water AI Fix — `rec` [#52164](https://www.nexusmods.com/skyrimspecialedition/mods/52164)
- Фаза 7 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: VR-файл: VR 4.1
- Установщик: неизвестно — общие правила
- Заметка: NPC перестают стоять в воде и топтаться у кромки в бою. Брать VR-файл 4.1, не AE-версию 5.x.

### Combat Pathing Revolution + VR — `opt` [#86950](https://www.nexusmods.com/skyrimspecialedition/mods/86950)
- Также скачать: VR-DLL: https://www.nexusmods.com/skyrimspecialedition/mods/87895
- Фаза 7 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: NPC в бою кружат, отступают и обходят. Поверх основного — DLL с VR-страницы.

### AI Overhaul — `opt` [#21654](https://www.nexusmods.com/skyrimspecialedition/mods/21654)
- Фаза 7 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Живее распорядок и реакции ванильных NPC. Путь B — файл «SE Only», путь A — AE-файл. Нужны патчи с NPC-модами.

### Realistic AI Detection (RAID) — `opt` [#2345](https://www.nexusmods.com/skyrimspecialedition/mods/2345)
- Фаза 7 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Зорче зрение и слух врагов, дольше поиски, без скриптов. RAID 3 Medium или Lite.

### Smart NPC Potions — `opt` [#40102](https://www.nexusmods.com/skyrimspecialedition/mods/40102)
- Фаза 7 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Враги носят и пьют зелья, используют яды. VR заявлен в changelog.

### NPC Spell Variance — `opt` [#132097](https://www.nexusmods.com/skyrimspecialedition/mods/132097)
- Фаза 7 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Маги-NPC используют весь арсенал. VR-хук исправлен только в 2.7.1 — не брать старее.

### NPCs React To Invisibility + NPCs React To Necromancy — `opt` [#91480](https://www.nexusmods.com/skyrimspecialedition/mods/91480)
- Также скачать: Necromancy: https://www.nexusmods.com/skyrimspecialedition/mods/70428
- Фаза 7 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Озвученные реакции NPC на невидимость и поднятых мертвецов.

### Enhanced Reanimation + VR — `opt` [#43500](https://www.nexusmods.com/skyrimspecialedition/mods/43500)
- Также скачать: VR-файл: https://www.nexusmods.com/skyrimspecialedition/mods/59512
- Фаза 7 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Улучшенное поднятие мёртвых. Основной 1.5.1 и VR-файл 1.5.1 поверх; SE 1.5.2 без VR-обновления не ставить.

### Frozen Electrocuted Combustion VR — `opt` [#59118](https://www.nexusmods.com/skyrimspecialedition/mods/59118)
- Фаза 7 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Замороженные, обугленные и наэлектризованные тела. Брать VR-страницу, не SE 3532.

### Arena — An Encounter Zone Overhaul — `opt` [#33487](https://www.nexusmods.com/skyrimspecialedition/mods/33487)
- Фаза 7 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Опасность растёт по регионам, а не под уровень игрока. Совместим с Locational Encounter Zones.

### Trade and Barter — `opt` [#23081](https://www.nexusmods.com/skyrimspecialedition/mods/23081)
- Фаза 7 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Настройка курсов торговли и золота торговцев.

### Realistic Mining and Chopping for VR + VR Refit — `rec` [#16692](https://www.nexusmods.com/skyrimspecialedition/mods/16692)
- Также скачать: VR Refit: https://www.nexusmods.com/skyrimspecialedition/mods/49205
- Фаза 7 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Руду и дрова добывают настоящими взмахами, а VR Refit роняет их физическими предметами. Файл «for VR - USSEP». 8 VR-сборок.

### Gift by Hand VR — `opt` [#99809](https://www.nexusmods.com/skyrimspecialedition/mods/99809)
- Фаза 7 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Отдать предмет NPC, протянув его рукой.

### Sleeping Expanded — `opt` [#59250](https://www.nexusmods.com/skyrimspecialedition/mods/59250)
- Фаза 7 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Разные позы сна NPC и реакции на спящих.

### Be Seated — Skyrim VR Edition — `opt` [#16613](https://www.nexusmods.com/skyrimspecialedition/mods/16613)
- Фаза 7 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Сесть где угодно — на землю, у костра.

### SunHelm Survival — `opt` [#39414](https://www.nexusmods.com/skyrimspecialedition/mods/39414)
- Фаза 7 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Голод, жажда, усталость, холод. CC-выживание на странице отключено, дубля нет.

### Recipe Auto-Learn + Reading Is Good — `opt` [#84909](https://www.nexusmods.com/skyrimspecialedition/mods/84909)
- Также скачать: Reading Is Good VR: https://www.nexusmods.com/skyrimspecialedition/mods/42026
- Фаза 7 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Рецепты открывают эффекты ингредиентов; книги навыков дают опыт сразу. У Reading Is Good брать VR-файл.

### Mum's the Word NG — `opt` [#77409](https://www.nexusmods.com/skyrimspecialedition/mods/77409)
- Фаза 7 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Снимает метку «украдено», если кражу никто не видел — с HIGGS легко схватить чужое. VR заявлен.

### Honed Metal — `opt` [#61015](https://www.nexusmods.com/skyrimspecialedition/mods/61015)
- Фаза 7 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: VR-файл: VR
- Установщик: неизвестно — общие правила
- Заметка: Кузнецы и маги за плату куют и зачаровывают снаряжение.

### GIST — Genuinely Intelligent Soul Trap — `opt` [#15755](https://www.nexusmods.com/skyrimspecialedition/mods/15755)
- Фаза 7 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Душа идёт в самый подходящий камень.

### SCIE — Crafting Inventory Extender — `opt` [#170497](https://www.nexusmods.com/skyrimspecialedition/mods/170497)
- Фаза 7 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Верстак берёт материалы из ближних сундуков и у спутников. В 2.6 исправлен VR-вылет на старте.

### Dirt and Blood — `opt` [#38886](https://www.nexusmods.com/skyrimspecialedition/mods/38886)
- Фаза 7 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: На телах копятся грязь и кровь, смываются водой. Поставить VR-патч «No Washing Animation».

### Dynamic Things Alternative + Random Barrel Roll — `opt` [#60741](https://www.nexusmods.com/skyrimspecialedition/mods/60741)
- Также скачать: Random Barrel Roll: https://www.nexusmods.com/skyrimspecialedition/mods/78195
- Фаза 7 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Разнообразие контейнеров и случайный поворот бочек через BOS VR.

### Better Resource Warnings — `opt` [#26751](https://www.nexusmods.com/skyrimspecialedition/mods/26751)
- Фаза 7 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Сердцебиение и дыхание при низком здоровье — в шлеме звук заметнее полосок.

### Sink Or Swim NG — `opt` [#78610](https://www.nexusmods.com/skyrimspecialedition/mods/78610)
- Фаза 7 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: В тяжёлой броне игрок тонет и идёт по дну. Сборка NG для AE/VR, не старая 42962.

### Tamrielic Names + NPCs Names Distributor — `opt` [#73153](https://www.nexusmods.com/skyrimspecialedition/mods/73153)
- Также скачать: NND: https://www.nexusmods.com/skyrimspecialedition/mods/73081
- Фаза 7 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Безымянные NPC получают имена по расе. Полезно с ИИ-NPC.

## 14 ИИ-NPC

### SkyrimNet — `opt` [ссылка](https://github.com/MinLL/SkyrimNet-GamePlugin/releases)
- Фаза 9 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Развивается активнее всех, VR-фиксы почти в каждой бете. Для VR требует Skyrim VR ESL Support, Refocused, MFG Fix NG, po3 Tweaks SE и VR. Модели через OpenRouter, часть платная.

### Mantella — `opt` [#98631](https://www.nexusmods.com/skyrimspecialedition/mods/98631)
- Фаза 9 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Проще в настройке, бесплатная модель по умолчанию, голос Piper или XTTS. Замечены вылеты вместе с Fuz Ro D-oh.

### CHIM — `opt` [#126330](https://www.nexusmods.com/skyrimspecialedition/mods/126330)
- Фаза 9 · тип `unknown` · установка `mo2_mod` · надёжность данных `low`
- Файл: основной файл
- Установщик: неизвестно — общие правила
- Заметка: Больше всего возможностей, ставится сложнее всех.

## 15 VR-рантайм и производительность

### OpenComposite Unleashed for Skyrim VR — `rec` [#171182](https://www.nexusmods.com/skyrimspecialedition/mods/171182)
- Фаза 2 · тип `root_files` · установка `root_builder` · надёжность данных `medium`
- Файл: «Open Composite Unleashed for Skyrim VR» 5.0.0 (Stormcrown VR, 2026-09-19). Название страницы на Nexus — «Open Composite XR with Working Keyboard for VR».
- Установщик: неизвестно — общие правила
- Требует: Root Builder (#31720); OpenXR-рантайм: SteamVR, VDXR или Meta (не мод)
- Не вместе с: Skyrim VR OpenComposite Fixes Custom Build (#85389); оверлеи SteamVR (fpsVR не покажется)
- Группа «одно из»: `opencomposite`
- Порядок в MO2: Сепаратор «Инструменты и корень».
- Настройки: openvr_api.dll и opencomposite.ini должны лежать в папке Root внутри мода. Если её нет — создать и перенести туда файлы. Root Builder подменит openvr_api.dll в корне игры. OpenXR-рантайм: в Virtual Desktop Streamer, приложении Oculus и SteamVR выставить один рантайм (SteamVR или VDXR) — по вики FUS. Разрешение рендера менять только в одном месте (opencomposite.ini, SteamVR или VD), иначе оно перемножится. Нагрузку смотреть через Oculus Debug Tool или график Virtual Desktop. После отключения OC: Root Builder → Clear и очистить Overwrite.
- Проверка: В окне SteamVR написано «Now Playing - OpenComposite_SkyrimVR» (по вики FUS), при VDXR игра идёт без SteamVR. Виртуальная клавиатура работает при вводе имени.
- Заметка: OpenXR в обход SteamVR. FUS сообщал о приросте до ~30%. В этой сборке работает виртуальная клавиатура. Оверлеи SteamVR пропадают. DLL — в корень через Root Builder.

### VR FPS Stabilizer — `opt` [#31392](https://www.nexusmods.com/skyrimspecialedition/mods/31392)
- Фаза 2 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: «VR FPS Stabilizer (FOMOD Installer)» 1.4.12 (Stormcrown VR, Tahrovin, 2026-08).
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457)
- Настройки: Целевую частоту в ini задать под частоту шлема. Имена ключей — смотреть в файле мода.
- Проверка: В sksevr.log плагин загружен. В тяжёлых сценах меньше репроекции.
- Заметка: Снижает настройки на лету при просадках.

### S.L.A.C.K. — Save and Load Accelerator — `rec` [#163969](https://www.nexusmods.com/skyrimspecialedition/mods/163969)
- Фаза 2 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `high`
- Файл: «Save.Load.Accelerator.For.SKSE.Cosaves.VR.zip» 1.5.1 (сборка под SKSE 2.0.12 / VR 1.4.15). Из AIO-архива с FOMOD выбрать VR.
- Установщик: Если берёте AIO-архив — выбрать VR. VR.zip ставится без установщика.
- Требует: SKSEVR 2.0.12 (#30457); VR Address Library for SKSEVR (#58101)
- Настройки: Ini «!!!!!!!##$Save&LoadAcceleratorForSKSECosaves.ini» — оставить по умолчанию. Дополняет Seamless Saving VR, не заменяет его.
- Проверка: В sksevr.log плагин загружен. Сохранение и загрузка с ко-сейвом заметно быстрее.
- Заметка: Ускоряет запись и чтение ко-сейвов SKSE в разы. Дополняет Seamless Saving VR. Отдельный VR-архив под SKSEVR 2.0.12.
