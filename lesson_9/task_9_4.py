

class Car:
    def __init__(self,speed,color,name, is_police = False):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        self.speed += 10
        return f'Машина {self.name} поехала'

    def stop(self):
        self.speed = 0
        return f'Машина {self.name} остановилась'

    def turn(self,direction):
        self.direction = direction
        if self.direction == 'Направо':
            return f'Машина {self.name} повернула направо'
        elif self.direction == 'Налево':
            return f'Машина {self.name} повернула налево'
        else:
            return f'Не правильно указано направление(Введите: Направо или Налево)'

    def show_speed(self):
        return f'Скорость машины {self.name} - {self.speed}'

class TownCar(Car):

    def __init__(self,speed,color,name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed > 60:
            return f'Скорость машины {self.name} превышена, пожалуйста снизте скорость'
        else:
            return f'Скорость машины {self.name} - {self.speed}'

class WorkCar(Car):

    def __init__(self,speed,color,name):
        super().__init__(speed, color, name)

    def show_speed(self):
        if self.speed > 40:
            return f'Скорость машины {self.name} превышена, пожалуйста снизте скорость'
        else:
            return f'Скорость машины {self.name} - {self.speed}'

class PoliceCar(Car):

    def __init__(self,speed,color,name,is_police = True):
        super().__init__(speed, color, name,is_police)

towncar = TownCar(60,color='black',name='#1')
print(towncar.name)
print(towncar.speed)
print(towncar.color)
print(towncar.is_police)
print(towncar.go())
print(towncar.show_speed())
print(towncar.stop())
print(towncar.show_speed())
print(towncar.turn('Налево'))
print(towncar.go())
print(towncar.show_speed())
print()
workcar = WorkCar(40,color='green',name='#2')
print(workcar.name)
print(workcar.speed)
print(workcar.color)
print(workcar.is_police)
print(workcar.go())
print(workcar.show_speed())
print(workcar.stop())
print(workcar.show_speed())
print(workcar.turn('Направо'))
print(workcar.go())
print(workcar.show_speed())
print()
policecar = PoliceCar(100,color='blue',name='#3')
print(policecar.name)
print(policecar.speed)
print(policecar.color)
print(policecar.is_police)
print(policecar.go())
print(policecar.show_speed())
print(policecar.stop())
print(policecar.show_speed())
print(policecar.turn('Налево'))
print(policecar.go())
print(policecar.show_speed())