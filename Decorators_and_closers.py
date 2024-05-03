# example for closers
import time


# def outer_func(x):
#     def inner_func(y):
#         return x + y
#
#     return inner_func
#
#
# outer = outer_func(4)
# result = outer(5)
# print(result)

def create_summer():
    summa = 2

    def quantity():
        nonlocal summa
        summa += 1
        return summa

    def distinction():
        nonlocal summa
        summa -= 1
        return summa

    def get_sum():
        return summa

    return quantity, distinction, get_sum


quanter, distincter, getter = create_summer()


#
# print(quanter())
# print(quanter())
# print(quanter())
# print(quanter())
# print(distincter())
# print(getter())

# Decorators ---->>>
def timer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, *kwargs)
        end = time.time()
        print(f'{func.__name__},{start - end}')
        return result

    return wrapper


@timer
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# print(factorial(10))
