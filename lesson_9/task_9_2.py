
class Road:

    def __init__(self,length,width):
        self._length = length
        self._width = width

    def mass_of_asphalt(self):
        return (f'{self._length} м*{self._width} м*25 кг*5 см = {self._length *self._width *25 *5 //1000} т')




a = Road(20,5000)
print(a.mass_of_asphalt())
a = Road(30,8000)
print(a.mass_of_asphalt())