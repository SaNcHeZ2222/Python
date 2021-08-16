def val_checker(lambda_func):
    def name_calc(func):
        def value_calc(*args):

            if lambda_func(*args):
                print(f'{func(*args)}')
            else:
                print(f'ValueError: wrong val {args[0]}')
        return value_calc
    return name_calc


@val_checker(lambda x: x > 0)
def calc_cube(x):
    return x ** 3


calc_cube(-5)