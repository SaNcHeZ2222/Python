def type_logger(func):
    def args_logger(*args):
        print(f'{func(*args)}: {type(args)}')
    return args_logger


@type_logger
def calc_cube(x):
    return x ** 3


calc_cube(7)