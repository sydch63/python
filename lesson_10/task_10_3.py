
class Cell:

    def __init__(self,number):
        self.number = int(number)

    def __add__(self, other):
        return Cell(self.number + other.number)

    def __sub__(self,other):
        if Cell(self.number - other.number).number >= 0:
            return Cell(self.number - other.number)
        else:
            raise ValueError("Ячеек не может быть меньше 0")

    def __mul__(self, other):
        return Cell(self.number*other.number)

    def __floordiv__(self, other):
        return Cell(self.number//other.number)

    def make_order(self,row):
        value_row = self.number // row
        if self.number% row == 0:
            return '\n'.join(['*'*row]*value_row)
        else:
            remainder  = self.number % row
            return str(value_row *'*****\n'+ ('*'*remainder))


c1 = Cell(16)
print(f'Первая клетка:\n{c1.make_order(5)}')
c2 = Cell(4)
print(f'Вторая клетка:\n{c2.make_order(5)}')
c3 = Cell(8)
print(f'Третья клетка: \n{c3.make_order(5)}')
c4 = Cell(10)
print(f'Четвертая клетка:\n{c4.make_order(5)}')
c5 = Cell(2)
print(f'Пятая клетка:\n{c5.make_order(5)}')
print()
print(f'Операция сложения:\n\tПолученный тип:{type((c2+c3))}\n\tРезультат:{(c2+c3).number}\n{(c2+c3).make_order(5)}')
print()
print(f'Операция вычитания:\n\tПолученный тип:{type((c1-c2))}\n\tРезультат:{(c1-c2).number}\n{(c1-c2).make_order(5)}')
print()
print(f'Операция умножения:\n\tПолученный тип:{type((c2*c3))}\n\tРезультат:{(c2*c3).number}\n{(c2*c3).make_order(5)}')
print()
print(f'Операция деление:\n\tПолученный тип:{type((c1//c5))}\n\tРезультат:{(c1//c5).number}\n{(c1//c5).make_order(5)}')