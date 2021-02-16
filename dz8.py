import random
import string
# # №1. Даны списки names и domains (создать самостоятельно).
# Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фам?лию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.
# Буквы в строке МОГУТ повторяться (перемешивание алфавита не подойдет, так как буквы не смогут повторяться)
def create_email(domains,names):
    name=random.choice(names)
    number = random.randint(100, 999)
    site = ''.join(random.choice(string.ascii_letters) for i in range(random.randint(5, 7)))
    domain=random.choice(domains)
    return  name+'.'+str(number)+"@"+site+'.'+domain
names = ["king", "miller", "kean", 'small', 'apple']
domains = ["net", "com", "ua", 'ru', 'gov']
email=create_email(domains, names)
# 2. Написать функцию, которая генерирует и возвращает строку случайной длинны.
# Минимальную и максимальную длину строки ограничить с помощью параметров min_limit, max_limit, передаваемых в функцию.
def create_str(min_limit, max_limit):
    return ''.join(random.choice(string.ascii_letters+string.digits) for i in range(random.randint(min_limit, max_limit)))
# 3. Написать функцию (или последовательность нескольких функций), которые преобразуют случайную строку,
# полученную в п 2 по следующим правилам:
# В строке должны присутствовать большие и маленькие буквы английского алфавита, цифры, пробелы,
# знаки препинания, символ перехода на новую строку (\n).
# Строка должна выглядеть как текст. Слова отделяться друг от друга пробелами.
# Под словом будем понимать набор случайных букв от одной до 10.
# Большие буквы только в начале слов. Цифры не должны быть частями слов, а стоять отдельно.
# Знаки препинания всегда идут в конце слова.

# Функция разбиения строки на буквы и числа
def changedstr(newstr):
    def strsplit_symb(str):
        symbol=[value for value in newstr if value.isalpha()]
        l = len(newstr)
    # В список добавлю одну цифру,чтобы в любои случае на выходе была цифра, даже если её нет в строке(по требованию задачи)
        integ = [random.randint(1,9)]
        i = 0
        while i < l:
            s_int = ''
            a = newstr[i]
            while '0' <= a <= '9':
                s_int += a
                i += 1
                if i < l:
                    a = newstr[i]
                else:
                 break
            i += 1
        if s_int != '':
            integ.append(int(s_int))
        return [integ,symbol]
    integ=strsplit_symb(newstr)[0]
    symbol=strsplit_symb(newstr)[1]
    # Функция разбиения на слова
    def str_words(symbol):
        index = 0
        condition = True
        while condition:
            step = random.randint(1, 10)
            index += step
            if index < len(symbol):
                symbol[index] = " "
            else:
                condition = False
        newstrcomb = ("".join(symbol)).lower()
        newstr_space = newstrcomb.split(" ")
        return newstr_space
    str_space=str_words(symbol)
    result=[]
    for  word in str_space:
        if word != '':
            result.append(word.capitalize()+",")
    for  number in integ:
        result.append(str(number) + ".")
    result.append("\\n")
    finalstr=" ".join(result)
    return finalstr
newstr=create_str(5,40)
outputstr=changedstr(newstr)
print(newstr)
print(outputstr)