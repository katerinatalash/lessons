#int = -8 8
#float = 3.14
#bool = True and False
#str = "наша строка"


#print("Hello 'world'")
# str1 = """stroka1
# stroka2
#     lknjnj
#     mkkmkmkm"""
# print(str1)


# str2 = "Kakaya-to stroka    \nPerenos stroki \nTrety stroka   \n Stroka"
# print(str2)


# hello = "HELLO WORLD".lower()
# print(hello.upper())


# name = input("Your name:    ").lower()
# text = f'Hello {name}, i am your code'
# print(text)

# text1 = "something"
# print(text1.capitalize())
# print(text1.title())

# name = input("Enter your name:   ").lower()
# # print(name.startswith('ba'))
# # print(name.endswith('bek'))

# if name.startswith('a') and name.endswith('k'):
#     print("Your name start A and end K")
# else:
#     print("Other name")


# text = '        mir trud may     '.strip().upper()
# print(text)

# text = 'mir trud may'
# text2 = '//'.join(text)
# print(text2)

# text = 'mir trud may may may may may'
# print(text.count('may'))

# text = 'somethtext'
# print(text.isalpha())
# int1 = '112455'.isdigit()
# print(int1)

# text = 'Somethtext'.split('t')
# print(len(text))
# print(text)

# password1 = input('Your password:  ')
# password2 = input('Repeat password:  ')

# if not password1.isalpha() and not password1.isdigit() and len(password1) >= 8 and password1 == password2:
#     print(f'Good password:  {password1}')
# else:
#     print('Wrond password')


# password1 = input('Your password:  ')
# if not password1.isalpha() or password1.isdigit():
#     print(f'Wrong password')
# else:
#     print(f'Good password:  {password1}')


# text = "hellt"
# print(text.replace('t', 'o'))


# a = 'hello'
# b = 'world'
# c = 123
# print(a + b + str(c))

# print('a' + 'b' + 'c')



# str2 = 'bla bla bla'.split()
# str1 = '|'.join(str2)
# print(str1)
# print(len(str2))
# str3 = 'blablabla'
# print(str3.replace('bla', 'hello world'))

# a = 'asd'. center(100)
# print(a)



print('WORK')

print('\nProblem 0')
a = 'I dont know what i do,'
b = 'but i do!'
print(a.lower(), b.upper())


print('\nProblem 1')
c= True
print(str(c))


print('\nProblem 2')
text1 = 'GitHub'
text = input('Write simvol: ')
if text == 'G' or text == 'i' or text == 't' or text == 'H' or text == 'u' or text == 'b':
    print(text1.split(text))
else:
    print('Wrong simvol')

print('\nProblem 3')
srt1 = 'Ботнер IPStorm, в который ранее входили лише Windows-машины, увеличился до 135000 зараженных систем'
print(srt1.replace('е', '3'))

print('\nProblem 4')
a = input('Your name: ')
b = input('Your age: ')
c = input('Film: ')
print(f'Hello {a}, {c} is very good choice')


print('\nProblem 5')
gh = 'Googleс оздаст специальную коменду для поиска багов в особо важных приложениях'
print(gh.split())
print(len(gh.split()))

print('\nProblem 6')
text = 'Самые важные события в мире инфосека за сентябрь'
print('|'.join(text))

print('\nProblem 7')
text = 'хакеры слили в сетьданные пакистанской энергетичексой компании k-Elektric'
print(text.title())



