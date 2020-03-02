class Product:
    __slots__ = ('__name', '__description', '__price')

    gogo = 'llittler'

    def __init__(self, name, description, price):
        self.__name = name
        self.__price = price
        self.__description = description

a = Product('a', 'b', 'c')
print(a.gogo)