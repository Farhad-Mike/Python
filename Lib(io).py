import io

io.StringIO('string') # для создания объектов подобных строкам которые ведут себя как текстовые файлы размещенные в памяти.Это может быть удобно, когда необходимо использовать программный код, выполняющий запись в файл, для записи в строку. string не обязательный аргумент
o = io.StringIO() 
o.getvalue() # вернуть все значение записаное в этот объект