






























print('\nWork 1')
lang1 = 'go'
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
for i in languages:
    if i == lang1:
        print("This language is in list")

print('\nWork 2')
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
for i in languages:
    if i == 'php':
        break
    print(i)

print('\nWork 3')
a = 7
b = 0
while b < 5:
    a *= a
    b += 1
    print(a)


a = 7
for i in range(5):
    a*=a
    print(a)


print('\nWork 4')
languages = ['go', 'java', 'php', 'python', 'javascript', 'ruby']
for i in languages:
    index = languages.index(i)
    print(f'{index} {i}')

print('\nWork 5')
a = 0
b = 10
while a < b:
    a += 1
    print(a)
a = 0
while a < b - 1:
    b -= 1
    print(b)


print('\nWork 6')
names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават',
 'Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан')
for i in names:
    index = names.index(i)
    if index % 2 == 0:
        print(f'{index} {i}')

print('\nWork 7')
names = ('Максат','Лязат','Данияр','Айбек','Атай','Салават',
 'Адинай','Жоомарт','Алымбек','Эрмек','Дастан','Бекмамат','Аслан')
names1 = names[1::2]
for i in names1:
    print(i)

print('\nWork 8')
a = 17000
if -1000 < a <= -99 or 99 <= a < 1000:
    print("ok 1")
if a >= 0 and a % 2 == 0:
    print('ok 2')
if a % 31 == 0:
    print('ok 3')
if (a > 100 and a % 17 == 0) or (a > 150 and a == 13**2):
    print('ok 4')


print('\nWork 9')
a = list(range(-100, 101, 1))
print(a)
b = 0
c = 0
n = 0
for i in a:
    if i % 13 == 0 and i % 2 == 0:
        #print(i ** 2)
        b += 1
    if a.index(i) == n + 6 and i % 2 == 0:
        print(i)
        n += 7
        c += 1
#print(b)
print(c)


