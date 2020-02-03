script.py > file.txt # перенаправить весь вывод программы в файл
script.py < file.dat # or file.txt

import bisect # содержит функции поиска в отсортировачных эелементах, а так же функции вставки с сохранением порядка.
import weakref # содержит средства создания слабых ссылок, как обычные ссылки но, если единственная ссылка на объект – слабая ссылка, то такой объект может считаться готовым к утилизации.
import bz2 # обеспечивает возможность работы с файлами .bz2
import gzip # обеспечивает возможность работы с файлами .gz
import tarfile # обеспечивает возможность работы с файлами .tar, .tar.gz (а также .tgz) и .tar.bz2
import zipfile # обеспечивает возможность работы с файлами .zip
import aifc # реализует поддержку формата AIFF (Audio Interchange File Format – формат файлов для обмена аудиоданными) 
import wave # обеспечивает возможность для работы с файлами .wav (несжатыми)
import audioop # разновидностями аудиоданных можно манипулировать
import sndhdr # предоставляет пару функций, позволяющих определить тип аудиоданных, хранящихся в файле, и некоторые характеристики этих данных, такие как частота дискретизации.
import configparser # предоставляет функции чтения и записи конфигурационных файлов (Нап: .ini).
import csv # обеспечивает средства чтения и записи этих форматов и в состоянии учитывать некоторые особенности, препятствующие возможности непосредственной обработки файлов CSV.
import pickle # используется для сохранения на диске и восстановления с диска произвольных объектов Python (включая целые коллекции)
import base64 # используется для обработки двоичных данных, внедренных в сообщения электронной почты в виде текста ASCII. Он также может использоваться для сохранения двоичных данных в файлах с расширением .py.
import bz2 # используется для работы с форматом сжатия bzip2. Версии Python для Windows всегда собираются со встроенной поддержкой сжатия bzip2, поэтому отсутствовать она может только в некоторых сборках для UNIX.
import shutil # предоставляет высокоуровневые функции для работы с файлами и каталогами
import tempfile # create temporary files and catalogs
import filecmp # может использоваться для сравнения файлов
import subprocess # позволяющими запускать другие процессы, взаимодействовать с ними с помощью каналов и получать возвращаемые значения.
import multiprocessing # обладающего обширными возможностями распределения работы между несколькими процессами и сбора результатов.
import mimetypes # включает функцию mimetypes.guess_type(), которая пытается определить тип MIME файла.
import socket # предоставляет наиболее фундаментальные функциональные возможности для работы с сетями
import ssl # Настроить шифрование и аутентификацию при работе с сокетами
import socketserver # предоставляет реализации серверов TCP/UDP 
import asyncore # Асинхронная обработка сокетов на стороне клиентов и серверов
import asynchat # построенный на основе asyncore более высокоуровневый модуль
import wsgiref # предоставляет рекомендации по внедрению WSGI и содержит модули для реализации серверов HTTP
import http.server # предоставляет реализацию сервера HTTP
import http.cookies, http.cookiejar # содержат функции для работы с cookies
import cgi, cgitb # поддержка сценариев CGI предоставляется модулями
import http.client # Доступ к запросам HTTP на стороне клиента
import urllib: urllib.parse, urllib.request, urllib.response, urllib.error, urllib.robotparser # более простой и удобный доступ к адресам URL
import json # Данные в формате JSON могут читаться и записываться
import xmlrpc.server, xmlrpc.client # поддержка XML-RPC (Remote Procedure Call – вызов удаленных процедур)
import ftplib # возможности для работы на стороне клиента с протоколом FTP
import nntplib # для работы с протоколом NNTP (Network News Transport Protocol – сетевой протокол передачи новостей)
import telnetlib # для работы с протоколом TELNET
import smtpd # предоставляет реализацию сервера SMTP (Simple Mail Transport Protocol)
import smtplib # предоставляет возможность реализации клиентов электронной почты для протокола SMTP
import imaplib # для протокола IMAP4 (internet Message Access Protocol – протокол интерактивного доступа к электронной почте)
import poplib # for POP3 protocol
import mailbox # Возможность доступа к почтовым ящикам различных форматов
import email # Отдельные сообщения электронной почты (включая сообщения, состоящие из нескольких частей) могут создаваться и обрабатываться


















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


expression1 if boolExpression else expression2 # if bool_expression is True then return expression1 otherwise return expression2


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

print('string', file=filename) # Можно записывать информацию в файл через print()

sys.stdout = io.StringIO() # весь вывод будет записоваться как строка в объект созданный при помощи io.StringOI
sys.stdout = sys.__stdout__ # восстановить обычную работу объекта
sys.stdout.getvalue() # вернуть все значение записаное в этот объект (т.е в io.StringIO())

fh = urllib.request.urlopen("http://www.python.org/index.html") # Загрузка файлов из Интернета
html = fh.read().decode("utf8")