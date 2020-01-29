script.py > file.txt # перенаправить весь вывод программы в файл
script.py < file.dat # or file.txt

from importlib import reload
from module import * # import all props like global variables

importlib.reload(fileName)
#script.pyw will play the script without open DOS window. (When file dbclicked)
dir(importlib) # show all attribute from obj
exec(open('moduleName').read()) #like from, import module without need in future use importlib.reload()


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



# OPEN
fin = open('filename and path', encoding='utf8') # open and read file
fout = open('filename and path', 'w', encoding='utg8') # open/create and write file
append = open('filename and path', 'a', encoding='utf8') # open/create and append in file
fin.read() # read all file like one line
fin.readlines() # read file like a few lines
fout.write('string') # write a new information in a file/append a new information in a file. After information we can add \n.
fout.close() # close file and empty buffer.

iterabelObj = iter(x) # Первый способ: возвращает итератор для данного объекта или возбуждает исключение StopIteration. Второй способ: передается функция/метод итерируемого объекта и специальное значение, при каждом шаге итерирования вызывается указанная функция и если значение функции не равно специальному значению то возвращается результат, в противном случае возбуждается StopIteration.
next(iterabelObj) # следующий шаг итерации.

# Все итераторы поддерживают фенкции:
    all(x)
    any(x)
    sum(x)
    len(x)
    min(x)
    max(x)
enumerate(iterator, start=1) # Итерирует объект и при каждой итерации возвращает номер итерации и значение, необязательный аргумент start указывает с какой итерации начинать

zip(iterator1, iterator2, ... iteratorN) # Функция zip() принимает один или более итерируемых объектов и возвращает итератор, который в свою очередь возвращает кортежи. Первый кортеж включает в себя первые элементы всех итерируемых объектов, второй кортеж – вторые элементы и т. д., итерации прекращаются, как только содержимое любого из итерируемых объектов будет исчерпано.

reversed(x) # желательно сделать преобразование типа после reversed
sorted(x, key=func) # Элементы итератора должны бить одного типа. Каждый итерируемый объект будет проходить через функцию а потом сортироваться. Функция не изменяет конечный итератор
sorted(x, reverse=True) 


raise errorName(args) # get an except, args will be showed
raise # get active except or empty


class exceptionName(baseException): pass # create yourself exception. 

isinstance(obj, obj2) # return True if first obj is the same type as obj2

s = lambda arguments: expression # Обычно используют позиционные аргументы хотя допускаются и другие как в обычных def функциях. Сами аргументы не обязательны

assert boolean_expression, optional_expression # Используется разработчиками, а не для конечных пользователей. Если boolean_expression вернет False то возбуждает исключение AssertionError c необязательным аргументом optional_expression.

python -0 filename.py Or PYTHONOPTIMIZE = 'O' # запустить игнорируя assert 
python -00 filename.py # запустить игнорируя строки документирования и assert

import xml.sax.saxutils # содержит удобную функцию xml.sax.saxutils.escape(), которая принимает строку и возвращает эквивалентную ей строку, в которой специальные символы языка разметки HTML («&», «<» и «>») замещаются их эквивалентами («&amp;», «&lt;» и «&gt;»).

funcName.__doc__ # return document of a function