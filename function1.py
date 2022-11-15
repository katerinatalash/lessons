# def print_text():
#     print('Hello world')
# print_text()


# def sum_number():
#     num1 = 10
#     num2 = 20
#     return 10 + 20
# print(sum_number())



# def sum2(a:int, b:int) -> int:
#      return a + b
# print(sum2(120, 210))
# sum_result = sum2(30, 12)
# print(sum_result)



# def my_len(arr:list) -> int:
#     count = 0
#     for i in arr:
#         count += 1
#     return count

# list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# result = my_len(list)
# print(result)




# a = ['Bishkek', 'Osh', 'Kant']

# def list_city(city_arr: list):
#     for i in city_arr:
#       print(i)

# def add_city():
#     new_city = input('Enter new city name: ')
#     if new_city in a:
#         print('Такой город есть')
#         list_city(a)
#     else:
#         a.append(new_city)
#         print('Город добавлен')
#         list_city(a)

# def main():
#     command = input('добавить/отобразить/выход: ')
#     if command == 'добавить':
#         add_city()
#     elif command == 'отобразить':
#         list_city(a)
#     elif command == 'выход':
#         exit()

# while True:
#     main()




# a = 10
# def prnt(c):
#     b = 20
#     return c + b + a

# result = prnt(4343)
# print(result)
# print(a)




# def a(b):
#     return b**2
# print(a(2))



# print('My work 1')

# list_1 = ['name', 'age', '1', '19']

# def rasdel(arr: list) -> list:
#     seredina = len(arr) // 2
#     l1 = arr[0:seredina][::-1]
#     l2 = arr[seredina:][::-1]
#     return l1 + l2

# print(rasdel(list_1))

# print('My work 2')

# fibonachi = [0, 1]

# def fibo(arr:list):
#     a = 0
#     b = 1
#     while a < 20:
#         summ_fib = arr[a] + arr[b]
#         arr.append(summ_fib)
#         a += 1
#         b += 1        
#     return arr

# print(fibo(fibonachi))



# print('My work 3')

# def sumn(a, b):
#     return a + b

# def vich(a, b):
#     return b - a

# def funk():
#     a = int(input('Enter a: '))
#     b = int(input('Enter b: '))
#     if a > b:
#         print(sumn(a,b))
#     elif b > a:
#         print(vich(a, b))
#     else:
#         print("Zero")
# funk()





# print('My work 4')

# def fale_name(a):
#     return a + '.py'

# def sozdat_fale():
#     a = input('Enter name fale:  ')
#     with open(fale_name(a), 'w') as f:
#         print('ok')
# var1 = sozdat_fale
# var1()


# from random import choice
# def generator(arr:list):
#     numb = ''
#     while len(numb) < 6:
#         choice1 = choice(arr)
#         numb += choice1
#     return numb

# def gen_number():
#     print(f'0444{generator("145790")}')

# gen_number()  
# gen_number()  
# gen_number()  




# # from itertools import product
# # a = "145790"
# # [print(''.join(i)) for i in product(a, a, a ,a ,a ,a)]



# a = '145790'
# i = 0
# while i<999999:
#     good = True
#     for c in str(i):
#         if c not in a:
#             good = False
#     if good:
#         print(str(i).zfill(6))
#     i+=1





