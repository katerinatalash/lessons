# dict1 = {}
# print(type(dict1))

# d = dict(short = 'dict', long = 'dict')
# print(d)


#dict1 ={









# person = {
#     'name': 'Will Smith',
#     'age': 20,
#     'profession': 'actor'
# }

# person['height'] = 180
# person['age'] = 40
# person['planet'] = 'Mars'
# person2 = {'rase': 'troll'}
# person.update(person2)     # обновляет словарь
# person.pop('race')   # удаляет элемент по ключу
# c = person.get('name')  # выводит значение по ключу

# a = person.copy()

# person.setdefault(7) # создает новую пару ключ: значение, но если такое значение есть,
# # ничего не произойдет
# print(person)


# print(person.values())
# print(person.keys())
# print(person.items())


# dict1 = {}
# dict1['one'] = [1, 2, 3]
# dict1['two'] = [4, 5, 6]
# print(len(dict1))

# for key in person:
#     print(key)

# for value in person.values():
#     print(value)























# rooms = {'bathroom', 'hall', 'bedroom'}
# print(type(rooms))

# set1 = set()
# a = 10
# c = 'str'
# d = True
# set1.add(a)
# set1.add(c)
# set1.add(d)
# print(set1)


# set_1 = {9, 8, 4, 4, 4 , 4, 3}
# set_1.clear()
# set_2 = set_1.copy()
# print(len(set_1))




from turtle import update


# print('Problem 0')
# dates_of_birth = {3,10,11,13,31,21,1,7,10,3,5,6,6}
# dates_of_birth.discard(7)
# print(dates_of_birth)

# print('\nProblem 1')
# farm_1 = {'dog', 'cat', 'mouse', 'sheep'}
# farm_2 = {'cow', 'horse', 'donkey', 'cat', 'dog'}
# print(farm_1.intersection(farm_2))

# print('\nProblem 2')
# farm_1 = {'dog', 'cat', 'mouse', 'sheep'}
# farm_2 = {'cow', 'horse', 'donkey', 'cat', 'dog'}
# print(farm_2.difference(farm_1))

# print('\nProblem 3')
# set1 = {1, 2, 3, 4, 5}
# set1.add(6)
# print(set1)
# set1.pop()
# print(set1)


# print('\nProblem 000')
# menu = {'lagman': 120, 'plov': 120, 'borsh': 100}

# menu['besh_barmak'] = 130
# menu1 = {'lagman': 135}
# menu.update(menu1)
# menu.pop('borsh')
# print(menu)


# print('\nProblem 10')
# menu = {'lagman': 120, 'plov': 120, 'borsh': 100}
# menu.setdefault( 'drinks', ['cola',  'fanta',  'sprite'])
# print(menu)

# print('\nProblem 20')
# set1 = {'add', 'update', 'intersection', 'remove', 'difference', 'clear', 'discard', 'pop'}
# set2 = {'clear', 'get', 'keys', 'values', 'items', 'update'}
# print(set1.intersection(set2))

# print('\nProblem 31')
# dic1 = {}
# i = 1
# while i <= 3:
#     a = input('Name:  ')
#     b = input('Login:  ')
#     i += 1
#     dic1.setdefault(a, b)
#     print(dic1)

# print('\nProblem 27')
# dic1 = {
#     'Kate': 'doctor',
#     'Ann': 'teacher',
#     'Kris': 'artist',
#     'Jane': 'singer',
#     'Emma': 'lawyer'
# }
# for keys, values in dic1.items():
#     print(f'Hello {keys}, greate profession {values}')

# print('\nProblem 22')
# set1 = set()
# i = 1
# while i <= 10:
#     a = int(input('Number: '))
#     i += 1
#     set1.add(a)
# print(set1)
# print(tuple(set1))


# print('\nProblem 11')
# south_american_countries = ['Argentina', 'Bolivia', 'Brazil', 'Chile', 'Colombia',
# 'Ecuador', 'Guyana', 'Paraguay', 'Peru', 'Suriname', 'Suriname', 'Uruguay', 'Venezuela']
# set1 = set(south_american_countries)
# list1 = list(set1)
# print(list1)



# print('\nProblem 101')
# suitcase = []
# i = 1
# while i <= 5:
#     a = input('Take with:   ')
#     suitcase.append(a)
#     i += 1
# print(suitcase)

# suitcase.pop(4)
# print(suitcase)


# print('\nProblem 101')
farm_1 = {'dog', 'cat', 'mouse', 'sheep'}
farm_2 = {'cow', 'horse', 'donkey', 'cat', 'dog'}
for i in farm_2:
    farm_1.add(i)
print(farm_1)
