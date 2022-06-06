from time import sleep
from itertools import cycle


class TrafficLight:
    __dct = {'Красный':7, 'Желтый':2, 'Зеленый':12}
    __color = ''

    def state(self):
        return self.__color

    def running(self):
        all_sum = 10
        while all_sum != 0:
            for color, time in self.__dct.items():
                self.__color = color
                print(f'Цвет: {self.state()}, Продолжительность {time} сек')
                sleep(time)
                all_sum -= 1
                if all_sum == 0:
                    break

a = TrafficLight()
a.running()