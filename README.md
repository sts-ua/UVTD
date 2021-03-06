# Словник відеоігрової термінології

Наразі проектом займаються:
Demetrios (теоретичне планування, наукова сторона, контакт із Valve та КНУ ім. Т.Шевченка)
sergiy.bogdancev (можливо візьме участь як програміст)
SHooZ (можливо візьме участь як програміст)

Потрібні інші програмісти, щоби розподілити задачі на невеличкі частини. Після реалізації пункту 1 будуть потрібні редактори, які готуватимуть попередні версії словникових статей. Після підготовки попередніх версій знайдемо вчених-лексикографів для перевірки.

## Основні засади

1. Орієнтація на створення науково вивіреного ресурсу, а не чергова самодіяльність (тобто необхідність супервізії від мовознавчої наукової інституції чи хоча б окремих спеціалістів-науковців)

2. Словник створюється на базі корпусу двомовних текстів, з яких автоматично виокремлюються найчастіші слова і вислови (тобто першочергові задачі — технічні), а потім вручну чи напівавтоматично редагується

3. Словник може розташовуватися як на localization.com.ua (наприклад, на dic.localization.com.ua), так і на сайті наукової інституції, з якою ми співпрацюватимемо (наприклад, на mova.info), або ж навіть на сервері перекладів Valve, якщо їм сподобається ідея (через це відпочатку треба відштовхуватися від Source-формату текстів)

## Roadmap

1. - [ ] Створення частотного словника слів та виразів

    1. - [ ] Створення скрипта, який автоматично переводитиме Source-тексти у зручну для подальшої роботи базу даних, де:

        * - [ ] зберігатиметься токен і його переклад, ідентифікатор токена, назва файла, дата додавання

        * - [ ] буде можливість легкої зворотної конвертації у Source-формат (знадобиться для подальшої роботи, а також у випадку інтеграції з STS)

        * - [ ] буде можливість оновлення змінених/доданих токенів (непріоритетно)

        * - [ ] буде можливість працювати з іншими форматами (щоби залучати двомовні тексти локалізацій ігор з-поза STS) (непріоритетно)

    1. - [ ] Створення скрипта, який зможе проаналізувати масив доданих двомовних текстів (усі файли з STS) і створити два частотні словники: слів (словоформ) та виразів, де до кожної словоформи буде прив’язана інформація про випадки її вживання.      Інтерфейс має виглядати приблизно так:

           слово1 - 456 вживань

           слово2 - 350 вживань

           слово3 - 300 вживань

           Де при натисканні на кількість вживань можна проглядати всі вживання у форматі:

           слово1 (англ.) - id вживання - токен АБО речення (тобто з довгих токенів брати тільки речення від крапки/початку рядка до крапки/кінця рядка, але не менше ніж 5 слів до і 5 слів після) - переклад токена АБО абзац (ідеально з довгих токенів брати лише потрібний абзац перекладу, але якщо це складно, то можна весь токен) - id токена з посиланням на токен на СТС - назва файлу - назва гри/програми/сайту (наприклад, Dota 2, Клієнт Steam, Steamworks, Steam Community тощо)

           Тобто треба буде ще окрему табличку, де файли будуть прив’язані до певних програм чи сайтів.

           Аналогічно треба буде зробити для словосполучень: від двох слів до речення, враховуючи лише ті, де буде 2 і більше вживань. Може бути, що кількість вийде занадто велика, тоді треба обдумати як це оптимізувати. Словосполучення можуть бути двох типів: сталий вираз чи ідіома, стандартний часто повторюваний текст (речення)

1. - [ ] Створення власне глосарію

    1. - [ ] Створення інтерфейсу редагування автоматично створеного частотного словника

        Додавання можливості на основі вище описаного інтерфейсу перегляду створювати словникові записи.

        Тобто редактор бачить слововживання і:

        1. Позначає чи це слово у первісній формі чи в похідній (word/words), похідну форму прив’язує до основної

        1. Позначає чи це слово має стосунок до відеоігрової чи розробницької термінології, чи воно загального вжитку і його не варто враховувати. У першому випадку створюється запис у новій таблиці глосарію, куди потім переноситиметься і додаватиметься подальша інформація.

        1. Позначає важливість терміну (принаймні 3: важливе/середнє/не важливе)

        1. Якщо слово відеоігрове, то проглядає всі приклади вживання, на основі яких визначає основні варіанти перекладу і створює відповідні записи:

           Переклад1 - Приклад вживання (один чи кілька) і джерело (назва гри чи програми, із можливістю перейти до токена)
           Переклад2 - Приклад вживання (один чи кілька) і джерело (назва гри чи програми, із можливістю перейти до токена)

        1. Має бути функція додавати різні позначки до перекладів, наприклад вказувати, що це власна назва, чи що це арахаїзм, жаргонізм або сленг

        1. Можлива функція додавання синонімів (тобто мають виокремлюватися різні значення слова, але якщо в межах одного значення можливі різні переклади, то це теж варто вказати)

        1. Після перевірки науковим редактором запис «заморожується» і без крайньої потреби більше не редагується; варто також зберегти інфо, хто підготував запис словникової статті і хто з науковців його перевірив.

    1. - [ ] Створення інтерфейсу відображення для простих користувачів

    1. - [ ] Розгляд можливості інтеграції зі Steam Translation Server (для всіх мов)
