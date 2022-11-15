# list1 = []
# print(type(list1))

# list2 = [123, 3.14, 'name', True, [1, 2, 3]]



# list1 = ['valentina', 'adilet', 'akan', 'azim', 'altynai', 'kaynush',
# 'tima', 'suyunt', 'adil', 'samat', 'azamat']
# start stop step
# list1.append('dog')
# print(list1)
# print(list1[-3:-7:-1])
# print(list1[-1::-2])
# print(list1.index('azim'))

# print(list1[start:stop:step])


# list2 = []
# list2.append('john')
# list2.append('bob')
# list2.append('sveta')
# list2.append('alina')
# list2.append('gennadiy')

# name = input('Enter u name:')
# list2.append(name)
# print(list2)



# list1 = ['valentina', 'adilet', 'akan', 'azim', 'altynai', 'kaynush', 
# 'tima', 'suyunt', 'adil', 'samat', 'azamat', 'samat']
# list2 = ['bakai', 'azat', 'bektur', 'nik']
# list1.extend(list2)
# print(list1)
# print(list2)

# list1.remove('tima')
# list1.pop(5)
# print(list1)



# list1 = ['valentina', 'adilet', 'akan', 'azim', 'altynai', 'kaynush', 
# 'tima', 'suyunt', 'adil', 'samat', 'azamat', 'samat']

# mid = len(list1)//2
# print(mid)
# print(list1[:mid:2])





# names = []
# name1 = input('enter name1: ')
# name2 = input('enter name2: ')
# name3 = input('enter name3: ')
# name4 = input('enter name4: ')
# name5 = input('enter name5: ')
# name6 = input('enter name6: ')

# names.extend([name1, name2, name3, name4, name5, name6])
# print(names)



# list1 = ['valentina', 'adilet', 'akan', 'azim', 'altynai', 'kaynush', 
# 'tima', 'suyunt', 'adil', 'samat', 'azamat', 'samat']

# name = input('enter name:  ')
# if name in list1:
#     list1.remove(name)
#     print(f'Name {name} was delete')
# else:
#     print(f"there is no name {name}")

# a = ', '.join(list1)
# print(a)





# names = [('Alex', 19), ('Sultan', 22)]
# name = input('enter name:  ')
# age = int(input('enter age:  '))

# names.append((name, age))
# print(names)


# list1 = ['valentina', 'adilet', 'akan', 'azim', 'altynai', 'kaynush', 
# 'tima', 'suyunt', 'adil', 'samat', 'azamat', 'samat']

# tuple1 = tuple(list1)
# list2 = list(tuple1)
# print(list2)

# a = list(range(0, 100, 4))
# print(a)
# print(a[-1::-5])
# b = list(range(16, 100, 20))
# print(b)


# list1 = [1,3,6,5,4,10,7,8]
# print(list1[0] + list1[5])
# list1.reverse()
# list1.sort()
# print((list1))
# print(list1)




from matplotlib.patches import Ellipse


print('Problem 0')
tuple1 = (1, 2, 3)
tuple2 = ('as', 'gh', 'jk')
tuple3 = (5, 69, 89)
tuple4 = ('jhh', 'jnjj')
tuple5 = (23, 'gughh')
list1 = [tuple1, tuple2, tuple3, tuple4, tuple5]
print(list1)


print('\nProblem 1')
tuple1 = (1, "tyu", 789)
print(tuple1[1])
print(tuple1[0])
print(tuple1[2])


print('\nProblem 2')
list1 = [584, 58.6, 'hello', (1,2,3), [67, 979]]
print(list1)


print('\nProblem 3')
list1 = ['Kate', 'Anna', 'Liza', 'Daria', 'Emma']
list2 = ', '.join(list1)
print(list2)

print('\nProblem 4')
list1 = ['hhgh', 'hbhbhb', 'jjjh']
list2 = ['jjjh', 'bhhjhhb', 'jhjbgv']
#list1.append(list2)
#print(list1)
list1.extend(list2)
print(list1)


print('\nProblem 5')
name = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  
'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 
'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon',]
print(name.count('Jack'))

print('\nProblem 6')
name = ['Jack', 'Jimmy', 'Jackson', 'Jhon', 'Jackson', 'Jhon',  
'Jimmy', 'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 
'Jackson', 'Jhon','Jack', 'Jimmy', 'Jack', 'Jackson', 'Jhon', 'Oskar']
name.remove('Oskar')
print(name)

print('\nProblem 7')

#name = input('Name: ')
#age = input('Age: ')
#its = input('ITC: ')
#list1 = [name, age, its]
#print(list1)

print('\nProblem 8')
pythonList = ["int", "str", "bool", "if", "else", "elif", "loop", "tuple", "list", "None", True, False]
a = pythonList.index('loop')
pythonList.pop(a)
print(pythonList)

print('\nProblem 9')
numbers = [123, 321, 2, 543, 64, 463, 234, 867, 6234, 63246, 3, 43]
a = 1
for i in numbers:
    a = a * i
print(a)

print('\nProblem 10')
a = '123 text'
numbers = []
letters = []
for i in a:
    if i in 'abcdefghijklmnopqrstuvwxyz':
        letters.append(i)
    elif i in '1234567890':
        numbers.append(i)
print(letters)
print(numbers)

print('\nProblem 11')
pythonList = ["int", "str", "bool", "if", "else", "elif", "loop", "tuple", "list", "None", True, False]
print(pythonList[1:4])



print('\nWork 1')
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
for i in a:
    if i > 5:
        print(i)


print('\nWork 2')
digits = (113,118,-5,1,135,137,0,142,144,17,154,0,155,2,159,172)
for i in digits:
    print(i/9)

print('\nWork 3')
fruits = ('banana','stawberry','apple','orange','limon','ananas')
print(f'First {fruits[0]}, Last {fruits[-1]}')

print('\nWork 4')
spisok_1 = ('Lamborgini', 17, '4456', 2020, 'Paris', 'USA', 11, 23)
spisok_2 = ('Ferrari', 17, 4456, 2021, 'Paris', 'UK', 777, 23)
for i in spisok_2:
    if i not in spisok_1:
        print(i)


print('\nWork 5')
a = range(300)
for i in a:
    if i%2 == 0:
        print(i)
    if i == 237:
        break

print('\nWork 6')
numbers = [0,2,4,7,1,8,0,-3,7,0,-2,4,0,0,-1,7,-43,0,8,-3,6,9]
abc = []
for i in numbers:
    if i < 0:
        abc.append(-1)
    elif i > 0:
        abc.append(1)
    else:
        abc.append(0)
print(abc)


        
    
