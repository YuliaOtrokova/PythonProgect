#Напишите программу, которая проверяет является ли год високосным.
# Таковыми считаются года, которые делятся без остатка на 4 (2004, 2008)
# и не являются столетиями (500, 600).
# Однако, если год делится без остатка  на 400, он также считается високосным (1200, 2000)

print('Введите год: ')
a=int(input())
if a % 4 == 0 or a % 400 ==0:
    print('Год високосный')
elif a % 100 == 0:
    print('Год високосный')
else:
    print('Год невисокосный')


# year = int(input('Введите год '))
# if (year % 4 == 0 and year % 100 != 0 or year % 400 == 0):
#     print('this is visocosnyy god')
# else:
#     print('this is not visokosnyy god')