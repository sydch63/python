
class MyExceptionDiv(Exception):pass

def my_div(a,b):
    try:
        return int(a/b)
    except ZeroDivisionError:
        raise MyExceptionDiv(f'На ноль делить нельзя')


print(my_div(10,5))
my_div(2,0)