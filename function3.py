arr = [1,2,3,4, [5,6,7,[8,9, [10, 11], [12, 13]]], [14, 15]]

# answer = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

# res = []
# def func(arr):
#     for i in arr:
#         if type(i) == list:
#             func(i)
#         else:
#             res.append(i)
# func(arr)

# print(res)


# def func(value):
#     print(value)
#     if value < 5:
#         func(value+1)
#     # print(value)

# func(1)

# def factorial(n):
#     if n == 1:
#         return 1
#     else:
#         print(n)
#         # print(n * factorial(n-1))
#         return (n * factorial(n-1))

# print(factorial(4))


# a = lambda a, b: a + b

# print(a(10,20))
# print(a(10,20))


# f = lambda x: 'like' if x > 100 else ('gg' if x > 0 else 'dislike')


# print(f(-10))

# x = 10
# def func(x):
# result = 'like' if x > 100 else ('gg' if x > 0 else 'dislike')
# print(result)
# print(func(10))



# b = [4, 5, lambda: 'lambda', 7, 8]

# print(b[2]())



# def get_filter(a, filter=None):
#     if filter is None:
#         return a
    
#     res = []
#     for x in a:
#         if filter(x):
#             res.append(x)
#     return res

# lst = [5,3,0,-6,8,10,1]

# r = get_filter(lst, lambda x: x % 2 == 0)
# print(r)

# a = lambda x, y: x ** 2
# print(a(2,2))



# a = 0
# def recur(a):
#     a += 1
#     if a == 50:
#         return a
#     print(a, 'hello')
#     recur(a)

# recur(a)


# a = [[[[[[[[[[[[[1]]]]]]]]]]]]] 

# def rec(a):
#     if type(a) == list:
#         a = a[0]
#         print(a)
#         return rec(a)
#     else:
#         return a

# print(rec(a))


# def rec(x):
#     print(x)
#     rec(x+1)

# rec(1)


# def tagMaker(func):
#     def wrapper(*args, **kwargs):
#         print('<div>')
#         func(*args, **kwargs)
#         print('</div>')
#     return wrapper

# @tagMaker
# def printText(text):
#     print(text)
# printText('HELLO')


# def func_decorator(func):
#     def wrapper(title):
#         print('Что то делаем до вызова функции')
#         func(title)
#         print('Что-то делаем посое вызова функции')
#     return wrapper

# @func_decorator
# def some_func(title):
#     print(f'title = {title}')
# some_func('STROKA')

from time import time
def timer(func):
    def wrapper():
        start = time()
        func()
        print(time() - start)
    return wrapper

@timer
def func():
    for i in range(1, 100000):
        print(i)

func()