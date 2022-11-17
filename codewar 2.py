# for i in range (1, 20):
#     if i % 3 == 0 and i % 5 == 0:
#         print('FizzBuzz')
#     elif i % 3 == 0:
#         print('Fizz')
#     elif i % 5 == 0:
#         print('Buzz')
#
#     else:
#         print(i)

n = 100
f0 = 0
f1 = 1
for i in range(0, n+1):
    fib = f0 + f1
    f0 = f1
    f1 = fib
    print(fib)
