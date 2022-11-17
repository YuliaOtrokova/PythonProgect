# 4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую 3 значения (с помощью кортежа):
#      периметр квадрата, площадь квадрата и диагональ квадрата.
# 1 вариант

# import math as n
#
# def square(side):
#     return (side * 4, side ** 2, round(n.sqrt(2 * (side ** 2)), 2))
#
# square_data = square(int(input('Inpute square side: ')))
# print(f'square area: {square_data[0]}, perinent: {square_data[1]}, diagonal: {square_data[2]}')
# print(square(9))

#4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
#      в формате аргумент: значение. Например:
# 	name: John
# 	last_name: Smith
# 	age: 35
# 	position: web developer

# def name_arg(**kwargs):
#     for key, value in kwargs.items():
#         print("{}: {}".format(key, value))
# name_arg(name = 'Лев', last_name = 'Толстой', age = 85, position = 'писатель', book = 'Война и мир')


# 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
#      положительные числа
#
my_list = [20, -3, 15, 2, -1, -21]
func = list(filter(lambda x: x >=0, my_list))
# print(func)

# 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке
# my_list = [20, -3, 15, 2, -1, -21]
# import functools
# res = functools.reduce(lambda x, y: x*y, func)
# print(res)

# 4.5. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
#      Примените эти функции в качестве методов в другом файле.
#
from my_file import *
res = sum_it(9, 45)
print(res)

res1 = prod(5, 8)
print(res1)

res2 = division(5, 4)
print(res2)

res3 = squaring(5)
print(res3)

res4 = cubbing(5)
print(res4)



