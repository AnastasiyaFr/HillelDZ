# 1) Создать список из 20 случайных целых чисел в диапазоне от 1 до 100.
# Задание можно выполнить и через обычный цикл и через генератор списков.
import random
list1=[random.randint(1,100) for value in range(0,20)]
print(list1)
# 2) Создать словарь triangle в который записать точки A B C (ключи),
# и их координаты - кортежи (значения), созданные случайным образом с помощью модуля random в диапазоне от -10 до 10 по каждой оси.
import random
triangle={"A":{random.randint(-10,10),random.randint(-10,10)},"B":{random.randint(-10,10),random.randint(-10,10)},"C":{random.randint(-10,10),random.randint(-10,10)}}
print(triangle)
# 3) Создать функцию my_print, которая принимает в виде параметра строку и печатает ее
# с тремя символами * вначале и в конце строки.
# Пример:
# my_str = 'I'm the string'
# Печатает ***I'm the string***
def my_print(mystr):
  print('***'+mystr+'***')
my_str = "'I'm the string'"
my_print(my_str)
# 4) Дан список словарей persons в формате [{"name": "John", "age": 15}, ... ,{"name": "Jack", "age": 45}]
# а) Напечатать имя самого молодого человека. Если возраст совпадает - напечатать все имена.
persons=[{"name": "John", "age": 15}, {"name": "Jack", "age": 15} ,{"name": "Jack", "age": 45}]
ages=[value["age"] for value in persons]
for value in persons:
    if value["age"]==min(ages):
        print(value["name"])
# б) Напечатать самое длинное имя. Если длина имени совпадает - напечатать все имена.
persons=[{"name": "Jo", "age": 15}, {"name": "Jack", "age": 15} ,{"name": "Jacky", "age": 45}]
names=[len(value["name"]) for value in persons]
print(max(names))
for value in persons:
    if len(value["name"])==max(names):
        print(value["name"])
# в) Посчитать среднее количество лет всех людей из списка.
persons=[{"name": "John", "age": 15}, {"name": "Jack", "age": 15} ,{"name": "Jack", "age": 45}]
ages_r=[value["age"] for value in persons]
result4=sum(ages_r)/len(ages_r)
print(result4)
# 5) Даны два словаря my_dict_1 и my_dict_2.
my_dict_1={"name": "John", "house": 15,"street":"Krasnaya"}
my_dict_2={"name": "Jack", "age": 15}
# а) Создать список из ключей, которые есть в обоих словарях.
keys_mydict1=set(my_dict_1.keys())
keys_mydict2=set(my_dict_2.keys())
result4a=[key for key in keys_mydict1.intersection(keys_mydict2)]
print(result4a)
# б) Создать список из ключей, которые есть в первом, но нет во втором словаре.
result4b=[key for key in keys_mydict1.difference(keys_mydict2)]
print(result4b)
# в) Создать новый словарь из пар {ключ:значение}, для ключей, которые есть в первом, но нет во втором словаре.
mydict_result_v={key:item for key,item in my_dict_1.items() if key in result4b}
print(mydict_result_v)
# г) Объединить эти два словаря в новый словарь по правилу:
# если ключ есть только в одном из двух словарей - поместить пару ключ:значение,
# если ключ есть в двух словарях - поместить пару {ключ: [значение_из_первого_словаря, значение_из_второго_словаря]},
term1_1=keys_mydict1.difference(keys_mydict2)
term1_2=keys_mydict2.difference(keys_mydict1)
term2=keys_mydict1.intersection(keys_mydict2)
union=keys_mydict1.union(keys_mydict2)
dictt1_2={key:item for key,item in my_dict_2.items() if key in term1_2}
dictt1_1 = {key: item for key, item in my_dict_1.items()if key in term1_1}
dictt2 = {key: [item1, item2] for key, item1 in my_dict_1.items() if key in term2 for key, item2  in my_dict_2.items() if key in term2}
result4g=dictt1_1.copy()
result4g.update(dictt1_2)
result4g.update(dictt2)
print(result4g)