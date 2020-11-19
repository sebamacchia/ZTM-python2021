# decorators

# def my_decorator(func):
#     def wrap_func(x):
#         print('#######')
#         func(x)
#         print('#####')
#
#     return wrap_func
#
#
# @my_decorator
# def hello(gre):
#     print(gre)
#
#
# hello('holaseba')


# PERFORMANCE DECORADOR

from time import time


def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'is took {t2-t1} mseconds')
        return result
    return wrapper


@performance
def long_time():
    for i in range(100000000):
        i * 5
    print('listo')


long_time()
