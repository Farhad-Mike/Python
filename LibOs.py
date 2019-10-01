import os

os.listdir(r'Derictory\Derictory\File') # возвращает список файлов и каталогов в указанном каталоге, но при этом в список никогда не включаются специальные имена каталогов «.» или «..».
os.path.getsize(r'Directory\Directory\File') # возвращает размер заданного файла в байтах
os.path.isfile(r'Directory\Directory\File') # True/False если заданный файл существует в данном каталоге