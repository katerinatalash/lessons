# print()
# len()
# input()
# abs()
# eval()
# all()
# any()


# a = [True, True, False]
# print(all(a))


# a = [2, 4, 8, 6, 7, 4, 3]
# b = []
# for i in a:
#     if i % 2 == 0:
#         b.append(True)
#     else:
#         b.append(False)
# print(all(b))
# print(any(b))


# print(abs(-500))

 
# a = [1,2,3,4,5,6]
# a.reverse()
# print(a)

# print(min(a))
# print(max(a))
# print(sum(a))


# while True:
#     a = eval(input('>>>'))
#     print(a)


# a = [10,15,20,30,40]
# b = slice(1,2)
# print(a[b])



# a = 10 / 3
# print(round(a, 1))


# a = eval('2 + 2')
# print(a)


# print(5/0)
# try:
#     a = input('Enter 1:   ')
#     b = input('Enter 2:   ')
#     print(a / b)
# except ZeroDivisionError:
#     print('На ноль делить нельзя')
# except ValueError:
#     print('Вводи только числа')


# try:
#     a = input('Enter 1:   ')
#     b = input('Enter 2:   ')
#     print(a / b)
# except (ZeroDivisionError, ValueError, NameError):
#     print('Поймал все ошибки')
# else:
#     print('Ошибок не было')
# finally:
#     print('FINALLY')

# try:
#     print('asd' / 5)
# except Exception as e:
#     print(f'Код вырубился из-за ошибки: {e}')



# try:
#     a = [1,2,3,4,5,6]
#     print(a[10])
# except:
#     print('Такого индекса нет')



# dict1 = {
#     'key':'value'
# }
# print(dict1['sdas'])


# print('Problem 1')
# values = ('Razakov 32', 10, 1005, ['tables', 'chairs'], 23.00)
# a = []
# for i in values:
#     try:
#         set(i)
#         a.append('True')
#         # print('True')
#     except:
#         # print("Fals")   
#         a.append('Fals')
# print(a)
# print(all(a))

    
# print('\nProblem 2')
# set1 = []
# i = 1
# while i <= 5:
#     c = int(input('Enter num:  '))
#     set1.append(c)
#     i += 1
# print(set1)
# print(min(set1))


# print('\nProblem 3')
# try:
#     a = eval(input('>>>'))
#     print('Такая есть', a)
# except:
#     print('Такой функции нет')



# print('\nProblem 4')
# pro = 3.47
# sum1 = int(input('Your summ:  '))
# if sum1 >= 50000:
#     perep = sum1 * (pro/100)
#     print(round(perep, 2))
# else:
#     print("you summ too small")


# at = 10
# rin = 15
# wo = 20

# for e in range(-at, at):
#     try:
#         print(e, wo / e)
#     except ZeroDivisionError:
#         print("На ноль делить нельзя")
#     if e > 5:
#         print('at > 5')
   



# ist = []
# for i in range(10):
#     ist.append(i)
# print(ist)

# a = list(reversed(ist))
# print(a)
# sls_obj = slice(0,8)
# print(a[sls_obj])


# a = 0 
# b = 1 
# numbers = []
# while b > a and b <= 10:
#     numbers.append(b)
#     b += 1
# print(numbers)




dict1 = {'name': 'Join', 'lastname': 'Snow', 12: 'age'}
for x in dict1.keys():
    try:
        a = x + 'abc'
        print(a)
    except TypeError:
        print(str(x) + 'abc')
