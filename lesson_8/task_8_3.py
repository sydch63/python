def type_logger(func):
    def wrapper(*args, **kwargs):
        if func.__name__ == 'calc_cube': print(f'Call for: {func.__name__}')
        if func.__name__ == 'render_input': print(f'Call for: {func.__name__}')
        result = func(*args, **kwargs)
        print(f'{args[0]}: {type(args[0])}')
        lst = []
        if func.__name__ == 'render_input':
            for key in kwargs.keys():
                lst.append(f'{key} = {kwargs[key]}: {type(kwargs[key])}')
            print(','.join(lst))
        return print(f'Result: {result}  type: {type(args[0])}')
    return wrapper



@type_logger
def calc_cube(x):
    return x ** 3

@type_logger
def render_input(*args,**kwargs):
   return 1

f = calc_cube(5)
print()
render_input(1,a = 2,b = True,c = "q")





