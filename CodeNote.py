script.py > file.txt # перенаправить весь вывод программы в файл
script.py < file.dat # or file.txt

from importlib import reload
from module import * # import all props like global variables

importlib.reload(fileName)
#script.pyw will play the script without open DOS window. (When file dbclicked)
dir(importlib) # show all attribute from obj
exec(open('moduleName').read()) #like from, import module without need in future use importlib.reload()
<<<<<<< HEAD
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
 
=======

>>>>>>> d9f4c08dc3f3713e46f85ab44eb7acb8a766b067


help(str.replace) #show help for all methods

var1, *var2, var3 = [1, 2, 2, 2, 3] # var = 1, var2 = [2, 2, 2], var3 = 3

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
x is y # x == y

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

type(obj) # shoq type of object

None # like null and like undefined

var is var2 # compare link. Is var the same like var2? return True or False
var is not var2



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

def someFunc():
    global x
    x = 'Global variable' #create inside function a global variable or use for change the global variable

iter(var) # создает итерируемы объект из коллекции




