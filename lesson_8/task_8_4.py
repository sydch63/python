
def val_checker(func_lambda):
    def _val_checker(func):
        def wrapper(*args):
            try:
                result = func(*args)
                if func_lambda(*args) is True:
                    return print(result)
                else:
                    raise ValueError(f'wrong val {args[0]}')
            except ValueError:
                raise
        return wrapper
    return _val_checker

@val_checker(lambda x: x > 0)
def calc_cube(x):
   return x ** 3

a = calc_cube(5)