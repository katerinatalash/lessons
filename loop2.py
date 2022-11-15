# for i in range(1, 10):
#     for j in range(20, 50, 10):
#         print(i, j)


# for i in range(1, 10):
#     for j in range(1, 11, 1):
#         print(f'{i} * {j} = {i*j}')



# lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# for i in lst:
#     for j in i:
#         print(j)


# lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# lst2 = []
# for i in lst:
#     for j in i:
#         lst2.append(j)
# print(lst2)


# lst = [[1, 2, 3], ['first', 'second', 'third'], [7, 8, 9]]
# letters = []
# numbers = []
# for i in lst:
#     for j in i:
#         if j in range(0,100):
#             numbers.append(j)
#         else:
#             letters.append(j)
# print(numbers)
# print(letters)


# lst = [[1, 2, 3], ['first', 'second', 'third'], [7, 8, 9]]
# letters = []
# numbers = []
# for i in lst:
#     for j in i:
#         if type(j) == str:
#             letters.append(j)
#         else:
#             numbers.append(j)
# print(letters)
# print(numbers)


# from time import sleep
# import time
# for h in range(24):
#     for m in range(60):
#          for s in range(60):
#             print(f'{h}:{m}:{s}')
#             sleep(0.01)








# from click import command


# while True:
#     command = input('Enter command: - +, exit:   ')
#     if command == '+':
#         num1 = int(input('Enter 1 numb:  '))
#         num2 = int(input('Enter 2 numb:  '))
#         print(f'{num1} + {num2} = {num1 + num2}')
#     elif command == '-':
#         num1 = int(input('Enter 1 numb:  '))
#         num2 = int(input('Enter 2 numb:  '))
#         print(f'{num1} - {num2} = {num1 - num2}')
#     else:
#         break
    




f = []

while True:
    num1 = input('Enter number:   ') 
    
    if num1 != 'end':
        d = int(num1)
        f.append(d)
        
    if num1 == 'end':
        a = []
        for i in f:
            a.append(str(i))
        print(', '.join(a))
       # print(', '.join([str(i) for i in f]))
        print(sum(f))
        print((sum(f)/len(f)))
        break
    
    

    
    