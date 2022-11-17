# from rew_my_file import *
#
# arr1 = [6, 5, 4, 3, 2]
# arr2 = [7, 8, 9, 10, 11, 12]
#
# print(sum_arrs(arr1, arr2))
# print(sum_arrs2(arr1=arr2, arr2=arr1))
# print(sum_arr3(arr1, arr2))
#
# arr3 = [1, 4, 7, 9, 0, 4, 7]
# print(round(avarage_arr(arr3), 2))


x = 3
def new_one():
    x = 2
    print(f'inner: {x}')

print(f'Output: {x}')
new_one()
print(f'Output: {x}')