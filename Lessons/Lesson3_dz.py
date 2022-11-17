# 3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3
# my_list = ['a', 'b', [1, 2, 3], 'd']
# print(my_list[2])  #[-2] тоже работает

# 3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
#    - получите сумму всех чисел,
#    - распечатайте все строки, где есть буква 'a'
#ПЕРВОЕ РЕШЕНИЕ
# list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# print(list_1[2] + list_1[4] + list_1[6] + list_1[7])
# print(list_1[1], list_1[5])

#ВТОРОЕ РЕШЕНИЕ:
# sum = 0
# for i in list_1:
#     if type(i) == int or type(i) == float:
#         sum += i
# print('Summa ravna', sum)


#ТРЕТЬЕ РЕШЕНИЕ
# result = list(filter(lambda x: isinstance(x, int), list_1))
# print(sum(result))
#
#ЧЕТВЕРТОЕ РЕШЕНИЕ - CАМОЕ ИНТЕРЕСНОЕ!!!!!
# print('Original list:', list_1)
# print('Sum of all numbers:', sum([x for x in list_1 if type(x) == int]))
# print('All words with "a":', [y for y in list_1 if type(y) == str and "a" in y])



# 3.3. Превратите лист ['cat', 'dog', 'horse, 'cow'] в кортеж
# list_1 = ['cat', 'dog', 'horse', 'cow']
# tuple_1 = tuple(list_1)
# print(type(tuple_1))


# 3.4. Напишите программу, которая определяет, какая семья больше.
#       1) Программа имеет два input() - например, family_1, family_2.
#       2) Членов семьи нужно перечислить через запятую.
#      Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')
#
#ПЕРВОЕ РЕШЕНИЕ:
# family_1 = input('Члены первой семьи: \n').split(',')
# family_2 = input('Члены второй семьи: \n').split(',')
# family_1_members = len(family_1)
# family_2_members = len(family_2)
# print(f'В первой семье {family_1_members} чл')
# print(f'Во второй семье {family_2_members} чл')
# if family_1_members > family_2_members:
#     print('Первая семья больше')
# elif family_2_members > family_1_members:
#     print('Вторая семья больше')
# else:
#     print('Семьи равны')

#ВТОРОЕ РЕШЕНИЕ
# fam1 = input('family_1: ')
# fam2 = input('family_2: ')
# tuple1 = tuple(fam1.split(','))
# tuple2 = tuple(fam2.split(','))
# print(tuple1)
# print(tuple2)
# if len(tuple1) > len(tuple2):
#     print(tuple1)
# elif len(tuple1) < len(tuple2):
#     print(tuple2)
# else:
#     print('Equal')


# 3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
#     о вашем любимом фильме.
#     - распечатайте только ключи
#     - распечатайте только значения
#     - распечатайте пары ключ - значение

#ПЕРВОЕ РЕШЕНИЕ
# film = {'title': 'Titanic',
#         'director': 'Cameron',
#         'year': '1997',
#         'budget': '200 million',
#         'main_actor': 'DiCaprio',
#         'slogan': 'my heart'}
# print(*film.keys())
# print(*film.values())
# print(*film.items())

#ВТОРОЕ РЕШЕНИЕ
# for x in film:
    # print(x)
    # print(film[x])
#
# for x, y in film.items():
#     print(x, y)



#
# 3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
#
# my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# sum_dic = sum(my_dictionary.values())
# print(sum_dic)
#
#
# sum_dic = (sum(my_dictionary[item]for item in my_dictionary))
# print(sum_dic)

# print(sum(my_dictionary.values()))   - ЛУЧШЕЕ РЕШЕНИЕ



# 3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
# #
# list_2 = [1, 2, 3, 4, 5, 3, 2, 1]
# ints_list_3 = list(set(list_2))
# print(*ints_list_3)


# 3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
#      - найдите значения, которые встречаются в обоих множествах
#      - найдите значения, которые не встречаются в обоих множествах
# #      - проверьте являются ли эти множества подмножествами друг друга
# set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}
# set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
# print(set1.intersection(set2))
# print(set1.difference(set2))
# print(set2.issuperset(set1))
# print(set1.issuperset(set2))
# print(set1.issubset(set2))

#ВТОРОЕ РЕШЕНИЕ
# i = set1.intersection(set2)
# l = (set2^set1)
# b = set1.difference(set2)
# c = set1.issubset(set2)
#
# print(i)
# print(l)
# print(b)
# print(c)









