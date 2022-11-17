from functools import reduce

def sum_arrs(*args):
    result = []
    for i in args:
        # print(i)
        result += i
    # print(result)
    total = 0
    for num in result:
        total += num
    return total

def sum_arrs2(arr1, arr2):
    print(arr1)
    print(arr2)
    return sum(arr1 + arr2)

def sum_arr3(arr1, arr2):
    # arr0 = arr1 + arr2
    return reduce(lambda x, y: x+y, arr1 + arr2)


def avarage_arr(arr):
    # if len(arr) == 0:
    #     return 0
    # else:
    #     return sum(arr)/len(arr)

    return sum(arr)/len(arr) if len(arr) > 0 else 0 #второй вариант

    return filter(lambda x: x)