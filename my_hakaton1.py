# a = input('Enter action: +,-,/,*,**, //,%:    ')
# num1 = int(input('Enter number 1: '))
# num2 = int(input('Enter number 2: '))
# if a == '+':
#     print(num1 + num2)
# elif a == '-':
#     print(num1 - num2)
# elif a == '/':
#     print(num1 / num2)
# elif a == '*':
#     print(num1 * num2)
# elif a == '**':
#     print(num1 ** num2)
# elif a == '//':
#     print(num1 // num2)
# elif a == '%':
#     print(num1 % num2)
# else:
#     print("Wrong action")


# a = [1, 1, 2, 3, 13, 13, 13, 13, 13, 13, 13, 13, 13, 5, 8, 13, 21, 34, 1, 55, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 13, 1313, 13, 13, 13, 13, 13, 89]
# a.append(13)
# print(a)
# b = a.count(13)
# print(b)
# print(len(a))
# c = b * 100/len(a)
# if c > 70:
#     print('НЕУЖЕЛИ')
# elif c < 70:
#     print('Я ТАК И ЗНАЛ')
# else:
#     print('СОВПАДЕНИЕ')


# users = []
# a = 0
# while a < 2:
#     log1 = int(input('Enter login: '))
#     pas1 = int(input('Enter password: '))
#     users.append((log1, pas1))
#     a += 1
# print(users)
# log2 = int(input('Enter login: '))
# pas2 = int(input('Enter password: '))
# for i in users:
#     if (log2, pas2) == i:
#         print('Добро пожаловать')
#         break
# else:
#     print('Неверный логин или пароль')




# dict1 = {'a': 5, 'b': 3, 'c': 8, 'd': 15}
# # b = list(dict1.keys())
# # c = list(dict1.values())
# # print(b)
# # print(c)
# # for i in c:
# #     if i % 3 == 0: 
# #         ind = c.index(i)
# #         print(f'{b[ind]} = Hi')
# #     if i % 5 == 0:
# #         ind = c.index(i)
# #         print(f'{b[ind]} = Bye')
# for key, value in dict1.items():
#     if value % 3 == 0:
#         print(f'{key} = Hi')
#     if value % 5 == 0:
#         print(f"{key} = Bye")


# languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
# a = 0
# for i in languages:
#     print(f'{a} {i}')
#     a += 1

# sum1 = 0
# for i in range(1,1001):
#     if i % 3 == 0 or i % 5 ==0:
#         sum1 += i
# print(sum1)
    


# a = '4729461084'
# b = ''.join(a)
# c = list(b)
# sum1 = 0
# for i in c:
#     d = int(i)
#     sum1 += d
# print(sum1)
    
# from datetime import datetime   
# # date1 = input('Enter date: ')
# date1 = '2022-12-22 22:12'
# # 'Enter date if format YYYY-MM-DD HH:MM'
# date2 = datetime.strptime(date1, "%Y-%m-%d %H:%M")
# print(date2)
# out = {}
# out['year'] = date2.year
# out['month'] = date2.month
# out['day'] = date2.day
# out['minute'] = date2.minute
# out['second'] = date2.second
# print(out)



# words = ['Anna', 'civic', 'kayak', 'Level', 'Madam', 'Mom', 'Noon', 'Racecar', 'Radar', 'еще', 'кабак', 'шалаш', 'лишил','language', 'which', 'means', 'vendor', 'слова', 'фраза', 'введите', 'слово', 'кнопк    у']
# for i in words:
#     a = i.lower()
#     if a == a[::-1]:
#         print(i)

citylist = []
while True:
    do1 = input('''Выберите действие:
    1. Добавить новый город
    2. Отобразить список городов
    3. Заменить город
    4. Удалить город
    5. Выход
    ''')
    if do1 == '1':
        do2 = input('Введите название города: ')          
        if do2 not in citylist and do2.isalpha():
            citylist.append(do2)
            print('Город добавлен')
        elif do2 in citylist and do2.isalpha():
            print('Такой город уже есть!')
        else:
            print("Некорректное значение")
    elif do1 == '2':
        a = 1
        print('Список городов:')
        for i in citylist:
            print(f'{a}. {i}')
            a += 1
    elif do1 == '3':
        a = input('Текущий город: ')
        b = input('Новый город: ')
        if a not in citylist and a.isalpha():
            print('Текущий город отсутствует') 
        elif b in citylist and b.isalpha():
            print('Такой город уже есть!') 
        elif a in citylist and b not in citylist:
            ind = citylist.index(a)
            citylist[ind] = b
            print('Город заменен') 
        else:
            print("Некорректное значение")
    elif do1 == '4':
        c = input('Введите название города: ')
        if c not in citylist and c.isalpha():
            print('Текущий город отсутствует') 
        elif c in citylist:
            ind = citylist.index(c)
            citylist.pop(ind)
            print('Город удален') 
        else:
            print("Некорректное значение")
    elif do1 == '5':
        break



    
