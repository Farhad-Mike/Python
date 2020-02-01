Идентификаторы могу начинатся с "_" или символа алфавита.Не должны использоваться имена, начинающиеся и заканчивающиеся двумя символами подчеркивания (такие как __lt__). Мы можем использовать в идентификаторах национальные символы и символы греческого алфавита.b

i += True увеличит значение i на единицу.

0b110111101100101011011110 # двоичное число
0o67545336 # восьмеричное число
0xDECADEE # шестнадцатеричное число

Любые встроенные типы могут вызываться без аргументов.

Если аргумент имеет тип, для которого поддерживается преобразование в требуемый тип, и преобразование терпит неудачу, возбуждается исключение ValueError, в противном случае возвращается результат преобразования – объект.
Если тип аргумента не поддерживает преобразование в требуемый тип, возбуждается исключение TypeError.

Все битовые операторы (|, ^, &, << и >>) имеют соответствующие комбинированные операторы присваивания (|=, ^=, &=, <<= и >>=)

int + float == float
float + complex == complex
int + decimal.Decimal == decimal.Decimal

Примеры нескольких комплексных чисел: 3.5+2j, 0.5j, 4+0j, –1–3.7j. Обратите внимание, что если действительная часть числа равна 0, ее можно вообще опустить. Отдельные части комплексного числа доступны в виде атрибутов real и imag.
За исключением //, %, divmod() и версии pow() с тремя аргументами все остальные арифметические операторы и функции, могут использоваться для работы с комплексными числами.
Функции в модуле math не работают с комплексными числами. Это сделано преднамеренно, чтобы гарантировать, что пользователи модуля math будут получать исключения вместо получения комплексных чисел в некоторых случаях.
Если возникает необходимость использовать комплексные числа, можно воспользоваться модулем cmath, который содержит комплексные версии большинства тригонометрических и логарифмических функций, присутствующих в модуле math, плюс ряд функций, специально предназначенных для работы с комплексными числами, таких как cmath.phase(), cmath.polar() и cmath.rect(), а также константы cmath.pi и cmath.e, которые хранят те же самые значения типа float,
что и родственные им константы в модуле math.

В decimal.Decimal() следует записывать целые числа, числа в строке, экспоненциальные числа в строке. float числа не точные поэтому задать типом float не рекомендуется.
Все арифметические операторы и функции, включая соответствующие им комбинированные операторы присваивания, могут использоваться применительно к значениям типа decimal.Decimal, но с некоторыми ограничениями. Если слева от оператора ** находится объект типа decimal.Decimal, то справа от оператора должно быть целое число. Точно так же, если первый аргумент функции pow() имеет тип decimal.Decimal, то второй и необязательный третий аргументы должны быть целыми числами.
Некоторые функции, присутствующие в модуле math, реализованы как методы типа decimal.Decimal. Например, чтобы вычислить ex, где x имеет тип float, вызывается функция math.exp(x), а когда x имеет тип decimal.Decimal, следует использовать метод x.exp().

Названия символов Юникода не чувствительны к регистру и пробелы внутри них являются необязательными.

Числа, строки и кортежи являются неизменяемыми, а списки и словари – нет (они легко могут изменяться в любой своей части)
В отличии от JavaScript в Python при использовании оператора + литералы должны бить одного типа. Например нельзя сложить строку с числом.
Размер целых чисел в языке Python ограничивается только объемом памяти,

Проверка истинности в Python

Любое число, не равное 0, или непустой объект - true
Числа, равные 0, пустые объекты и значение None - false
Операции сравнения применяются к структурам данных рекурсивно
Операции сравнения возвращают True или False
Логические операторы and и or возвращают истинный или ложный объект-операнд

While - один из самых универсальных циклов в Python, поэтому довольно медленный.
Цикл for уже чуточку сложнее, чуть менее универсальный, но выполняется гораздо быстрее цикла while.

str.split(' ') не может разделитьпобуквенно как в JS

Комплексные числа нельзя сравнить, но можно проверить на равенство
r'C:\newt.txt' Это называется "Сырые" строки

Кортежи относятся к разряду неизменяемых объектов, поэтому после создания кортеж нельзя изменить. Списки относятся к разряду изменяемых объектов, поэтому мы легко можем вставлять и удалять элементы списка по своему желанию.

Одно из преимуществ операции проверки идентичности (is) заключается в высокой скорости ее выполнения. Это обусловлено тем, что сравниваются ссылки на объекты, а не сами объекты. Оператор is сравнивает только адреса памяти, в которых располагаются объекты. Чаще всего оператор is используется для сравнения элемента данных со встроенным пустым объектом None.

В отличие от JS в Python вес заглавной и строчной буквы не отличается т.е А == а (в Python)

Python предоставляет ключевое слово pass, которое представляет собой инструкцию, не делающую ровным счетом ничего, и которая может использоваться везде, где требуется блок кода (или когда мы хотим указать на наличие особого случая), но никаких действий выполнять не требуется.

a += 1 работает быстрее чем a = a + 1 так как ищет переменную всего один раз. Это относится также к JS

Имена всех стандартных модулей состоят только из символов нижнего регистра, поэтому для отличия своих модулей при именовании модулей многие программисты используют прием чередования регистра символов (например, MyModule).

Попытка обращения к индексу, находящемуся за пределами строки (или к любому индексу в пустой строке), будет вызывать исключение IndexError.

Функции в модуле math не работают с комплексными числами. Это сделано преднамеренно, чтобы гарантировать, что пользователи модуля math будут получать исключения вместо получения комплексных чисел в некоторых случаях.

Если возникает необходимость использовать комплексные числа, можно воспользоваться модулем cmath, который содержит комплексные версии большинства тригонометрических и логарифмических функций, присутствующих в модуле math, плюс ряд функций, специально предназначенных для работы с комплексными числами, таких как cmath.phase(), cmath.polar() и cmath.rect(), а также константы cmath.pi и cmath.e, которые хранят те же самые значения типа float, что и родственные им константы в модуле math.

Репрезентативная форма т.е форма для обработке на Python.
Строковая форма т.е для пользователя

In interactive mode, the last printed expression is assigned to the variable _.

You cannot convert complex numbers into another number type.

Once a set is created, you cannot change its items, but you can add new items.

Кортежи могут сравниваться с помощью стандартных операторов сравнения (<, <=, ==, !=, >=, >), при этом сравнивание производится поэлементно (и рекурсивно, при наличии вложенных элементов, таких как кортежи в кортежах).

Если словарь, для которого было получено представление, изменяется (dict.items(), dict.keys() и dict.values()), то представление будет отражать эти изменения.

Любой объект, имеющий метод __iter__(), или любая последовательность (то есть объект, имеющий метод __getitem__(), принимающий целочисленный аргумент со значением от 0 и выше), является итерируемым и может предоставлять итератор.
Все встроенные неизменяемые типы данных, такие как float, frozenset, int, str и tuple, являются хешируемыми объектами и могут добавляться во множества. Встроенные изменяемые типы данных, такие как dict, list и set, не являются хешируемыми объектами, так как значение хеша в каждом конкретном случае зависит от содержащихся в объекте элементов, поэтому они не могут добавляться в множества.

В множествах элементы не повторяются

Если двухместный оператор применяется ко множеству и фиксированному множеству, тип результата будет совпадать с типом операнда, стоящего слева от оператора. В случае операторов == и != порядок операндов не имеет значения, и выражение f == s вернет True, только если оба множества содержат одни и те же элементы.

Функция enumerate() принимает необязательный именованный аргумент start, который по умолчанию имеет значение 0. Мы передаем в этом аргументе значение 1, так как, в соответствии с общепринятыми соглашениями, нумерация строк в текстовых файлах начинается с 1.

В соответствии с общепринятыми соглашениями первая строка в описании должна представлять собой краткое, однострочное описание функции, затем следует пустая строка и далее следует полное описание функции, в конце которого приводится несколько примеров того, как может выглядеть использование функции в интерактивной оболочке. В главе 5 мы узнаем, как примеры, присутствующие в описании функции, могут использоваться для нужд модульного тестирования.

Для работы с параметрами командной строки в стандартной библиотеке имеется два модуля – optparse и getopt. Модуль getopt популярен, так как он прост в использовании и к тому же давно входит в состав библиотеки. Модуль optparse более новый и обладает более широкими возможностями.

#('/', '\', 'A:', 'B:', ..., 'Z:', 'a:', 'b:', ..., 'z:'). Любое имя файла в тарболле, начинающееся с указанных префиксов, считается подозрительным – в именах файлов в тарболле не должны использоваться абсолютные пути, поскольку это влечет за собой риск перезаписи системных файлов

Модуль tarfile определяет множество собственных исключений

В стандартной библиотеке Python имеется реализация WSGI (Web Server Gateway Interface – интерфейс шлюза вебсервера), представляющая собой стандартный интерфейс между веб-серверами и веб-приложениями, написанными на языке Python.



#

