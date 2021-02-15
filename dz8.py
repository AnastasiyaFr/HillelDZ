# # №1. Даны списки names и domains (создать самостоятельно).
# Написать функцию для генерирования e-mail в формате:
# фамилия.число_от_100_до_999@строка_букв_длинной_от_5_до_7_символов.домен
# фам?лию и домен брать случайным образом из заданных списков переданных в функцию в виде параметров.
# Строку и число генерировать случайным образом.
# Буквы в строке МОГУТ повторяться (перемешивание алфавита не подойдет, так как буквы не смогут повторяться)
def create_email(domains,names):

    import random
    import string

    name=random.choice(names)
    number = random.randint(100, 999)
    site = ''.join(random.choice(string.ascii_letters) for i in range(random.randint(5, 7)))
    domain=random.choice(domains)

    return  name+'.'+str(number)+"@"+site+'.'+domain

names = ["king", "miller", "kean", 'small', 'apple']
domains = ["net", "com", "ua", 'ru', 'gov']
email=create_email(domains, names)
print(email)
# 2. Написать функцию, которая генерирует и возвращает строку случайной длинны.
# Минимальную и максимальную длину строки ограничить с помощью параметров min_limit, max_limit, передаваемых в функцию.
def create_str(min_limit, max_limit):
    import random
    import string
    return ''.join(random.choice(string.ascii_letters+string.digits) for i in range(random.randint(min_limit, max_limit)))
min_limit=5
max_limit=25
newstr=create_str(min_limit,max_limit)
print(newstr)
# 3. Написать функцию (или последовательность нескольких функций), которые преобразуют случайную строку,
# полученную в п 2 по следующим правилам:
# В строке должны присутствовать большие и маленькие буквы английского алфавита, цифры, пробелы,
# знаки препинания, символ перехода на новую строку (\n).
# Строка должна выглядеть как текст. Слова отделяться друг от друга пробелами.
# Под словом будем понимать набор случайных букв от одной до 10.
# Большие буквы только в начале слов. Цифры не должны быть частями слов, а стоять отдельно.
# Знаки препинания всегда идут в конце слова.