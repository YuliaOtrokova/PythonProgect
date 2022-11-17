# s = 'FUDDDFFFFFDDDDDD'
# 1 задача
    # from itertools import count
    #
    # def count_valleys(s):
    #     valleys = 0
    #     counter = 0
    #     is_valley = False
    #     for i in s:
    #         if i == 'U':
    #             counter +=1
    #         elif i == 'D':
    #             counter -=1
    #
    #         if counter < 0 and is_valley: # ==False
    #             is_valley = True
    #
    #         if counter == 0 and is_valley:
    #             valleys += 1
    #             is_valley = False
    #
    #     return valleys
    #
    # #DDUUDDUU
    # print(f"{2} {count_valleys('DDUUDDUU')}")

def sum_of_diff(arr):
    if len(arr) <= 1:
        return 0

    diff = []
    arr.sort(reverse=True)
    for i in range(len(arr)):
        if i + 1 < len(arr):
            t = abs(arr[1] - arr[i+1])
            diff.append(t)

    return sum(diff)

print(sum_of_diff([2, 1, 10]))




