

################################# CREATE DECORATOR (START) #################################
def decor(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('Also I have add some new features to the function')
        return result
    wrapper.__name__ = func.__name__
    wrapper.__doc__ = func.__doc__
    return wrapper

@decor
def scream(self, s):
    print(s.upper())
################################# CREATE DECORATOR (END) #################################

################################# CREATE DECORATOR WITH PARAMETERS FOR DECORATOR (START) #################################
def bounded(minimum, maximum):
    def decorator(function):
        @functools.wraps(function)
        def wrapper(*args, **kwargs):
            result = function(*args, **kwargs)
            if result < minimum:
                return minimum
            elif result > maximum:
                return maximum
            else:
                return result
        return wrapper
    return decorator

@bounded(0, 100)
def percent(amount, total):
    return (amount / total) * 100
################################# CREATE DECORATOR WITH PARAMETERS FOR DECORATOR (END) #################################

################################# CREATE DECORATOR WITH USE FUNCTOOLS MODULE (START) #################################
def decor(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print('Also I have add some new features to the function')
        return result
    return wrapper

@decor
def scream(self, s):
    print(s.upper())
################################# CREATE DECORATOR WITH USE FUNCTOOLS MODULE (END) ################################# 

################################# CREATE DECORATOR IN A CLASS (START) ################################# 
class Talk:
    def decor(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            print('Also I have add some new features to the function')
            return result
        return wrapper

    @decor
    def scream(self, s):
        print(s.upper())

do = Talk()
do.scream('Look good')
################################# CREATE DECORATOR IN A CLASS (END) ################################# 

################################# FIXED ATTRIBUTES IN A CLASS (START) ################################# 
class Machine:
    __slots__ = ('x', 'y', 'z') # Кроме этих атрибутов нельзя будет добавить новые. Экземпляры класса не будут содержать __dict__
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
################################# FIXED ATTRIBUTES IN A CLASS (END) ################################# 

################################# SETTER, GETTER, DELETER IN A CLASS (START) ################################# 
class Machine(object):
    def __init__(self, power = 300, weight = 1000, color = 'Blue', signal = 'Hight'):
        self.power = power
        self.weight = weight
        self.color = color
        self.signal = signal

    @property
    def signal(self):
        return self.__signal

    @signal.setter
    def signal(self, signal):
        assert signal.title() in {'Hight', 'Normal', 'Low'}, 'It can"t be used as a signal'
        self.__signal = signal

    @property
    def light(self):
        return self.__carLight
    
    @light.setter # also exist light.getter, light.deleter
    def light(self, carLight):
        assert carLight in {'black', 'purple', 'blue', 'red', 'yellow', 'green'}, 'The selected color can"t be'
        self.__carLight = carLight
################################# SETTER, GETTER, DELETER IN A CLASS (END) ################################# 

################################# COPY ANY FILE BY USING BUFFERSIZE (START) ################################# 
infile = open('sound.mp3', 'rb')
outfile = open('new.mp3', 'wb')
buffersize = 100000
buffer = infile.read(buffersize)
while len(buffer):
    outfile.write(buffer)
    print('.', end='')
    buffer = infile.read(buffersize)
print('done')
################################# COPY ANY FILE BY USING BUFFERSIZE (END) ################################# 

################################# CREATE SQLITE3 DATABASE (START) #################################
db = sqlite3.connect('C:/Users/FRDevelop/Desktop/data.db')
db.execute('drop table if exists test')
db.execute('create table test (t1 text, i1 int)')
db.execute('insert into test (t1, i1) values (?, ?)', ('one', 1))
db.execute('insert into test (t1, i1) values (?, ?)', ('two', 2))
db.execute('insert into test (t1, i1) values (?, ?)', ('three', 3))
db.commit()
cursor = db.execute('select * from test order by t1')
for row in cursor:
    print(row)
################################# CREATE SQLITE3 DATABASE (END) ################################# 

################################# CREATE SORTING CLASS (END) ################################# 
class SortKey:
    def __init__(self, *attribute_names):
        self.attribute_names = attribute_names
    def __call__(self, instance):
        values = []
        for attribute_name in self.attribute_names:
            values.append(getattr(instance, attribute_name))
        return values

class Person():
    def __init__(self, name, surname, email):
        self.name = name
        self.surname = surname
        self.email = email
    
FARHAD = Person('Farhad', 'Mike', 'fraksimike@gmail.com')
AYTEN = Person('Ayten', 'Mike', 'aytenmike@gmail.com')
LISA = Person('Lisa', 'Mike', 'lisamike@gmail.com')
person = [FARHAD, AYTEN, LISA]
person.sort(key=SortKey('name'))
################################# CREATE SORTING CLASS (END) ################################# 

################################# CONTEXT MANAGER (START) ################################# 
with contextlib.nested(open(filename), open(newfile, 'w')) as (fin, fout): # Библеотека позволяет не ломая дизайн кода использовать несколько менеджеров концекста в одной инструкции with
    for line in fin:
        fout.write(line)
################################# CONTEXT MANAGER (END) ################################# 
