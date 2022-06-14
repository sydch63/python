
class Worker:

    def __init__(self, name,surname,position ,wage,bonus):
        self._income = {"wage":wage,'bonus':bonus}
        self.name = name
        self.surname = surname
        self.position = position


class Position(Worker):

    def __init__(self,name,surname,position,wage,bonus):
        super().__init__(name,surname,position,wage,bonus)

    def get_full_name(self):
        return f'Имя Фамилия: {self.name} {self.surname}, Должность: {self.position}'

    def get_total_income(self):
        return f"Доход сотрудника: {self._income['wage']+self._income['bonus']}"


man1 = Position('Pavel','Sidorov','Engineer',100,50)
print(man1.get_full_name())
print(man1.get_total_income())
man2 = Position('Максим','Киляков','Водитель',1000,10)
print(man2.get_full_name())
print(man2.get_total_income())

'''Не понял зачем тут использовать геттер и сеттер,если вопрос о них был, так как изначально
у нас нет дефолтных значений для оклада и премии. Как я понял, геттер и сеттер исползуются, чтобы защищеные атрибуты класса
получать и менять только при необходимости в каком либо из экспляров класса
'''