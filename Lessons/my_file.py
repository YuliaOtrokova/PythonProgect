def sum_it(x, y):
    return x + y
#
def prod(x, y):
    return x*y


def division(x, y):

    try:
        return round(x/y, 2)
    except ZeroDivisionError:
        print('На ноль делить нельзя')

def squaring(x):
    return x**2

def cubbing(x):
    return x**3

# def div(x, y):
#     try:
#        return x/y
#     except ZeroDivisionError:
#         return ""
