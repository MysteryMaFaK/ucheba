import html

NX = "https://www.nexusmods.com/skyrimspecialedition/mods/{}"


def nx(i):
    return NX.format(i)


# tag: core = обязательно, rec = рекомендую, opt = по желанию, alt = альтернатива
SECTIONS = [
    {
        "id": "tools",
        "title": "Инструменты и подготовка",
        "lead": "Чистая Skyrim VR 1.4.15 в отдельной библиотеке Steam (не Program Files), один запуск до главного меню. "
                "Суперсэмплинг в SteamVR — 100% и глобально, и для игры: резкость даёт апскейлер, а не SS.",
        "items": [
            dict(name="Mod Organizer 2", url="https://github.com/ModOrganizer2/modorganizer/releases", ver="2.5.2",
                 tag="core", note="Портативный инстанс в отдельной папке. Профиль с локальными INI — так настройки VR не смешаются с другими сборками."),
            dict(name="Root Builder", id=31720, ver="5.1.x", tag="core",
                 note="Кладёт в корень игры загрузчик SKSEVR, Part 2 от Engine Fixes VR и DLL OpenComposite, не трогая папку Steam."),
            dict(name="SSEEdit (xEdit)", id=164, ver="4.1.5+", tag="core",
                 note="Режим VR: аргумент -tes5vr. Чистка мастеров, просмотр конфликтов, ручные патчи."),
            dict(name="LOOT", url="https://loot.github.io/", tag="core",
                 note="Сортировка плагинов, Skyrim VR поддерживается. После сортировки — ручная проверка конфликтов в xEdit."),
            dict(name="BethINI Pie + Skyrim VR Plugin for Bethini Pie", url="https://www.nexusmods.com/site/mods/631", extra=[("VR-плагин", nx(177465))],
                 tag="core", note="INI под VR. Плагин VR ещё и требование Skyrim VR Fixes for Latest USSEP."),
            dict(name="Pandora Behaviour Engine+", id=133232, ver="4.x / 5.0 beta", tag="rec",
                 note="Сборка поведений для OAR и анимаций. Поддержку Skyrim VR вернули в 4.1.2-beta. Если какой-то мод не собирается — запасной вариант Nemesis."),
            dict(name="Synthesis", url="https://github.com/Mutagen-Modding/Synthesis/releases", tag="rec",
                 note="Патчеры в финале сборки. Запускается после всех модов, перед генерацией LOD."),
            dict(name="fpsVR или SteamVR Frame Timing", url="https://store.steampowered.com/app/908520/fpsVR/", tag="rec",
                 note="Без замеров время кадра не настроить. Смотрите на CPU и GPU frametime, а не на загрузку видеокарты."),
        ],
    },
    {
        "id": "base",
        "title": "База игры: мастера и USSEP",
        "lead": "Выберите один путь. Путь A даёт совместимость с модами, рассчитанными на свежий USSEP и записи SSE 1.6, но требует купленную Skyrim SE/AE.",
        "items": [
            dict(name="Путь A. Обновлённые мастера SSE 1.6.1170 + 4 бесплатных CC", url="https://www.nexusmods.com/skyrimspecialedition/articles/6529",
                 extra=[("гайд по мастерам", "https://www.nexusmods.com/skyrimspecialedition/articles/6642")], tag="alt",
                 note="По гайду infernalryan (обновлён 23.07.2026): Skyrim.esm, Update.esm, DLC и CC Survival Mode, Saints & Seducers, Rare Curios, Fishing из SE/AE переносятся в VR отдельным модом."),
            dict(name="USSEP (последний, 4.3.x)", id=266, tag="alt", group="A",
                 note="Только для пути A. Предупреждение на странице о версии SSE 1.6.1130+ закрывают подготовленные по гайду файлы."),
            dict(name="Skyrim VR Strings Fix for Updated SSE Master Files", id=176040, ver="2.0", tag="alt", group="A",
                 note="Без него пропадает текст, а отмычки могут не подниматься. Проверьте, что в архиве есть строки для языка, на котором вы играете."),
            dict(name="Survival Mode Prompt Removed (Disable Permanently)", id=59049, tag="alt", group="A",
                 note="Плагин Survival Mode остаётся включённым (его требует свежий USSEP), но режим выживания не предлагается."),
            dict(name="Skyrim VR Survival Text Removed", id=177398, tag="alt", group="A",
                 note="Убирает «SURV=…» из карточек предметов."),
            dict(name="Skyrim VR Fixes for Latest USSEP", id=177650, tag="opt", group="A",
                 note="Ставить, если видите белые деревья в Playroom или в мире. ESL-мастер сразу после USSEP. С шейдерами семейства CS обычно не нужен — шаг убран из гайда."),
            dict(name="Путь B. USSEP 4.2.5b + Skyrim VR USSEP patch for 4.2.5b", id=91475, tag="alt",
                 note="Если SE/AE нет. USSEP 4.2.5b берётся из старых файлов страницы 266. Так собран Stormcrown VR (сентябрь 2026). Моды, требующие свежий USSEP, проверять вручную."),
            dict(name="Чистка мастеров в SSEEdit", url="https://www.nexusmods.com/skyrimspecialedition/mods/113681", tag="rec",
                 note="Quick Auto Clean для Update, Dawnguard, HearthFires, Dragonborn. DynDOLOD потом не ругается на удалённые большие референсы."),
        ],
    },
    {
        "id": "frameworks",
        "title": "SKSEVR, библиотеки и фреймворки",
        "lead": "Правило VR: у многих SKSE-модов отдельная VR-страница или VR-файл. Если у мода две страницы (основной и VR), ставится основной, а поверх — DLL с VR-страницы.",
        "items": [
            dict(name="SKSEVR", id=30457, ver="2.0.12", tag="core",
                 note="Загрузчик и DLL — в корень через Root Builder, скрипты — как обычный мод. Игра запускается только через sksevr_loader.exe."),
            dict(name="VR Address Library for SKSEVR", id=58101, ver="0.27x, окт. 2026", tag="core",
                 note="Обновлять вместе с каждым SKSE-плагином: новые версии плагинов просят новые адреса."),
            dict(name="Engine Fixes VR", id=62089, ver="7.10", tag="core",
                 note="Part 1 — мод, Part 2 — в корень. В EngineFixes.toml поставить MaxStdio = 8192: это требование Skyrim VR ESL Support. Старый отдельный ObjectLOD/Shadow Map fix не ставить — он уже внутри с 7.4.9."),
            dict(name="Skyrim VR ESL Support", id=106712, ver="1.3.2", tag="core",
                 note="ESL и ESPFE в VR, включая расширенный диапазон 1.6.1130. Работает только с официальным SKSEVR 2.0.12. Должен стоять до запуска DynDOLOD."),
            dict(name="Crash Logger SSE AE VR", id=59818, tag="core", note="Логи вылетов. Без него конфликт в 300 модах не найти."),
            dict(name="Skyrim VR Tools", id=27782, tag="core", note="Основа для многих VR-модов: VR Climbing, Spellsiphon и других."),
            dict(name="PapyrusUtil VR", id=13048, file="VR", tag="core", note="Файл с пометкой VR."),
            dict(name="JContainers VR", id=16495, file="VR", ver="4.3.x", tag="core", note="Файл с пометкой VR."),
            dict(name="powerofthree's Papyrus Extender + Papyrus Extender VR", id=22854, extra=[("VR-DLL", nx(58296))], tag="core",
                 note="Сначала основной мод, поверх DLL со страницы VR."),
            dict(name="powerofthree's Tweaks + po3 Tweaks VR", id=51073, extra=[("VR-DLL", nx(59510))], tag="core",
                 note="INI из основного мода, DLL из VR-версии."),
            dict(name="Spell Perk Item Distributor VR", id=59121, ver="7.3", tag="core"),
            dict(name="Keyword Item Distributor", id=55728, file="VR", ver="4.1", tag="core"),
            dict(name="Base Object Swapper VR", id=61734, tag="core"),
            dict(name="SkyPatcher", id=106659, file="VR", tag="core"),
            dict(name="MCM Helper", id=53000, tag="core"),
            dict(name="SkyUI VR", id=91535, tag="core", note="Меню настроек модов (MCM) в VR."),
            dict(name="Container Distribution Framework + VR", id=120152, extra=[("VR-DLL", nx(139051))], tag="rec"),
            dict(name="FormList Manipulator", id=74037, tag="rec"),
            dict(name="Description Framework", id=105799, tag="rec"),
            dict(name="Inventory Interface Information Injector", id=85702, file="VR", tag="rec"),
            dict(name="Sound Record Distributor", id=77815, tag="rec", note="Нужен звуковым модам из раздела «Звук»."),
            dict(name="ConsoleUtilVR", id=47189, tag="rec"),
            dict(name="SKSE Menu Framework + ImGui VR Helper", id=120352, extra=[("ImGui VR Helper", nx(183466))], tag="rec",
                 note="Меню Open Shaders и других ImGui-модов прямо в шлеме, без снятия гарнитуры."),
            dict(name="MFG Fix NG", id=133568, tag="rec", note="Мимика и липсинк. Требование SkyrimNet."),
            dict(name="Skyrim VR Refocused", id=32737, tag="rec",
                 note="Возвращает фокус окну игры. Нужен модам, которые эмулируют нажатия. Ищет окно с заголовком «Skyrim VR»."),
        ],
    },
    {
        "id": "fixes",
        "title": "Движок, стабильность, производительность",
        "lead": "VR чаще упирается в процессор, чем в видеокарту. Всё, что снимает нагрузку со скриптов и отрисовки объектов, окупается в каждом кадре.",
        "items": [
            dict(name="Poached Bugs VR", id=107053, tag="core",
                 note="Порт фиксов Scrambled Bugs (сам Scrambled Bugs в VR не работает). Файл Simonrim Choice Config — если ставите моды SimonRim."),
            dict(name="Papyrus Tweaks NG", id=77779, tag="core"),
            dict(name="Skyrim freeze fix NG", id=160704, tag="rec"),
            dict(name="Disabled Reference Integrity Fix (VR)", id=175062, file="VR", tag="rec"),
            dict(name="Block Condition Freeze CTD Fix", id=193168, tag="rec", note="Свежий, сентябрь 2026."),
            dict(name="NPC AI Process Position Fix NG", id=69326, tag="rec"),
            dict(name="Animated Static Reload Fix NG", id=69331, tag="rec"),
            dict(name="Stagger Effect Fix", id=110508, tag="rec"),
            dict(name="Animation Queue Fix", id=82395, tag="rec"),
            dict(name="Seamless Saving VR", id=174106, tag="rec", note="Ускоряет сохранение — меньше подвисаний на автосейвах."),
            dict(name="Faster Decompression", id=174643, tag="rec"),
            dict(name="Disk Cache Enabler", id=100975, tag="rec"),
            dict(name="PrivateProfileRedirector", id=18860, file="VR 0.6.2", tag="rec", note="Быстрее старт игры."),
            dict(name="Skyrim Priority SE AE VR", id=50129, tag="rec"),
            dict(name="SCROTE — Simply Optimized Scripts", id=97155, tag="rec"),
            dict(name="eFPS — Exterior FPS boost + Patch Hub", id=54907, extra=[("Patch Hub", nx(54998))], tag="rec",
                 note="Плоскости окклюзии в экстерьерах — меньше объектов в кадре, прямая экономия CPU."),
            dict(name="Lightened Skyrim — BOS edition", id=111475, tag="rec", note="В тестах FUS давал 1–2 мс на кадр."),
            dict(name="Inertia (Floating Gear Fix)", id=148746, tag="rec"),
            dict(name="Assorted Mesh Fixes", id=32117, tag="rec"),
            dict(name="Unofficial Material Fix", id=21027, tag="rec"),
            dict(name="Skyrim Landscape and Water Fixes", id=26138, tag="rec"),
            dict(name="Navigator — Navmesh Fixes", id=52641, tag="rec"),
            dict(name="Increase Actor Limit for VR", id=37440, tag="opt"),
        ],
    },
    {
        "id": "vr",
        "title": "VR-ядро: тело, руки, физика",
        "lead": "VRIK, HIGGS и PLANCK — фундамент. Новые моды 2026 года от Asterrath (Physical Collision, True Wield и другие) построены поверх них и ставятся набором.",
        "items": [
            dict(name="VRIK Player Avatar", id=23416, ver="0.8.7", tag="core", note="Тело игрока, холстеры, жесты."),
            dict(name="HIGGS — Enhanced VR Interaction", id=43930, ver="1.10.10", tag="core", note="Коллизии рук, хват двумя руками, гравиперчатки."),
            dict(name="PLANCK", id=66025, ver="0.8.1", tag="core", note="Физические удары и реакции NPC. Требует HIGGS 1.6.0+ и SKSEVR 2.0.12."),
            dict(name="Physical Collision VR", id=186335, ver="5.2", tag="rec",
                 note="Руки и оружие упираются в стены, столы и щит. Требует HIGGS, PLANCK, VRIK. Не совмещать с другими модами коллизии оружия вроде Pseudo Physical Weapon Collision and Parry — они делают одно и то же."),
            dict(name="True Wield VR", id=191123, tag="rec", note="Масса оружия и хват в любой точке рукояти. Требует Physical Collision VR, MCM Helper, SkyUI VR."),
            dict(name="Immersive Weapon Penetration VR", id=184223, tag="rec", note="Колющий удар входит в тело и застревает. Требует HIGGS, PLANCK, VRIK."),
            dict(name="Swap Drop and Hold Redux — VR", id=185816, tag="rec", note="Смена, бросание и удержание предметов в руке."),
            dict(name="Spell Wheel VR", id=47630, ver="1.5.11", tag="core", note="Выбор заклинаний и предметов жестом, без меню."),
            dict(name="Weapon Throw VR", id=31374, ver="1.4", tag="rec"),
            dict(name="Interactive Activators VR", id=161676, tag="rec", note="Физические рычаги, цепи и кнопки. Заменил Interactive Pullchains VR."),
            dict(name="Instant Equip VR", id=44571, tag="rec"),
            dict(name="Dialogue Movement Enabler VR", id=59816, tag="rec"),
            dict(name="Stop Trigger Unsheathing For VR", id=55962, tag="rec"),
            dict(name="Dual Casting Fix VR", id=92804, tag="rec"),
            dict(name="Haptic Skyrim VR", id=20364, tag="rec", note="Отдача в контроллеры от лука, магии и ударов."),
            dict(name="Seamless Arrow Nocking VR + Immersive Crossbow Reload VR", id=117254, extra=[("Crossbow Reload", nx(139152))], tag="rec"),
            dict(name="Magic Improvements for Skyrim VR", id=55751, tag="rec"),
            dict(name="Lethal Unarmed VR", id=191124, tag="opt", note="Захваты: схватить за руку, бросить, придушить."),
            dict(name="VR Climbing", id=168553, tag="opt", note="Лазание руками. Требует HIGGS и Skyrim VR Tools. На странице стоит метка AI-generated."),
            dict(name="Spellsiphon", id=26627, tag="opt", note="Жестовая магия."),
            dict(name="To Your Face", id=24720, file="VR", tag="opt"),
            dict(name="Sprint Jump VR", id=28354, tag="opt"),
        ],
    },
    {
        "id": "ui",
        "title": "Интерфейс",
        "lead": "SkyUI VR и MCM Helper уже стоят в разделе фреймворков.",
        "items": [
            dict(name="moreHUD VR", id=33215, tag="rec"),
            dict(name="QuickLoot IE", id=120075, tag="rec", note="Быстрый лут. Работает в VR — стоит в Yggdrasil VR и Stormcrown VR."),
            dict(name="VR Console Selection Fix", id=140752, tag="rec"),
            dict(name="No Menu Fade Out VR", id=185197, tag="opt"),
            dict(name="Norden UI — VR Edition", id=169537, tag="opt", note="Тема интерфейса."),
        ],
    },
    {
        "id": "gfx",
        "title": "Графика: шейдеры и свет",
        "lead": "Официальный Community Shaders с версии 1.7 убрал поддержку VR. Для VR в 2026 году — форки. Ставится один, не два.",
        "items": [
            dict(name="Open Shaders", id=180419, ver="2.17.0", tag="core",
                 note="Форк Community Shaders от alandtse, всё в одном архиве: DLSS/DLAA/FSR для VR, фовеальный рендеринг, Skylighting, Light Limit Fix, Grass Lighting, Dynamic Cubemaps, тени облаков и рельефа, Wetness. Ставится вместо CS: те же файлы и папка настроек. Так собран Yggdrasil VR."),
            dict(name="Community Shaders Expanded (CSX), VR-сборка", id=166950, ver="3.19.x-VR", tag="alt",
                 note="Альтернатива Open Shaders: вернул Particle Lights и Screen Space Shadows в VR, упор на стабильность. Так собраны Stormcrown VR и MGO 4.0."),
            dict(name="Light Placer + Light Placer VR", id=127557, extra=[("VR-DLL", nx(135822))], tag="core",
                 note="Огни на мешах и эффектах через JSON. ENB Light в CS 1.4+ не работает, его заменяет Light Placer. Основной мод — конфиги, VR-страница — DLL."),
            dict(name="CS Light", id=138443, tag="rec",
                 note="Конфиги Light Placer для свечей, факелов, эффектов. Не включайте одновременно опции «ENB lights for effect shaders» и «Magic FX lights» — свет удвоится."),
        ],
    },
    {
        "id": "world",
        "title": "Освещение, погода, вода",
        "lead": "Lux ставится без разделённых мешей: с Light Limit Fix они не нужны и добавляют draw calls, а в VR сцена рисуется для двух глаз.",
        "items": [
            dict(name="Lux + Lux Patch Hub", id=43158, extra=[("Patch Hub", nx(113002))], tag="core",
                 note="В установщике не выбирайте split meshes. Меши с префиксом Lux_ оставьте — они заменяют модели, а не режут их."),
            dict(name="Lux Via + Patch Hub", id=63588, extra=[("Patch Hub", nx(116722))], tag="rec", note="Свет на дорогах и мостах."),
            dict(name="Lux Orbis + Patch Hub", id=56095, extra=[("Patch Hub", nx(114169))], tag="opt",
                 note="Больше уличных огней. Красиво, но дороже — включать при запасе по времени кадра."),
            dict(name="Azurite Weathers III + MCM + Azurite III HDR", id=42731, extra=[("MCM", nx(139858)), ("HDR", nx(138991))], tag="core",
                 note="FUS перешёл на III как на более оптимизированную для VR, особенно небо. Volumetric Mists к ней не ставят."),
            dict(name="Splashes of Storms + VR", id=72115, extra=[("VR-DLL", nx(73111))], tag="rec"),
            dict(name="Splashes of Skyrim + VR", id=47710, extra=[("VR-DLL", nx(58104))], tag="rec"),
            dict(name="Dynamic Wind Framework + Dynamic Wind — Skyrim", id=177023, extra=[("Dynamic Wind — Skyrim", nx(177024))], tag="rec",
                 note="Ветер для растительности, 2026 год, есть в Stormcrown VR."),
            dict(name="Simplicity of Sea", id=56520, tag="rec", note="Вода под шейдерные эффекты воды. Стоит в Stormcrown VR и MGO 4.0. Ставится один водный мод."),
            dict(name="Water for ENB", id=37061, tag="alt", note="Альтернатива Simplicity of Sea, вариант Tempus VR."),
            dict(name="Map Weather — CS", id=170955, tag="opt"),
        ],
    },
    {
        "id": "land",
        "title": "Трава, деревья, ландшафт",
        "lead": "Это модели, а не текстуры, и они сильнее всего бьют по FPS вне городов. Выбираем сейчас, текстурные варианты — на этапе текстур.",
        "items": [
            dict(name="No Grass In Objects NG", id=42161, ver="1.6.14", tag="core",
                 note="Прекэш травы: большой выигрыш в VR и основа для Grass LOD в DynDOLOD. После смены травы или iMinGrassSize кэш генерируется заново."),
            dict(name="Grass Cache Helper NG", id=101095, tag="core"),
            dict(name="Landscape Fixes For Grass Mods", id=9005, tag="core"),
            dict(name="Merethic Grasslands", id=164058, tag="rec", note="Трава в ванильном стиле. Выбрана в Stormcrown VR, где упор на производительность."),
            dict(name="Cathedral 3D Grass Library + 3D-растения", id=80687, tag="alt", note="Плотнее и красивее, но тяжелее."),
            dict(name="Happy Little Trees + DynDOLOD 3 Add-On", id=50961, extra=[("LOD add-on", nx(56907))], tag="rec",
                 note="Лёгкие деревья с хорошими LOD."),
            dict(name="Seasons of Skyrim", url="https://www.nexusmods.com/skyrimspecialedition/search/?gsearch=Seasons%20of%20Skyrim", tag="opt",
                 note="Работает в VR (есть в MGO), но кэш травы и LOD придётся генерировать на каждый сезон."),
        ],
    },
    {
        "id": "anim",
        "title": "Анимации и физика",
        "lead": "В VR анимации игрока заменяет VRIK, поэтому смысл имеют анимации NPC и физика.",
        "items": [
            dict(name="Open Animation Replacer", id=92109, ver="3.2.1", tag="core", note="Официально поддерживает SE, AE и VR."),
            dict(name="Paired Animation Improvements", id=99621, tag="rec"),
            dict(name="Mu Joint Fix (DLL)", id=61479, tag="rec"),
            dict(name="FSMP — Faster HDT-SMP", id=57339, tag="opt", note="Только если будут SMP-волосы или одежда. Проверьте VR-вариант в установщике."),
            dict(name="Dynamic Armor Physics", id=186346, tag="opt", note="2026 год, есть в Stormcrown VR."),
        ],
    },
    {
        "id": "combat",
        "title": "Бой и геймплей",
        "lead": "Минимальная VR-дружелюбная база. Полный набор SimonRim (Mysticism, Apothecary, Thaumaturgy и т. д.) — по вкусу, с Poached Bugs VR.",
        "items": [
            dict(name="Blade and Blunt + Blade and Blunt VR", id=34549, extra=[("VR", nx(120494))], tag="rec"),
            dict(name="Adamant + Adamant — VR Tweaks", id=30191, extra=[("VR Tweaks", nx(190589))], tag="rec"),
            dict(name="Accuracy — Localized Combat Damage", id=187578, tag="opt", note="Урон по зонам попадания, 2026 год."),
            dict(name="Core Impact Framework", id=146873, tag="opt"),
            dict(name="Ricochet — Arrow Physics Framework", id=160603, tag="opt"),
            dict(name="Dismembering Framework", id=126203, tag="opt"),
            dict(name="NPCs Take Cover", id=111890, tag="opt"),
            dict(name="Enemy Friendly Fire", id=50483, file="VR", tag="opt"),
        ],
    },
    {
        "id": "audio",
        "title": "Звук",
        "lead": "В шлеме звук определяет ощущение пространства не меньше картинки.",
        "items": [
            dict(name="Audio Overhaul for Skyrim", id=12466, tag="rec"),
            dict(name="Regional Sounds Expansion + Reverb Interior Sounds Expansion", id=77829, extra=[("Reverb Interior", nx(77947))], tag="rec"),
            dict(name="Acoustic Space Improvement Fixes", id=78992, tag="rec"),
            dict(name="Immersive Sounds Compendium + AOS–ISC patch", id=523, extra=[("патч", nx(36761))], tag="alt"),
            dict(name="True 3D Sound for Headphones", id=1897, tag="rec", note="HRTF-позиционирование для наушников гарнитуры."),
        ],
    },
    {
        "id": "ai",
        "title": "ИИ-NPC",
        "lead": "Та самая «next-gen» часть роликов. Ставится один из трёх — они конфликтуют по смыслу.",
        "items": [
            dict(name="SkyrimNet", url="https://github.com/MinLL/SkyrimNet-GamePlugin/releases", ver="Beta26, 03.10.2026", tag="opt",
                 note="Развивается активнее всех, VR-фиксы почти в каждой бете. Для VR требует Skyrim VR ESL Support, Refocused, MFG Fix NG, po3 Tweaks SE и VR. Модели через OpenRouter, часть платная."),
            dict(name="Mantella", id=98631, ver="0.14", tag="opt",
                 note="Проще в настройке, бесплатная модель по умолчанию, голос Piper или XTTS. Замечены вылеты вместе с Fuz Ro D-oh."),
            dict(name="CHIM", id=126330, tag="opt", note="Больше всего возможностей, ставится сложнее всех."),
        ],
    },
    {
        "id": "perf",
        "title": "VR-рантайм",
        "lead": "Сначала Open Shaders с апскейлом и фовеальным рендерингом, потом OpenComposite, потом всё остальное.",
        "items": [
            dict(name="OpenComposite Unleashed for Skyrim VR", id=171182, ver="5.0", tag="rec",
                 note="OpenXR в обход SteamVR. FUS сообщал о приросте до ~30%. В этой сборке работает виртуальная клавиатура. Оверлеи SteamVR пропадают. DLL — в корень через Root Builder."),
            dict(name="VR FPS Stabilizer", id=31392, ver="1.4.12", tag="opt", note="Снижает настройки на лету при просадках."),
        ],
    },
]

DONT = [
    ("Community Shaders 1.7 и новее", "Официальный CS убрал поддержку VR. Нужен Open Shaders или CSX."),
    ("Два шейдерных пакета сразу", "Open Shaders, CSX и CS используют одни и те же файлы. Только один."),
    ("ENB", "Несовместим с семейством CS и слишком дорог для VR."),
    ("SSE Engine Fixes, Address Library for SKSE, SKSE64", "Это версии для SE/AE. В VR — Engine Fixes VR, VR Address Library, SKSEVR."),
    ("Backported Extended ESL Support", "Без VR-поддержки. Вместо него Skyrim VR ESL Support."),
    ("Scrambled Bugs", "В VR не работает. Вместо него Poached Bugs VR."),
    ("SSE Display Tweaks", "Нет VR-сборки, частоту кадров в VR задаёт шлем."),
    ("Precision, True Directional Movement, SkyParkour, SkyClimb", "Только для плоского режима. В VR их роль играют PLANCK, Physical Collision VR, VR Climbing."),
    ("Skyrim Upscaler VR (PureDark) или vrperfkit вместе с апскейлом Open Shaders", "Два апскейлера дерутся за один кадр. Апскейл — только встроенный."),
    ("ENB Light и Particle Lights for ENB", "Не работают с CS 1.4+ и Open Shaders. Свет — через Light Placer. Исключение — CSX."),
    ("Volumetric Mists с Azurite III", "FUS убрал его ради производительности, автор погоды больше не рекомендует."),
    ("Разделённые меши Lux", "С Light Limit Fix не нужны, только добавляют draw calls."),
    ("Две сборки OpenComposite", "Старый OpenComposite Fixes Custom Build или Unleashed — что-то одно."),
    ("Fuz Ro D-oh VR без необходимости", "Принудительно включает субтитры. Ставить, только если его требует другой мод."),
]

GEN_STEPS = [
    ("Установлены все моды, включая текстуры. LOOT, ручная проверка конфликтов в xEdit.", None),
    ("ParallaxGen (PGPatcher) — если ставили PBR или parallax-текстуры.", nx(120946)),
    ("Synthesis-патчеры.", None),
    ("Прекэш травы через NGIO, папку Grass из Overwrite — в отдельный мод.", None),
    ("xLODGen: LOD рельефа с SSE Terrain Tamriel.", nx(54680)),
    ("TexGen, затем DynDOLOD 3 с Resources SE 3 и DynDOLOD DLL NG. Руководство — DynDOLOD_Manual_TES5VR в архиве.", nx(68518)),
    ("Тестовый прогон: Вайтран, Рифтен, лес у Ривервуда. Время кадра, лог Crash Logger.", None),
]

MO2_ORDER = [
    "Инструменты и корень (SKSEVR, Engine Fixes VR Part 2, OpenComposite — через Root Builder)",
    "Мастера и USSEP",
    "Фреймворки и библиотеки",
    "Фиксы движка и производительность",
    "Open Shaders, Light Placer",
    "VR-ядро",
    "Интерфейс",
    "Звук",
    "Свет, погода, вода",
    "Трава, деревья, ландшафт",
    "Анимации и физика",
    "Бой и геймплей",
    "ИИ-NPC",
    "Текстуры — на финальном этапе",
    "Патчи (Lux Patch Hub и т. п.) — ниже модов, которые они патчат",
    "Сгенерированное: ParallaxGen, Synthesis, Grass Cache, xLODGen, TexGen, DynDOLOD — в самом низу",
]

SOURCES = [
    ("Skyrim Modding Guides SSE/AE/VR — infernalryan", nx(113681)),
    ("Skyrim Initial Setup (VR) — infernalryan", "https://www.nexusmods.com/skyrimspecialedition/articles/6529"),
    ("Community Shaders: снятие поддержки VR", "https://www.nexusmods.com/skyrimspecialedition/articles/12159"),
    ("Open Shaders — релизы", "https://github.com/alandtse/open-shaders/releases"),
    ("Community Shaders Expanded (CSX) — GitHub", "https://github.com/ParticleTroned/skyrim-community-shaders"),
    ("Wabbajack: отчёты по спискам (Yggdrasil VR, Stormcrown VR, FUS)", "https://github.com/wabbajack-tools/mod-lists/tree/master/reports"),
    ("FUS — релизы и вики", "https://github.com/Kvitekvist/FUS/releases"),
    ("Pandora Behaviour Engine+ — релизы", "https://github.com/Monitor221hz/Pandora-Behaviour-Engine-Plus/releases"),
    ("SkyrimNet — релизы", "https://github.com/MinLL/SkyrimNet-GamePlugin/releases"),
    ("Mantella — релизы", "https://github.com/art-from-the-machine/Mantella/releases"),
    ("Smooth Terrain — исходники (VR в CMake)", "https://github.com/hakasapl/SmoothTerrain"),
    ("Save Unbaker и Simple Offence Suppression — README с VR-ссылками", "https://github.com/powerof3"),
    ("Отчёт Panda's Sovngarde (VR)", "https://github.com/wabbajack-tools/mod-lists/blob/master/reports/VirtualPanda/PandasSovngarde/status.md"),
    ("Отчёт Tahrovin — Grit (VR)", "https://github.com/wabbajack-tools/mod-lists/blob/master/reports/TahrovinGrit/tahrovingrit/status.md"),
    ("Отчёт NGVO (плоская next-gen сборка)", "https://github.com/wabbajack-tools/mod-lists/blob/master/reports/GhoulifiedReality/NGVO/status.md"),
]

TAGS = {"core": "обязательно", "rec": "рекомендую", "opt": "по желанию", "alt": "выбор", "try": "проверить"}

AFTER = {
    "gfx": """<div class="panel"><h3>Open Shaders под VR: с чего начать</h3><ul>
<li>Апскейл: DLAA при запасе по GPU, иначе DLSS Quality или Balanced; на AMD — FSR. Генерацию кадров в VR не включайте — для этого есть ASW, SSW или Motion Smoothing шлема.</li>
<li>Фовеальный рендеринг: включить, начать с умеренного пресета.</li>
<li>Сразу: Grass Lighting, Dynamic Cubemaps, Cloud Shadows, Skylighting.</li>
<li>По одному, с замером: Wetness Effects (≈0,5–1,5 мс), Screen Space GI/AO (≈0,5–0,8 мс), Screen Space Shadows (≈0,4 мс), Terrain Blending (≈0,3 мс).</li>
<li>Как и CS 1.4+, требует Engine Fixes VR и Crash Logger.</li>
</ul><p>Миллисекунды — замеры автора VR-форка из гайда MGO, на вашем железе будут другими. Мерить в экстерьере Вайтрана и в лесу у Ривервуда.</p></div>""",
    "perf": """<div class="panel"><h3>INI и шлем</h3><ul>
<li>SteamVR: разрешение рендера 100% глобально и для игры. Суперсэмплинг поверх апскейла только съедает кадры.</li>
<li>BethINI Pie с VR-плагином: пресет Medium или High, дальше точечно.</li>
<li>iMinGrassSize: чем больше значение, тем меньше травы. После изменения прекэш NGIO генерируется заново.</li>
<li>fMinOccludeeBoxExtent: FUS держит 60 — около 5% быстрее, но ночью изредка мерцают дальние окна; 600 убирает мерцание LOD-огней.</li>
<li>Если кадр не укладывается в бюджет: снизить частоту шлема (90 → 72 Гц) или зафиксировать половинную частоту с ASW/SSW.</li>
</ul></div>""",
}


def esc(s):
    return html.escape(s, quote=True)


def item_html(sec_id, it, idx):
    url = it.get("url") or nx(it["id"])
    key = f"{sec_id}-{it.get('id', idx)}"
    meta = []
    if it.get("id"):
        meta.append(f'<span class="mid">#{it["id"]}</span>')
    if it.get("ver"):
        meta.append(f'<span class="ver">{esc(it["ver"])}</span>')
    if it.get("file"):
        meta.append(f'<span class="file">файл: {esc(it["file"])}</span>')
    extra = "".join(f' <a class="xl" href="{esc(u)}" target="_blank" rel="noopener">{esc(t)}</a>' for t, u in it.get("extra", []))
    note = f'<p class="note">{esc(it["note"])}</p>' if it.get("note") else ""
    tag = it["tag"]
    newattr = ' data-new="1"' if it.get("new") else ""
    badge = '<span class="nb">новое</span>' if it.get("new") else ""
    return (
        f'<li class="mod" data-tag="{tag}"{newattr} data-key="{esc(key)}">'
        f'<input type="checkbox" id="c-{esc(key)}" aria-label="Отметить: {esc(it["name"])}">'
        f'<div class="body"><div class="head">'
        f'<label for="c-{esc(key)}" class="nm"><a href="{esc(url)}" target="_blank" rel="noopener">{esc(it["name"])}</a></label>{badge}{extra}'
        f'<span class="tag t-{tag}">{TAGS[tag]}</span></div>'
        f'<div class="meta">{"".join(meta)}</div>{note}</div></li>'
    )


def merge():
    import sys as _s, os as _o; _s.path.insert(0, _o.path.dirname(_o.path.abspath(__file__))); import additions as A
    global DONT
    for s in SECTIONS:
        for i, it in enumerate(s["items"]):
            if it.get("id") in A.REPLACE:
                s["items"][i] = A.REPLACE[it["id"]]
            elif it.get("id") in A.PATCH_NOTES:
                it["note"] = it.get("note", "") + A.PATCH_NOTES[it["id"]]
        s["items"].extend(A.ADD.get(s["id"], []))
    for after, sec in A.NEW_SECTIONS:
        idx = next(i for i, s in enumerate(SECTIONS) if s["id"] == after)
        SECTIONS.insert(idx + 1, sec)
    DONT = [A.DONT_REPLACE.get(a, (a, b)) for a, b in DONT] + A.DONT_ADD


def build():
    merge()
    total = sum(len(s["items"]) for s in SECTIONS)
    nav = "".join(f'<a href="#{s["id"]}">{esc(s["title"])}</a>' for s in SECTIONS)
    secs = []
    for s in SECTIONS:
        items = "".join(item_html(s["id"], it, i) for i, it in enumerate(s["items"]))
        secs.append(
            f'<section id="{s["id"]}" class="sec"><h2>{esc(s["title"])} <span class="cnt" data-sec="{s["id"]}"></span></h2>'
            f'<p class="lead">{esc(s["lead"])}</p><ul class="mods">{items}</ul>{AFTER.get(s["id"], "")}</section>'
        )
    dont = "".join(f'<li><strong>{esc(a)}</strong><span>{esc(b)}</span></li>' for a, b in DONT)
    gen = "".join(
        f'<li>{esc(t)}' + (f' <a href="{esc(u)}" target="_blank" rel="noopener">страница</a>' if u else "") + "</li>"
        for t, u in GEN_STEPS
    )
    mo2 = "".join(f"<li>{esc(x)}</li>" for x in MO2_ORDER)
    src = "".join(f'<li><a href="{esc(u)}" target="_blank" rel="noopener">{esc(t)}</a></li>' for t, u in SOURCES)
    return TEMPLATE.replace("{{NAV}}", nav).replace("{{SECTIONS}}", "".join(secs)).replace("{{DONT}}", dont) \
        .replace("{{GEN}}", gen).replace("{{MO2}}", mo2).replace("{{SRC}}", src).replace("{{TOTAL}}", str(total))


TEMPLATE = open(__file__.replace("build_page.py", "template.html"), encoding="utf-8").read()

if __name__ == "__main__":
    import sys
    open(sys.argv[1], "w", encoding="utf-8").write(build())
    print("ok", sum(len(s["items"]) for s in SECTIONS), "items", sum(1 for s in SECTIONS for it in s["items"] if it.get("new")), "new")
