#1. Дано целое число (int). Определить сколько нулей в этом числе.
value1=input("Введите целое число")
result=[]
for symbol in value1:
     if symbol=="0":
         result.append(symbol)
print(len(result))
#2. Дано целое число (int). Определить сколько нулей в конце этого числа.

#3a. Даны списки my_list_1 и my_list_2.
#Создать список my_result в который вначале поместить
#элементы на четных местах из my_list_1, а потом все элементы на нечетных местах из my_list_2.
my_list1=[1,2,3,4,5,6,7]
my_list2=[1,2,3,4,5,6,7]
my_result3a = []
for symbol in my_list1[::2]:
    my_result3a.append(symbol)
for symbol in my_list2[1::2]:
    my_result3a.append(symbol)
print(my_result3a)
#3b. Даны списки my_list_1 и my_list_2. Создать список my_result в который
#вначале поместить четные элементы (ИМЕННО ЭЛЕМЕНТЫ) из my_list_1 и потом нечетные элементы из my_list_2.
my_result3b = []
for symbol in my_list1:
    if not int(symbol) % 2:
        my_result3b.append(symbol)
for symbol in my_list2:
    if  symbol % 2:
        my_result3b.append(symbol)
print(my_result3b)
#4. Дан список my_list. СОЗДАТЬ НОВЫЙ список new_list у которого первый элемент из my_list
#стоит на последнем месте. Если my_list [1,2,3,4], то new_list [2,3,4,1]
myresult4=my_list1[1:]
myresult4.append(my_list1[0])
print(myresult4)
#5.Дан список my_list. В ЭТОМ списке первый элемент переставить на последнее место.
#[1,2,3,4] -> [2,3,4,1]. Пересоздавать список нельзя! (используйте метод pop)
my_list1.append(my_list1.pop(0))
print(my_list1)
#Дана строка в которой есть числа (разделяются пробелами).
#Например "43 больше чем 34 но меньше чем 56". Найти сумму ВСЕХ ЧИСЕЛ (А НЕ ЦИФР) в этой строке.
value6=input("Введите строку с числами")
value6=value6.split(" ")
result6=[]
for symbol in value6:
    if symbol.isdigit():
        result6.append(int(symbol))
print(sum(result6))
#7. Дана строка my_str. Разделите эту строку на пары из двух символов и поместите эти пары в список.
#Если строка содержит нечетное количество символов, пропущенный второй символ последней пары должен
#быть заменен подчеркиванием ('_'). Примеры: 'abcd' -> ['ab', 'cd'], 'abcde' -> ['ab', 'cd', e_']
my_str='abce'
my_str_7_1=[]
my_str_7_2=[]
result7=[]
for symbol in my_str[::2]:
   my_str_7_1.append(symbol)
for symbol in my_str[1::2]:
    my_str_7_2.append(symbol)
if len(my_str_7_1)>len(my_str_7_2):
    my_str_7_2.append('_')
for index in range(len(my_str_7_1)):
     result7.append((my_str_7_1[index]+my_str_7_2[index]))
print(result7)
#8.Дана строка my_str в которой символы не повторяются и два символа l_limit, r_limit,
#которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
#В переменную sub_str поместить часть строки между этими символами.
my_str = "My_long str"
r_limit = "t"
l_limit = "o"
for index,symbol in enumerate(my_str):
    if symbol==l_limit:
        start=index+1
    if symbol == r_limit:
        finish=index
print(my_str[start:finish])
#9. Дана строка my_str в которой символы МОГУТ повторяться и два символа l_limit, r_limit,
#которые точно находятся в этой строке. Причем l_limit левее чем r_limit.
#В переменную sub_str поместить НАИБОЛЬШУЮ часть строки между этими символами.
#my_str = "My long string", l_limit = "o", r_limit = "g" -> sub_str = "ng strin".
my_str = "My long string"
r_limit = "g"
l_limit = "o"
start=[]
finish=[]
for index,symbol in enumerate(my_str):
    if symbol==l_limit:
        start.append(index)
    if symbol == r_limit:
        finish.append(index)
st=min(start)
fn=max(finish)
print(my_str[st+1:fn])
#Дан список чисел. Определите, сколько в этом списке элементов,
#которые больше суммы двух своих соседей (слева и справа), и НАПЕЧАТАЙТЕ КОЛИЧЕСТВО таких элементов.
#Крайние элементы списка никогда не учитываются, поскольку у них недостаточно соседей.
#Для списка [2,4,1,5,3,9,0,7] ответом будет 3 потому что 4 > 2+1, 5 > 1+3, 9>3+0.
mylist_10=[2,4,1,5,3,9,0,7]
result10=[]
for index,symbol in enumerate(mylist_10[1::2]):
  result10.append(int(mylist_10[index+1])+int(mylist_10[index-1]))
result10.pop(0)
print(len(result10))