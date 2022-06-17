
class MyValidation:pass


value = None
lst_user = []

def value_valid(value):
    try:
        if isinstance(int(value), int):
            return value
    except ValueError:
        raise MyValidation

while value != 'stop':
    value = input('Введите число(остановка-stop): ')
    try:
        if value == 'stop':
            print(lst_user)
            break
        else:
            lst_user.append(value_valid(value))
    except Exception:
        print("Вы ввели не число")




