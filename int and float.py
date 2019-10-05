--5 # 5
20 // 6 #how much 6 in 20?
20 % 6 # 2
ord('a') #str.codePointAt();
chr(число) # String.fromCodePoint();
7 // 2 # answer 3
7 % 2 # answer 1
abs(num) # absolute number
divmod(x, y) # like (x // y, x % y)
pow(x, y[, z]) # like pow(x, y) % z
max(num, num, num) # Math.max(); or max(arr)
min(num, num, num) # Math.min(); or min(arr)
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
-4e9
8.9e-4
x, y, z = 1, 2, 3
-89.5+2.125j # z.real, z.imag (-89.5, 2.125)
-89.5+2.125j.conjugate() # (-89.5-2.125j) изменяет знак мнимой части