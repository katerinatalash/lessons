# transport = input("Какой транспорт вы выбираете: самолет, поезд, автобус: ")

# if transport == "самолет":
#     ticket_type = input("Каким классом вы хотите лететь: эконом, бизнес: ")
#     if ticket_type == "эконом":
#         plase = input("Где вы хотите себе место: у окна, в проходе: ")
#     else: 
#         plase = "у вас свой зал"
# elif transport == "поезд":
#     ticket_type = input("Каким классом вы хотите ехать: купе, плацкарт: ")
#     if ticket_type == "купе":
#         plase = input("Выберете одно из свободных мест: 12, 58, 23: ")
#     elif ticket_type == "плацкарт":
#         plase = "В плацкарте мест не осталось"
#         exit()
# elif transport == "автобус":
#     ticket_type = input("Как вы хотите ехать: сидя, стоя: ")
#     if ticket_type == "сидя":
#         plase = input("Выберете место: 6, 8, 10: ")
#     else: 
#         plase = "вы можете ехать где угодно"
# else:
#     print("Такого вида транспорта нет")

# print(f"Вы выбрали {transport}, ваше место: {plase}")





# food = input("Что закажете: шаурма, пирожок, самса: ")

# if food == "шаурма":
#     food_type = input("Какую начинку вы хотите: мясо, курица, сыр: ")
#     if food_type == "мясо":
#         wait = input("Шаурма с мясом готовится, будете ждать: да, нет: ")
#         if wait == "да":
#             a = input("Сколько возьмете:  ") 
#         else:
#             print("выберете что-то другое")
#             exit()

#     elif food_type == "курица":
#         wait = input("Шаурма с курицей готовится, будете ждать: да, нет: ")
#         if wait == "да":
#             a = input("Сколько возьмете:  ") 
#         else:
#             print("выберете что-то другое")
#             exit()


#     elif food_type == "сыр":
#         wait = input("Шаурма с сыром готовится, будете ждать: да, нет: ")
#         if wait == "да":
#             a = input("Сколько возьмете:  ") 
#         else:
#             print("выберете что-то другое")
#             exit()


# if food == "пирожок":
#     food_type = input("Какую начинку вы хотите: мясо, курица, сыр: ")
#     if food_type == "мясо":
#         wait = input("Пирожок с мясом готовится, будете ждать: да, нет: ")
#         if wait == "да":
#             a = input("Сколько возьмете:  ") 
#         else:
#             print("выберете что-то другое")
#             exit()


#     elif food_type == "курица":
#         wait = input("Пирожок с курицей готовится, будете ждать: да, нет: ")
#         if wait == "да":
#             a = input("Сколько возьмете:  ") 
#         else:
#             print("выберете что-то другое")
#             exit()


#     elif food_type == "сыр":
#         wait = input("Пирожок с сыром готовится, будете ждать: да, нет: ")
#         if wait == "да":
#             a = input("Сколько возьмете:  ") 
#         else:
#             print("выберете что-то другое")
#             exit()

# if food == "самса":
#     food_type = input("Какую начинку вы хотите: мясо, курица, сыр: ")
#     if food_type == "мясо":
#         wait = input("Самса с мясом готовится, будете ждать: да, нет: ")
#         if wait == "да":
#             a = input("Сколько возьмете:  ") 
#         else:
#             print("выберете что-то другое")
#             exit()


#     elif food_type == "курица":
#         wait = input("Самса с курицей готовится, будете ждать: да, нет: ")
#         if wait == "да":
#             a = input("Сколько возьмете:  ") 
#         else:
#             print("выберете что-то другое")
#             exit()


#     elif food_type == "сыр":
#         wait = input("Самса с сыром готовится, будете ждать: да, нет: ")
#         if wait == "да":
#             a = input("Сколько возьмете:  ") 
#         else:
#             print("выберете что-то другое")
#             exit()

# else:
#     print("Такого блюда у нас нет")    
#     exit()


# hot = input("Нужно ли разогреть: да, нет:  ")
# if hot == "да":
#     hot1 = "Разогреть"
# else:
#     hot1 = "Не разогревать"
# drink = input("Что будете пить: чай, кофе, вода: ")
# if drink == "чай":
#     dr = "напиток - чай"
# elif drink == "кофе":
#     dr = "напиток - кофе"
# elif drink == "вода":
#     dr = "напиток - воду"
# else:
#     dr = "без напитка"         

# print(f"Вы выбрали: {food} {food_type} - {a} шт, {dr}    {hot1}")



food = input("Что закажете: шаурма, пирожок, самса: ")
if food == "шаурма":
    food_type = input("Какую начинку вы хотите: мясо, курица, сыр: ")
    if food_type == "мясо" or food_type == "курица" or food_type == "сыр":
        wait = input(f"Шаурма - {food_type} готовится, будете ждать: да, нет: ")
        if wait == "да":
            a = input("Сколько возьмете:  ") 
        else:
            print("выберете что-то другое")
            exit()  
elif food == "пирожок":
    food_type = input("Какую начинку вы хотите: капуста, курица, вишня: ")
    if food_type == "капуста" or food_type == "курица" or food_type == "вишня":
        wait = input(f"Пирожок - {food_type} готовится, будете ждать: да, нет: ")
        if wait == "да":
            a = input("Сколько возьмете:  ") 
        else:
            print("выберете что-то другое")
            exit()  
elif food == "самса":
    food_type = input("Какую начинку вы хотите: джусай, курица, мясо: ")
    if food_type == "мясо" or food_type == "курица" or food_type == "джусай":
        wait = input(f"Самса - {food_type} готовится, будете ждать: да, нет: ")
        if wait == "да":
            a = input("Сколько возьмете:  ") 
        else:
            print("выберете что-то другое")
            exit()  
else:
    print("Такого блюда у нас нет")    
    exit()


hot = input("Нужно ли разогреть: да, нет:  ")
if hot == "да":
    hot1 = "Разогреть"
else:
    hot1 = "Не разогревать"
drink = input("Что будете пить: чай, кофе, вода: ")
if drink == "чай" or drink == "кофе" or drink == "вода":
    dr = f"ваш напиток {drink}"
else:
    dr = "без напитка"
                    

print(f"Вы выбрали: {food} {food_type} - {a} шт, {dr}    {hot1}")