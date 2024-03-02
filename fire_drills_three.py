def func_to_calculate(*args):

    Q = ((2 * 50 * x) % 30)**0.5
    map(lambda x: Q , args)


print(func_to_calculate(2, 3, 4))
