#Задание 1
#У вас есть список my_list с значениями типа int.
#Распечатать те значения, которые больше 100.
#Задание выполнить с помощью цикла for.
from typing import Tuple

my_list1=[1,2,130,150,5]
for value in my_list1:
    if value >100:
        print (value)

#2) У вас есть список my_list с значениями типа int, и пустой список my_results.
#Добавить в my_results те значения, которые больше 100.
#Распечатать список my_results.
#Задание выполнить с помощью цикла for.

my_results=[]
for value in my_list1:
    if value >100:
        my_results.append(value)
print(my_results)

#3) У вас есть список my_list с значениями типа int.
#Если в my_list количество элементов меньше 2, то в конец добавить значение 0.
#Если количество элементов больше или равно 2, то добавить сумму последних двух элементов.
#Количество элементов в списке можно получить с помощью функции len(my_list)
my_list3=[1,2,130,120,5]
if len(my_list3) <2:
    my_list3.append(0)
else:
    my_list3.append(my_list3[-1]+my_list3[-2])
print(my_list3)
#5) У вас есть список значений my_list и список индексов my_indexes
#(начинается с нуля и количество элементов совпадает с количеством в my_list.
#Распечатать значения из my_list через обращение по индексу.
my_list5 = "zxcvvbnm"
my_indexes = [0,1,2,3,4,5,6,7,]
for index in my_indexes:
	print(my_list5[index])
#6) У вас есть два списка my_list_1 и my_list_2 равной длинны и
#список индексов my_indexes (начинается с нуля и количество элементов совпадает с количеством в my_list_1.
#Распечатать пары значений из my_list_1 и my_list_2 через обращение по индексу.
my_list6_1 = [1,2,3,3,5,6,7,8]
my_list6_2 = [-1,-2,-3,-4,-5,-6,-7,-8]
my_indexes_6 = [0,1,2,3,4,5,6,7]
for index in my_indexes_6:
	print((my_list6_1[index],my_list6_2[index]))
#7) У вас есть строка my_string = '0123456789'.
#Сгенерировать целые числа (тип int) от 0 до 99 и поместить их в список.
#Задание нужно выполнить ТОЛЬКО через цикл в цикле(См. пример выше) и приведение типов .
# my_string = '0123456781'
# result7=[]
# for symbol in my_string:
#         result7.append(int(symbol))
# print(result7)
my_string = '0123456789'
result7=[]
for symbol1 in my_string:
    for symbol2  in my_string:
        value=int(symbol1+symbol2)
        result7.append(value)
print(result7)