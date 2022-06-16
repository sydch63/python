import abc

class Clothes(abc.ABC):

    lst_cloth = []
    def __init__(self,name):
        self.name = name
        self.lst_cloth.append(self)
        self.reserved_cloth = None


    @abc.abstractmethod
    def cloth_require(self):
        pass

    @property
    def calc_cloth(self):
        return self.reserved_cloth

    @property
    def cloth_summary(self):
        try:
            if isinstance(self, Coat):
                return round(sum(value.calc_cloth for value in self.lst_cloth if isinstance(value,Coat)),2)
            elif isinstance(self, Suit):
                return round(sum(value.calc_cloth for value in self.lst_cloth if isinstance(value,Suit)), 2)
        except TypeError:
            raise TypeError("Нужно выполнить add_to_reserve")


class Coat(Clothes):

    def __init__(self,name,param):
        super().__init__(name)
        self.param = param

    def cloth_require(self):
        self.coat_value_cloth = round(self.param/6.5 + 0.5,2)
        return f'Для пошива "{self.name}" нужно {self.coat_value_cloth} ткани'

    def add_to_reserve(self):
        try:
            self.reserved_cloth = self.coat_value_cloth
            Clothes.cloth_summary
        except AttributeError:
            raise AttributeError("Сначала, нужно выполнить cloth_require")

class Suit(Clothes):

    def __init__(self,name,param):
        super().__init__(name)
        self.param = param

    def cloth_require(self):
        self.suit_value_cloth = round(self.param*2 + 0.3,2)
        return f'Для пошива "{self.name}" нужно {self.suit_value_cloth} ткани'

    def add_to_reserve(self):
        try:
            self.reserved_cloth = self.suit_value_cloth
            Clothes.cloth_summary
        except AttributeError:
            raise AttributeError("Сначала, нужно выполнить cloth_require")



c1 = Coat("Красное пальто",12)
print(c1.cloth_require())
c1.add_to_reserve()
print(f'Общее кол-во ткани для пальто: {c1.cloth_summary}')
c2 = Coat("Зеленое пальто",8)
print(c2.cloth_require())
c2.add_to_reserve()
print(f'Общее кол-во ткани для пальто: {c2.cloth_summary}')
c3 = Coat("Зеленое пальто",5)
print(c3.cloth_require())
c3.add_to_reserve()
print(f'Общее кол-во ткани для пальто: {c2.cloth_summary}')
print()

s1 = Suit("Черный костюм",12)
print(s1.cloth_require())
s1.add_to_reserve()
print(f'Общее кол-во ткани для костюмов: {s1.cloth_summary}')
s2 = Suit("Белый костюм",8)
print(s2.cloth_require())
s2.add_to_reserve()
print(f'Общее кол-во ткани для костюмов: {s1.cloth_summary}')
s3 = Suit("Синий костюм",3)
print(s3.cloth_require())
s3.add_to_reserve()
print(f'Общее кол-во ткани для костюмов: {s3.cloth_summary}')