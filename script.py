class Family(object):
    def __init__(self, name, surname):
        self.__name = name
        self.__surname = surname
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, name):
        assert isinstance(name, str)
        self.__name = name
    
farhad = Family(63, 'Maharramov')

print(farhad.name)
print(farhad.name)