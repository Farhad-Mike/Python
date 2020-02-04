class Machine(object):
    def __init__(self, power = 300, weight = 1000, color = 'Blue', carLight = 'white'):
        self.power = power
        self.weight = weight
        self.color = color
        self.light = carLight
    
    @property
    def light(self):
        return self.__carLight
    
    @light.setter
    def light(self, carLight):
        assert carLight in {'black', 'purple', 'blue', 'red', 'yellow', 'green', 'white'}, 'The selected color can"t be'
        self.__carLight = carLight
    

car = Machine(2000, 4.5, 'black', 'gogr')

print(car.color, car.power, car.weight, car.carLight)

