class DateInitError(Exception):pass



class Date:

    def __init__(self,date):
        try:
            if Date.validation_date(Date.extract_date(date)):
                self.date = date
            else:
               raise DateInitError
        except DateInitError:
            raise DateInitError(f'Дата: {date}, результат: дата не прошла валидацию')


    @classmethod
    def extract_date(cls,date):
        lst_date = []
        try:
            for i in date.split('-'):
                lst_date.append(i)
            day = int(lst_date[0])
            month = int(lst_date[1])
            year = int(lst_date[2])
            tpl_date = day,month,year
            return tpl_date
        except Exception:
            raise ValueError('Format date: "dd-mm-yyyy"')

    @staticmethod
    def validation_date(date):
        day,month,year = date
        valid_value = 0
        if 1<= day <= 31:
            valid_value = 1
        if 1<= month <= 12:
            valid_value += 1
        if 1900 <= year <= 2022:
            valid_value += 1
        if valid_value == 3:
            valid_value = True
            return valid_value
        else:
            valid_value = False
            return valid_value

    def __str__(self):
        day,month,year = Date.extract_date(self.date)
        return f'{year}.{month}.{day}'



d1 = Date('31-12-2021')
print(d1)
d = Date('17-08-1900')
print(d)
# d2 = Date('32-12-2022')
# print(d2)
# d3 = Date('29_09-1997')
# print(d3)