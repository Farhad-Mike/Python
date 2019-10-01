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

def someFunc:
    global x
    x = 'Global variable' #create inside function a global variable or use for change the global variable




