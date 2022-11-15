# def summa1(a ,b):
#     return f"{a} + {b} = {a + b}"
# print(summa1(1, 2))


# def square(x , n=2):
#     return x ** n
# print(square(12, 1))


# def login(name, age):
#     return f'Ваше имя {name}, вам {age} лет'
# imya = input('Введи имя: ')
# god = input('Введи возраст: ')
# print(login(imya, god))



# def file(text):
#     with open(text, 'w')as f:
#          f.write('blablabla')
# text = input('Введи текст: ')
# file(text)



# def func(*args):
#    return type(args)
# print(func(1,2,3,4,5,6,7,8,9))


# def func(**kwargs):
#    return kwargs, type(kwargs)
# print(func(name='azat', age = 17))




# def chet_nechet(x):
#     if x % 2 == 0:
#          return f'{x} - четное'
#     else:
#         return f'{x} - не четное'
# while True:
#     numb = int(input('>>>'))
#     print(chet_nechet(numb))



# def chetnoe(x):
#     if x % 2 ==0:
#         return True 
#     return False
# print(chetnoe(9))

# for i in range(1,20):
#     if chetnoe(i):
#         print(f'{i} - четное')
#     else:
#         print(f'{i} - не четное')


# def gen_number():
#     from random import choice
#     num = '0444'
#     for a in range(6):
#         num += choice('145790')
#     return num
# for i in range(10):
#     print(i+1, f'Ваш номер телефона: {gen_number()}')



