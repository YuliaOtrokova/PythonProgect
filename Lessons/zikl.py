#Напишите программу, которая печатает введенный текст заданное количество раз, построчно.
# Текст и количество повторений нужно ввести с помощью inpit()


#while
text = input("Enter your text: ")
num = int(input('Enter the number of repetitions: '))
i = 1
while i <= num:
    print(text, end = ' ')
    i += 1

#for
message = input('text')
i = int(input('povtoreniya'))
for index in range (1):
    print(index, message)