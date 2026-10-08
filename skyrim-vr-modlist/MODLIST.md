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
- Настройки: В EngineFixes.toml (7.x), секция [Patches]: bMaxStdIO = true (значение по умолчанию, число не задаётся). Файл создаётся при первом запуске игры. Страница ESL Support требует MaxStdio — true в старых версиях или 4096 в новых. Отдельный ObjectLOD/Shadow Map fix не ставить: он встроен с 7.4.9, а если стоит — удалить.
- Проверка: В sksevr.log Engine Fixes загружен. В логе ESL Support нет предупреждения про MaxStdio. При неправильно поставленном Part 2 плагин не грузится.
- Заметка: Part 1 — мод, Part 2 — в корень. В EngineFixes.toml в секции [Patches] оставить bMaxStdIO = true (по умолчанию): это требование Skyrim VR ESL Support. Старый отдельный ObjectLOD/Shadow Map fix не ставить — он уже внутри с 7.4.9.

### Skyrim VR ESL Support — `core` [#106712](https://www.nexusmods.com/skyrimspecialedition/mods/106712)
- Фаза 2 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `high`
- Файл: Основной «Skyrim VR ESL» 1.3.2 (Stormcrown, Librum, Ygg). С той же страницы: «PapyrusUtil ESL Patch» 1.1 — ставить обязательно, он есть в 7 VR-списках, включая Stormcrown. «RaceMenu ESL Patch» 1.0 — только для старого RaceMenu VR 0.4.14 (#19080, так в Panda). Со RacemenuVR 0.5 (#156898) VR-списки его не ставят.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101); Engine Fixes VR (#62089)
- Не вместе с: Backported Extended ESL Support
- Порядок в MO2: PapyrusUtil ESL Patch — ниже PapyrusUtil VR, чтобы его перезаписать.
- Настройки: Работает только с официальным SKSEVR 2.0.12. Нужен включённый bMaxStdIO в Engine Fixes VR (EngineFixes.toml, секция [Patches]). Ставить до запуска xEdit, LOOT и DynDOLOD. После включения ESL лучше начать новую игру.
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
- Фаза 3 · тип `mixed` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Основной файл «VRIK Player Avatar» 0.8.7 (Stormcrown VR, Yggdrasil VR, Tahrovin - Grit, 2026-09-18). Файл «VRIK Rift-Index-WMR Controller Bindings V2.1.0» — это биндинги SteamVR, в MO2 не ставить: импортировать в SteamVR, если у вас Index/Rift/WMR. Старые 0.8.2–0.8.5 не брать.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); SkyUI VR (#91535)
- Не вместе с: Show Player In Inventory (плоский режим); View Yourself VR (#16809) — клон вместо тела
- Порядок в MO2: Сепаратор «VR-ядро», ниже SkyUI VR и SKSEVR. Все аддоны VRIK (Arctal's Tweaks, Closed Fist, Neutral Animations, Inventory Selfie) — ниже VRIK.
- Порядок плагина: Плагин VRIK из архива — LOOT, ручного порядка нет. Arctal's VRIK Tweaks — после VRIK.
- Настройки: После первого входа: меню VRIK в MCM (SkyUI VR) → калибровка роста и рук. fNearDistance задавать в MCM VRIK (минимум 3.0; меньшие значения мерцают), а не в INI. Три INI VRIK лежат в SKSE\Plugins: сохранить копию перед обновлением. ShowFistWhileUnarmed оставить выключенным, если ставите VRIK Closed Fist. Open Hand Casting выключить, если ставите ISPVR. Без калибровки руки/рост будут неверными.
- Проверка: В sksevr.log строка о загрузке VRIK без ошибки. В игре виден аватар и холстеры, руки следуют за контроллерами; в MCM есть страница VRIK. Сделать цикл «сохранить — загрузить» перед калибровкой.
- Заметка: Тело игрока, холстеры, жесты.

### HIGGS — Enhanced VR Interaction — `core` [#43930](https://www.nexusmods.com/skyrimspecialedition/mods/43930)
- Фаза 3 · тип `mixed` · установка `mo2_mod` · надёжность данных `high`
- Файл: Основной файл «HIGGS» 1.10.10 (Tempus, Stormcrown, SoG, Tahrovin - Grit, Panda's, Librum, Yggdrasil). Старые 1.10.0–1.10.8 не брать.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457)
- Порядок в MO2: «VR-ядро», рядом с VRIK. Все аддоны HIGGS (PLANCK, Physical Collision VR, Pull Arrows, Immersive Harvesting и др.) — ниже HIGGS.
- Порядок плагина: Плагин из архива (higgs_vr.esp) — LOOT; ручного порядка нет.
- Настройки: Настройки HIGGS в higgs_vr.ini (SKSE\Plugins); синее свечение захватываемых объектов отключается ключом DisableShaders=1 (по комментарию на странице Interactive Activators VR). Только PC VR, не Quest-автономка.
- Проверка: В sksevr.log HIGGS загружен без ошибки версии. В игре предмет хватается рукой, работают гравиперчатки и хват оружия двумя руками.
- Заметка: Коллизии рук, хват двумя руками, гравиперчатки.

### PLANCK — `core` [#66025](https://www.nexusmods.com/skyrimspecialedition/mods/66025)
- Фаза 3 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `high`
- Файл: Основной файл «PLANCK» 0.8.1 (Yggdrasil VR, Spirit of Grit, Tahrovin - Grit, 2026-07-30). Версии 0.4–0.7.1 из старых списков не брать.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); HIGGS (#43930) 1.6.0 и новее
- Порядок в MO2: «VR-ядро», ниже HIGGS. PLANCK VR Stability Patch — ниже PLANCK (перезаписывает activeragdoll.dll).
- Настройки: INI PLANCK лежит в SKSE\Plugins (имя файла неизвестно — смотреть в папке мода). При вылетах ставить PLANCK VR Stability Patch (vr-188233). Если ставите NPC Spell Variance — нужен «NPC Spell Variance VR Patch» (GitHub Treatid2): без него возможны проблемы collision-alpha.
- Проверка: В sksevr.log PLANCK загружен без ошибки. Удар или толчок по NPC даёт физическую реакцию (ragdoll); activeragdoll.log создаётся рядом с логами SKSE.
- Заметка: Физические удары и реакции NPC. Требует HIGGS 1.6.0+ и SKSEVR 2.0.12.

### Physical Collision VR — `rec` [#186335](https://www.nexusmods.com/skyrimspecialedition/mods/186335)
- Фаза 3 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `high`
- Файл: Основной файл «PhysicalCollisionVR» 5.2.x (Yggdrasil VR — 5.2.0, 2026-10-03; на странице уже 5.2.1 от 06.10.2026). Версия должна быть 5.0.0 и новее: True Wield VR и Swap Drop and Hold Redux 3.0.0 требуют именно её. Один DLL и один INI, ESP нет.
- Установщик: неизвестно — общие правила. Файл 5.0.0 на Nexus был помечен как FOMOD; архив 5.2.0 в Yggdrasil — без пометки. Если установщик есть и спрашивает про True Wield VR / Swap Drop and Hold — выбрать вариант с ними (они у нас стоят).
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101); VRIK Player Avatar (#23416); HIGGS (#43930); PLANCK (#66025)
- Не вместе с: Pseudo Physical Weapon Collision and Parry (#100781) — делает то же самое; Precision (плоский режим)
- Порядок в MO2: «VR-ядро», ниже HIGGS, PLANCK, VRIK и Immersive Weapon Penetration VR. True Wield VR, Swap Drop and Hold Redux — ниже него.
- Настройки: INI рядом с DLL: жёсткость, размер руки, сила следования; режим коллизии оружия Full / Simple / Off, коллизия рук отдельно. Начать с настроек по умолчанию. Метка AI-Generated на странице.
- Проверка: В sksevr.log DLL загружена. Ладонь упирается в стену, оружие ложится на стол, меч звенит о собственный щит.
- Заметка: Руки и оружие упираются в стены, столы и щит. Требует HIGGS, PLANCK, VRIK. Не совмещать с другими модами коллизии оружия вроде Pseudo Physical Weapon Collision and Parry — они делают одно и то же.

### True Wield VR — `rec` [#191123](https://www.nexusmods.com/skyrimspecialedition/mods/191123)
- Фаза 3 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Основной файл «TrueWieldVR» 1.2.0 (Yggdrasil VR, 2026-10-03). Нужен Physical Collision VR 5.0.0 и новее (лучше 5.2.x, как в Yggdrasil).
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101); Physical Collision VR (#186335); HIGGS (#43930); PLANCK (#66025); VRIK Player Avatar (#23416); MCM Helper (#53000); SkyUI VR (#91535)
- Не вместе с: XPMSSE Weapon Styles — на странице предупреждение о вылетах: не включать этот модуль из XPMSSE
- Порядок в MO2: Ниже Physical Collision VR. Swap Drop and Hold Redux — ниже True Wield VR.
- Настройки: Вес и хват настраиваются в MCM (MCM Helper). Вес оружия задаётся по классам: кинжалы, мечи, топоры и булавы, двуручные, секиры и молоты. Скользить хватом вверх по рукояти — оружие легче.
- Проверка: В sksevr.log DLL загружена. Тяжёлый молот в одной руке «провисает», хват ближе к лезвию делает его легче. В MCM есть страница True Wield.
- Заметка: Масса оружия и хват в любой точке рукояти. Требует Physical Collision VR, MCM Helper, SkyUI VR.

### Immersive Weapon Penetration VR — `rec` [#184223](https://www.nexusmods.com/skyrimspecialedition/mods/184223)
- Фаза 3 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `high`
- Файл: Основной файл «ImmersiveWeaponPenetrationVR» 1.8.0 (Yggdrasil VR, 2026-10-03; Spirit of Grit и Tahrovin - Grit держат 1.6.1). Брать 1.8.0: Swap Drop and Hold Redux 2.0.0+ рекомендует именно её.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101); HIGGS (#43930); PLANCK (#66025); VRIK Player Avatar (#23416)
- Порядок в MO2: «VR-ядро», рядом с Physical Collision VR; Physical Collision VR — ниже него (он уступает руку застрявшему клинку).
- Настройки: Настройки по умолчанию. Метка AI-Generated на странице.
- Проверка: В sksevr.log DLL загружена. Колющий удар входит в тело NPC, вытащить клинок нужно усилием.
- Заметка: Колющий удар входит в тело и застревает. Требует HIGGS, PLANCK, VRIK.

### Swap Drop and Hold Redux — VR — `rec` [#185816](https://www.nexusmods.com/skyrimspecialedition/mods/185816)
- Фаза 3 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Основной файл «SwapDropAndHoldRedux 3.0.0 FOMOD» (Yggdrasil VR, 2026-10-03). Версия 3.0.0 требует Physical Collision VR и True Wield VR.
- Установщик: неизвестно — общие правила. В имени файла есть «FOMOD», а описание Nexus говорит о ручной установке DLL + INI в SKSE\Plugins — опции читать в установщике; при выборе вариантов предпочесть тот, что использует Physical Collision VR и True Wield VR.
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101); HIGGS (#43930); Instant Equip VR (#44571); Physical Collision VR (#186335) — обязателен для 3.0.0; True Wield VR (#191123) — обязателен для 3.0.0
- Не вместе с: Swap Drop and Hold (#49425) и Swap Drop and Hold Add Spells (#55983) — старый скриптовый предшественник; Redux их заменяет (проверить на странице)
- Порядок в MO2: Ниже True Wield VR и Physical Collision VR. Immersive Weapon Penetration VR 1.8.0 — рекомендован.
- Настройки: Файл SwapDropAndHoldRedux.ini в SKSE\Plugins (по описанию Nexus). Метка AI-Generated не подтверждена.
- Проверка: В sksevr.log DLL загружена. Оружие в руке можно сменить, бросить и удержать жестом.
- Заметка: Смена, бросание и удержание предметов в руке.

### Spell Wheel VR — `core` [#47630](https://www.nexusmods.com/skyrimspecialedition/mods/47630)
- Фаза 3 · тип `mixed` · установка `mo2_mod` · надёжность данных `high`
- Файл: Основной файл «Spell Wheel VR» 1.5.11 (Stormcrown, SoG, Tahrovin - Grit, Yggdrasil VR, 2026-08-09). Не брать 1.2–1.5.9 из старых списков. Русский/французский/китайский переводы — отдельные страницы, не нужны.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); Skyrim VR Tools (#27782); SkyUI VR (#91535)
- Порядок в MO2: «VR-ядро», ниже SkyUI VR. Durability VR, Steeds of Ultima VR — ниже Spell Wheel VR.
- Настройки: Колесо и кнопка вызова — в MCM Spell Wheel VR. Работает с HIGGS 1.10.3 и новее. Durability VR требует версию 1.4.12+, Steeds of Ultima — 1.4.2+; наша 1.5.11 их покрывает.
- Проверка: В MCM есть страница Spell Wheel VR; кнопка вызывает колесо с заклинаниями, оружием, зельями.
- Заметка: Выбор заклинаний и предметов жестом, без меню.

### Weapon Throw VR — `rec` [#31374](https://www.nexusmods.com/skyrimspecialedition/mods/31374)
- Фаза 3 · тип `mixed` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Основной файл «Weapon Throw VR» 1.4.0 (Yggdrasil VR, SoG, Tahrovin - Grit, 2026-08-09). Версии 1.3.19–1.3.20 из старых списков не брать: Pull Arrows VR 2.0 просит свежую.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); Skyrim VR Tools (#27782); SkyUI VR (#91535)
- Не вместе с: Throwable Weapons SKSE (#182872) и другие метатели оружия — не вместе
- Порядок в MO2: «VR-ядро», ниже HIGGS. Pull Arrows VR и Durability VR — ниже него.
- Настройки: Настройки в MCM (SkyUI VR). Режим Auto Return влияет на износ в Durability VR: брошенное оружие изнашивается, только если Auto Return включён.
- Проверка: В MCM есть Weapon Throw VR. Оружие, брошенное рукой, летит и (при Auto Return) возвращается. В sksevr.log нет ошибок плагина.

### Interactive Activators VR — `rec` [#161676](https://www.nexusmods.com/skyrimspecialedition/mods/161676)
- Фаза 3 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `low`
- Файл: Основной файл «Interactive Activators VR» 1.1.8 (Yggdrasil, SoG, Tahrovin - Grit, Stormcrown, 2026-08-30). Старые 1.0.3–1.1.6 не брать.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101); HIGGS (#43930)
- Не вместе с: Interactive Pullchains VR — предшественник, заменён этим модом
- Порядок в MO2: «VR-ядро», ниже HIGGS.
- Настройки: Настройки по умолчанию. В комментариях Nexus советуют не ставить Dwemer Gates Don't Reset («Unaggressive Dragon Priests Fix + Dwemer Gates Don't Reset», fixes-69026) вместе с патчем GDOS — проверить, нужен ли патч.
- Проверка: В sksevr.log DLL загружена. Рычаги, цепочки и кнопки двигаются рукой; подсвеченные активаторы можно схватить HIGGS.
- Заметка: Физические рычаги, цепи и кнопки. Заменил Interactive Pullchains VR.

### Instant Equip VR — `rec` [#44571](https://www.nexusmods.com/skyrimspecialedition/mods/44571)
- Фаза 3 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Основной файл «Instant Equip VR» 1.2.0 (Yggdrasil, Stormcrown, Tempus, Panda's, Librum). Не брать 1.0.0 (SoG, Tahrovin - Grit, FUS).
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457)
- Порядок в MO2: «VR-ядро». Swap Drop and Hold Redux и Steeds of Ultima — ниже него.
- Настройки: Не требуется. Нужен Swap Drop and Hold Redux (жёстко) и Steeds of Ultima VR (жёстко).
- Проверка: В sksevr.log плагин загружен. Взятое в руку оружие экипируется мгновенно, без анимации.

### Dialogue Movement Enabler VR — `rec` [#59816](https://www.nexusmods.com/skyrimspecialedition/mods/59816)
- Фаза 3 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Основной файл «Dialogue Movement Enabler VR» 2.3.0 (Stormcrown, SoG, Tahrovin - Grit, Tahrovin, Yggdrasil, 2026-07-02). Не брать 2.2.0 (старые списки).
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101) 0.230.0 и новее
- Не вместе с: Dialogue Movement Enabler (SE, #43708) — плоская версия
- Порядок в MO2: «VR-ядро». No Menu Fade Out VR — ниже него.
- Настройки: Не требуется. Нужен No Menu Fade Out VR (жёстко) и желателен для Immersive NPC Dialogue VR.
- Проверка: В sksevr.log DLL загружена. Во время диалога можно ходить и поворачиваться.

### Stop Trigger Unsheathing For VR — `rec` [#55962](https://www.nexusmods.com/skyrimspecialedition/mods/55962)
- Фаза 3 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `high`
- Файл: Основной файл «STUF VR» 1.0.0 — единственный, во всех 9 VR-листах.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457)
- Не вместе с: Stop Automatic Weapon Draw NG (#99667) — тот же эффект
- Порядок в MO2: Без особых правил.
- Настройки: Не требуется.
- Проверка: Нажатие курка без оружия в руке не вынимает оружие. В sksevr.log нет ошибок плагина.

### Dual Casting Fix VR — `rec` [#92804](https://www.nexusmods.com/skyrimspecialedition/mods/92804)
- Фаза 3 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `high`
- Файл: Основной файл «Dual Casting Fix VR» 1.0.0 — единственный, 8 VR-листов.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101) 0.98.0 и новее
- Не вместе с: Dual Casting Fix (плоский, #92454) — не ставить
- Порядок в MO2: Без особых правил. ESP нет.
- Настройки: Не требуется. На странице нужен VC++ Redistributable.
- Проверка: Двойное заклинание в обеих руках считается двойным (усиленным). В sksevr.log нет ошибок плагина.

### Haptic Skyrim VR — `rec` [#20364](https://www.nexusmods.com/skyrimspecialedition/mods/20364)
- Фаза 3 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Основной файл «Haptic Skyrim VR» 1.8.0 (Stormcrown, SoG, Tahrovin - Grit, Librum, Yggdrasil). Версию 1.7.3 из старых списков не брать: 1.8.0 переписан с нуля как чистый SKSE-плагин без ESP и скриптов.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); Skyrim VR Tools (#27782); VR Address Library for SKSEVR (#58101)
- Не вместе с: Старые версии Haptic Skyrim VR с ESP и скриптами (1.7.x) — удалить до установки 1.8.0
- Порядок в MO2: Без особых правил. ISPVR, Magic Improvements — совместимы.
- Настройки: Параметры задаются INI и через SKSE-интерфейс ChangeSetting(); имя INI неизвестно — смотреть в папке мода.
- Проверка: В sksevr.log плагин загружен. Контроллеры вибрируют при натяжении лука, касте и ударе.
- Заметка: Отдача в контроллеры от лука, магии и ударов.

### Seamless Arrow Nocking VR + Immersive Crossbow Reload VR — `rec` [#117254](https://www.nexusmods.com/skyrimspecialedition/mods/117254)
- Также скачать: Crossbow Reload: https://www.nexusmods.com/skyrimspecialedition/mods/139152
- Фаза 3 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Два архива. 1) «Seamless Arrow Nocking» 1.0.4 (#117254, 6 VR-листов). 2) «Immersive Crossbow Reload VR» 1.0.4 (#139152, 8 VR-листов). Ставить каждый как отдельный мод.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101); Skyrim VR Tools (#27782)
- Порядок в MO2: Ниже Simple Realistic Archery VR. Pull Arrows VR — совместим.
- Настройки: В INI Seamless Arrow Nocking есть опция запрета стрельбы при низкой выносливости; по желанию. Требования Crossbow Reload отдельно не проверены.
- Проверка: В sksevr.log оба плагина загружены. Стрела накладывается на тетиву рукой без пауз; арбалет перезаряжается жестом.

### Magic Improvements for Skyrim VR — `rec` [#55751](https://www.nexusmods.com/skyrimspecialedition/mods/55751)
- Фаза 3 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `high`
- Файл: Основной файл «MISVR» 1.2.0 — единственный, во всех 9 VR-листах.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457)
- Не вместе с: SpellBender VR (#164902) и Spell Auto-Aim VR (#119689) — перекрываются по прицеливанию заклинаний, подбирать вместе осторожно
- Порядок в MO2: Без особых правил.
- Настройки: INI в SKSE\Plugins (имя неизвестно). Исходники — GitHub adamhynek/misvr.
- Проверка: В sksevr.log плагин загружен. Огненные шары и молнии ведут себя лучше, прицел заклинаний от руки.

### Lethal Unarmed VR — `opt` [#191124](https://www.nexusmods.com/skyrimspecialedition/mods/191124)
- Фаза 3 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `low`
- Файл: Основной файл «LethalUnarmedVR 3.0.0 FOMOD» (Yggdrasil VR, 2026-10-03). Автор Asterrath, метка AI Assisted.
- Установщик: неизвестно — общие правила (в имени файла есть «FOMOD»; опции на странице не найдены, читать установщик).
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101); HIGGS (#43930); VRIK Player Avatar (#23416); PLANCK (#66025)
- Порядок в MO2: Ниже Physical Collision VR и Immersive Weapon Penetration VR. VRIK Closed Fist — рядом.
- Настройки: Настройки по умолчанию. Хват за руку, бросок и удушение работают через HIGGS.
- Проверка: В sksevr.log DLL загружена. Схватить врага за руку — можно тащить и бросать; рука на горле — удушение.
- Заметка: Захваты: схватить за руку, бросить, придушить.

### VR Climbing — Aelove Ver — `opt` [#170321](https://www.nexusmods.com/skyrimspecialedition/mods/170321)
- Фаза 3 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Основной файл «VR Climbing - Aelove Version» 0.11.3 (Tahrovin - Grit и Yggdrasil VR, 2026-09-19). Оригинал «VR Climbing» (#168553, 0.11.0) НЕ ставить: форк самостоятельный.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101); HIGGS (#43930); Skyrim VR Tools (#27782)
- Не вместе с: VR Climbing (#168553) — оригинал; нужен один из двух; SkyClimb, SkyParkour, StepUpOnto, EVG Animated Traversal (плоский режим)
- Группа «одно из»: `climbing`
- Порядок в MO2: Ниже HIGGS.
- Настройки: Доп. параметры (например, минимум выносливости для лазания, по умолчанию 75; 0 — отключить) — в INI мода; имя INI неизвестно (у оригинала VRClimbing.ini). Метка AI-generated.
- Проверка: В sksevr.log плагин загружен. Скалы и уступы можно хватать контроллерами и подтягиваться.
- Заметка: Форк VR Climbing с доп. настройками, свежие VR-сборки перешли на него. Ставить вместо оригинала 168553. Нужны HIGGS и Skyrim VR Tools. Метка AI-generated.

### Spellsiphon — `opt` [#26627](https://www.nexusmods.com/skyrimspecialedition/mods/26627)
- Фаза 3 · тип `mixed` · установка `mo2_mod` · надёжность данных `low`
- Файл: Основной файл «Spellsiphon - Complete Edition» 5.28 (Tempus, FUS, Panda's, Yggdrasil). Версия 5.27 у SoG/Tahrovin; отдельный патч кинжальной анимации не нужен (он в Complete Edition). Файл «Book at Archmage Quarters» не нужен.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); Skyrim VR Tools (#27782)
- Порядок в MO2: Без особых правил. ISPVR рекомендован как пара.
- Порядок плагина: Обычный ESP — LOOT.
- Настройки: Назначение кнопок — в игре (в FUS есть схема биндингов Spellsiphon). Мод работает и в VR, и в плоском режиме; для лука рекомендуют Simple Realistic Archery VR.
- Проверка: Заклинания вызываются жестом, перерыв между кастами работает. Нет конфликта с ISPVR.
- Заметка: Жестовая магия.

### To Your Face — `opt` [#24720](https://www.nexusmods.com/skyrimspecialedition/mods/24720)
- Фаза 3 · тип `plugin_only` · установка `mo2_mod` · надёжность данных `low`
- Файл: Файл «To Your Face VR» 1.0f (Tempus, Stormcrown, Panda's, Librum, FUS, Yggdrasil). Файл «To Your Face SE» 1.0h (в Librum) НЕ брать.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457)
- Порядок в MO2: Без особых правил.
- Порядок плагина: ESP — LOOT.
- Настройки: Не требуется.
- Проверка: Собеседник в диалоге поворачивается лицом к игроку.

### Sprint Jump VR — `opt` [#28354](https://www.nexusmods.com/skyrimspecialedition/mods/28354)
- Фаза 3 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Основной файл «SprintJumpVR» 2.0.2 (7 VR-листов). Не брать 1.x.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457)
- Не вместе с: Auto Sneak and Jump VR (#23649) — выбрать одну схему прыжка (отключить авто-прыжок там)
- Порядок в MO2: Без особых правил.
- Настройки: INI в SKSE\Plugins (имя неизвестно). Многократный прыжок включается там же.
- Проверка: Прыжок во время бега работает. В sksevr.log нет ошибок плагина.

### Arctal's VRIK Tweaks — `rec` [#63663](https://www.nexusmods.com/skyrimspecialedition/mods/63663)
- Фаза 3 · тип `mixed` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Основной файл «Arctals VRIK Tweaks» 2.0 (Panda's, Librum, FUS, Tempus, Yggdrasil). Варианты «Merged» (1.2) и 1.9 не брать. Русификация — отдельная страница #165797 (по желанию).
- Установщик: неизвестно — общие правила
- Требует: VRIK Player Avatar (#23416); Skyrim VR ESL Support (#106712) — плагин ESL
- Не вместе с: Arctal's VRIK Tweaks - Merged (старый вариант)
- Порядок в MO2: Ниже VRIK.
- Порядок плагина: ESL-плагин — после VRIK.esp; LOOT. Не обновлять посреди сохранения со старой версии (ESL-сжатие).
- Настройки: Ползунок NearDist убран: fNearDistance теперь в MCM VRIK. Остальное — MCM Arctal's Tweaks (быстрые жесты для заклинаний и криков, ragdoll).
- Проверка: В MCM есть страница Arctal's VRIK Tweaks. В sksevr.log нет ошибок. Жесты работают.
- Заметка: Быстрые жесты для заклинаний и криков, правка ragdoll, fNearDistance против мерцания снега. 8 VR-сборок, есть русификация.

### No Stagger Mod — `rec` [#16335](https://www.nexusmods.com/skyrimspecialedition/mods/16335)
- Фаза 3 · тип `plugin_only` · установка `mo2_mod` · надёжность данных `high`
- Файл: Файл «NoStaggerMod v 1.0» — единственный, 9 VR-листов.
- Установщик: неизвестно — общие правила
- Порядок в MO2: Без особых правил.
- Порядок плагина: ESP на 1 КБ — LOOT.
- Настройки: Не требуется. Игрок перестаёт шататься от ударов — баланс сложности смещается.
- Проверка: Удар по игроку не дёргает камеру.
- Заметка: Убирает пошатывание игрока — в VR оно дёргает камеру и укачивает. Во всех 9 VR-сборках.

### Neutral VR Animations for VRIK — `opt` [#28831](https://www.nexusmods.com/skyrimspecialedition/mods/28831)
- Фаза 3 · тип `mixed` · установка `mo2_mod` · надёжность данных `low`
- Файл: Файл «Neutral VR Animations for VRIK and PCEA2» 0.0.1 (FUS, Panda's, Tahrovin, Tempus, Yggdrasil). Единственный файл.
- Установщик: неизвестно — общие правила
- Требует: VRIK Player Avatar (#23416)
- Порядок в MO2: Ниже VRIK и Open Animation Replacer.
- Настройки: Содержит анимации: если в архиве есть папки FNIS/Nemesis_Engine, после установки запустить Pandora (группа behavior-engine). Неизвестно — проверить архив.
- Проверка: Тело VRIK не принимает боевые стойки при ходьбе. После Pandora — без ошибок.
- Заметка: Тело VRIK не принимает боевые стойки.

### SKSEVR Perk Extender — `opt` [#16330](https://www.nexusmods.com/skyrimspecialedition/mods/16330)
- Фаза 3 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `high`
- Файл: Файл «SKSEVR Perk Extender» 2.0 — единственный, 8 VR-листов.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457)
- Порядок в MO2: Содержит statsmenu.swf — он должен ПОБЕЖДАТЬ у UI-модов: ставить НИЖЕ Norden UI VR и SkyUI VR (нижний в списке MO2 имеет больший приоритет).
- Настройки: Не требуется.
- Проверка: Вход в дерево перков не вылетает, большие перк-моды открываются.
- Заметка: Без него большие перк-моды вылетают при входе в дерево. Его statsmenu.swf не давать перезаписать.

### Smooth Carriage Ride VR + Im Walkin' Here VR — `opt` [#129594](https://www.nexusmods.com/skyrimspecialedition/mods/129594)
- Также скачать: Im Walkin' Here: https://www.nexusmods.com/skyrimspecialedition/mods/39433
- Фаза 3 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Два архива. 1) «SmoothCarriageRideVR» 0.5 (#129594, 5 VR-листов). 2) «ImWalkinHereVR» v0.2 BETA (#39433, 4 VR-листа). Ставить отдельными модами.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101); VRIK Player Avatar (#23416) 0.8.4 и новее (иначе карета переворачивает вид)
- Порядок в MO2: Ниже VRIK.
- Настройки: Не требуется. Smooth Carriage Ride сглаживает только дрожание положения; Touring Carriages поддержан экспериментально.
- Проверка: В карете камера не дёргается. Im Walkin' Here: NPC не толкают игрока.
- Заметка: Комфорт: карета не трясёт камеру, NPC не сдвигают игрока толчками.

### No more werewolf hat — `opt` [#104975](https://www.nexusmods.com/skyrimspecialedition/mods/104975)
- Фаза 3 · тип `assets_only` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Файл «No more werewolf hat» 1.0 (Librum VR, SoG, Tahrovin, Tahrovin - Grit). Только меш.
- Установщик: неизвестно — общие правила
- Не вместе с: Другие замены меша оборотня — не вместе
- Порядок в MO2: Ниже модов тела/существ, которые меняют меш оборотня (победить должен этот).
- Настройки: Не требуется.
- Проверка: Голова оборотня не закрывает обзор.
- Заметка: Голова вервольфа больше не закрывает обзор.

### VR Equip — `opt` [#83092](https://www.nexusmods.com/skyrimspecialedition/mods/83092)
- Фаза 3 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Файл «VR Equip» 1.3.2 (FUS, Panda's, Tempus, Yggdrasil).
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); HIGGS (#43930); VRIK Player Avatar (#23416)
- Порядок в MO2: Ниже HIGGS и VRIK. Instant Equip VR — рядом (парные моды).
- Настройки: Для ног советуют Feet max height=60 и Feet width=40 (по странице).
- Проверка: Поднести вещь к голове — одеть шлем, к торсу — броню, к ногам — обувь.
- Заметка: Поднёс вещь к телу — надел, ко рту — съел.

### Auto Sneak and Jump VR — `opt` [#23649](https://www.nexusmods.com/skyrimspecialedition/mods/23649)
- Фаза 3 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Файл «Auto Sneak and Jump VR» 0.5.0 (6 VR-листов).
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457)
- Не вместе с: Sprint Jump VR (#28354) — выбрать одну схему прыжка; Встроенный Physical Sneaking Skyrim VR — отключить в настройках игры (playroom)
- Порядок в MO2: Без особых правил.
- Настройки: В INI JumpThreshold (порог роста головы для прыжка); авто-прыжок можно ослабить там же. Известная жалоба: «залипание» приседа.
- Проверка: Реальное приседание включает скрытность.
- Заметка: Скрытность — когда реально приседаете, прыжок — когда подпрыгиваете. Со Sprint Jump VR выбрать одну схему.

### Spell Auto-Aim VR — `opt` [#119689](https://www.nexusmods.com/skyrimspecialedition/mods/119689)
- Фаза 3 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Файл «Spell Auto Aim VR» 1.0.1 (Tempus, Panda's, Tahrovin, FUS).
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457)
- Не вместе с: SpellBender VR (#164902) — взаимоисключаются (автор SpellBender); Magic Improvements for Skyrim VR — частично дублирует прицеливание, подбирать силу
- Порядок в MO2: Без особых правил.
- Настройки: В INI подобрать силу автонаведения. DLL + конфиг, ESP нет.
- Проверка: Заклинания слегка доводятся до цели.
- Заметка: Мягкое автонаведение заклинаний. Не совместим со SpellBender VR.

### Durability VR + Immersive Smithing — `opt` [#76830](https://www.nexusmods.com/skyrimspecialedition/mods/76830)
- Также скачать: Immersive Smithing: https://www.nexusmods.com/skyrimspecialedition/mods/72298
- Фаза 3 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Два архива. 1) «Durability VR» 1.1.4 (Spirit of Grit, Tahrovin - Grit, 2025-11-09). 2) «Immersive Smithing» 1.0.5 (#72298; Panda's, SoG): HIGGS 1.5.8+, PLANCK 0.4.6+, Spell Wheel VR 1.3.0+, последний VRIK. Из страницы Immersive Smithing взять ещё «EmbersXD - Compatibility Patch» (у нас Embers XD).
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); Spell Wheel VR (#47630) 1.4.12 и новее; HIGGS (#43930); PLANCK (#66025); VRIK Player Avatar (#23416); Weapon Throw VR (#31374) 1.3.14 и новее — если ставите
- Порядок в MO2: Ниже Spell Wheel VR и Weapon Throw VR. Immersive Smithing — ниже Durability VR; EmbersXD Compatibility Patch — ниже Embers XD и Immersive Smithing.
- Настройки: Износ и полоски на запястье настраиваются в MCM. «SIMM Compatible Smelter» — только если ставите SIMM (в манифесте нет).
- Проверка: На запястье полоски износа. У наковальни можно починить и улучшить молотом. В sksevr.log нет ошибок.
- Заметка: Износ снаряжения с полосками на запястье и физическая кузня с молотом.

### PLANCK VR Stability Patch — `opt` [#188233](https://www.nexusmods.com/skyrimspecialedition/mods/188233)
- Фаза 3 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Файл «PLANCK VR Stability Patch» 1.3.1 (Tahrovin - Grit, 2026-09-21; Nexus-страница 188233). На GitHub уже вышли 1.3.2 (21.09, pre-release: давал нестабильность VRIK) и 1.3.3 (23.09, pre-release, исправление); брать 1.3.1, если на Nexus нет более нового стабильного файла.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); PLANCK (#66025) ровно 0.8.1
- Не вместе с: PLANCK других версий (0.7.x и ранее)
- Порядок в MO2: Ниже PLANCK; перезаписывает activeragdoll.dll (разрешить замену).
- Настройки: В INI PLANCK секция [Settings]: enableWeaponNodeRebinding=true (false — отключить), rebindUnobservedWeaponNodes=false; в 1.3.3 добавлен enableHiggsBodyReportingQualityRefresh. Настройки не перечитываются на лету. При сбое приложить activeragdoll.log.
- Проверка: В activeragdoll.log есть строка версии патча. Вылетов PLANCK при ударах по NPC нет.
- Заметка: Неофициальная пересборка DLL PLANCK 0.8.1. Ставить, если PLANCK вылетает. Перезаписывает activeragdoll.dll.

### VRIK Closed Fist — `opt` [#182410](https://www.nexusmods.com/skyrimspecialedition/mods/182410)
- Фаза 3 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Файл «VRIK Closed Fist» 1.1 (страница), в списках: Tahrovin 1, SoG и Grit без номера. Берите последнюю.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VRIK Player Avatar (#23416)
- Не вместе с: Опция ShowFistWhileUnarmed в VRIK — не включать одновременно
- Порядок в MO2: Ниже VRIK. Lethal Unarmed VR — рядом.
- Настройки: Работает через VRIK API, настроек нет.
- Проверка: При обнажённых кулаках руки сжимаются в кулак.
- Заметка: Свободные руки сжимаются в кулак. Пара к Lethal Unarmed VR.

### Steeds of Ultima — VR Mounted Combat — `opt` [#81220](https://www.nexusmods.com/skyrimspecialedition/mods/81220)
- Фаза 3 · тип `mixed` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Основной файл «Steeds of Ultima - VR» 1.1.2 (Tempus VR, Librum VR, 2025-08). Не брать 1.1.0–1.1.1.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); Pandora Behaviour Engine+ (#133232) (или Nemesis); Spell Wheel VR (#47630) 1.4.2 и новее; Instant Equip VR (#44571); VRIK Player Avatar (#23416) 0.8.2 и новее
- Не вместе с: HorsePower, Skyrim Mounted Movesets (плоский режим)
- Порядок в MO2: Ниже Spell Wheel VR и Instant Equip VR.
- Настройки: После установки обязательно запустить Pandora из MO2 (нужен Nemesis-патч поведений).
- Проверка: После Pandora без ошибок. С седла работают магия, крики, посохи.
- Заметка: Магия, крики и посохи с седла. Nemesis-патч собрать через Pandora.

## 06 Хайтек 2026

### Smooth Terrain — `rec` [#186875](https://www.nexusmods.com/skyrimspecialedition/mods/186875)
- Фаза 8 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `high`
- Файл: Основной файл «Smooth Terrain» 0.6.0 (Yggdrasil VR, 2026-08-27). Один DLL для SE/AE/VR.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101) свежая (в Offsets есть VR 1.4.15)
- Не вместе с: Dynamic Terrain Deformation (только SE/AE, в списке «не ставить»)
- Порядок в MO2: Ниже Open Shaders. DynamicShader — DynamicSnow — ниже него.
- Настройки: SKSE\Plugins\SmoothTerrain.ini: iSubdivisions=2 (0–3, 4×/16×/64× треугольников), fMaxRise=20.0, iSmoothedQuads=3, iGradientStep=2. Для VR начать с умолчаний; если fpsVR показывает перегрузку — iSubdivisions=1 и iSmoothedQuads=2. Метка AI Assisted.
- Проверка: В sksevr.log плагин загружен. Холмы без углов, коллизия не изменилась. Время кадра в Вайтране и Ривервуде в норме.
- Заметка: Ваш пример. На лету дробит меши ландшафта вокруг игрока: холмы без углов, коллизия и сейвы не меняются. Одна DLL на SE/AE/VR (видно в исходниках), стоит в Yggdrasil VR рядом с Open Shaders. Метка AI Assisted. Начните с настроек по умолчанию и сверьте время кадра.

### Helios + MMSF, Luma Utility, XEMI Utility — `opt` [#181533](https://www.nexusmods.com/skyrimspecialedition/mods/181533)
- Также скачать: MMSF: https://www.nexusmods.com/skyrimspecialedition/mods/183073; Luma: https://www.nexusmods.com/skyrimspecialedition/mods/177961; XEMI: https://www.nexusmods.com/skyrimspecialedition/mods/159084
- Фаза 8 · тип `mixed` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Четыре архива одной связкой (Stormcrown VR, июль 2026): «Helios» 1.01 (#181533), «MMSF» 1.1.0.0 (#183073), «Luma Utility» 1.7.0.0 (#177961), «XEMI Util» 1.6.0.0 (#159084). Luma и MMSF 2.x НЕ брать: Helios 1.01 с ними несовместим (использует удалённую Papyrus-функцию).
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101); Regional Sounds Expansion + Reverb Interior Sounds Expansion (#77829) — если у погоды нет звуков интерьера
- Не вместе с: Luma Utility 2.x и MMSF 2.x; DIAL (#149920) — предшественник; Region Weather - Engine Fix (#191323) — автор признаёт несовместимость
- Порядок в MO2: Luma, MMSF, XEMI — любой порядок (у Luma порядок не важен); Helios — ниже Lux и CS Light, чтобы подчинить их интерьерный свет погоде.
- Порядок плагина: Helios.esp — после Lux и CS Light; LOOT.
- Настройки: Пары версий строго: MMSF 1.1.0.0 с Luma 1.7.0.0; смешивание версий даёт вылеты (API MMSF переписан в 2.0). В Helios 1.01 своей DLL нет.
- Проверка: В sksevr.log загружены Luma, MMSF, XEMI. В интерьере с окнами свет меняется с погодой и временем суток.
- Заметка: Ваш пример, преемник DIAL: свет в интерьерах с окнами следует за погодой и временем суток. Набор версий как в Stormcrown VR: Helios 1.01, Luma 1.7, MMSF 1.1, XEMI 1.6. Luma и MMSF 2.x с ним несовместимы. С интерьерным светом Lux связку никто не проверял.

### Inventory Selfie VR — Redux — `rec` [#190704](https://www.nexusmods.com/skyrimspecialedition/mods/190704)
- Фаза 8 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Основной файл «Inventory Selfie VR - Redux» 1.3 (исправляет вылет с HDT-SMP; Tahrovin - Grit ставит 1.2).
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101); VRIK Player Avatar (#23416) 0.8.7 и новее
- Не вместе с: View Yourself VR (#16809) — клон; Show Player In Inventory (плоский режим)
- Порядок в MO2: Ниже VRIK.
- Настройки: Работает через настройку VRIK showBodyInMenu; настроек в Redux нет.
- Проверка: В инвентаре виден настоящий аватар VRIK, а не клон.
- Заметка: VR-замена Show Player In Inventory: в меню видно настоящее тело VRIK, без клона. Нужен VRIK 0.8.7+. Берите 1.3 — в ней исправлен вылет с HDT-SMP. Стоит в Tahrovin — Grit. Со старым View Yourself VR вместе не ставить.

### Pull Arrows VR — Immersive Extraction — `rec` [#169833](https://www.nexusmods.com/skyrimspecialedition/mods/169833)
- Фаза 8 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Основной файл «Pull Arrows VR» 2.0.0 (Spirit of Grit, Tahrovin - Grit, 2026-07-12). 1.2.0 (Panda's) не брать.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101); HIGGS (#43930); Weapon Throw VR (#31374) — последняя версия; SkyUI VR (#91535)
- Порядок в MO2: Ниже Weapon Throw VR, HIGGS и Broken Feathers.
- Настройки: Настройки в MCM (шанс поломки стрелы при вытаскивании). Запускать через sksevr_loader.exe.
- Проверка: Стрела или болт, вытаскиваемые рукой из тела, с сопротивлением, звуком и кровью.
- Заметка: Стрелы, болты и брошенное оружие вытаскиваются из тел рукой: с сопротивлением, звуком и кровью. Нужны HIGGS, Weapon Throw VR и Broken Feathers. Есть в трёх VR-сборках.

### Cold Breath NG — `rec` [#174838](https://www.nexusmods.com/skyrimspecialedition/mods/174838)
- Фаза 8 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `low`
- Файл: Основной файл «Cold Breath NG» последней версии (SE-листы берут 1.8). Автор заявляет поддержку 1.5.97/1.6/VR.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Не вместе с: Wet and Cold Breath и другие скриптовые моды пара изо рта — убрать
- Порядок в MO2: Без особых правил.
- Настройки: Не требуется.
- Проверка: В sksevr.log нет ошибок. У NPC в Винтерхолде идёт пар изо рта.
- Заметка: Пар изо рта на холоде у игрока, NPC и существ, без скриптов. Автор прямо пишет «для 1.5.97/1.6/VR». Старые скриптовые моды пара убрать. Проверка: у NPC в Винтерхолде идёт пар, в sksevr.log нет ошибок.

### Interactive Waters — VR (beta) — `opt` [#166560](https://www.nexusmods.com/skyrimspecialedition/mods/166560)
- Фаза 8 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Основной файл «Interactive Waters - VR» (в VR-листах — «Interactive Water VR» 1.2.2.1; на странице уже 1.3.1). Брать последний; при проблемах — 1.2.2.1 (Librum VR, Panda's Sovngarde).
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Порядок в MO2: Ниже воды Open Shaders / Splashes of Skyrim VR.
- Настройки: В бета-версии мод не включается на новой игре: загрузить сохранение. Проверить вместе с Splashes of Skyrim VR и водой Open Shaders.
- Проверка: Рука в воде даёт рябь, волны и брызги.
- Заметка: Руки поднимают на воде рябь, волны и брызги, эффект зависит от скорости и силы удара. Только VR, стоит в Librum VR и Panda's Sovngarde. Бета.

### Immersive Harvesting VR — `opt` [#186754](https://www.nexusmods.com/skyrimspecialedition/mods/186754)
- Фаза 8 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Основной файл «Immersive Harvesting» 1.5.23 (Yggdrasil VR, 2026-09-19).
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101) 0.194 и новее; HIGGS (#43930)
- Не вместе с: Smart Harvest NG AutoLoot (#37091); IHarvest (#27789); Dynamic Looting and Harvesting Animations; Любые автосборы
- Порядок в MO2: Ниже HIGGS и Interactive Activators VR.
- Настройки: Настройки по умолчанию. Метка AI-Generated Content.
- Проверка: Растения срываются рукой через HIGGS, ингредиент сразу в ладони.
- Заметка: Растения срываются рукой через HIGGS, ингредиент сразу в ладони. Стоит в Yggdrasil VR. Метка AI-Generated. С автосбором не совмещать.

### ISPVR — Immersive Spellcasting VR — `opt` [#164183](https://www.nexusmods.com/skyrimspecialedition/mods/164183)
- Фаза 8 · тип `mixed` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Основной файл «ISPVR - Immersive Spellcasting VR» 1.1.1 (Panda's Sovngarde). Опциональный патч HIGGS — по желанию.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101); HIGGS (#43930); VRIK Player Avatar (#23416)
- Не вместе с: Open Hand Casting в VRIK (выключить в MCM VRIK)
- Порядок в MO2: Ниже VRIK и MISVR.
- Порядок плагина: ESP — включить в plugins.txt; LOOT.
- Настройки: В MCM VRIK выключить Open Hand Casting. Для контроллеров без ремней выключить опцию Immersive Input. MCM — SkyUI VR (по желанию).
- Проверка: Сжал кисть — заряд, вибрация — готово, раскрыл — выстрел.
- Заметка: Магия кистью: сжал — заряд, вибрация — готово, раскрыл ладонь — выстрел. В VRIK выключить Open Hand Casting. Стоит в Panda's Sovngarde.

### Steeds of Omega VR — NPC Mounted Combat — `opt` [#169221](https://www.nexusmods.com/skyrimspecialedition/mods/169221)
- Фаза 8 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Основной файл «Steeds of Omega - VR (Mounted NPC combat)» 0.9.5 beta (Tempus VR).
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Не вместе с: HorsePower, Skyrim Mounted Movesets (плоский режим)
- Порядок в MO2: Ниже Steeds of Ultima VR.
- Настройки: Бета. Рекомендуются Steeds of Ultima VR, Glaive Danger, Hold Riders, Horsemen Torch Wield Fix (для последнего нужен Pandora).
- Проверка: Конные NPC в бою атакуют, отходят и не падают с лошадей.
- Заметка: Конные NPC в бою атакуют, отходят и не падают с лошадей; всадника можно стащить через HIGGS. Пара к Steeds of Ultima VR. Стоит в Tempus VR.

### Dynamic Footprints SKSE — `try` [#175254](https://www.nexusmods.com/skyrimspecialedition/mods/175254)
- Фаза 8 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Основной файл «Dynamic Footprints Skse BASE» v2.3 (LoreRim, Wunduniik, CSVP). Файлы «NMN DynamicFootprints CPM Vanaheimr» — пресеты текстур, не нужны. Аддон Beast Race Expansion (#177496) — по желанию.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101); Keyword Item Distributor (#55728) — необязательно
- Не вместе с: Footprints + SPID for Footprints (#3808); DynamicShader — DynamicSnow (дублируют следы)
- Группа «одно из»: `footprints`
- Порядок в MO2: Ниже Footprints-модов, если оставите их ненадолго для проверки.
- Настройки: Автор: «рассчитан на SE, AE и VR, VR проверить не могу», есть отзыв о работе в VR.
- Проверка: В sksevr.log строка о загрузке DynamicFootprints без ошибок. По снегу у Виндхельма остаются следы игрока и NPC.
- Заметка: Работающая в VR часть идеи Dynamic Terrain Deformation: следы игрока, NPC и существ на снегу, пепле и песке. Автор: «рассчитан на SE, AE и VR, VR проверить не могу», есть отзыв о работе в VR. Вместо старых Footprints, не вместе.

### DynamicShader — DynamicSnow — `try` [#189713](https://www.nexusmods.com/skyrimspecialedition/mods/189713)
- Фаза 8 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `low`
- Файл: Релиз «DynamicSnow-v630» (2026-08-30), плагин DynamicSnow.dll. Нужен ещё DynamicShader Core (DynamicShader.dll).
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101); Smooth Terrain (#186875)
- Не вместе с: Dynamic Footprints SKSE (#175254); Фича динамического снега Community Shaders / Open Shaders
- Группа «одно из»: `snow-deformation`
- Порядок в MO2: Порядок: Smooth Terrain → DynamicShader Core → DynamicSnow (нижний выше по приоритету).
- Настройки: SKSE\Plugins\DynamicSnow.ini, [General] MaxFootprints=100–2000 (по умолчанию 400); для VR начать со 100. Перезапуск игры для применения. README заявляет только SE/AE, VR не подтверждён: пробовать на отдельном сохранении.
- Проверка: В sksevr.log обе DLL (DynamicShader и DynamicSnow) загружены. DynamicSnow.log не пуст. В снегу у Виндхельма остаются борозды.
- Заметка: Настоящая деформация вершин ландшафта поверх Smooth Terrain: колеи в снегу, песке и грязи. В README только SE/AE, VR не подтверждён. Только для эксперимента на отдельном сохранении, не вместе с Dynamic Footprints.

### XPMF — Extended Projected Materials Framework — `try` [#192698](https://www.nexusmods.com/skyrimspecialedition/mods/192698)
- Фаза 8 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Основной файл «XPMF» 0.7.0 (Morning Star, 2026-10-03). Профили — JSON в Data\SKSE\Plugins\XPMF\: snow.json, snow_pbr.json, ash.json, ash_pbr.json.
- Установщик: неизвестно — общие правила (в пакете 4 профиля; оставить пары под тип текстур ландшафта: *_pbr — для PBR).
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101) 0.266.0 и новее
- Порядок в MO2: Ниже Seasons of Skyrim. Simplicity of Snow Sulfur Ash Moss (#192910) — ниже XPMF.
- Настройки: Профили: snow / ash и их _pbr-варианты — выбрать по текстурам (текстуры — поздний этап, вернуться к выбору). Версия 0.x.
- Проверка: В sksevr.log XPMF загружен. Под крышами и укрытиями чисто, на открытых местах снег по текстуре земли.
- Заметка: Проецируемый снег и пепел на объектах: текстура как у земли, под крышами чисто, учитывает Seasons of Skyrim. VR заявлен, нужен VR Address Library 0.266+. Версия 0.x.

### Frostwalker — `try` [#184628](https://www.nexusmods.com/skyrimspecialedition/mods/184628)
- Фаза 8 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Основной файл «Frostwalker» 2.2 (True North, 2026-09-23).
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Порядок в MO2: Без особых правил.
- Настройки: Настройки — SKSE\Plugins\Frostwalker.ini (плагин сам его записывает). Метка AI-assisted не подтверждена.
- Проверка: Морозное заклинание в воду создаёт льдины, по ним можно идти.
- Заметка: Морозная магия превращает воду в льдины, по которым можно идти. В исходниках есть отдельные VR-адреса. Проверка: заморозить воду морозным заклинанием.

### Bobbing Framework — `try` [#186081](https://www.nexusmods.com/skyrimspecialedition/mods/186081)
- Фаза 8 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `low`
- Файл: Основной файл «Bobbing Framework» последней версии. VR-листов нет.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101); SKSE Menu Framework (#120352); ImGui VR Helper (#183466)
- Порядок в MO2: Ставить вместе с Dynamic Wind (world-177023) — ниже него.
- Настройки: Меню настроек — через SKSE Menu Framework. В VR автор отключил хук отрисовки из-за вылетов: эффект может быть слабее.
- Проверка: В sksevr.log нет ошибок. Лодки у Рифтена покачиваются.
- Заметка: Лодки и плавучие предметы покачиваются на воде без замены мешей. В VR автор отключил хук отрисовки из-за вылетов. Проверка: лодки у Рифтена.

### Immersive NPC Dialogue — VR — `try` [#184804](https://www.nexusmods.com/skyrimspecialedition/mods/184804)
- Фаза 8 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Основной файл «Immersive NPC Dialogue - VR» 1.1 (автор TheMachinaGod, июль 2026). Метка AI-Generated.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); HIGGS (#43930); VRIK Player Avatar (#23416)
- Порядок в MO2: Ниже VRIK и HIGGS.
- Настройки: Рекомендуются Dialogue Movement Enabler VR и VRIK Closed Fist (чтобы взмах не стал ударом). Меню диалога переносится на запястье; подсказки «Talk to» можно скрыть.
- Проверка: Взмах руки в сторону NPC начинает диалог; варианты на запястье.
- Заметка: Разговор начинается взмахом руки в сторону NPC, варианты ответа — на запястье. Только SKSEVR, автор Interactive Waters. Ни в одной сборке пока нет.

### Palm Compass VR — `try` [#189452](https://www.nexusmods.com/skyrimspecialedition/mods/189452)
- Фаза 8 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Основной файл «Palm Compass VR» (версия 2 и новее). Метка AI-Generated.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); HIGGS (#43930); VRIK Player Avatar (#23416); SkyUI VR (#91535)
- Не вместе с: VR HUD UI Reworked (#172476) и другие моды, двигающие узел компаса
- Порядок в MO2: Ниже VRIK.
- Настройки: В MCM VRIK включить «right palm up for compass»; в настройках Skyrim VR установить Compass = low. Свой MCM — позиция и масштаб.
- Проверка: Раскрытая правая ладонь вверх показывает компас над ладонью.
- Заметка: Компас уходит с HUD на ладонь: подняли раскрытую руку — компас над ней. Нужны VRIK и HIGGS. Метка AI-Generated.

### Horizon Fix — `opt` [#184607](https://www.nexusmods.com/skyrimspecialedition/mods/184607)
- Фаза 8 · тип `mixed` · установка `mo2_mod` · надёжность данных `low`
- Файл: Основной файл «Horizon Fix» 0.5.1 или новее (Winds of the North, Nordic Souls PBR, 2026-08-07). Файл «Horizon Fix AE» 0.4.1 не брать. Опционально «Horizon Fix Exponential Height Fog Config» под фичу Open Shaders.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Порядок в MO2: Ниже Open Shaders.
- Настройки: SKSE\Plugins\HorizonFix.ini: fWaterSkirtRadius=2000000.0, fHorizonBlendDegrees=1.5, sWorldSpaceBlocklist (по умолчанию города и Долина Фалмер). В Open Shaders есть одноимённая фича-компаньон: не включать дважды, проверить в меню END. В VR работает урезанно (подбор цвета по кадру выключен). Использовался ИИ при разработке.
- Проверка: В sksevr.log плагин загружен. Нет резкой полосы воды у горизонта.
- Заметка: Убирает разрыв на горизонте: полоса перехода к небу и водная «юбка» до горизонта. В коде есть отдельная VR-ветка, в Open Shaders — фича-компаньон. В VR работает урезанно.

## 07 Интерфейс

### moreHUD VR — `rec` [#33215](https://www.nexusmods.com/skyrimspecialedition/mods/33215)
- Фаза 4 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `high`
- Файл: Основной файл «moreHUD VR» 1.1.0 (9 VR-листов). «Debug Symbols» не нужны.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457) 2.0.12+; VR Address Library for SKSEVR (#58101) (с 1.1.0); SkyUI VR (#91535) — необязательно, для MCM
- Порядок в MO2: Ниже SkyUI VR. Norden UI VR — своя заплатка для moreHUD VR.
- Порядок плагина: ESP из архива — LOOT.
- Настройки: Настройки в MCM. Пара moreHUD Inventory Edition VR (#59142) — по желанию, нужен SkyUI VR.
- Проверка: Над целью видны HUD-показатели, в sksevr.log нет ошибок.

### QuickLoot IE — `rec` [#120075](https://www.nexusmods.com/skyrimspecialedition/mods/120075)
- Фаза 4 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Основной файл «QuickLoot IE - A QuickLoot EE Fork» 4.1.3 (Stormcrown VR, Yggdrasil VR, 2026-09-17). Не брать 3.x из SE-листов.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101); SkyUI VR (#91535); PapyrusUtil VR (#13048); Inventory Interface Information Injector (#85702) — необязательно
- Не вместе с: Quickloot VR (#102094); QuickLoot EE / QuickLoot RE
- Порядок в MO2: Ниже I4 и SkyUI VR.
- Настройки: Настройки в MCM (SkyUI VR). Поддержка VR заявлена как экспериментальная с 4.1.0, но стоит в Yggdrasil VR и Stormcrown VR.
- Проверка: В sksevr.log плагин загружен. При наведении на труп или сундук появляется окно быстрого лута.
- Заметка: Быстрый лут. Работает в VR — стоит в Yggdrasil VR и Stormcrown VR.

### VR Console Selection Fix — `rec` [#140752](https://www.nexusmods.com/skyrimspecialedition/mods/140752)
- Фаза 4 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Файл «Console Selection Fix» 1.2.1 (7 VR-листов).
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Порядок в MO2: Без особых правил.
- Настройки: Не требуется.
- Проверка: Консольная команда выбора цели работает мышью. В sksevr.log нет ошибок.

### No Menu Fade Out VR — `opt` [#185197](https://www.nexusmods.com/skyrimspecialedition/mods/185197)
- Фаза 4 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Основной файл «No Menu Fade Out VR» 1.0.2 (Stormcrown, SoG, Tahrovin - Grit, Yggdrasil).
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); Dialogue Movement Enabler VR (#59816)
- Порядок в MO2: Ниже Dialogue Movement Enabler VR.
- Настройки: NoMenuFadeOutVR.ini в SKSE\Plugins.
- Проверка: Меню диалога не гаснет.

### Norden UI — VR Edition — `opt` [#169537](https://www.nexusmods.com/skyrimspecialedition/mods/169537)
- Фаза 4 · тип `assets_only` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Файлы «Norden UI VR Edition» 1.2 (Tempus VR) и заплатки «PATCH - moreHUD VR», «PATCH - UIextensions», «PATCH - SkyUI Weapons Pack» (по установленным модам).
- Установщик: неизвестно — общие правила. По описанию Nexus файлы кладутся поверх SkyUI VR с перезаписью (в MO2 — мод ниже SkyUI VR).
- Требует: SkyUI VR (#91535); Inventory Interface Information Injector (#85702)
- Не вместе с: Edge UI - VR Edition (#168702) — держать выключенным; Clear HUD VR + Clean Menu, Minimal Enemy Healthbar VR — конфликт по HUD-файлам
- Порядок в MO2: Ниже SkyUI VR, выше SKSEVR Perk Extender (его statsmenu.swf должен победить). Заплатки — ниже Norden. COCKS — проверить меню крафта.
- Настройки: Рекомендуются SkyUI Colored Category Icons и Colorful Map Markers VR (в манифесте нет).
- Проверка: Меню инвентаря в стиле Norden; в sksevr.log нет ошибок.
- Заметка: Тема интерфейса.

### Essential Favorites VR + Favorite Misc Items — `rec` [#59554](https://www.nexusmods.com/skyrimspecialedition/mods/59554)
- Также скачать: Favorite Misc Items: https://www.nexusmods.com/skyrimspecialedition/mods/42750
- Фаза 4 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Два архива. 1) «Essential Favorites VR» 2.2.0 (6 VR-листов). 2) «Favorite Misc Items VR» 3.5 (Tempus, SoG, Grit) — версия 4.0.0 у Librum VR под вопросом.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101) 0.24.0 и новее; SkyUI VR (#91535)
- Не вместе с: Essential Favorites (#42997) и Support Equipped Items — базовые SE-файлы не ставить
- Порядок в MO2: Ниже SkyUI VR.
- Настройки: Favorite Misc Items добавляет в Избранное факелы и кирки.
- Проверка: Вещь из Избранного нельзя продать, выбросить или разобрать.
- Заметка: Избранное нельзя случайно продать или выронить — с HIGGS это частая беда. Favorite Misc Items добавляет в Избранное факелы и кирки, VR-файл.

### VR Menu Mouse Fix — `opt` [#33414](https://www.nexusmods.com/skyrimspecialedition/mods/33414)
- Фаза 4 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `high`
- Файл: Файл «Menu Mouse Fix» 1.6.0 (7 VR-листов).
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); Skyrim VR Tools (#27782); SkyUI VR (#91535)
- Порядок в MO2: Ниже SkyUI VR.
- Настройки: Кнопка клика по умолчанию — Trigger. Stable Hands — необязательно.
- Проверка: Курсор от контроллера в MCM, поиске SkyUI, назначении клавиш.
- Заметка: Курсор от контроллера в MCM, поиске SkyUI, назначении клавиш.

### Crafting Categories for SkyUI VR (COCKS) — `opt` [#81409](https://www.nexusmods.com/skyrimspecialedition/mods/81409)
- Фаза 4 · тип `mixed` · установка `mo2_mod` · надёжность данных `low`
- Файл: Файл «Crafting Categories for SkyUI VR» 1.1.1 (страница 81409, VR-файл от 23.04.2024). Основной файл 1.2.0 — SE, не брать.
- Установщик: неизвестно — общие правила
- Требует: SkyUI VR (#91535)
- Не вместе с: Crafting Categories for SkyUI (SE-файл)
- Порядок в MO2: Ниже SkyUI VR; с Norden UI VR — проверить меню крафта.
- Настройки: Без настроек.
- Проверка: В кузнице категории вместо одного длинного списка.
- Заметка: Категории в меню кузницы вместо одного длинного списка.

### Floating Subtitles VR — `opt` [#183714](https://www.nexusmods.com/skyrimspecialedition/mods/183714)
- Фаза 4 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Два архива. 1) «Floating Subtitles» 3.3.4 (#154424, Skyrim Unification Project — 3.3.4; Spirit of Grit — 3.3.3). 2) «Floating Subtitles VR» 3.3.4 (#183714) поверх основного — та же мажорная версия.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101) 0.230.0 и новее; ImGui VR Helper (#183466) 1.5.1 и новее
- Не вместе с: Subtitles VR (#131015); Fuz Ro D-oh — не нужен
- Группа «одно из»: `subtitles`
- Порядок в MO2: VR-мод — ниже основного, чтобы перезаписать его файлы. ImGui VR Helper — выше (в сепараторе фреймворков).
- Настройки: Оба архива нужны. В Spirit of Grit рядом стоит imGui Icons (#114790) — для SMF/Floating Subtitles проверить требования (у SKSE Menu Framework imGui Icons указан обязательным).
- Проверка: В sksevr.log оба плагина загружены. Субтитры висят над говорящим NPC.
- Заметка: Субтитры висят над говорящим NPC. Нужен ImGui VR Helper. Метка AI-Generated.

### Floating Damage NG — `opt` [#184159](https://www.nexusmods.com/skyrimspecialedition/mods/184159)
- Фаза 4 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `high`
- Файл: Основной файл «Floating Damage NG» 1.4.0 (Spirit of Grit, Tahrovin - Grit).
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101) 0.230.0 и новее; ImGui VR Helper (#183466) 1.5.4 и новее; SKSE Menu Framework (#120352) — необязательно
- Не вместе с: Floating Damage Numbers NG (#190796); Modern Floating Damage; Floating Damage (SE)
- Порядок в MO2: Ниже ImGui VR Helper.
- Настройки: Data\SKSE\Plugins\FloatingDamageNG.ini (фильтры, цвета, стиль). Без ImGui VR Helper цифры в VR не показываются. Игрок видит урон в метре перед собой на высоте груди.
- Проверка: Число урона висит в воздухе у цели. Лог FloatingDamageNG-combat.log создаётся рядом с логами SKSE.
- Заметка: Числа урона висят в 3D у цели. Нужен ImGui VR Helper 1.5.4+.

### Clear HUD VR + Clean Menu — `opt` [#49657](https://www.nexusmods.com/skyrimspecialedition/mods/49657)
- Также скачать: Clean Menu: https://www.nexusmods.com/skyrimspecialedition/mods/53524
- Фаза 4 · тип `assets_only` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Два архива. 1) «Clear HUD VR» 1.0.0 (8 VR-листов). 2) «Clean Menu» 1.0 (#53524). Из страницы Clean Menu НЕ брать файл «Unobtrusive HUD» (дублирует Clear HUD).
- Установщик: FOMOD есть у Clear HUD VR (выбор скрываемых элементов HUD); названия опций неизвестны — читать установщик. Скрывать: полосы здоровья, магии и запаса сил, счётчик стрел.
- Не вместе с: Unobtrusive HUD (#53524, файл); Less HUD VR; VR HUD UI Reworked (#172476)
- Группа «одно из»: `hud-clean`
- Порядок в MO2: Ниже moreHUD VR и Norden UI VR; HUD-файл у них общий, побеждает нижний.
- Настройки: Не требуется.
- Проверка: HUD чист, в sksevr.log нет ошибок.
- Заметка: Чистый HUD и главное меню. Unobtrusive HUD не нужен — дублирует Clear HUD.

### Minimal Enemy Healthbar VR — `opt` [#17812](https://www.nexusmods.com/skyrimspecialedition/mods/17812)
- Фаза 4 · тип `assets_only` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Файл «No Enemybar and no Names» 0.7 (Tempus, Panda's, Librum, FUS). Варианты на странице: «Enemy Healthbar Red with Names», «Enemy Healthbar Red without Names».
- Установщик: неизвестно — общие правила
- Порядок в MO2: Ниже Clear HUD VR и Norden UI VR; HUD-файл общий.
- Настройки: Не требуется.
- Проверка: Нет полоски здоровья врага.

### Dynamic Location Pop-ups (VR) — `opt` [#155978](https://www.nexusmods.com/skyrimspecialedition/mods/155978)
- Также скачать: основной: https://www.nexusmods.com/skyrimspecialedition/mods/153122
- Фаза 4 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Два архива. 1) «Dynamic Location Pop-ups» 1.0.1 (#153122). 2) «Dynamic Location Pop-ups VR» 1.0.1 (#155978) поверх основного (Tempus Maledictum VR ставит оба).
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101) 0.185.0 и новее
- Порядок в MO2: VR-файл — ниже основного.
- Настройки: Настройки в INI основного мода (SKSE\Plugins).
- Проверка: При входе в локацию появляется её название.
- Заметка: Название локации при каждом входе.

### RacemenuVR — `opt` [#156898](https://www.nexusmods.com/skyrimspecialedition/mods/156898)
- Фаза 4 · тип `mixed` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Основной файл «RacemenuVR» 0.5 (#156898; Spirit of Grit, Tahrovin - Grit, Tahrovin, Librum VR) поверх RaceMenu Anniversary Edition 0.4.19.16 (те же списки).
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101); SkyUI VR (#91535)
- Не вместе с: RaceMenu VR 2 (#192158); RaceMenu VR Layout Fix
- Группа «одно из»: `racemenu`
- Порядок в MO2: Ниже RaceMenu; он перезаписывает часть файлов. RaceMenu VR Position Tweaks (#174652) — ниже и требует RacemenuVR.
- Настройки: Редактор персонажа открывается в VR; расположение — Position Tweaks по желанию.
- Проверка: В sksevr.log RaceMenu загружен. В начале игры открывается редактор персонажа.
- Заметка: Редактор персонажа. Проверенный вариант из 4 VR-сборок.

### RaceMenu VR 2 — `try` [#192158](https://www.nexusmods.com/skyrimspecialedition/mods/192158)
- Фаза 4 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `low`
- Файл: Файл «RaceMenu VR 2» (бета, номера 0.1.x). Основа — RaceMenu SE 0.4.20.0 с оригинальными BSA, ESP и скриптами (не пакет LE).
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457) 2.0.12; VR Address Library for SKSEVR (#58101); SkyUI VR (#91535)
- Не вместе с: RacemenuVR (#156898); RaceMenu VR Layout Fix; RaceMenu VR Position Tweaks (#174652)
- Группа «одно из»: `racemenu`
- Порядок в MO2: Ниже RaceMenu (SE): его skee64.dll должен победить; сохранить пользовательский INI.
- Настройки: Только VR 1.4.15. Бета; в листах нет. Новые функции: стабильный вид лица, Sculpt с undo, своя клавиатура.
- Проверка: Редактор персонажа открывается; в sksevr.log нет ошибок skee64.
- Заметка: Новая надстройка: стабильный вид лица, Sculpt с undo, своя клавиатура. Бета, вместо RacemenuVR.

### I5 — Information Injector Improved — `try` [#192976](https://www.nexusmods.com/skyrimspecialedition/mods/192976)
- Фаза 4 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Файл «Inventory Interface Information Injector Improved» 0.4.0 (04.10.2026); VR включён с 0.3.0.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101); SkyUI VR (#91535); Inventory Interface Information Injector (#85702) — обязателен
- Порядок в MO2: Ниже I4.
- Настройки: Консольные команды: i5 status, i5 debug on|off, i5 cache purge. Кэш в co-save.
- Проверка: В sksevr.log плагин загружен. Меню инвентаря не тормозит при обновлениях.
- Заметка: Преемник I4: меню не тормозит при каждом обновлении. VR включён в 0.3. Если I4 не вылетает — оставить I4.

## 08 Звук

### Audio Overhaul for Skyrim — `rec` [#12466](https://www.nexusmods.com/skyrimspecialedition/mods/12466)
- Фаза 4 · тип `mixed` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Audio Overhaul for Skyrim 4.1.3, основной файл со SKSE (Audio Overhaul for Skyrim (4.1.3)-12466-4-1-3-1683940246.7z; Stormcrown VR, Librum VR). Файл «Non-SKSE - Epic Game Store - Game Pass» не брать. Tempus VR держит старую 3.4.3 — не брать.
- Установщик: неизвестно — общие правила
- Требует: Sound Record Distributor (#77815); Engine Fixes VR (#62089); SKSEVR (#30457)
- Не вместе с: Immersive Sounds Compendium (audio-523) вместо AOS — выбрать одно, либо оба только с патчем AOS–ISC (#36761)
- Группа «одно из»: `audio-stack`
- Порядок в MO2: Раздел «08 Звук», первым в стеке (самый низкий приоритет среди звука). Ниже по порядку: RSE, RISE, ASIF.
- Порядок плагина: После Sound Record Distributor; остальное по LOOT.
- Настройки: Выбор стека: по умолчанию AOS + RSE + RISE + ASIF (как Stormcrown VR). Требует рабочий SRD и Engine Fixes VR (регулировка громкости). Версию 4.1.3 не смешивать со старой 3.x.
- Проверка: В sksevr.log SRD загружен и находит конфиги AOS. В игре другие шаги, ветер, бой — звук насыщеннее ванильного.

### Regional Sounds Expansion + Reverb Interior Sounds Expansion — `rec` [#77829](https://www.nexusmods.com/skyrimspecialedition/mods/77829)
- Также скачать: Reverb Interior: https://www.nexusmods.com/skyrimspecialedition/mods/77947
- Фаза 4 · тип `mixed` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Два архива: Regional Sounds Expansion 2.1.0 (Regional Sounds Expansion (2.1.0)-77829-2-1-0-1748013115.7z; Stormcrown VR, Panda) и Reverb Interior Sounds Expansion 1.5.0 со страницы 77947 (Reverb Interior Sounds Expansion (1.5.0)-77947-1-5-0-1675142342.7z; Stormcrown VR, Panda). RSE 2.0.0 — старее.
- Установщик: неизвестно — общие правила
- Требует: Sound Record Distributor (#77815); SKSEVR (#30457)
- Порядок в MO2: Раздел «08 Звук». RSE ниже AOS (перекрывает регионы AOS), RISE ниже RSE. Ставится при любом выборе стека (AOS или ISC).
- Порядок плагина: После SRD; по LOOT.
- Настройки: Отдельного патча RSE–RISE нет: RISE подмешивает звуки RSE в записи регионов через SRD. Ставить обе страницы.
- Проверка: В sksevr.log SRD применил конфиги RSE и RISE. В городах и подземельях разные реверберации.

### Acoustic Space Improvement Fixes — `rec` [#78992](https://www.nexusmods.com/skyrimspecialedition/mods/78992)
- Фаза 4 · тип `mixed` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Acoustic Space Improvement Fixes 1.3.3, SkyPatcher-версия (Acoustic Space Improvement Fixes (SkyPatcher)-78992-1-3-3-1747812242.7z; Stormcrown VR). Запасной — Plugin Version (...(Plugin Version)-78992-1-3-3-1747812411.7z; Panda) без SkyPatcher. Файл «Patch for Extended Cut - Saints and Seducers» не нужен.
- Установщик: неизвестно — общие правила
- Требует: SkyPatcher (#106659)
- Не вместе с: Обе версии (SkyPatcher и Plugin) одновременно
- Порядок в MO2: Раздел «08 Звук», ниже RISE.
- Порядок плагина: Plugin Version — после RISE; SkyPatcher-версия плагина не имеет.
- Настройки: Во всех списках стоит вместе с RISE и RSE — ставить после них. Если SkyPatcher в VR работает нестабильно — взять Plugin Version.
- Проверка: Нет ошибок SkyPatcher в логе. Маленькие дома звучат тише и теснее, чем в ваниле.

### Immersive Sounds Compendium + AOS–ISC patch — `alt` [#523](https://www.nexusmods.com/skyrimspecialedition/mods/523)
- Также скачать: патч: https://www.nexusmods.com/skyrimspecialedition/mods/36761
- Фаза 4 · тип `mixed` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Immersive Sounds - Compendium 3.0 (Immersive Sounds Compendium 3.0-523-3-0-1629219996.zip; Tempus, Librum, Grit x2, Tahrovin, FUS, Ygg, Panda). Для SRD-варианта (Panda) поверх — «ISC-SRDified Main File» 2.2.1 (#78446, ISC-SRDified Main File-78446-2-2-1-1698505409.zip; он убирает часть патчей). Патч AOS–ISC (#36761, 1.1.0) ставить ТОЛЬКО если установлен AOS: Tempus и Librum держат AOS + ISC + патч.
- Установщик: нет установщика (по заметке куратора); состав неизвестен
- Не вместе с: Audio Overhaul for Skyrim (audio-12466) в варианте «или-или»; вместе — только с патчем #36761; AOS без патча AOS–ISC (#36761), если ISC включён
- Группа «одно из»: `audio-stack`
- Порядок в MO2: Раздел «08 Звук». Если ISC вместо AOS — на месте AOS; ISC-SRDified ниже ISC; RSE, RISE, ASIF ниже. Патч AOS–ISC (при обоих) — ниже AOS и ISC.
- Порядок плагина: Патч AOS–ISC и ISC-SRDified — после соответствующих плагинов; остальное по LOOT.
- Настройки: Альтернативный стек: ISC + RSE + RISE + ASIF (Panda, SRD-вариант). Не включать AOS и ISC одновременно без патча #36761. SRD (frameworks-77815) нужен только для ISC-SRDified. ESP-версия ISC 3.0 без SRDified — вариант FUS/Ygg/Grit.
- Проверка: ISC-плагин активен, SRD (если вариант SRDified) загружен. Звуки оружия и окружения ISC слышны, нет двойных звуков с AOS.

### True 3D Sound for Headphones — `rec` [#1897](https://www.nexusmods.com/skyrimspecialedition/mods/1897)
- Фаза 4 · тип `root_files` · установка `root_builder` · надёжность данных `low`
- Файл: Skyrim SE 3D Sound (X3DAudio HRTF) 1.0 (Skyrim SE 3D Sound (X3DAudio HRTF)-1897-1-0.zip; FUS, Yggdrasil VR, Panda). Ставить в корень игры через Root Builder, не в Data.
- Установщик: нет установщика; состав архива не проверен (ожидается X3DAudio1_7.dll)
- Не вместе с: Другие обработчики пространственного звука (Windows Sonic, Dolby, драйвер гарнитуры) одновременно
- Порядок в MO2: Раздел «08 Звук», файлы уходят в корень через Root Builder; порядок среди звуковых модов не важен.
- Настройки: Отключить любую другую пространственную обработку звука на гарнитуре и звуковой карте. Работает только на наушниках. Автор родственной страницы 98346 просит копировать файлы вручную, не через менеджер — здесь заменяет Root Builder. Если звук пропал — убрать DLL из корня.
- Проверка: В корне игры после запуска появилась X3DAudio1_7.dll. Направление звука чёткое, звук есть.
- Заметка: HRTF-позиционирование для наушников гарнитуры.

### UHDAP — Music HQ — `opt` [#18115](https://www.nexusmods.com/skyrimspecialedition/mods/18115)
- Фаза 4 · тип `assets_only` · установка `mo2_mod` · надёжность данных `medium`
- Файл: «Music - HQ» (Music - HQ-18115-0-1.7z): все VR-списки, музыка. «Voices EN - Part 1» и «Voices EN - Part 2» (оба архива) — только при английской озвучке (FUS, Ygg, Panda). Большие архивы.
- Установщик: нет установщика (отдельные файлы)
- Не вместе с: Другие моды озвучки (перекрывают голоса UHDAP)
- Порядок в MO2: Раздел «08 Звук», самым первым (низший приоритет): музыкальные моды и озвучка должны перекрывать UHDAP.
- Настройки: Голоса EN не ставить при русской озвучке.
- Проверка: Музыка в меню и в мире играет без артефактов. Файлы лежат в Data\Music.
- Заметка: Ванильная музыка без артефактов. Голоса EN — только при английской озвучке.

### Wildwood Echoes + Murmurs and Mead — `opt` [#112008](https://www.nexusmods.com/skyrimspecialedition/mods/112008)
- Также скачать: Murmurs and Mead: https://www.nexusmods.com/skyrimspecialedition/mods/114716
- Фаза 4 · тип `mixed` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Wildwood Echoes 1.3 (Wildwood Echoes-112008-1-3-1716161041.7z; Librum VR и SE) + Murmurs and Mead 1.1 со страницы 114716 (Murmurs and Mead-114716-1-1-1711757412.7z; только SE-списки). 1.4 (2026) — новее, в VR не проверена.
- Установщик: Murmurs and Mead: FOMOD есть (описание WJ), варианты неизвестны — общие правила
- Требует: Sound Record Distributor (#77815); Base Object Swapper VR (#61734); SKSEVR (#30457)
- Не вместе с: Не дублировать лесные и таверные звуки другими модами на тот же SRD-слой
- Порядок в MO2: Раздел «08 Звук», ниже RSE и RISE. Проверить в xEdit пересечения по звуковым регионам.
- Порядок плагина: По LOOT.
- Настройки: Murmurs and Mead заменяет одиночный таверный цикл через Base Object Swapper — нужен BOS VR. Wildwood Echoes — только через SRD.
- Проверка: В sksevr.log SRD и BOS применили файлы без ошибок. В лесу слышны ветер, лягушки, вой; в таверне разные варианты шума.
- Заметка: Звуки леса и 18 вариантов шума таверн.

### Haunting Harmonies of Hjaalmarch + Whispers of the Daedric Princes — `opt` [#125873](https://www.nexusmods.com/skyrimspecialedition/mods/125873)
- Также скачать: Whispers: https://www.nexusmods.com/skyrimspecialedition/mods/141931
- Фаза 4 · тип `mixed` · установка `mo2_mod` · надёжность данных `low`
- Файл: The Haunting Harmonies of Hjaalmarch 1.0 (The Haunting Harmonies of Hjaalmarch-125873-1-0-1724214662.7z) + Whispers of the Daedric Princes 1.2 со страницы 141931 (Whispers of the Daedric Princes-141931-1-2-1740012920.7z). В VR-списках оба не встречаются.
- Установщик: Haunting Harmonies: FOMOD есть (описание WJ), варианты неизвестны — общие правила
- Требует: Sound Record Distributor (#77815); Base Object Swapper VR (#61734); SKSEVR (#30457)
- Порядок в MO2: Раздел «08 Звук», ниже RSE и RISE (SRD распределяет поверх).
- Порядок плагина: По LOOT.
- Настройки: Whispers требует Base Object Swapper (VR-версия в наборе). Опция «замолчать после квеста» — выбрать на странице или в установщике.
- Проверка: В sksevr.log SRD и BOS загрузили файлы. В Морфале слышен болотный фон, у святилищ — шёпот.
- Заметка: Атмосфера болот Морфала и шёпот у святилищ. Позиционный звук в шлеме.

### Immersive Draw Sheathe Sounds VR — `opt` [#44992](https://www.nexusmods.com/skyrimspecialedition/mods/44992)
- Фаза 4 · тип `mixed` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Immersive Draw Sheathe Sounds VR 1.1 (Immersive Draw Sheathe Sounds VR-44992-1-1-1643041361.7z; Stormcrown VR, Panda, Grit x2). Файл 1.0 — старее.
- Установщик: неизвестно — общие правила
- Порядок в MO2: Раздел «08 Звук», ниже AOS: пересекается по звукам оружия.
- Порядок плагина: После AOS; конфликты по SNDR проверить в xEdit.
- Настройки: Проверить, не конфликтуют ли записи с AOS (одни дескрипторы). Если конфликт — оставить версию Draw Sheathe.
- Проверка: Звуки доставания и убирания оружия соответствуют VR-версии, нет двойного звука.

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
- Фаза 6 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Main «Open Animation Replacer» 3.2.1 (Yggdrasil VR, 2026-08-31: «Open Animation Replacer 92109 3.2.1») — один архив для SE/AE/VR, отдельного VR-файла нет. Версии 2.3.6 (Panda, Tempus, Tahrovin, Librum, FUS) и 2.1.0 (Grit) — только как откат, если 3.2.1 не загрузится. Пре-релизы и файлы для моддеров не брать.
- Установщик: нет установщика (по именам архивов); структуру проверить при установке. Если установщик есть — неизвестно — общие правила.
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101); Paired Animation Improvements (#99621); Animation Queue Fix (#82395)
- Не вместе с: Dynamic Animation Replacer (DAR) — не ставить, OAR сам читает DAR-папки
- Порядок в MO2: Раздел «11 Анимации и физика», первым среди анимаций: до всех OAR/DAR-пакетов, после XPMSSE. Приоритет между OAR-пакетами задаётся не порядком в MO2, а полем priority в config.json каждого пакета (переопределяется в меню OAR). Порядок MO2 важен только при совпадении одних и тех же файлов.
- Настройки: Настройки OAR — INI/JSON в SKSE\Plugins (точное имя смотреть в архиве), по умолчанию не менять. Меню OAR в игре (ImGui) проверить в шлеме: если не открывается — открывать через SKSE Menu Framework + ImGui VR Helper (#120352) или править config.json пакетов вручную.
- Проверка: В Documents\My Games\Skyrim VR\SKSE\sksevr.log DLL OAR загружена без ошибки версии/адресов. В игре NPC ходят и стоят без T-позы, в логе OAR (рядом с sksevr.log) нет ошибок чтения пакетов.
- Заметка: Официально поддерживает SE, AE и VR.

### Paired Animation Improvements — `rec` [#99621](https://www.nexusmods.com/skyrimspecialedition/mods/99621)
- Фаза 6 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Main «Paired Animation Improvements» 1.0.3 (Yggdrasil VR, 2026-08-31), иначе 1.0.2 (Panda, FUS, Tempus, Librum, Grit). Файл «Horse Mount and Dismount Double Sound Fix» (тот же ID) — не ставить, если нет двойного звука посадки на коня (Panda и FUS берут).
- Установщик: нет установщика (по именам архивов); структуру проверить при установке.
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101); Open Animation Replacer (#92109)
- Порядок в MO2: Раздел «11 Анимации и физика», сразу после OAR. Конфликтов файлов не ожидается.
- Настройки: Без настроек.
- Проверка: В Documents\My Games\Skyrim VR\SKSE\sksevr.log DLL загружена. Парные анимации (добивания, рукопожатия квестов) играют без зависания персонажей.

### Mu Joint Fix (DLL) — `rec` [#61479](https://www.nexusmods.com/skyrimspecialedition/mods/61479)
- Фаза 6 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `low`
- Файл: Main «Mu Joint Fix» 2.1.3 (Yggdrasil VR, 2026-09-18: «MuJointFix 61479 2.1.3»), запасной вариант 2.1.2 (Librum VR, Yggdrasil VR). Старую 2.0.17 не брать. Назначение мода и состав архива не подтверждены — смотреть описание на странице.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Порядок в MO2: Раздел «11 Анимации и физика» после XPMSSE. Конфликтов файлов не ожидается.
- Настройки: Без настроек, пока описание не требует иного.
- Проверка: В Documents\My Games\Skyrim VR\SKSE\sksevr.log DLL загружена без ошибки. Если DLL не грузится или в архиве нет SKSE\Plugins\*.dll — отключить мод, не чинить.

### FSMP — Faster HDT-SMP — `opt` [#57339](https://www.nexusmods.com/skyrimspecialedition/mods/57339)
- Фаза 6 · тип `mixed` · установка `mo2_mod` · надёжность данных `low`
- Файл: Только если в сборке есть SMP-волосы или одежда. Вариант A (VR-проверен в свежем списке): основной файл «FSMP 4.0.1» (Tahrovin - Grit, 2026-07-05). Вариант Б (проверен в Panda's и Tahrovin): «Faster HDT-SMP» 2.5.1 + отдельный файл «XML VR» 1.0 (конфиги для VR от Alandtse). Версию 4.1.1 (SE-списки, 2026-08) брать, только если её установщик явно предлагает рантайм Skyrim VR/1.4.15. Файлы 1.50.9 rc1 / 2.1.3 (Grit) — устарели.
- Установщик: Установщик FSMP, вероятно, спрашивает версию игры/платформу: выбирать Skyrim VR (Steam, 1.4.15), CUDA-вариант не брать, AVX2 — если CPU поддерживает. Точные названия опций — неизвестно — общие правила.
- Требует: SKSEVR (#30457); XPMSSE + XP32 First Person Skeleton CTD Bugfix for VR (#1988); SKSE Menu Framework + ImGui VR Helper (#120352)
- Не вместе с: HDT-SMP оригинальный (DaymareOn/aers) и другие сборки hdtSMP64.dll — только один SMP-движок; XPMSSE без VR-фикса (#34301) — вылеты
- Порядок в MO2: Раздел «11 Анимации и физика», сразу ниже XPMSSE и его VR-фикса. «XML VR» — отдельным модом ниже основного FSMP (должен его перезаписывать).
- Настройки: Сначала замерить кадр без SMP-одежды, потом включать. Лимиты физики держать низкими; параметры — в hdtSkinnedMeshConfigs\configs.xml (по SE-гайдам; сверить с FSMP wiki). Сверить Requirements: старые версии просят SkyUI VR (#91535), PapyrusUtil VR (#13048), JContainers VR (#16495), ConsoleUtilVR (#47189) — все есть в манифесте. SKSE Menu Framework + ImGui VR Helper нужны только для FSMP 4.x (меню вместо MCM).
- Проверка: В Documents\My Games\Skyrim VR\SKSE\sksevr.log виден hdtSMP64/FSMP DLL без ошибки. В игре на NPC с SMP-волосами двигаются волосы, кадр в городе не падает ниже допустимого.
- Заметка: Только если будут SMP-волосы или одежда. Проверьте VR-вариант в установщике. Нужен XPMSSE с VR-фиксом.

### Dynamic Armor Physics — `opt` [#186346](https://www.nexusmods.com/skyrimspecialedition/mods/186346)
- Фаза 6 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Main «Dynamic Armor Physics - Latest Version» 1.0.3 (Stormcrown VR, 2026-08-01) — VR-проверено; 1.0.4 (SUP, SE) — только после проверки sksevr.log. Единственный VR-список — Stormcrown.
- Установщик: нет установщика (по именам архивов); структуру проверить при установке.
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101); XPMSSE + XP32 First Person Skeleton CTD Bugfix for VR (#1988)
- Порядок в MO2: Раздел «11 Анимации и физика», ниже XPMSSE и FSMP. Конфликтов файлов не ожидается.
- Настройки: Четыре профиля веса (без брони/одежда/лёгкая/тяжёлая) — по умолчанию.
- Проверка: В Documents\My Games\Skyrim VR\SKSE\sksevr.log DLL загружена. Тела убитых NPC падают с разным весом/звуком в зависимости от брони.
- Заметка: 2026 год, есть в Stormcrown VR.

### XPMSSE + XP32 First Person Skeleton CTD Bugfix for VR — `core` [#1988](https://www.nexusmods.com/skyrimspecialedition/mods/1988)
- Также скачать: VR-фикс: https://www.nexusmods.com/skyrimspecialedition/mods/34301
- Фаза 6 · тип `mixed` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Ставить ДВА мода. 1) Основной «XP32 Maximum Skeleton Special Extended» (#1988), файл 5.06 (Panda, Tahrovin, Grit, Librum VR, CSVP). Версии 4.80/4.81 (Tempus, Yggdrasil VR) — не брать. 2) Отдельным модом «XP32 First Person Skeleton CTD Bugfix for VR» (#34301): самая свежая 5.06-1 (Librum VR, 2025-10), иначе 5.06 (Panda, Tempus, Grit). Версию 4.71 (Yggdrasil) вместе с 5.06 не брать. Основной файл без VR-фикса в VR даёт вылеты.
- Установщик: Установщик основного XPMSSE: названия опций — неизвестно — общие правила. По смыслу: взять скелет и скелеты существ; физику SMP включать, только если ставится FSMP; опции первого лица/оружейных стилей игрока в VR не нужны (управляет VRIK), брать вариант по умолчанию. VR-фикс #34301 — без установщика (по имени).
- Требует: SKSEVR (#30457)
- Не вместе с: Любой другой скелет и моды, перезаписывающие meshes\actors\character\character assets\skeleton*.nif и meshes\actors\character\_1stperson\skeleton.nif; XPMSSE без VR-фикса #34301
- Порядок в MO2: Первым в разделе «11 Анимации и физика», до анимаций и FSMP. «VR-фикс» — отдельный мод СРАЗУ НИЖЕ основного (выше приоритет), он обязан выиграть конфликт по _1stperson\skeleton.nif. Если конфликт с файлами VRIK/HIGGS/PLANCK по skeleton*.nif — открыть оба в MO2 и разобрать, не гадать (VRIK просит, чтобы его файлы перезаписывали остальное).
- Порядок плагина: XPMSSE.esp/плагин — если есть в архиве, включить; LOOT.
- Настройки: Настроек нет. Меню XPMSE (если есть в MCM) не трогать.
- Проверка: Игра грузит сейв без вылета; достать лук и меч, поднять руки — нет T-позы и ошибок скелета. В MO2 конфликт по _1stperson\skeleton.nif: победитель — VR-фикс.
- Заметка: Расширенный скелет — база для FSMP и многих анимаций. Без VR-фикса поверх SE-скелет в VR даёт вылеты.

### NPC Animation Remix + Gesture Animation Remix (OAR) — `rec` [#63471](https://www.nexusmods.com/skyrimspecialedition/mods/63471)
- Также скачать: Gesture Remix: https://www.nexusmods.com/skyrimspecialedition/mods/64420
- Фаза 6 · тип `assets_only` · установка `mo2_mod` · надёжность данных `medium`
- Файл: NPC Animation Remix (OAR): «main archive» последней OAR-версии (2.3.0 — SE-списки 2026-06; VR-проверено 2.0.0 в Panda's и FUS) + «shield patch» той же ветки (2.0.0 у Panda/FUS; ставят все VR-списки). Gesture Animation Remix (#64420): «main archive» (OAR) 2.1.1 + «shield patch» 1.2.0 (Panda, FUS). Если 2.3.0 вызывает ошибки OAR — откат на 2.0.0. Не брать DAR-архивы (1.x) и «(no looped idles)».
- Установщик: нет установщика (по именам архивов); структуру проверить при установке.
- Требует: Open Animation Replacer (#92109)
- Не вместе с: Reanimated NPC Animations — дублирует; EVG Animation Variance (#38534) — частично дублирует, приоритет у Remix
- Порядок в MO2: После OAR и PAI. Gesture Remix — ниже NPC Remix. В OAR у Remix приоритет выше EVG и Pristine. Приоритет между OAR-пакетами задаётся не порядком в MO2, а полем priority в config.json каждого пакета (переопределяется в меню OAR). Порядок MO2 важен только при совпадении одних и тех же файлов.
- Настройки: Без настроек.
- Проверка: В диалоге NPC стоят и жестикулируют без деревянных поз, щит в руке NPC не торчит из-за спины. В логе OAR нет ошибок пакета.
- Заметка: Стойки, ходьба и жесты NPC в диалогах. В VR собеседник в метре от вас — деревянные позы видно сразу.

### Expressive Facial Animation — Male + Female — `rec` [#19532](https://www.nexusmods.com/skyrimspecialedition/mods/19532)
- Также скачать: Female: https://www.nexusmods.com/skyrimspecialedition/mods/19181
- Фаза 6 · тип `assets_only` · установка `mo2_mod` · надёжность данных `high`
- Файл: Два архива, оба Main: «Expressive Facial Animation - Male Edition» (#19532) 1.21 и «Expressive Facial Animation - Female Edition» (#19181) 1.7 — как во всех 7 VR-списках.
- Установщик: нет установщика (по именам архивов); структуру проверить при установке.
- Порядок в MO2: Раздел «11 Анимации и физика». Желательно ниже MFG Fix NG (#133568), но не обязательно.
- Настройки: MFG Fix NG (#133568) из манифеста дополняет эффект, обязательным не является.
- Проверка: В диалоге у NPC мигают глаза и меняется выражение лица; нет искажённых лиц.
- Заметка: Мимика и моргание NPC. Дополняет MFG Fix NG и ИИ-NPC.

### Pristine Vanilla Movement — `opt` [#66635](https://www.nexusmods.com/skyrimspecialedition/mods/66635)
- Фаза 6 · тип `assets_only` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Main «Pristine Vanilla Movement» 1.1.1 (все 6 VR-списков: Librum, Panda, Grit, Tahrovin, Tahrovin-Grit, Tempus). «Sprint - No Camera Shake» не брать (в VR нет тряски камеры).
- Установщик: нет установщика (по именам архивов); структуру проверить при установке. Архив, вероятно, DAR-формата (папка DynamicAnimationReplacer) — OAR её читает; ничего конвертировать не нужно.
- Требует: Open Animation Replacer (#92109)
- Не вместе с: Animation Motion Revolution — оба меняют передвижение, оставить только Pristine
- Порядок в MO2: После OAR; ниже NPC Animation Remix (у Remix приоритет выше). Приоритет между OAR-пакетами задаётся не порядком в MO2, а полем priority в config.json каждого пакета (переопределяется в меню OAR).
- Настройки: Без настроек.
- Проверка: NPC ходят и бегают без T-позы и скольжения. Нет конфликтов по meshes\actors\character\animations в MO2 с другими пакетами движения.
- Заметка: Исправленные ванильные анимации передвижения — база под OAR-пакеты.

### Arm Movement Animations (OAR) — `opt` [#62849](https://www.nexusmods.com/skyrimspecialedition/mods/62849)
- Фаза 6 · тип `assets_only` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Main «Arm Movement Animations (OAR)» 2.2.0 (Panda, FUS, CSVP, Nordic Souls). Не брать DAR-версии «Immersive Folded Hands» 1.x и «Harkon dialogue moving animation replacer (DAR folder)».
- Установщик: нет установщика (по именам архивов); структуру проверить при установке.
- Требует: Open Animation Replacer (#92109)
- Порядок в MO2: После NPC Animation Remix. Приоритет между OAR-пакетами задаётся полем priority в config.json каждого пакета, порядок MO2 важен только при совпадении файлов.
- Настройки: Без настроек.
- Проверка: NPC при ходьбе держат руки естественно; нет лишних конфликтов с NPC Animation Remix в окне OAR.
- Заметка: NPC при ходьбе держат руки естественно.

### Take a Seat + Improved Table Transitions — `opt` [#54193](https://www.nexusmods.com/skyrimspecialedition/mods/54193)
- Также скачать: Table Transitions: https://www.nexusmods.com/skyrimspecialedition/mods/84160
- Фаза 6 · тип `assets_only` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Take a Seat: «Take a Seat - OAR Animations» 1.01 (Tempus, Panda, Librum, Nordic Souls, LoreRim) — не DAR 1.0. Improved Table Transitions (#84160): вариант «Improved Table Sit Transition OAR» 1.4 (Panda's, CSVP) или 1.5 (NGVO, 2025-09); «Improved Table Transitions» 1.3 (Librum, LoreRim) — старая.
- Установщик: нет установщика (по именам архивов); структуру проверить при установке.
- Требует: Open Animation Replacer (#92109)
- Не вместе с: Take a Seat DAR-версия 1.0 (FUS, Yggdrasil) — не смешивать с OAR-версией
- Порядок в MO2: После OAR. Table Transitions — ниже Take a Seat. Приоритет между OAR-пакетами задаётся полем priority в config.json.
- Настройки: Без настроек.
- Проверка: NPC садятся на скамьи и за столы плавно, без телепорта.
- Заметка: Позы сидения и плавный вход за стол без телепорта.

### Lively Children Animations (OAR) — `opt` [#67557](https://www.nexusmods.com/skyrimspecialedition/mods/67557)
- Фаза 6 · тип `assets_only` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Main «Lively Children Animations (OAR)» 2.2.1 (Panda's VR, CSVP, Nordic Souls). DAR 1.0.0 (Yggdrasil, Elysium) не брать.
- Установщик: нет установщика (по именам архивов); структуру проверить при установке.
- Требует: Open Animation Replacer (#92109)
- Порядок в MO2: После NPC Animation Remix. Приоритет между OAR-пакетами задаётся полем priority в config.json.
- Настройки: Без настроек.
- Проверка: Дети в городах не стоят деревянно.

### EVG Conditional Idles — `opt` [#34006](https://www.nexusmods.com/skyrimspecialedition/mods/34006)
- Фаза 6 · тип `assets_only` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Только «EVG Conditional Idles» 1.51 (Tempus, Panda, FUS, CSVP, SUP). «EVG Animation Variance» (#38534) НЕ брать: по заметке куратора дублирует Remix (VR-списки его ставят — отклонение сознательное). «(beta) Wade In Water Animations» не брать. 1.42 (Yggdrasil) — устарела.
- Установщик: нет установщика (по именам архивов); структуру проверить при установке. Архив может быть DAR-формата — OAR читает.
- Требует: Open Animation Replacer (#92109)
- Не вместе с: EVG Animation Variance (#38534) — дублирует NPC Animation Remix
- Порядок в MO2: Ниже NPC Animation Remix: при конфликте приоритет у Remix. Приоритет между OAR-пакетами задаётся полем priority в config.json.
- Настройки: Без настроек.
- Проверка: Мёрзнущие/уставшие NPC играют свои стойки; Remix-позы не ломаются.
- Заметка: NPC мёрзнет, устал, ранен. Animation Variance не брать — дублирует Remix.

### Goetia Animations — Spell Casting + Conditional Shouts — `opt` [#70204](https://www.nexusmods.com/skyrimspecialedition/mods/70204)
- Также скачать: Shouts: https://www.nexusmods.com/skyrimspecialedition/mods/76388
- Фаза 6 · тип `assets_only` · установка `mo2_mod` · надёжность данных `medium`
- Файл: «Goetia Animations - Magic Spell Casting» 1.4 (Tempus, Panda, CSVP, Nordic Souls, NGVO; в SUP — 1.5b) и «Goetia Animations - Conditional Shouts» (#76388) 1.2 (Tempus, Panda). «Momentum Whirlwind Sprint» (Panda, #76388) — не брать, это для игрока в 3-м лице.
- Установщик: нет установщика (по именам архивов); структуру проверить при установке.
- Требует: Open Animation Replacer (#92109)
- Порядок в MO2: После OAR. Приоритет между OAR-пакетами задаётся полем priority в config.json.
- Настройки: Эффект виден только у NPC-магов; у игрока в VR каст задают VRIK/Spell Wheel.
- Проверка: NPC-маг при касте и крике играет новые анимации. Если страница требует Nemesis/Pandora — прогнать Pandora (#133232) и проверить, что нет T-позы.
- Заметка: Каст и крики у NPC-магов. У игрока в VR не видны.

### Leviathan / Vanargand Animations (стойки и атаки NPC) — `opt` [#47092](https://www.nexusmods.com/skyrimspecialedition/mods/47092)
- Фаза 6 · тип `assets_only` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Стойки и атаки NPC, семь архивов (как в Panda's Sovngarde): Leviathan — «Two-Handed High Stance SE» (#47092) 1.4, «Two-Handed Normal Attacks For High Stance» (#48550) 1.2, «Two-Handed Power Attacks For High Stance» (#50545) 1.4c; Vanargand — «One handed Mid Stance» (#57544) 1.2, «One handed Normal Attacks» (#58326) 1.1, «One Handed Power Attacks» (#58997) 1.2, «Dual Wield Attacks» (#63566) 1.0. Sneak-пакеты Vanargand для игрока не брать. В SE-списках 2026 (SUP) — 1.5/1.4/1.5/1.4b — только после проверки.
- Установщик: нет установщика (по именам архивов); структуру проверить при установке.
- Требует: Open Animation Replacer (#92109)
- Не вместе с: Reanimated NPC Animations / другие пакеты боевых анимаций NPC с теми же условиями; MCO / BFCO / ADXP / Precision — не нужны и в VR бесполезны
- Порядок в MO2: После OAR и NPC Animation Remix. Все семь пакетов — подряд. Приоритет между OAR-пакетами задаётся полем priority в config.json.
- Настройки: Анимации действуют на NPC и на игрока в 3-м лице; в VR атаками игрока управляют VRIK/HIGGS/PLANCK — отдельно это не настраивать.
- Проверка: Бандит и страж держат разные стойки в бою; нет скольжения и T-позы при атаке.
- Заметка: Разнообразие врагов в ближнем бою. Sneak-пакеты для игрока не брать.

### Conditional Tavern Cheering (OAR) — `opt` [#63029](https://www.nexusmods.com/skyrimspecialedition/mods/63029)
- Фаза 6 · тип `assets_only` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Main «Conditional Tavern Cheering (OAR)» 1.3.0 (Panda, FUS, CSVP, Nordic Souls). DAR 1.0.3 (Tempus, Yggdrasil) не брать.
- Установщик: нет установщика (по именам архивов); структуру проверить при установке.
- Требует: Open Animation Replacer (#92109)
- Порядок в MO2: После OAR. Приоритет между OAR-пакетами задаётся полем priority в config.json.
- Настройки: Без настроек.
- Проверка: Посетители таверны аплодируют, когда играет бард.

### Super Fast Get Up Animation — `opt` [#46714](https://www.nexusmods.com/skyrimspecialedition/mods/46714)
- Фаза 6 · тип `assets_only` · установка `mo2_mod` · надёжность данных `high`
- Файл: Main «Super Fast Get Up Animation» 1.0 (5 VR-списков и 9 SE-списков, везде один файл 1615242774).
- Установщик: нет установщика (по именам архивов); структуру проверить при установке.
- Не вместе с: Другие моды, заменяющие анимацию вставания после падения (getup)
- Порядок в MO2: Раздел «11 Анимации и физика», после OAR-пакетов (обычная замена hkx без OAR). Конфликт с другими вставаниями решать вручную в MO2.
- Настройки: Без настроек.
- Проверка: После нокдауна от PLANCK/HIGGS-удара NPC быстро встаёт. Нет T-позы.
- Заметка: С PLANCK враги падают часто — быстрый подъём не тормозит бой.

### Variadic Collision Dynamics — `try` [#183892](https://www.nexusmods.com/skyrimspecialedition/mods/183892)
- Также скачать: Resources: https://www.nexusmods.com/skyrimspecialedition/mods/184110
- Фаза 6 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `low`
- Файл: «Variadic Collision Dynamics» (#183892) последняя 1.3.5 (True North, SE, 2026-09-19) + «Resources» (#184110) 1.0.11. По чейнджлогу с 1.3.2 одна DLL для SE/AE/VR. VR-списков нет — ставить только по разрешению (метка try).
- Установщик: нет установщика (по именам архивов); структуру проверить при установке.
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Не вместе с: PLANCK / Physical Collision VR — возможный конфликт капсулы игрока; Collision Sentinel (#181445) — есть жалоба на конфликт
- Порядок в MO2: Раздел «11 Анимации и физика», последним из DLL; по одному и с отдельным тестом.
- Настройки: Если игрок застревает/проваливается — удалить мод, не настраивать.
- Проверка: В Documents\My Games\Skyrim VR\SKSE\sksevr.log DLL загружена, нет конфликта с PLANCK при приседании и подъёме на уступ.
- Заметка: Капсула коллизии меняется по позе — меньше застреваний. Капсула игрока в VR — зона PLANCK, конфликт вероятен.

### A-Pose Bug Fix — `try` [#168903](https://www.nexusmods.com/skyrimspecialedition/mods/168903)
- Фаза 6 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `low`
- Файл: «A-Pose Fix» (#168903) v1.1.0 (NGVO, Tomes of Talos; Nordic Souls — v1.1.0-a 2026-03). VR-файла нет. Ставить только если появилась A-поза.
- Установщик: нет установщика (по именам архивов); структуру проверить при установке.
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101); Pandora Behaviour Engine+ (#133232)
- Порядок в MO2: Раздел «11 Анимации и физика», последним; по одному.
- Настройки: Не ставить по умолчанию.
- Проверка: В Documents\My Games\Skyrim VR\SKSE\sksevr.log DLL загружена без ошибок; после установки A-поза исчезла, иначе удалить.
- Заметка: Только как лекарство, если появится A-поза. VR не подтверждён.

## 12 Бой и геймплей

### Blade and Blunt + Blade and Blunt VR — `rec` [#34549](https://www.nexusmods.com/skyrimspecialedition/mods/34549)
- Также скачать: VR: https://www.nexusmods.com/skyrimspecialedition/mods/120494
- Фаза 7 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Ставить ДВА мода. 1) Основной «Blade and Blunt - A Combat Overhaul» (#34549) 3.8.3 (Stormcrown VR, 2025-09); fallback 3.7.4 (Tempus, Panda, Tahrovin, FUS). Версии 4.0.x (SE-списки 2026-08) — НЕ брать: Stormcrown VR после выхода 4.0 остался на 3.8.3 и VR-порта под 4.x в списках нет. Версия 1.4.1 (Grit, Yggdrasil, FUS) — старая, без DLL, не брать. 2) Поверх — «Blade and Blunt VR» (#120494) 1.0.2 (Stormcrown), иначе 1.0.1 (Tempus, Panda, Tahrovin, FUS). Перед установкой открыть страницу #120494 и сверить, какие версии основного она поддерживает.
- Установщик: неизвестно — общие правила (по именам архивов — два отдельных файла без установщика).
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101); Spell Perk Item Distributor VR (#59121); Poached Bugs VR (#107053); Dual Casting Fix VR (#92804); SkyUI VR (#91535)
- Не вместе с: Scrambled Bugs (SE/AE) — в VR не работает, вместо него Poached Bugs VR; Precision, True Directional Movement, MCO/BFCO/ADXP; Другие крупные боевые оверхолы (Wildcat, Valhalla Combat и т. п.) — не смешивать
- Порядок в MO2: Раздел «12 Бой и геймплей». Порядок: Blade and Blunt (основной) → Blade and Blunt VR СРАЗУ НИЖЕ (его VR-DLL должна перезаписать SE-DLL). Adamant и Mysticism — выше. Simonrim Choice Config из Poached Bugs VR должен стоять ниже Core Poached Bugs VR.
- Порядок плагина: Плагины Blade and Blunt — после Adamant и Mysticism; остальное LOOT.
- Настройки: Настройки через MCM. В VR не включать вторую модель урона от ударов (PLANCK/HIGGS) без проверки: смотреть, нет ли двойного расхода выносливости; начальные значения не менять.
- Проверка: В Documents\My Games\Skyrim VR\SKSE\sksevr.log DLL Blade and Blunt загружена (без ошибки версии/адресов). В MCM есть «Blade and Blunt». В бою расходуется выносливость от удара, нет двойного урона.

### Adamant + Adamant — VR Tweaks — `rec` [#30191](https://www.nexusmods.com/skyrimspecialedition/mods/30191)
- Также скачать: VR Tweaks: https://www.nexusmods.com/skyrimspecialedition/mods/190589
- Фаза 7 · тип `mixed` · установка `mo2_mod` · надёжность данных `low`
- Файл: Основной «Adamant - A Perk Overhaul» (#30191) 5.9.2 (все VR-списки, включая Stormcrown). Версию 6.0.x (SE-списки 2026-08) НЕ брать без проверки страницы #190589: Stormcrown VR остался на 5.9.2 и дополнительно ставит «Adamant - VR Tweaks» (#190589) 1.2 (2026-09-04) — этот файл брать поверх. Что именно меняет VR Tweaks и какую версию Adamant он требует — сверить на странице. Опционально (не по умолчанию): «Adamant - Smithing Addon» 5.4.6 (Stormcrown, FUS) и «Simonrim Attack Speed Fix» 1.0.0 (Panda) — их назначение не проверено.
- Установщик: неизвестно — общие правила (по именам архивов — отдельные файлы).
- Требует: Mysticism — A Magic Overhaul (#27839); Poached Bugs VR (#107053); SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Не вместе с: Другие перковые оверхолы (Ordinator, Vokrii, Perk Tree Overhaul и т. п.); Skyrim VR perk-limit патчи, дублирующие VR Tweaks — сверить
- Порядок в MO2: Раздел «12 Бой и геймплей». Порядок: Mysticism → Adamant → Adamant VR Tweaks (ниже Adamant, перезаписывает). Poached Bugs VR с Simonrim Choice Config (из #107053) — в разделе фиксов, отдельный мод.
- Порядок плагина: Adamant после Mysticism; остальное LOOT. Патчи под Adamant (Blade and Blunt и пр.) — ниже самого Adamant.
- Настройки: Начальные значения не менять.
- Проверка: Окно перков показывает перки Adamant; нет вылета при открытии дерева умений. В Documents\My Games\Skyrim VR\SKSE\sksevr.log DLL VR Tweaks (если она есть) загружена без ошибки.

### Accuracy — Localized Combat Damage — `opt` [#187578](https://www.nexusmods.com/skyrimspecialedition/mods/187578)
- Фаза 7 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Main «Accuracy - Latest Version» 1.0.1 (SUP, SE, 2026-09) или VR-проверенная 1.0.0 (Stormcrown VR, 2026-08-07). Один универсальный архив.
- Установщик: нет установщика (по именам архивов); структуру проверить при установке.
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101); Core Impact Framework (#146873)
- Не вместе с: Другие моды урона по зонам попадания
- Порядок в MO2: Раздел «12 Бой и геймплей», ниже Core Impact Framework.
- Настройки: Урон по зонам — настройки в JSON/INI конфигах (имя смотреть в архиве). Начальные не менять.
- Проверка: В Documents\My Games\Skyrim VR\SKSE\sksevr.log DLL загружена. Попадание в голову незащищённого противника наносит заметно больше урона, чем в ногу в тяжёлой броне.
- Заметка: Урон по зонам попадания, 2026 год.

### Core Impact Framework — `opt` [#146873](https://www.nexusmods.com/skyrimspecialedition/mods/146873)
- Фаза 7 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `high`
- Файл: Main «Core Impact Framework - Latest Version» 2.0.5 (Stormcrown VR, 2026-08-28). Старые 1.2.x (Tempus, Panda) не брать: конфиги Sanguine Symphony 1.3.x рассчитаны на 2.x.
- Установщик: нет установщика (по именам архивов; DLL + JSON-конфиги, без плагина).
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Не вместе с: Другие моды звуков/эффектов попаданий (Improved Weapon Impact Effects и т. п.) — дублируют
- Порядок в MO2: Раздел «12 Бой и геймплей». Сначала CIF, потом его конфиги (Sanguine Symphony) — ниже.
- Настройки: Свои конфиги CIF не править: Sanguine Symphony ставит готовые.
- Проверка: В Documents\My Games\Skyrim VR\SKSE\sksevr.log DLL загружена. При ударе по броне/плоти слышны и видны разные эффекты.

### Ricochet — Arrow Physics Framework — `opt` [#160603](https://www.nexusmods.com/skyrimspecialedition/mods/160603)
- Фаза 7 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Main «Ricochet Framework - Latest Version» 1.1.2 (Stormcrown VR, 2026-08-16); 1.1.3 (SUP, SE) — после проверки. Файл «MCM menu» (MCM-02) — по желанию, Stormcrown VR его не ставит.
- Установщик: нет установщика (по именам архивов); структуру проверить при установке.
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Порядок в MO2: Раздел «12 Бой и геймплей». Конфликтов файлов не ожидается.
- Настройки: Если ставится файл MCM menu — нужен SkyUI VR (#91535). Иначе настройки по умолчанию.
- Проверка: В Documents\My Games\Skyrim VR\SKSE\sksevr.log DLL загружена. Стрела по камню/металлу рикошетит, без вылетов в бою.

### Dismembering Framework — `opt` [#126203](https://www.nexusmods.com/skyrimspecialedition/mods/126203)
- Фаза 7 · тип `mixed` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Main «Dismembering Framework - Latest Version» 1.2.3 (Yggdrasil VR, 2026-09-02), запасной 1.2.2 (Stormcrown VR). Версии 1.0.6 (Tempus, Grit, Tahrovin) не брать. Работает только вместе с пакетами ресурсов из следующего пункта (#126328).
- Установщик: нет установщика (по именам архивов). Если установщик есть — неизвестно — общие правила.
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101); SkyUI VR (#91535)
- Не вместе с: Precision — в этой сборке не ставится (только для плоского режима)
- Порядок в MO2: Раздел «12 Бой и геймплей». DF → DF Asset Packs → Next-Gen Decapitations (в таком порядке, нижние перезаписывают).
- Порядок плагина: LOOT; DF-плагин выше его пакетов ресурсов.
- Настройки: Настройки через MCM. Для VR шансы расчленения держать умеренными — проверить кадр в бою. Начальные не менять.
- Проверка: В Documents\My Games\Skyrim VR\SKSE\sksevr.log DLL загружена. В MCM есть Dismembering Framework. Сильный удар по гуманоиду отрубает конечность без вылета.

### NPCs Take Cover — `opt` [#111890](https://www.nexusmods.com/skyrimspecialedition/mods/111890)
- Фаза 7 · тип `mixed` · установка `mo2_mod` · надёжность данных `low`
- Файл: Main «NPCs Take Cover» 1.02 (Stormcrown VR, CSVP, Nordic Souls; формат .rar — MO2 нужен 7-Zip/rar-плагин); 1.01 (Grit, Panda, Librum, LoreRim) — запасная.
- Установщик: неизвестно — общие правила.
- Порядок в MO2: Раздел «12 Бой и геймплей». Конфликтов файлов не ожидается.
- Порядок плагина: Плагин после USSEP; остальное LOOT. Другие моды боевого ИИ — решать по LOOT.
- Настройки: Без настроек.
- Проверка: Лучники прячутся за укрытиями и не стоят на открытом месте под выстрелами. Нет зависания ИИ.

### Enemy Friendly Fire — `opt` [#50483](https://www.nexusmods.com/skyrimspecialedition/mods/50483)
- Фаза 7 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Файл «Enemy Friendly Fire VR» 1.3.1 (Yggdrasil VR, 2026-08-26: «Enemy Friendly Fire VR 50483 1.3.1»). SE-версию 1.3.1/1.2.0/1.1.0 не брать — SE-DLL в VR не загрузится.
- Установщик: нет установщика (по именам архивов); структуру проверить при установке.
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Не вместе с: Enemy Friendly Fire SE/AE (основной файл без VR)
- Порядок в MO2: Раздел «12 Бой и геймплей». Конфликтов файлов не ожидается.
- Настройки: Без настроек.
- Проверка: В Documents\My Games\Skyrim VR\SKSE\sksevr.log DLL загружена. Стрелы и заклинания врагов задевают союзников.

### Simple Offence Suppression (VR) — `rec` [#59508](https://www.nexusmods.com/skyrimspecialedition/mods/59508)
- Фаза 7 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `low`
- Файл: Ставить ДВА мода (как Panda's Sovngarde и Yggdrasil VR): 1) основной «Simple Offence Suppression» (#41764) 2.1.0 («Simple Offence Suppression SE» — Yggdrasil); 2) поверх VR-файл «Simple Offence Suppression VR» (#59508) 2.1.0 — он содержит VR-DLL. Версии SE 2.2.1/2.3.1 с VR 2.1.0 не смешивать без проверки страницы #59508.
- Установщик: нет установщика (по именам архивов); структуру проверить при установке.
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101); SkyUI VR (#91535)
- Не вместе с: Simple Offence Suppression SE/AE без VR-файла — SE-DLL в VR не работает
- Порядок в MO2: Раздел «12 Бой и геймплей». Основной (#41764) → VR-файл (#59508) СРАЗУ НИЖЕ (VR-DLL выигрывает).
- Настройки: Настройки через MCM (SkyUI VR). Начальные не менять.
- Проверка: В Documents\My Games\Skyrim VR\SKSE\sksevr.log VR-DLL загружена без ошибки. Случайный удар по спутнику или нейтралу не делает его врагом.
- Заметка: Спутники и нейтралы не становятся врагами от случайного удара — с физическим боем это обычное дело.

### Mysticism — A Magic Overhaul — `rec` [#27839](https://www.nexusmods.com/skyrimspecialedition/mods/27839)
- Фаза 7 · тип `plugin_only` · установка `mo2_mod` · надёжность данных `high`
- Файл: Main «Mysticism - A Magic Overhaul» (#27839) 2.5.0 (Stormcrown VR, 2026-08-09). Запасная 2.4.2 (Panda's, FUS). «Ordinator Patch» не брать (Ordinator не ставится). Версии 1.x/2.2.4 (Librum, Grit, Tahrovin) устарели.
- Установщик: нет установщика (по именам архивов — один файл).
- Не вместе с: Другие перковые/магические оверхолы (Ordinator, Apocalypse, Enhanced Magic и т. п.)
- Порядок в MO2: Раздел «12 Бой и геймплей», перед Adamant. Spell Wheel VR, Magic Improvements VR, Spellsiphon не конфликтуют (другая область: ввод, не данные).
- Порядок плагина: Mysticism выше Adamant; остальное LOOT.
- Настройки: Без настроек. Poached Bugs VR со своим Simonrim Choice Config стоит отдельным модом в фиксах (g1b).
- Проверка: Заклинания в меню — переработанные Mysticism, нет ошибок плагина в xEdit.
- Заметка: Переработка всей магии, пара к Adamant. Без DLL, 7 VR-сборок.

### Thaumaturgy + Apothecary + Mundus — `opt` [#57138](https://www.nexusmods.com/skyrimspecialedition/mods/57138)
- Также скачать: Apothecary: https://www.nexusmods.com/skyrimspecialedition/mods/52130; Mundus: https://www.nexusmods.com/skyrimspecialedition/mods/33411
- Фаза 7 · тип `plugin_only` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Три отдельных мода SimonRim, везде Main: Thaumaturgy (#57138) 1.5 (Stormcrown VR, 2026-08-10; запасная 1.4.5 — Panda, FUS), Apothecary (#52130) 1.3.9 (Stormcrown, Panda, FUS), Mundus (#33411) 1.15.1 (Stormcrown; запасная 1.13.1). Не брать: Apothecary «Bruma/Fishing/Rare Curios/Food and Drink» патчи (этих модов нет), Thaumaturgy «Jump Boots Addon». «Enchantment XP Tweak» 1.5 (Stormcrown VR) / «Weapon Enchantment XP Tweak» 1.1 (Panda, FUS) — опционально, по умолчанию не ставить; если есть DLL, нужны SKSEVR и VR Address Library и проверка лога.
- Установщик: нет установщика (по именам архивов — отдельные файлы).
- Не вместе с: Другие оверхолы зачарования, алхимии и камней-хранителей
- Порядок в MO2: Раздел «12 Бой и геймплей», после Mysticism и Adamant: Thaumaturgy → Apothecary → Mundus. Если есть SunHelm Survival (#39414) — проверить на странице Apothecary патч под него.
- Порядок плагина: LOOT; все три после Adamant.
- Настройки: Без настроек.
- Проверка: В столах зачарования и алхимии есть переработанные эффекты; камни-хранители — Mundus. Нет ошибок плагина.
- Заметка: Зачарование, алхимия и камни-хранители из набора SimonRim. Опциональную DLL Enchantment XP Tweak не ставить без проверки.

### Experience — `opt` [#17751](https://www.nexusmods.com/skyrimspecialedition/mods/17751)
- Фаза 7 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Main «Experience» 3.7.3 (Stormcrown VR, 2025-11); 3.5.0 (Tempus) — запасная; «Experience NG» 3.1.0 (Grit) устарела. 3.7.4 (TNE, SE) — после проверки.
- Установщик: нет установщика (по именам архивов); структуру проверить при установке.
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Не вместе с: Другие моды на кривую опыта и уровней (Leveling Freedom и т. п.); Experience NG и Experience одновременно
- Порядок в MO2: Раздел «12 Бой и геймплей». Конфликтов файлов не ожидается.
- Настройки: Настройки в INI рядом с DLL (имя файла смотреть в архиве). Начальные не менять.
- Проверка: В Documents\My Games\Skyrim VR\SKSE\sksevr.log DLL загружена. Уровень растёт за квесты и открытия.
- Заметка: Уровень за квесты и исследование. DLL с VR Address Library, стоит в Stormcrown VR.

### Death Drop Overhaul — `opt` [#151590](https://www.nexusmods.com/skyrimspecialedition/mods/151590)
- Фаза 7 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Main «Death Drop Overhaul - Latest Version» 1.3.6 (Stormcrown VR и Yggdrasil VR, 2026-09-06). 1.1.0 (Panda) — старая.
- Установщик: нет установщика (по именам архивов); структуру проверить при установке.
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101); HIGGS — Enhanced VR Interaction (#43930)
- Не вместе с: Другие моды выпадения оружия при смерти
- Порядок в MO2: Раздел «12 Бой и геймплей». Конфликтов файлов не ожидается.
- Настройки: Без настроек. HIGGS нужен только чтобы поднимать упавшее оружие рукой, DLL от него не зависит.
- Проверка: В Documents\My Games\Skyrim VR\SKSE\sksevr.log DLL загружена. Оружие убитого падает с инерцией и его можно схватить HIGGS.
- Заметка: Оружие убитых падает с инерцией, его можно поднять HIGGS.

### Magic Sneak Attacks VR + Physical Dodge VR — `opt` [#68028](https://www.nexusmods.com/skyrimspecialedition/mods/68028)
- Также скачать: Physical Dodge: https://www.nexusmods.com/skyrimspecialedition/mods/58605
- Фаза 7 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `low`
- Файл: Два отдельных мода. «Magic Sneak Attacks VR» (#68028) 1.3.0 (Panda, FUS, Yggdrasil VR); 1.1.0 (Grit, Tahrovin) — старая. «Physical Dodge VR» (#58605) 0.1 (6 VR-списков). SE-версию Magic Sneak Attacks (#67613) поверх не ставить.
- Установщик: нет установщика (по именам архивов); структуру проверить при установке.
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Не вместе с: Magic Sneak Attacks SE/AE (#67613) — SE-DLL в VR не работает
- Порядок в MO2: Раздел «12 Бой и геймплей». Physical Dodge VR — ниже PLANCK и Physical Collision VR.
- Настройки: Магические скрытые атаки: перки скрытности Adamant не дублируют множитель — сверить в MCM/INI, если он есть.
- Проверка: В Documents\My Games\Skyrim VR\SKSE\sksevr.log обе DLL загружены. Скрытая атака заклинанием наносит множитель, рывок корпуса уклоняется.
- Заметка: Скрытые атаки магией; уклонение рывком корпуса.

### Throat Slit — VR — `opt` [#184140](https://www.nexusmods.com/skyrimspecialedition/mods/184140)
- Фаза 7 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `low`
- Файл: Main «Throat Slit VR» (#184140) 1.2 (Yggdrasil VR, 2026-07-25). Единственный VR-список.
- Установщик: нет установщика (по именам архивов); структуру проверить при установке.
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Порядок в MO2: Раздел «12 Бой и геймплей». Конфликтов файлов не ожидается.
- Настройки: Без настроек. Не совмещать на одном движении с Immersive Weapon Penetration VR без проверки.
- Проверка: В Documents\My Games\Skyrim VR\SKSE\sksevr.log DLL загружена. Скрытое движение кинжалом по горлу срабатывает без вылета и двойных ударов.
- Заметка: Горло перерезают движением руки с кинжалом.

### Dynamic Bloodpool Framework — `opt` [#172080](https://www.nexusmods.com/skyrimspecialedition/mods/172080)
- Фаза 7 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Main «Dynamic Bloodpool Framework - Latest Version» 1.0.1 (Panda's Sovngarde, единственный VR-список). 1.1.0 (Nordic Souls PBR, SE, 2026-07-25) — после проверки.
- Установщик: нет установщика (по именам архивов); структуру проверить при установке.
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Не вместе с: Другие моды луж крови
- Порядок в MO2: Раздел «12 Бой и геймплей». Ниже Core Impact Framework.
- Настройки: Лужи в других кровавых модах отключить.
- Проверка: В Documents\My Games\Skyrim VR\SKSE\sksevr.log DLL загружена. После убийства растекается лужа по рельефу.
- Заметка: Лужи крови растекаются по рельефу. VR Address Library в требованиях, стоит в Panda's Sovngarde.

### DF Asset Packs + Next-Gen Decapitations — `opt` [#126328](https://www.nexusmods.com/skyrimspecialedition/mods/126328)
- Также скачать: Humanoid: https://www.nexusmods.com/skyrimspecialedition/mods/126327; Decapitations: https://www.nexusmods.com/skyrimspecialedition/mods/135254
- Фаза 7 · тип `assets_only` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Четыре архива (Main): «Official Creature Asset Pack» (#126328) 1.0.2, «Official Humanoid Asset Pack» (#126327) 1.0.1 (в файле опечатка «Veersion»), «Next-Gen Decapitations» (#135254) 1.4.3 (Stormcrown VR) или 1.2.0/1.3.4 (старые). Патчи «CBBE-3BA» и «HIMBO» (#126327) — только под выбранное тело (решается на этапе тел).
- Установщик: неизвестно — общие правила.
- Требует: Dismembering Framework (#126203)
- Не вместе с: Другие пакеты ресурсов расчленения
- Порядок в MO2: Раздел «12 Бой и геймплей», ниже Dismembering Framework: Creature → Humanoid → Next-Gen Decapitations.
- Порядок плагина: Плагины DF-пакетов — после Dismembering Framework.
- Настройки: Без настроек.
- Проверка: Отрубленная голова/конечность у гуманоида, волка, тролля выглядит корректно, без «квадратных» дыр.
- Заметка: Нужны, если стоит Dismembering Framework.

### Sanguine Symphony — `opt` [#148388](https://www.nexusmods.com/skyrimspecialedition/mods/148388)
- Фаза 7 · тип `assets_only` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Main «Sanguine Symphony - Latest Version» 1.3.3 (Stormcrown VR, 2026-08-01, в паре с CIF 2.0.5); 1.3.5 (Morning Star, SE) — после проверки. «Ultra-HD Textures» — НЕ брать (текстуры отдельным этапом).
- Установщик: нет установщика (по именам архивов; JSON-конфиги CIF и звуки/эффекты).
- Требует: Core Impact Framework (#146873)
- Не вместе с: Другие конфиги CIF и моды звуков/эффектов попаданий
- Порядок в MO2: Раздел «12 Бой и геймплей», СРАЗУ НИЖЕ Core Impact Framework (должен перезаписать его конфиги).
- Настройки: Свои правки в конфигах CIF не вносить.
- Проверка: Эффект и звук удара зависят от брони и места удара. В MO2 нет конфликтов с другими CIF-конфигами.
- Заметка: Конфиги Core Impact Framework: отклик зависит от брони и места удара.

## 13 Мир, ИИ, погружение

### Locational Encounter Zones — `rec` [#85212](https://www.nexusmods.com/skyrimspecialedition/mods/85212)
- Фаза 7 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Locational Encounter Zones 1.0.3 (файл от 2026-08-24, его ставит Stormcrown VR). Запасной — 1.0.2 (Locational Encounter Zones-85212-1-0-2-1676905795.zip): 5 VR-списков.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Порядок в MO2: Раздел «13 Мир, ИИ, погружение», рядом с Arena. Порядок между ними не важен.
- Настройки: Менять нечего. Совместим с Arena (33487): ставить оба.
- Проверка: В sksevr.log DLL загружена без ошибки. У входа в подземелье стража того же уровня, что враги внутри.
- Заметка: Стража у входа в подземелье того же уровня, что и враги внутри. Одна DLL с VR-пресетом, 6 VR-сборок.

### Don't Stay in The Water — NPC Water AI Fix — `rec` [#52164](https://www.nexusmods.com/skyrimspecialedition/mods/52164)
- Фаза 7 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `high`
- Файл: Только файл «Don't Stay in The Water - VR» 4.1 (Don't Stay in The Water - VR-52164-4-1-1626445959.zip). Файлы «NPC Water AI Fix for SkyrimSE» 5.1 и «...AE 1.6.629 and newer» 5.1 не брать.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Не вместе с: NPC Water AI Fix 5.x (файлы SE и AE той же страницы)
- Порядок в MO2: Раздел «13 Мир, ИИ, погружение». Порядка относительно других модов нет.
- Настройки: Менять нечего. Страница VR-файла может не требовать Address Library явно — это не мешает, она уже стоит.
- Проверка: В sksevr.log плагин загружен без ошибки. Враги не стоят в воде, а выходят к игроку.
- Заметка: NPC перестают стоять в воде и топтаться у кромки в бою. Брать VR-файл 4.1, не AE-версию 5.x.

### Combat Pathing Revolution + VR — `opt` [#86950](https://www.nexusmods.com/skyrimspecialedition/mods/86950)
- Также скачать: VR-DLL: https://www.nexusmods.com/skyrimspecialedition/mods/87895
- Фаза 7 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Два архива. 1) Combat Pathing Revolution 0.30 со страницы 86950 (Combat Pathing Revolution-86950-v0-30-1678975298.7z). 2) Поверх него VR-файл со страницы 87895: Combat Pathing Revolution VR 0.30.1 (Combat Pathing Revolution VR-87895-0-30-1-1694056363.7z); он заменяет DLL и PDB. Оба архива стоят в FUS, Panda, Tahrovin, Tempus VR.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Не вместе с: Fenix Combat AI (страница CPR: переписывает дерево поведения ИИ, вместе с CPR вылеты)
- Порядок в MO2: Два отдельных мода: «CPR» и ниже «CPR VR DLL» (VR выше по приоритету, перезаписывает файлы). Behavior Data Injector — в раздел «02 SKSEVR и библиотеки»: сначала BDI, ниже BDI Universal Support (перезаписать DLL), и только потом CPR.
- Настройки: Менять нечего. Не ставить второй мод боевого ИИ, который переписывает behavior-дерево. Тег opt: при проблемах с поведениями (Pandora) отключить сначала CPR.
- Проверка: В sksevr.log загружены DLL CPR и Behavior Data Injector без ошибок. В бою NPC обходят и отступают, а не стоят.
- Заметка: NPC в бою кружат, отступают и обходят. Поверх основного — DLL с VR-страницы.

### AI Overhaul — `opt` [#21654](https://www.nexusmods.com/skyrimspecialedition/mods/21654)
- Фаза 7 · тип `plugin_only` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Путь B (USSEP 4.2.5b): только файл «AI Overhaul for SE Only» — 1.8.7 (AI Overhaul SE Only 1.8.7-21654-1-8-7-1746511421.zip, Panda) или 1.8.6 (FUS). Путь A (мастера 1.6.1170, USSEP 4.3.x): по заметке куратора AE-файл — «AI Overhaul AE 1.8.7» (LoreRim, Tomes of Talos, True North); он помечен как ESL. В VR-списках AE-файл не проверен: при красных мастерах в MO2/xEdit заменить на SE Only 1.8.7. Файл Lite и Scripted BETA не брать.
- Установщик: нет установщика (отдельные файлы SE Only / AE на странице)
- Не вместе с: AI Overhaul Lite (если ставится основной)
- Порядок в MO2: Раздел «13 Мир, ИИ, погружение», ниже USSEP и модов, меняющих NPC и расписания. Патчи совместимости с NPC-модами — ниже AI Overhaul.
- Порядок плагина: После USSEP и модов, правящих NPC/пакеты; остальное по LOOT. Если взят AE-файл — он ESL, проверить число плагинов.
- Настройки: Нужны патчи под NPC-моды (брать только для установленных, из xEdit-конфликтов). Расписания AI Overhaul меняются при загрузке старого сохранения — ставить на новую игру.
- Проверка: Плагин в списке активен, xEdit не показывает отсутствующих мастеров. Лог Papyrus без ошибок от AI Overhaul.
- Заметка: Живее распорядок и реакции ванильных NPC. Путь B — файл «SE Only», путь A — AE-файл. Нужны патчи с NPC-модами.

### Realistic AI Detection (RAID) — `opt` [#2345](https://www.nexusmods.com/skyrimspecialedition/mods/2345)
- Фаза 7 · тип `plugin_only` · установка `mo2_mod` · надёжность данных `high`
- Файл: RAID 3: «Realistic AI Detection 3 - Medium Interior Medium Exterior» 3.1 (Realistic AI Detection 3 - Medium Interior Medium Exterior-2345-3-1-1650801751.zip): Panda, Spirit of Grit, Tahrovin-Grit, Yggdrasil VR. Для лёгкого варианта — «RAID 3 - Lite» (FUS, Tahrovin). Только один файл из трёх (Lite / Medium / High).
- Установщик: нет установщика (отдельные файлы по уровню сложности)
- Не вместе с: Другие моды, переписывающие формулу обнаружения и скрытности; Второй файл RAID (Lite/Medium/High) одновременно
- Порядок в MO2: Раздел «13 Мир, ИИ, погружение». Мод без скриптов, порядок не критичен.
- Настройки: Менять нечего. Ничего больше про обнаружение не ставить.
- Проверка: Плагин активен. В стелсе враги замечают игрока заметно раньше, чем в ваниле.
- Заметка: Зорче зрение и слух врагов, дольше поиски, без скриптов. RAID 3 Medium или Lite.

### Smart NPC Potions — `opt` [#40102](https://www.nexusmods.com/skyrimspecialedition/mods/40102)
- Фаза 7 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Smart NPC Potions 1.22 (Smart NPC Potions-40102-1-22-1730744765.rar): Spirit of Grit, Tahrovin-Grit. Запасные: 1.11 (Tahrovin), новее — 1.30 (LoreRim, SKP). Архив .rar, нужен 7-Zip-движок MO2.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Не вместе с: Другие моды зелий и ядов для NPC
- Порядок в MO2: Раздел «13 Мир, ИИ, погружение». Рядом с Apothecary (combat-57138), если тот ставится.
- Настройки: INI в Data\SKSE\Plugins настраивает шансы — по желанию. Дополняет Apothecary.
- Проверка: В sksevr.log DLL загружена без ошибки. У врагов в бою есть зелья и яды.
- Заметка: Враги носят и пьют зелья, используют яды. VR заявлен в changelog.

### NPC Spell Variance — `opt` [#132097](https://www.nexusmods.com/skyrimspecialedition/mods/132097)
- Фаза 7 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: NPC Spell Variance не старее 2.7.1: 2.7.2 (True North, 2026-09-25) или 2.7.1 (Northern Experience, 2026-09-09). VR-проверенный запасной — 2.4.3 (NPC Spell Variance-132097-2-4-3-1752745072.7z, Panda), 2.1.5 (Tempus). Необязательный файл «NSV - Vanilla Runes for Spellcasters (SPID)» 2.1.6 (Panda) — только с SPID VR.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Порядок в MO2: Раздел «13 Мир, ИИ, погружение». Если ставится Adamant (combat-30191) — ниже него.
- Настройки: После первого запуска просмотреть INI. KID/SPID-аддоны для пакетов магии — по желанию.
- Проверка: В sksevr.log нет ошибки хука при загрузке. Маги в бою меняют заклинания, нет вылета при первом бою с магом. Вылет — откатить на 2.4.3.
- Заметка: Маги-NPC используют весь арсенал. VR-хук исправлен только в 2.7.1 — не брать старее.

### NPCs React To Invisibility + NPCs React To Necromancy — `opt` [#91480](https://www.nexusmods.com/skyrimspecialedition/mods/91480)
- Также скачать: Necromancy: https://www.nexusmods.com/skyrimspecialedition/mods/70428
- Фаза 7 · тип `mixed` · установка `mo2_mod` · надёжность данных `medium`
- Файл: NPCs React To Invisibility 1.11 (NPCs React To Invisibility-91480-1-11-1724586730.zip; FUS, Panda) + NPCs React To Necromancy 1.03 (#70428; NPCs React To Necromancy-70428-1-03-1739570458.zip; Panda). Только если ставится Apothecary (combat-57138) — файл «Patch for Apothecary's Ethereal Potions» 1.10 (#91480, Panda). Патчи «Bow of Shadows» (CC нет в наборе) и «No Consequences» не брать.
- Установщик: неизвестно — общие правила
- Порядок в MO2: Раздел «13 Мир, ИИ, погружение». Патч Apothecary — ниже Apothecary.
- Порядок плагина: Патч Apothecary — после Apothecary, по LOOT.
- Настройки: Менять нечего.
- Проверка: Плагины активны. Невидимость или поднятый мертвец рядом с NPC вызывает озвученную реплику.
- Заметка: Озвученные реакции NPC на невидимость и поднятых мертвецов.

### Enhanced Reanimation + VR — `opt` [#43500](https://www.nexusmods.com/skyrimspecialedition/mods/43500)
- Также скачать: VR-файл: https://www.nexusmods.com/skyrimspecialedition/mods/59512
- Фаза 7 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: VR-файл Enhanced Reanimation VR 1.5.1 со страницы 59512 (Enhanced Reanimation VR-59512-1-5-1-1669711333.7z): 6 VR-списков, описание — «SKSEVR plugin, built from po3's source». Основной Enhanced Reanimation 1.5.1 (#43500, Enhanced Reanimation-43500-1-5-1-1665607585.7z) ставят под него только Spirit of Grit, Tahrovin, Tahrovin-Grit; Panda, Tempus, Yggdrasil — один VR-файл. Версию SE 1.5.2 без VR-обновления не ставить.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Не вместе с: Enhanced Reanimation SE 1.5.2 (DLL без VR)
- Порядок в MO2: Если нужен основной файл — отдельный мод «Enhanced Reanimation», ниже него «Enhanced Reanimation VR» (VR выше по приоритету, перезаписывает DLL). Раздел «13 Мир, ИИ, погружение».
- Настройки: Сначала открыть VR-архив: если в нём есть ESP и ассеты — основной файл не нужен. Если ESP нет — поставить основной 1.5.1 и перезаписать DLL VR-файлом. В Data\SKSE\Plugins не должно остаться двух DLL Enhanced Reanimation.
- Проверка: В sksevr.log DLL VR загружена без ошибки. Поднятый мертвец встаёт с анимацией и эффектом.
- Заметка: Улучшенное поднятие мёртвых. Основной 1.5.1 и VR-файл 1.5.1 поверх; SE 1.5.2 без VR-обновления не ставить.

### Frozen Electrocuted Combustion VR — `opt` [#59118](https://www.nexusmods.com/skyrimspecialedition/mods/59118)
- Фаза 7 · тип `mixed` · установка `mo2_mod` · надёжность данных `high`
- Файл: Два архива: сначала оригинал Frozen Electrocuted Combustion 5.1.0 со страницы 3532 (Frozen Electrocuted Combustion-3532-5-1-0-1668639002.7z; во всех 7 VR-списках), затем поверх FEC VR 5.1.0.4 со страницы 59118 (FEC VR-59118-5-1-0-4-1702713188.7z; Librum, Panda, Grit, Tahrovin-Grit, Tahrovin). FEC 6.x (True North) не брать. Заметка куратора «VR вместо SE 3532» неверна: описание VR-файла — «requires original FEC to run».
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101); powerofthree's Papyrus Extender + Papyrus Extender VR (#22854)
- Не вместе с: Frozen Electrocuted Combustion 6.x (SE-версия новее 5.1.0)
- Порядок в MO2: Два мода: «FEC» выше, «FEC VR» ниже и перезаписывает. Раздел «09 Свет, погода, вода, VFX» или «13». Патч Embers XD — ниже обоих.
- Порядок плагина: Плагин FEC после Papyrus Extender; остальное по LOOT.
- Настройки: Если ставится Embers XD (world-37085): добавить «Embers XD - Frozen Electrocuted Combustion Patch» (#69446; 2.0 у Panda, 1.0 у Tempus) — в manifest его нет. Остальные патчи FEC (Ordinator и т.п.) не нужны.
- Проверка: В sksevr.log DLL FEC VR загружена. Убитый огнём враг обугливается, замороженный покрыт льдом.
- Заметка: Замороженные, обугленные и наэлектризованные тела. Брать VR-страницу, не SE 3532.

### Arena — An Encounter Zone Overhaul — `opt` [#33487](https://www.nexusmods.com/skyrimspecialedition/mods/33487)
- Фаза 7 · тип `plugin_only` · установка `mo2_mod` · надёжность данных `high`
- Файл: Arena - An Encounter Zone Overhaul 1.2.0, основной файл (Arena - An Encounter Zone Overhaul-33487-1-2-0-1687450157.7z; Stormcrown VR, Panda, FUS). Файл «Harder Easy Spawns» не брать.
- Установщик: неизвестно — общие правила
- Не вместе с: Open World Loot (в manifest нет); Другие моды, переделывающие encounter zones
- Порядок в MO2: Раздел «13 Мир, ИИ, погружение», рядом с Locational Encounter Zones.
- Порядок плагина: По LOOT.
- Настройки: Менять нечего. Совместим с Locational Encounter Zones (85212): ставить оба.
- Проверка: Плагин активен. Уровни врагов в регионе не равны уровню игрока на низких уровнях.
- Заметка: Опасность растёт по регионам, а не под уровень игрока. Совместим с Locational Encounter Zones.

### Trade and Barter — `opt` [#23081](https://www.nexusmods.com/skyrimspecialedition/mods/23081)
- Фаза 7 · тип `plugin_only` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Trade and Barter SE 2.2 (Trade and Barter SE-23081-2-2-1737695883.7z; Panda). Запасные — 2.1 (Tempus, Librum), 2.0 (Grit, Ygg). Отдельного VR-файла нет.
- Установщик: неизвестно — общие правила
- Не вместе с: Другие моды на цены, торговлю и золото торговцев
- Порядок в MO2: Раздел «13 Мир, ИИ, погружение».
- Порядок плагина: По LOOT.
- Настройки: Курсы и золото торговцев менять в INI/MCM по желанию.
- Проверка: Плагин активен. В торговле другие цены и золото торговцев, чем в ваниле.
- Заметка: Настройка курсов торговли и золота торговцев.

### Realistic Mining and Chopping for VR + VR Refit — `rec` [#16692](https://www.nexusmods.com/skyrimspecialedition/mods/16692)
- Также скачать: VR Refit: https://www.nexusmods.com/skyrimspecialedition/mods/49205
- Фаза 7 · тип `mixed` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Два архива. 1) Realistic Mining and Chopping for VR, файл «for VR - USSEP» 1.1.0 (Realistic Mining and Chopping for VR - USSEP-16692-1-1-0.zip; 8 VR-списков, в том числе Tempus на USSEP 4.3.2). 2) VR Refit - Mine Chop and Drop 1.0.4 со страницы 49205 (VR Refit - Mine Chop and Drop-49205-1-0-4-1648691454.zip; 6 VR-списков; 1.0.3 — FUS, Librum). Файл «Infinite Mining Nodes» не брать.
- Установщик: неизвестно — общие правила
- Требует: USSEP 4.3.x (#266, путь A) или USSEP 4.2.5b (#266 Old files, путь B)
- Порядок в MO2: Раздел «13 Мир, ИИ, погружение». VR Refit — отдельным модом ниже основного.
- Порядок плагина: Оба плагина ниже USSEP.
- Настройки: Требования на странице проверить: скорее всего SKSEVR, а VR Refit — HIGGS (уже в наборе). Оба файла стоят в 6 VR-списках вместе.
- Проверка: У рудной жилы и дерева нужны реальные удары киркой и топором. Руда и дрова падают физическими предметами.
- Заметка: Руду и дрова добывают настоящими взмахами, а VR Refit роняет их физическими предметами. Файл «for VR - USSEP». 8 VR-сборок.

### Gift by Hand VR — `opt` [#99809](https://www.nexusmods.com/skyrimspecialedition/mods/99809)
- Фаза 7 · тип `mixed` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Main file - Gift By Hand VR 2.1.0 (Main file - Gift By Hand VR-99809-2-1-0-1700472570.zip; FUS, Panda, Grit x2, Tahrovin; у Tempus файл с префиксом «1_Main file»). Остальные необязательные файлы не брать.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Порядок в MO2: Раздел «13 Мир, ИИ, погружение» или рядом с HIGGS; ниже HIGGS (vr-43930).
- Настройки: По описанию мод использует захват рукой — вероятно, зависит от HIGGS (он в наборе). Подтвердить по вкладке Requirements.
- Проверка: Отдать предмет компаньону, протянув руку. В sksevr.log нет ошибок плагина.
- Заметка: Отдать предмет NPC, протянув его рукой.

### Sleeping Expanded — `opt` [#59250](https://www.nexusmods.com/skyrimspecialedition/mods/59250)
- Фаза 7 · тип `mixed` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Sleeping Expanded 1.22 (Sleeping Expanded-59250-1-22-1670752210.zip): все 7 VR-списков, один и тот же архив с SE. Старый «Animations and NPC Reactions» 1.21 не нужен.
- Установщик: неизвестно — общие правила
- Порядок в MO2: Раздел «13 Мир, ИИ, погружение».
- Порядок плагина: По LOOT.
- Настройки: Если установщик или страница требуют OAR — Open Animation Replacer (anim-92109) уже в наборе. Если мод кладёт behavior-файлы, перегенерировать их Pandora (tools-133232). Состав архива не проверен.
- Проверка: NPC дышат во сне, при пробуждении ночью озвучены реакции.
- Заметка: Разные позы сна NPC и реакции на спящих.

### Be Seated — Skyrim VR Edition — `opt` [#16613](https://www.nexusmods.com/skyrimspecialedition/mods/16613)
- Фаза 7 · тип `mixed` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Be Seated 4.2.5, VR-редакция (Be Seated 4.2.5-16613-4-2-5-1655673281.zip; FUS, Librum, Tempus, Yggdrasil VR).
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457)
- Порядок в MO2: Раздел «13 Мир, ИИ, погружение».
- Настройки: Проверить Requirements на странице: вероятно, нужен SkyUI VR для MCM. Возможное перекрытие с Take a Seat (anim-54193) — оба про сидение; не включать оба без проверки.
- Проверка: Можно сесть на землю или у костра. Нет вылетов при вставании.
- Заметка: Сесть где угодно — на землю, у костра.

### SunHelm Survival — `opt` [#39414](https://www.nexusmods.com/skyrimspecialedition/mods/39414)
- Фаза 7 · тип `mixed` · установка `mo2_mod` · надёжность данных `medium`
- Файл: SunHelm Survival 3.1.4 (SunHelm Survival-39414-3-1-4-1661703641.7z; FUS, Panda, Spirit of Grit, Tahrovin-Grit). Ygg — 3.1.2a, Librum — 2.0.6 не брать.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); SkyUI VR (#91535)
- Не вместе с: Survival Mode Improved SKSE (в списке запретов); Режим выживания CC одновременно с SunHelm
- Порядок в MO2: Раздел «13 Мир, ИИ, погружение».
- Порядок плагина: По LOOT.
- Настройки: Плагин CC Survival Mode не удалять (путь A): страница SunHelm сама отключает CC-выживание. Настройки — в MCM. Начинать на новой игре.
- Проверка: В MCM есть пункт SunHelm. В игре появляются голод, жажда, усталость; предложения CC-выживания нет.
- Заметка: Голод, жажда, усталость, холод. CC-выживание на странице отключено, дубля нет.

### Recipe Auto-Learn + Reading Is Good — `opt` [#84909](https://www.nexusmods.com/skyrimspecialedition/mods/84909)
- Также скачать: Reading Is Good VR: https://www.nexusmods.com/skyrimspecialedition/mods/42026
- Фаза 7 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Recipe Auto-Learn 1.1.1 (Recipes 1.1.1-84909-1-1-1-1677267647.rar; FUS, Panda, Tempus VR; 1.2.0 — новее, SE). Reading Is Good — только VR-файл «Reading Is Good VR» 1.1.2 со страницы 42026 (Reading Is Good VR-42026-1-1-2-1664479626.7z; Spirit of Grit, Tahrovin-Grit); SE-файл «Reading Is Good SE» не брать.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Не вместе с: Reading Is Good SE (файл SE той же страницы)
- Порядок в MO2: Раздел «13 Мир, ИИ, погружение». Хорошо работает с Apothecary.
- Настройки: Менять нечего. Мод Reading Is Good (SKSE) — отдельный DLL, оба плагина должны быть в Data\SKSE\Plugins.
- Проверка: В sksevr.log обе DLL загружены. Прочитанная книга навыка даёт опыт сразу, рецепт открывает эффекты ингредиентов.
- Заметка: Рецепты открывают эффекты ингредиентов; книги навыков дают опыт сразу. У Reading Is Good брать VR-файл.

### Mum's the Word NG — `opt` [#77409](https://www.nexusmods.com/skyrimspecialedition/mods/77409)
- Фаза 7 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `high`
- Файл: Mum's the Word NG 2.1 (Mum's the Word-77409-2-1-1666299465.zip; Librum, Tahrovin, Grit x2, Tempus VR). Версия 2.2 (SKP) в VR не проверена.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Порядок в MO2: Раздел «13 Мир, ИИ, погружение».
- Настройки: Менять нечего. Описание: одна DLL на CLib-NG для всех SE, AE 1.6.629+ и VR.
- Проверка: В sksevr.log DLL загружена. Украденная вещь без свидетелей не помечена «украдено».
- Заметка: Снимает метку «украдено», если кражу никто не видел — с HIGGS легко схватить чужое. VR заявлен.

### Honed Metal — `opt` [#61015](https://www.nexusmods.com/skyrimspecialedition/mods/61015)
- Фаза 7 · тип `mixed` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Только «Honed Metal VR» 1.23 (Honed Metal VR-61015-1-23-1646437077.7z; Spirit of Grit, Tahrovin-Grit, Tempus). Основной SE/AE-файл 1.26.1 вместо VR не брать: Tempus ставит его вместе с VR-файлом, Grit-списки — один VR-файл. Файл «HonedMetal.ini - Ordinator» нужен только при Ordinator (в наборе нет).
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); SkyUI VR (#91535)
- Не вместе с: Honed Metal SE/AE-файл как замена VR-файла
- Порядок в MO2: Раздел «13 Мир, ИИ, погружение».
- Порядок плагина: По LOOT.
- Настройки: Настройка — MCM. Если VR-архив окажется неполным (нет ESP) — поставить основной 1.26.1 и перезаписать VR-файлом.
- Проверка: В MCM есть Honed Metal. Кузнец за плату куёт и зачаровывает.
- Заметка: Кузнецы и маги за плату куют и зачаровывают снаряжение.

### GIST — Genuinely Intelligent Soul Trap — `opt` [#15755](https://www.nexusmods.com/skyrimspecialedition/mods/15755)
- Фаза 7 · тип `plugin_only` · установка `mo2_mod` · надёжность данных `medium`
- Файл: GIST Soul Trap 1.3 (GIST Soul Trap-15755-1-3.zip): 6 VR-списков.
- Установщик: неизвестно — общие правила
- Не вместе с: Другие моды переработки захвата душ
- Порядок в MO2: Раздел «13 Мир, ИИ, погружение». Патчи совместимости — ниже.
- Порядок плагина: По LOOT.
- Настройки: Если Mysticism (combat-27839) трогает захват душ — на страницах Mysticism/GIST искать патч (FUS ставит такой для Sorcerer). Название патча неизвестно.
- Проверка: Плагин активен. Душа идёт в камень по размеру.
- Заметка: Душа идёт в самый подходящий камень.

### SCIE — Crafting Inventory Extender — `opt` [#170497](https://www.nexusmods.com/skyrimspecialedition/mods/170497)
- Фаза 7 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: SCIE-Main 2.6.0.0 или новее — в нём исправлены VR-вылет на старте (Hook 5) и нулевые счётчики. Tempus VR ставит SCIE-Main 2.5.3 (SCIE-Main-v2.5.3.zip-170497-2-5-3-0-1769949698.zip) — старее, не брать. Необязательные файлы: SCIE-HomeConfigs (есть у Tempus), CCOR/DLC/Babel — не нужны.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101); Skyrim VR ESL Support (#106712)
- Не вместе с: Craft from Containers и другие моды «крафт из сундуков»
- Порядок в MO2: Раздел «13 Мир, ИИ, погружение».
- Порядок плагина: По LOOT.
- Настройки: SkyUI VR нужен только для MCM. Ограничение VR: глобальные контейнеры могут не работать для неперсистентных ссылок (мод пишет об этом сам). Локальные контейнеры работают.
- Проверка: В sksevr.log DLL загружена, старт игры без вылета. У верстака в списке материалов есть предметы из соседних сундуков, счётчики не нулевые.
- Заметка: Верстак берёт материалы из ближних сундуков и у спутников. В 2.6 исправлен VR-вылет на старте.

### Dirt and Blood — `opt` [#38886](https://www.nexusmods.com/skyrimspecialedition/mods/38886)
- Фаза 7 · тип `mixed` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Dirt and Blood 2.37 (Dirt and Blood-38886-2-37-1735311983.rar; Librum VR, Panda) + «Optional patch for VR - No Washing Animation» (Optional patch for VR - No Washing Animation-38886-1-66-1612390710.zip; Librum VR). Версию 2.38 (SKP) не брать.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457)
- Не вместе с: Wash That Blood Off 2 VR (#62372) — не ставить вместе, функции смыва пересекаются
- Порядок в MO2: Раздел «13 Мир, ИИ, погружение». VR-патч — ниже основного.
- Порядок плагина: VR-патч — после основного.
- Настройки: Патч «No Washing Animation» ставить всегда. Если нужен Wash That Blood Off 2 VR (62372, 5 VR-списков) — выбрать что-то одно.
- Проверка: На теле копятся грязь и кровь. При входе в воду нет анимации умывания.
- Заметка: На телах копятся грязь и кровь, смываются водой. Поставить VR-патч «No Washing Animation».

### Dynamic Things Alternative + Random Barrel Roll — `opt` [#60741](https://www.nexusmods.com/skyrimspecialedition/mods/60741)
- Также скачать: Random Barrel Roll: https://www.nexusmods.com/skyrimspecialedition/mods/78195
- Фаза 7 · тип `mixed` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Dynamic Things Alternative - Base Object Swapper 0.3 (Dynamic Things Alternative - Base Object Swapper-60741-0-3-1728083488.7z; Panda, Tempus VR) — VR-проверенная. 0.5 (Stormcrown VR, 2026) — новее и «с DLL»: брать после проверки лога. Random Barrel Roll 0.1.1 (Random Barrel Roll-78195-0-1-1-1744090974.7z; Panda) или 0.1 (Grit, Tempus).
- Установщик: неизвестно — общие правила
- Требует: Base Object Swapper VR (#61734); SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Порядок в MO2: Раздел «13 Мир, ИИ, погружение», ниже Base Object Swapper VR. С Lightened Skyrim BOS не пересекается.
- Настройки: Если взят 0.5 и в sksevr.log ошибка DLL — вернуть 0.3.
- Проверка: В sksevr.log Base Object Swapper применил SWAP-файлы, ошибок нет. В мире больше разных контейнеров, бочки повёрнуты по-разному.
- Заметка: Разнообразие контейнеров и случайный поворот бочек через BOS VR.

### Better Resource Warnings — `opt` [#26751](https://www.nexusmods.com/skyrimspecialedition/mods/26751)
- Фаза 7 · тип `plugin_only` · установка `mo2_mod` · надёжность данных `high`
- Файл: Better Resource Warnings 2.2 (Better Resource Warnings-26751-2-2-1609018535.7z; FUS, Librum, Panda, Ygg).
- Установщик: неизвестно — общие правила
- Порядок в MO2: Раздел «13 Мир, ИИ, погружение».
- Настройки: Пороги здоровья и запаса сил — в настройках мода. Частично дублирует Immersive HUD и полоски на запястье Spell Wheel VR; при дубле отключить пороги здесь.
- Проверка: При низком здоровье слышны сердцебиение и дыхание.
- Заметка: Сердцебиение и дыхание при низком здоровье — в шлеме звук заметнее полосок.

### Sink Or Swim NG — `opt` [#78610](https://www.nexusmods.com/skyrimspecialedition/mods/78610)
- Фаза 7 · тип `skse_dll` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Sink Or Swim NG 1.9 (Sink Or Swim NG-78610-1-9-1668230874.rar; Librum VR, Spirit of Grit, Tahrovin, Tahrovin-Grit). Старый Sink Or Swim со страницы 42962 не ставить: Librum VR живёт без него; Grit-списки держат оба (причина неизвестна).
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Не вместе с: Sink Or Swim (#42962, старая версия)
- Порядок в MO2: Раздел «13 Мир, ИИ, погружение».
- Настройки: Если описание файла NG требует оригинал — поставить 42962 первым и перезаписать NG; иначе только NG.
- Проверка: В sksevr.log DLL загружена. В тяжёлой броне игрок идёт по дну, остальные тонут медленнее.
- Заметка: В тяжёлой броне игрок тонет и идёт по дну. Сборка NG для AE/VR, не старая 42962.

### Tamrielic Names + NPCs Names Distributor — `opt` [#73153](https://www.nexusmods.com/skyrimspecialedition/mods/73153)
- Также скачать: NND: https://www.nexusmods.com/skyrimspecialedition/mods/73081
- Фаза 7 · тип `mixed` · установка `mo2_mod` · надёжность данных `low`
- Файл: Tamrielic Names 1.2.1 (Tamrielic Names-73153-1-2-1-1725015432.zip; CSVP, LoreRim, Nordic Souls, Wunduniik, Northern Experience) + NPCs Names Distributor (#73081): 2.6.2 (LoreRim) или 2.6.3 (Northern Experience, 2026-09-01). Среди VR-списков не используется. Файл «NPCs Names Distributor INI» не нужен.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101); Spell Perk Item Distributor VR (#59121)
- Порядок в MO2: Раздел «13 Мир, ИИ, погружение». NND выше, Tamrielic Names ниже (его конфиги перезаписывают).
- Настройки: Tamrielic Names — только конфиги для NND. Проверить в архиве NND наличие VR-сборки DLL. Если у NND нет VR-DLL — пропустить пару целиком.
- Проверка: В sksevr.log NND загружен. Безымянные NPC получают имена по расе.
- Заметка: Безымянные NPC получают имена по расе. Полезно с ИИ-NPC.

## 14 ИИ-NPC

### SkyrimNet — `opt` [ссылка](https://github.com/MinLL/SkyrimNet-GamePlugin/releases)
- Фаза 9 · тип `mixed` · установка `mo2_mod` · надёжность данных `medium`
- Файл: Основной архив SkyrimNet из последнего релиза GitHub: MinLL/SkyrimNet-GamePlugin, Beta26 (тег vbeta26-rc4, 03.10.2026, четыре файла в релизе; имена не получены). Голоса Piper TTS — отдельным модом, только если выбран Piper.
- Установщик: нет установщика (по README): поставить мод, включить SkyrimNet.esp, дальше мастер настройки в браузере
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101); Skyrim VR ESL Support (#106712); Skyrim VR Refocused (#32737); MFG Fix NG (#133568); PapyrusUtil VR (#13048); powerofthree's Papyrus Extender + Papyrus Extender VR (#22854); powerofthree's Tweaks + po3 Tweaks VR (#51073)
- Не вместе с: Mantella (ai-98631); CHIM (ai-126330); Backported Extended ESL Support (в списке запретов)
- Группа «одно из»: `ai-npc`
- Порядок в MO2: Раздел «14 ИИ-NPC», ниже всех NPC-модов. Prisma UI и Media Keys Fix — в «02 SKSEVR и библиотеки».
- Порядок плагина: SkyrimNet.esp — после Skyrim VR ESL Support; остальное по LOOT.
- Настройки: Нужен ключ OpenRouter (или совместимый OpenAI API), CPU с AVX2. У po3 Tweaks оставить включённым «Load EditorIDs». Запуск через SKSE, затем localhost:8080 — мастер настройки. DBVO (1.1.1, не 2.x) и CUDA 12.x (не 13.x) — по желанию; DBVO в VR требует VR-патч DBVO. Piper-голоса, если Piper.
- Проверка: В sksevr.log SkyrimNet загружен. localhost:8080 открывается, мастер пройден, NPC отвечают на реплику.
- Заметка: Развивается активнее всех, VR-фиксы почти в каждой бете. Для VR требует Skyrim VR ESL Support, Refocused, MFG Fix NG, po3 Tweaks SE и VR. Модели через OpenRouter, часть платная.

### Mantella — `opt` [#98631](https://www.nexusmods.com/skyrimspecialedition/mods/98631)
- Фаза 9 · тип `mixed` · установка `mo2_mod` · надёжность данных `low`
- Файл: Mantella 0.14 — основной файл со страницы 98631 (релиз 0.14 на GitHub art-from-the-machine/Mantella от 21 апреля). Страница заявляет VR / SE / AE. Модель по умолчанию — бесплатная Gemma 4 через API. Голос — Piper или XTTS; распознавание речи — Moonshine или Whisper.
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101); PapyrusUtil VR (#13048)
- Не вместе с: SkyrimNet (ai-0); CHIM (ai-126330); Fuz Ro D-oh VR (вылеты, в списке запретов)
- Группа «одно из»: `ai-npc`
- Порядок в MO2: Раздел «14 ИИ-NPC», ниже всех NPC-модов.
- Порядок плагина: После USSEP (требование страницы); остальное по LOOT.
- Настройки: Для PapyrusUtil брать VR-версию (в наборе). Приложение Mantella запускается отдельно; ключ API и голос настраиваются в его интерфейсе. Список требований страницы 0.14 не прочитан — сверить вкладку Requirements.
- Проверка: В sksevr.log плагин загружен. Запущен Mantella, NPC отвечает голосом на реплику из микрофона.
- Заметка: Проще в настройке, бесплатная модель по умолчанию, голос Piper или XTTS. Замечены вылеты вместе с Fuz Ro D-oh.

### CHIM — `opt` [#126330](https://www.nexusmods.com/skyrimspecialedition/mods/126330)
- Фаза 9 · тип `guide_steps` · установка `manual_steps` · надёжность данных `low`
- Файл: Два шага. 1) Мод CHIM со страницы 126330 (файл AIAgent) в MO2. 2) Внешний сервер: DwemerDistroInstaller.exe из релиза Dwemer-Dynamics/DwemerDistro-Launcher (не ZIP), запуск от администратора, затем в лаунчере в Quickstart выбрать CHIM. Нативный плагин CHIM — одна DLL для SE, AE и VR (README).
- Установщик: неизвестно — общие правила
- Требует: SKSEVR (#30457); VR Address Library for SKSEVR (#58101)
- Не вместе с: SkyrimNet (ai-0); Mantella (ai-98631)
- Группа «одно из»: `ai-npc`
- Порядок в MO2: Раздел «14 ИИ-NPC», ниже всех NPC-модов.
- Порядок плагина: По LOOT.
- Настройки: Сервер, ключи API и голос настраивать в веб-интерфейсе DwemerDistro. Список модов-требований страницы 126330 не прочитан — сверить вкладку Requirements. После обновления мода обновлять и сервер.
- Проверка: В sksevr.log CHIM загружен. DwemerDistro запущен, NPC отвечает на реплику.
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
