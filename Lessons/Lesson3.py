## LISTS
#Create a list:
# l = [1, 'string', 12.3, 'Hello', 25]
# print(l)

# # Create a list: option 2
# sentence = 'What a wonderful life!'
# # my_list = list(sentence)
# # print(my_list)
# my_list1 = sentence.split(' ')
# # print(my_list1)
# print(my_list1[-1])

# For loop with list
# numbers = [1, 2, 3, 4, 5]
# for num in numbers:
#     print(num*2)

# In-place list mutating

l = [8, 7, 5, 10]
# print(l)
# print(id(l))
# l[0] = 0
# print((l))
# print(id(l))


# l1 = [25, 80]
# l.append(l1)
# print(l)
# print(id(l))
# print(l[-1][0]

# .append and .extend()
# add = 'extra'
# l.append(add)
# l1.extend(add)
# print(l)
# print(l1)

# .sort() and sorted()

nums = [2, 3, 1, 5, 6, 4, 0]
print(f'Initial list: {nums}')
print(id(nums))
#
print('SORTED()')
print(f'New sorted list: {sorted(nums)}')
print(f'Initial list after sorting: {nums}')
print(id(sorted(nums)))
print('.SORT()')
print(f'New sorted list: {nums.sort()}')  # None
print(f'Initial list After sorting: {nums}')
print(id(nums))
print(nums.reverse())
print(nums)
print(id(nums))