
#1) У вас есть переменная value, тип -int Написать тернарный оператор для переменной new_value по такому правилу: если value меньше 100, то new_value равно половине значения value, в противном случае - противоположне value число
#####################################################
value=int(input("ВВедите целое число"))
result= value/2 if value<100 else -value
print(result)

#2) У вас есть переменная value, тип - int. Написать тернарный оператор для переменной new_value по такому правилу: если value меньше 100, то new_value равно 1, в противном случае - 0
#####################################################
value2=int(input("ВВедите целое число"))
result2=1 if value2<100 else 0
print(result2)
#3) У вас есть переменная value, тип - int. Написать тернарный оператор для переменной new_value по такому правилу: если value меньше 100, то new_value равно True, в противном случае - False
#####################################################
value3=int(input("ВВедите целое число"))
result3=True if value3<100 else False
print(result3)
#4) У вас есть переменная my_str, тип - str. Заменить в my_str все маленькие буквы на большие.
#####################################################

#5) У вас есть переменная my_str, тип - str. Заменить в my_str все большие буквы на маленькие.
#####################################################
my_str5=input("ВВедите строку5")
for symbol in my_str5:
    if not my_str5.isupper(symbol):
        my_str5.capitalize(symbol)
print(my_str5)
#6) У вас есть переменная my_str, тип - str. Если ее длинна меньше 5, то допишите в конец строки себя же. Пример: было - "qwer", стало - "qwerqwer". Если длинна не меньше 5, то оставить строку как есть.
#####################################################
my_str6=input("ВВедите строку")
if len(my_str6)<5:
    my_str6=my_str6*2
print(my_str6)
#7) У вас есть переменная my_str, тип - str. Если ее длинна меньше 5, то допишите в конец строки перевернутую себя же. Пример: было - "qwer", стало - "qwerrewq". Если длинна не меньше 5, то оставить строку как есть.
#####################################################
my_str7=input("ВВедите строку")
if len(my_str7)<5:
    my_str7=my_str7+my_str7[::-1]
print(my_str7)
#8) У вас есть переменная my_str, тип - str. Вывести на экран все символы из этой строки, которые являются буквой или цифрой.
#####################################################
my_str8 = "Test string 123 QWE"
result8=[]
for symbol in my_str8:
    if symbol.isnumeric() or symbol.isalpha():
        result8.append(symbol)
print(result8)
#9) У вас есть переменная my_str, тип - str. Вывести на экран все символы из этой строки, которые не являются буквой или цифрой.
#####################################################
my_str9 = "Test #$!string 123 QWE"
result9=[]
for symbol in my_str9:
    if not symbol.isnumeric() and not symbol.isalpha():
        result9.append(symbol)
print(result9)
#10) У вас есть переменная my_str, тип - str. Вывести на экран все символы из этой строки, которые не являются буквой или цифрой и не пробел.
my_str9 = "Test #$!string 123 QWE"
result9=[]
for symbol in my_str9:
    if not symbol.isnumeric() and not symbol.isalpha() and not symbol.isspace():
        result9.append(symbol)
print(result9)