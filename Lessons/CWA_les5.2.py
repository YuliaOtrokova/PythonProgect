# 1 задача

# a = 'code'
# b = 'wa.rs'
# name = a + b
# print(name)

# 2 задача

# def number_to_string(num):
#    return str(num)

# 3 задача

# def string_to_number(s):
#     return int(s)

# 4 задача

# def get_sum_of_digits(num):
#     a = str(num)
#     sum = 0
#     # sum = None
#     # digits = list(num)
#     for x in a:
#         sum += int(x)
#     return sum
# print(get_sum_of_digits(123))

# 5 задача

# def make_upper_case(s):
#     return s.upper()

# 6 задача

# def switcheroo(s):
#     # x = a
#     # a = b
#     # b = x
#     return s.replace('a', 'x').replace('b', 'a').replace('x', 'b')

# 7 задача

# def solve(s):
#     countUpper = 0
#     countLower = 0
#     for i in s:
#         if i==i.upper():
#             countUpper +=1
#         else:
#             countLower += 1
#     if countUpper <= countLower:
#         s = s.lower()
#     else:
#         s = s.upper()
#     return s


# 8 задача

# def solution(string):
#     return string[::-1]
#     #new = list(string)
#     #new.reverse()
#     #return ''.join(new)

# 9 задача


# 10 задача

# def is_lucky(n):
#     return n%9 == 0

# 11 задача

# def sale_hotdogs(n):
#     if n<5:
#         return n*100
#     elif n>5 and n<10:
#         return n*95
#     else:
#         return n*90
#       # return n*90 if n>=10 else 95*n if n>=5 and n<10 else 100*n

# 12 задача
#
# def final_grade(exam, projects):
#     if exam > 90 or projects > 10:
#         return 100
#     elif exam > 75 and projects >=5:
#         return 90
#     elif exam > 50 and projects >=2:
#         return 75
#     else:
#         return 0

# 13 задача
# def double_char(s):
#     a = ""
#     for i in s:
#         i = i*2
#
# второй вариант
# def double_char(s):
#     return ''.join(map(lambda x:x*2, s))

# def double_char(s):
#     return ''.join([x*2 for x in s])

# 14 задача
# def function(start_num, end_num):
#     l1 = []
#     for i in range(start_num +1, end_num):
#         l1.append(i)
#     return l1

#второй вариант
# def function(start_num, end_num):
#     return list(range(start_num +1, end_num))

# 15 задача
# def check(seq, elem):
#     return elem in seq

# 16 задача
def filter_lucky(lst):
    ar = []
    for el in lst:
        if '7' in str(el):
            ar.append(el)
    # return [el for el in lst if '7' in str(el)]