import sys

sys.argv[1] # при вызове скрипта python это второй аргумент т.е аргумент после названия файла
sys.exit(x) # немедленно завершает работу программы, закрывая любые открытые файлы. Она принимает необязательный аргумент типа int, который передается вызывающей командной оболочке
sys.stdout # объектфайла, представляющий «стандартный поток вывода», который обычно связан с консолью и отличается от sys.stderr
sys.stderr # стандартный поток вывода сообщений об ошибках используя небуферизованный вывод.
sys.stdin
sys.exit() # сама программа может вызывать эту функцию. 0 - успешное завершение программы 1 - ошибка другого типа 2 - ошибка в использовании программы