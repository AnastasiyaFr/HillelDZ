# 1. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list по следующему правилу:
# Если строка стоит на нечетном месте в my_list, то ее заменить на
# перевернутую строку. "qwe" на "ewq".
# Если на четном - оставить без изменения.
# Задание сделать с использованием enumerate.## #
my_list1=["fgh","vbn","fjkli","fgh","vbn","fjkli"]
my_result1=[]
for index,symbol in enumerate(my_list1):
    if index%2:
        my_result1.append(symbol[::-1])
    else:
        my_result1.append(symbol)
print(my_result1)
# 2. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list у которых первый символ - буква "a".
# Вариант 1
my_list2=["fgh","abn","fjkli","agh","baaabn","fjali"]
my_result2=[]
for symbol in my_list2:
    if symbol[0]=="a":
        my_result2.append(symbol)
print(my_result2)
# Вариант 2
my_list2=["fgh","abn","fjkli","agh","baaabn","fjali"]
my_result2=[value for value in my_list2 if value[0]=="a" ]
print(my_result2)
# 3. Дан список строк my_list. Создать новый список в который поместить
# элементы из my_list в которых есть символ - буква "a" на любом месте.
# # Вариант 1
# my_list3=["fgh","abn","fajkli","agh","babn","fjali"]
# my_result3=[]
# for symbol in my_list3:
#     for symbol1 in symbol:
#         if symbol1=="a":
#             my_result3.append(symbol)
# print(my_result3)
# # Вариант 2
# my_list3=["fgh","abn","fajkli","agh","babn","fjali"]
# my_result3=[value for value in my_list3 if value.rfind("a")>=0]
# print(my_result3)
# Вариант 3 c in
my_list3=["fgh","abn","fajkli","agh","babn","fjali"]
my_result3=[value for value in my_list3 if "a" in value]
print(my_result3)

# 4. Дан список my_list в котором могум быть как строки (type str) так и целые числа (type int).
# Создать новый список в который поместить только строки из my_list.
# Вариант 1
my_list4=["fgh",56,"fajkli",789,"babn","fjali"]
my_result4=[]
for symbol in my_list4:
    if type(symbol)==str:
            my_result4.append(symbol)
print(my_result4)
# Вариант 2
my_list4=["fgh",56,"fajkli",789,"babn","fjali"]
my_result4=[value for value in my_list4 if type(value)==str ]
print(my_result4)
# 5. Дана строка my_str. Создать список в который поместить те символы из my_str,
# которые встречаются в строке только один раз.
my_str5="wsaafddff"
setmystr5=set(my_str5)
my_result5=[value for value in setmystr5 if my_str5.count(value)==1]
print(my_result5)
# 6. Даны две строки. Создать список в который поместить те символы,
# которые есть в обеих строках хотя бы раз.
# Вариант 1
my_str6_1="wsaafddffhjk"
my_str6_2="wsaafddff"
my_result6=[value for value in my_str6_1 if my_str6_2.count(value)>=1]
print(set(my_result6))
# Вариант 2
my_str6_1="wsaafddffhjk"
my_str6_2="wsaafddff"
my_set6_1=set(my_str6_1)
my_set6_2=set(my_str6_2)
my_result6=my_set6_1.intersection(my_set6_2)
print(list(my_result6))
# 7. Даны две строки. Создать список в который поместить те символы, которые есть в обеих строках,
# но в каждой только по одному разу.
my_str7_1="wsaafddffhjk"
my_str7_2="wsaafddff"
my_result7=[value for value in my_str7_1 if my_str7_2.count(value)==1 and my_str7_1.count(value)==1]
print(set(my_result7))
#Не уверена что Вы это имели ввиду
my_str7_1="wsaafddffhjk"
my_str7_2="wsaafddff"
my_str7set=set(my_str7_1).intersection(set(my_str7_2))
my_result7=[value for value in my_str7set if (my_str7_2+my_str7_1).count(value)==2]
print(my_result7)

# 8. Описать с помощью словаря следующую структуру для конкретного человека (можно придумать):
# Фамилия
# Имя
# Возраст
# Проживание
#     Страна
#     Город
#     Улица
# Работа
#     Наличие
#     Должность
person={"Фамилия":"Иванов",
        "Имя":"Петр",
        "Возраст":33,
        "Проживание":{
            "Страна":"Украина",
            "Город":"Днепр",
            "Улица":"Красная"}    ,
        "Работа":{"Наличие":True,
             "Должность":"Плотник"}}
print(person)
# 9. Описать с помощью словаря следующую структуру (рецепт ненастоящего торта,
# придумать и указать граммы для продуктов):
# Составляющие
#     Коржи
#         Мука
#         Молоко
#         Масло
#         Яйцо
#     Крем
#         Сахар
#         Масло
#         Ваниль
#         Сметана
#     Глазурь
#         Какао
#         Сахар
#         Масло
recept={"Коржи":{
            "Мука":500,
            "Молоко":200,
            "Масло":100,
            "Яйцо":3},
         "Крем":{
            "Сахар":250,
            "Масло":100,
            "Ваниль":10,
            "Сметана":900},
        "Глазурь":{
             "Какао":50,
             "Сахар":100,
             "Масло":100}}
print(recept)