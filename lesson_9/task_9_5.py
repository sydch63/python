

class Stationery:

    def __init__(self,title):
        self.title = title

    def draw(self):
        return f'Запуск отрисовки'

class Pen(Stationery):

    def __init__(self,title):
        super().__init__(title)

    def draw(self):
        return f'Запуск отрисовки {self.title} ручкой'

class Pencil(Stationery):

    def __init__(self,title):
        super().__init__(title)

    def draw(self):
        return f'Запуск отрисовки {self.title} карандашом'

class Handle(Stationery):

    def __init__(self,title):
        super().__init__(title)

    def draw(self):
        return f'Запуск отрисовки {self.title} маркером'

pen = Pen('синей')
print(pen.draw())
print()
pencil = Pencil('простым')
print(pencil.draw())
print()
handle = Handle('красным')
print(handle.draw())