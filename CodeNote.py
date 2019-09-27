script.py > file.txt # перенаправить весь вывод программы в файл
script.py < file.dat # or file.txt

import importlib
import math
import random
import re # regexp
import calendar
import sys
import decimal
import unicodedata

from importlib import reload
from module import * # import all props like global variables

importlib.reload(fileName)
math.pi
math.sqrt(num) #like Math.sqrt(num);
math.floor(num)
math.ceil(num)
math.hypot(x, y) # вычисляет расстояние от начала координат до точки (x, y) и дает тот же результат, что и выражение math.sqrt((x ** 2) + (y ** 2)).
math.modf(13.732) # (0.73199999999999932, 13.0)
math.acos(x) # Возвращает арккосинус x в радианах
math.acosh(x) # Возвращает гиперболический арккосинус x в радианах
math.asin(x) # Возвращает арксинус x в радианах
math.asinh(x) # Возвращает гиперболический арксинус x в радианах
math.atan(x) # Возвращает арктангенс x в радианах
math.atan2(y, x) # Возвращает арктангенс y/x в радианах
math.atanh(x) # Возвращает гиперболический арктангенс x в радианах большее и равное x, например, math.ceil(5.4) == 6
math.copysign(x,y) # Возвращает x со знаком числа y
math.cos(x) # Возвращает косинус x в радианах
math.cosh(x) # Возвращает гиперболический косинус x в радианах
math.degrees(r) # Преобразует число r, типа float, из радианов в градусы
math.e # Константа e, примерно равная значению 2.7182818284590451
math.exp(x) # Возвращает ex, то есть math.e ** x
math.fabs(x) # Возвращает |x|, то есть абсолютное значение x в виде числа типа float
math.factorial(x) # Возвращает x!
math.fmod(x, y) # Выполняет деление по модулю (возвращает остаток) числа x на число y; дает более точный результат, чем оператор %, применительно к числам типа float
math.frexp(x) # Возвращает кортеж из двух элементов с мантиссой (в виде числа типа float) и экспонентой (в виде числа типа int)
math.fsum(i) # Возвращает сумму значений в итерируемом объекте i в виде числа типа float
math.isinf(x) # Возвращает True, если значение x типа float является бес конечностью (±inf(±∞))
math.isnan(x) # Возвращает True, если значение x типа float не является числом
math.ldexp(m, e) # Возвращает m × 2e – операция, обратная math.frexp()
math.log(x, b) # Возвращает logbx, аргумент b является необязательным и по умолчанию имеет значение math.e
math.log10(x) # Возвращает log10x
math.log1p(x) # Возвращает loge(1+x); дает точные значения, даже когда значение x близко к 0
math.modf(x) # Возвращает дробную и целую часть числа x в виде двух значений типа float
math.radians(d) # Преобразует число d, типа float, из градусов в радианы
math.sin(x) # Возвращает синус x в радианах
math.sinh(x) # Возвращает гиперболический синус x в радианах
math.fsum(i) # Возвращает сумму значений в итерируемом объекте i в виде числа типа floata
math.tan(x) # Возвращает тангенс x в радианах
math.tanh(x) # Возвращает гиперболический тангенс x в радианах
math.trunc(x) # Возвращает целую часть числа x в виде значения типа int; то же самое, что и int(x)
random.random() #Math.random();
random.randrange(1, 10)
random.choice([num, num2, num3]) #choice one from gave
random.randint(1, 6) # choice one between 1 - 6
decimal.Decimal(number)
#script.pyw will play the script without open DOS window. (When file dbclicked)
sys.argv[1] # при вызове скрипта python это второй аргумент т.е аргумент после названия файла
dir(importlib) # show all attribute from obj
exec(open('moduleName').read()) #like from, import module without need in future use importlib.reload()
str(value) #String();
'Hello' 'World' # 'HelloWold'; not work with variables
4e9
-4e9
8.9e-4
x, y, z = 1, 2, 3
-89.5+2.125j # z.real, z.imag (-89.5, 2.125)
-89.5+2.125j.conjugate() # (-89.5-2.125j) изменяет знак мнимой части
#below code can be used not for only str. also for list and for cortages
len(value) #like str.length;
str[index] # str[0]
str[-1] #the first symbol from last
str[1:3] #str.substring(1, 3);
str[:3] #like str[0:3]
str[:] #copy all string
str[::-1] #reverse string
('theverylongstring')[2:10:2] # вырезать с шагом (first will select 'everylong' then will select 'eeyo')
str[2::2]
str * 3 #'strstrstr' make concatination of string
#above code can be used not for only str. also for list and for cortages


unicodedata.normalize('NFKD', str) # str.normalize();
str + 'str' #'someStringstr', str is not changes
str.find(str, [start],[end]) # Поиск подстроки в строке. Возвращает номер первого вхождения или -1
str.rfind(str, [start],[end]) # Поиск подстроки в строке. Возвращает номер последнего вхождения или -1
str.index(str, [start],[end]) # Поиск подстроки в строке. Возвращает номер первого вхождения или вызывает ValueError
str.rindex(str, [start],[end]) # Поиск подстроки в строке. Возвращает номер последнего вхождения или вызывает ValueError
str.replace(t, u, n) #will not change the str. Возвращает копию строки s, в которой каждое (но не более n, если этот аргумент определен) вхождение подстроки t замещается подстрокой u
str.split(t, n) # Возвращает список строк, выполняя разбиение строки s не более чем n раз по подстроке t. Если число n не задано, разбиение выполняется по всем найденным подстрокам t. Если подстрока t не задана, разбиение выполняется по пробельным символам. Для выполнения разбиения строки, начиная с правого края, используйте метод str.rsplit – этот метод имеет смысл применять, когда задано число разбиений n, которое меньше максимального числа возможных разбиений
str.rsplit(t, n)
str.splitlines(bool) # Возвращает список строк, выполняя разбиение строки s по символам перевода строки (\n), удаляя их, если в аргументе f задано значение False
str.upper() #str.toUpperCase();
str.lower()
str.isalpha() #	Состоит ли строка из букв-
str.isalnum() # Состоит ли строка из цифр или букв
str.isdigit() # Возвращает True, если строка s не пустая и содержит только символы ASCII, обозначающие цифры десятичной системы счисления
str.isdecimal() # Возвращает True, если строка s не пустая и содержит только символы Юникода, обозначающие цифры десятичной системы счисления
str.isidentifier() # Возвращает True, если строка s не пустая и является допустимым идентификатором
str.isprintable() # Возвращает True, если строка s пустая или содержит только печатаемые символы, включая пробел, но не символ перевода строки
str.isnumeric() # Возвращает True, если строка s не пустая и содержит только символы Юникода, используемые для обозначения чисел
str.islower() # Состоит ли строка из символов в нижнем регистре
str.isupper() # Состоит ли строка из символов в верхнем регистре
str.isspace() # Состоит ли строка из неотображаемых символов (пробел, символ перевода страницы ('\f'), "новая строка" ('\n'), "перевод каретки" ('\r'), "горизонтальная табуляция" ('\t') и "вертикальная табуляция" ('\v'))
str.istitle() # Начинаются ли слова в строке с заглавной буквы
str.startswith(str) #Начинается ли строка S с шаблона str
str.endswith(str) #Заканчивается ли строка S шаблоном str
str.join(arr) # Сборка строки из arr с разделителем str
str.lstrip('[]<>/sym') # delete space from start
str.rstrip('[]<>/sym') # delete space from end
str.strip('[]<>/sym') # delete spaces from start and end. Удаляет каждый из найденный символов если использовать с аргументом
str.partition(str2) # Возвращает кортеж, содержащий часть перед первым шаблоном, сам шаблон, и часть после шаблона. Если шаблон не найден, возвращается кортеж, содержащий саму строку, а затем две пустых строки
str.rpartition(str2) # Возвращает кортеж, содержащий часть перед последним шаблоном, сам шаблон, и часть после шаблона. Если шаблон не найден, возвращается кортеж, содержащий две пустых строки, а затем саму строку
str.zfill(width) # Делает длину строки не меньшей width, по необходимости заполняя первые символы нулями
str.ljust(width, "-") # Делает длину строки не меньшей width, по необходимости заполняя последние символы символом char
str.rjust(width, "-") # Делает длину строки не меньшей width, по необходимости заполняя первые символы символом fillchar
str.swapcase() # Переводит символы нижнего регистра в верхний, а верхнего – в нижний
str.capitalize() # Переводит первый символ строки в верхний регистр, а все остальные в нижний
str.title() # Первую букву каждого слова переводит в верхний регистр, а все остальные в нижний
str.center(width [,fill]) # Возвращает отцентрованную строку, по краям которой стоит символ fill (пробел по умолчанию)
str.count(str, [start],[end]) # Возвращает количество найденных str в диапазоне [начало, конец] (0 и длина строки по умолчанию)
str.expandtabs([tabsize]) # Возвращает копию строки, в которой все символы табуляции заменяются одним или несколькими пробелами, в зависимости от текущего столбца. Если TabSize не указан, размер табуляции полагается равным 8 пробелам
str.encode(encoding, err) # Возвращает объект типа bytes, представляющий строку в кодировке по умолчанию или в кодировке, определяемой аргументом encoding, с обработкой ошибок, определяемой необязательным аргументом err
table = str.maketrans(f, s, t) # Создать таблицу на замену каждого символа из аргументов f и s, в аргумент t записываются те символы которые нужно удалить
'some string for replace symbols'.translate(table)


'''some text''' # show the string with tabs and others spaces
'%s some value %s then will' % ('value1', 'value2') # result is 'value1 some value value2 then will'
'{0} some value {1} then will'.format('value1', 'value2') # result is 'value1 some value value2 then will'
'{second} some value {first} then will'.format(second = 'value1', first = 'value2') # result is 'value1 some value value2 then will'
'{{{0}}}'.format('string') # result is '{string}'
###
coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
'Coordinates: {latitude}, {longitude}'.format(**coord) # 'Coordinates: 37.24N, -115.81W'
###
help(str.replace) #show help for all methods


--5 # 5
20 // 6 #how much 6 in 20?
20 % 6 # 2
ord('a') #str.codePointAt();
chr(число) # String.fromCodePoint();


list(str) # create list from string
arr = [c * 2 for c in ‘spam’] # Дублирование символов в строке  [‘ss’, ‘pp’, ‘aa’, ‘mm’]
arr = [M[i][i] for i in [0, 1, 2]] # Выборка элементов диагонали матрицы
arr = [row[2] for row in arr] # create new array and add to them from all multidimensional arrays indexed elem
arr = [row[2] for row in arr if condition] #if condition return true then return elem
arr = [c + d for c in 'list' if c != 'i'  for d in 'spam' if d != 'a'] # ['ls', 'lp', 'lm', 'ss', 'sp', 'sm', 'ts', 'tp', 'tm']
arr.append(value) #like arr.push(); but can add only 1 value
list.append(arr, value) # second variant like arr.push()
arr.extend(arr2) # like arr.push(...arr2)
arr.pop()
arr.insert(position, newElem) #add new elem to the position
arr.remove(value) #find and delete the value
arr.sort()
arr.reverse()
arr.copy() # will copy list
arr * 3 #repeat inner elements a few times
arr + arr2
'value' in arr # does array contain the value. Return True or False
'value' not in arr # does array not contain the value. if not exist then return True
arr += 'str' # add like [s, t, r]
arr += ['str'] # add like ['str']
del arr # delete list
del arr[0] # delete index
arr.clear() # empties list
arr.index('element') # return index of first founded element

input('Question'); # prompt();
print('Avswer', end="value")

###############

if comparison:
    statement
elif comparison:
    statement
else:
    statement

###############


X and Y  # X && Y
X or Y  # X || Y
not X  # !X

A = Y if X else Z


while a < 15:
    statement
    statement2
    statement3


for i in 'hello world':
    statement:
    continue
    break
else:
    statement # will make statement if cicle completed by himself (wthout break);


for _ in range(N): # for(let i = 0; i < N; i++){}
    statement


7 // 2 # answer 3
7 % 2 # answer 1
abs(num) # absolute number
divmod(x, y) # like (x // y, x % y)
pow(x, y[, z]) # like pow(x, y) % z
max(num, num, num) # Math.max(); or max(arr)
max(num, num, num) # Math.min(); or min(arr)
round(num, n) # Math.round(num); argument n show how much numbers should be after dot

x | y # Побитовое или
x ^ y #	Побитовое исключающее или
x & y #	Побитовое и
x >> y # Битовый сдвиг вправо
x << y # Битовый сдвиг влево
~x # Инверсия битов
num.bit_length() # количество бит, необходимых для представления числа в двоичном виде, без учёта знака и лидирующих нулей.
num.to_bytes(length, byteorder, *, signed=False) # возвращает строку байтов, представляющих это число.
num.from_bytes(bytes, byteorder, *, signed=False) # возвращает число из данной строки байтов.
num.is_integer() # return True if num do not have float part (5.0 return True)
bin(num) # представление числа в двоичной системе. Возвращает строку
int('101011', система исчисления) # Применённая к числу с плавающей точкой, отсекает дробную часть.
hex(х) # преобразование целого числа в шестнадцатеричную строку. Возвращает строку
oct(х) # преобразование целого числа в восьмеричную строку. Возвращает строку




# for float numbers
(45.5).as_integer_ratio() # пара целых чисел, чьё отношение равно этому числу.
(45.5).is_integer() # is the number integer?
(45.5).hex() - переводит float в hex.
float.fromhex('0x1.5000000000000p+3') # переводит в float из шестнадцатеричной строки.
(45.5).as_integer_ratio() # rвозвращает две цифры при делении которых получается float число
# for float numbers

complex(1, 2) # create complex number (1 + 2j)
(1 + 2j).conjugate() # Сопряжённое число (("1 - 2j"))
(1 + 2j).imag # мнимая часть (2)
(1 + 2j).real # действительная часть (1)
abs((3 + 4j)) #модуль комплексного числа (5)
pow(3 + 4j, 2) # Возведение в степень (-7+24j)

\n	# Перевод строки
\a	# Звонок
\b	# Забой
\f	# Перевод страницы
\r	# Возврат каретки
\t	# Горизонтальная табуляция
\v	# Вертикальная табуляция
\N{id}	# Идентификатор ID базы данных Юникода
\uhhhh	# 16-битовый символ Юникода в 16-ричном представлении
\Uhhhh…	# 32-битовый символ Юникода в 32-ричном представлении
\xhh	# 16-ричное значение символа
\ooo	# 8-ричное значение символа
\0	# Символ Null (не является признаком конца строки)

r'C:\newt.txt' # Если перед открывающей кавычкой стоит символ 'r' (в любом регистре), то механизм экранирования отключается. Несмотря на назначение, "сырая" строка не может заканчиваться символом обратного слэша.

type(obj) # shoq type of object

(1, 2, 3, 4) # the type of data is TUPLE или на русском Кортежи.
1, 2, 3, 4 # кортежи также могут быть созданы без скобок
1, # for create one tuple
() # create empty tuple
tuple(obj) # convert to tuble
(1, 2, 3, 4).count('elem') # Returns the number of times a specified value occurs in a tuple

None # like null and like undefined

var is var2 # compare link. Is var the same like var2? return True or False
var is not var2

elem in list
elem in string
elem not in tuple # return True or False

and # && запинается на лжи
or # || запинается на правде
not # !


try:
    suite
except:
    suite  # like try catch


try:
    suite
except typeOfError as variableN: # в переменную variableN создает ссылку на объект исключения. И если уже в этом except тоже будет объект исключения то перехватится еще одним   следующим except
    suite


def functionName(arguments):
    suite


range(startNum, stopNum, step) # не включительно stopNum
range(stopNum) # startNum = 0, step = 1

def someFunc:
    global x
    x = 'Global variable' #create inside function a global variable or use for change the global variable

setter = {'a', 'few', 'some', 'value'} # Once a set is created, you cannot change its items, but you can add new items.
setter.add('elem') # add one element
setter.update(['a', 'few', 'new', 'elements']) # add a few new elements
setter.discard('element') # don't return error if element doesn't exist
setter.remove('element') # return error if doesn't exist element
setter.pop()
setter.clear() # clear all set. Make them empty
setter.union(newSetter) # join sets
setter.update(newSetter) # join sets. Both union() and update() will exclude any duplicate items.
set.isdisjoint()
del setter # delete set
key in setter # True/False
