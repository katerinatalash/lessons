# if - если
# elif - иначе если
#  else -  иначе


#a = 40
#b = 20
#c = 10
#if a != b:
#    print(False)
#elif a > c:
#    print(True)


#lang = input("Выбери язык: EN RU KG:   ")
#if lang == "EN":
#    print("Hello")
#elif lang == "RU": 
#    print("Привет")
#elif lang == "KG":
#    print("Салам")
#else:
#    print("Такого языка нет") 


#b = 3 ** 2
#a = 2 ** 3
#if a > b:
#    print("a>b")
#elif b > a:
#    print("b>a")


#age = int(input("Введите ваш возраст:   "))
#if age >= 18:
#    print("Вы можете войти", age, "лет")
#elif age < 18 and age > 12:
#    print("Вы подросток, вам нельзя", age, "лет")
#elif age < 0 and age == 0:
#    print("Что ты такое")
#else:
#    print("Ты ребенок, тебе", age, "лет") 


#login = input("Введите ваш логин:   ")
#password1 = int(input("Введите пароль:   "))
#password2 = int(input("Повторите пароль:   "))
#if password1 == password2:
#    print("Ваш логин:", login, ", ", "Ваш пароль:", password1)
#else:
#    print("Пароль неверный")


#num1 = int(input("Enter number 1:   "))
#num2 = int(input("Enter number 2:   "))
#if num1 == num2:
#    print("Числа равны", num1, "=", num2)
#elif num1 > num2:
#    print(num1, ">", num2)
#elif num1 < num2:
#    print(num1, "<", num2)


#num1 = int(input("Введи число:   "))
#a = 2
#if num1 == a:
#    print(a * num1)
#elif num1 == 3:
#    print(a * num1)
#elif num1 == 4:
#    print(a * num1)
#else:
#    print("Введи нормально") 


#a = 5
#b = 3
#if a < b:
#    ptint(True)
#else:
#    print(False)


#a = input("Выбери действие: + - / *:")
#num1 = int(input("Введи первое число:   "))
#num2 = int(input("Введи второе число:   "))
#if a == "+":
#    print(num1 + num2)
#elif a == "-":
#    print(num1 - num2)
#elif a == "/":
#    print(num1 / num2)
#elif a == "*":
#    print(num1 * num2)
#else:
#    print("Такого действия нет")


#a = 10
#b = 10
#c = 5
#if a > c and b > c:
#    print("OK")
#else:
#    print("NE OK")


#a = 10
#b = 40
#c = 25
#if a > c or b > c:
#    print(True)
#else:
#    print(False)


#b = 5
#if b % 2 == 0:
#    print("Число четное")
#else:
#    print("Число не четное")


#САМОСТОЯТЕЛЬНАЯ РАБОТА

print("\nProblem 1")
a = 2 ** 3
b = 3 ** 2
if a > b:
    print("a>b")
elif b > a:
    print("b>a")
else:
    print("a=b")


print("\nProblem 2")
a = int(input("Введите число:    "))
if 0 <= a <= 21 or 57 <= a <= 100:
    print("Разрешенный диапазон")
elif 21 < a < 57:
    print("Запрещенный диапазон")
else:
    print("Запрещенное число")


print("\nProblem 3")
a = int(input("Введите число:    "))
if a % 2 == 0:
    print("Число четное")
else:
    print("Число НЕчетное")
if a % 3 == 0:
    print("Число делится на 3 без остатка")
else:
    print("Число НЕ делится на 3 без остатка")
if a**2 > 1000:
    print("Число в квадрате больше 1000")
else:
    print("Число в квадрате меньше 1000")


print("\nProblem 4")
a = 10
b = 20
if a > b or b > a:
    print(True)
else:
    print(False)


print("\nProblem 5")
a = 10 // 5
b = 10 / 5
if a == b:
    print(a + b)
else:
    print("НЕ равны")


print("\nProblem 6")
a = int(input("Введите число:    "))
b = int(input("Введите число:    "))
if a > b:
    print(b - a)
else:
    print(a - b)

print("\nProblem 7")
a = 10 
b = 5
if a > 0 and b > 0:
    print("Положительные")
else:
    print("Отрицательные")

print("\nProblem 8")
a = 10 
b = 5
if a > b:
    print(a + 2)
else:
    print(b + 2)


print("\nProblem 9")
a = int(input("Введите число:    "))
if a > 0:
    print("Положительное число")
elif a < 0:
    print("Отрицательное число")
else:
    print("a")

print("\nProblem 10")
age = int(input("Введите возраст:    "))
if age >= 18:
    print("Совершеннолетний")
elif age <= 4:
    print("Ребенок")
else:
    print("Несовершеннолетний")


print("\nProblem 11")
a = 45
b = 6
if a % b == 0:
    print("yes")
else:
    print("no")


print("\nProblem 12")
year = int(input("Введите год:    "))
if year == 2022:
    print("Текущий год")
elif year < 2022:
    print("Год прошел")
else:
    print("Год еще не наступил")


print("\nProblem 13")
year = int(input("Введите год рождения:    "))
age = 2022 - year
if age >= 18:
    print("Совершеннолетний")
elif age <= 4:
    print("Ребенок")
else:
    print("Несовершеннолетний")


print("\nProblem 14")
a = 4
b = 6
c = 8
if a > b and a > c:
    print("a max")
elif b > a and b > c:
    print("b max")
else:
    print("c max")
if a < b and a < c:
    print("a min")
elif b < a and b < c:
    print("b min")
else:
    print("c min")


print("\nProblem 15")
a = 17391
b = 546
c = 934
a1 = 17391 % 17
b1 = 546 % 17
c1 = 934 % 17
if a1 < b1 and a1 < c1:
    print("a% min")
elif b1 < a1 and b1 < c1:
    print("b% min")
else:
    print("c% min")
print(a1, b1, c1)


print("\nProblem 16")
x = 13
if 13**2 < 172:
    print((13**2)**2)
else:
    print(13**2)