
class ComplexNumber:

    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __add__(self, other):
        self.new_x =self.x + other.x
        self.new_y = self.y + other.y
        return ComplexNumber(self.new_x,self.new_y)

    def __sub__(self, other):
        self.new_x = self.x - other.x
        self.new_y = self.y - other.y
        return ComplexNumber(self.new_x,self.new_y)

    def __mul__(self, other):
        self.new_x = (self.x*other.x - self.y*other.y)
        self.new_y = (self.x*other.y + other.x*self.y)
        return ComplexNumber(self.new_x,self.new_y)

    def __str__(self):
        prnt = f'{self.x}+{self.y}j'
        if '+-' in prnt:
            return prnt.replace('+-', '-')
        else:
            return prnt

num1 = ComplexNumber(2,3)
num2 = ComplexNumber(-1,1)
print(f'Сложение: {num1 + num2}')
print(f'Вычитание: {num1 - num2}')
print(f'Умножение: {num1 * num2}')

