# Считать данные из файла names.txt и поместить в список только фамилии из файла.
# Каждая строка файла содержит номер, фамилию, страну, некоторое число (таблица взята с википедии).
# Фамилия находится всегда на одной и той же позиции в строке.
import os
file=open('names', 'r')
data=[]
for line in file.readlines():
    data.append(line)
result1=[]
for element in data:
        surname=list(element.split('\t'))
        result1.append(surname[1])
print(result1)
# 2. Создать функцию для записи в файл json.
# Создает и возвращает словарь со случайным количеством ключей (не менее 5 но не более 20 ключей).
# Ключи - уникальные случайные строки длинны 5 символов из маленьких букв английского алфавита
# (можно с повторениями символов).
# Значения - или целое число в диапазоне от -100 до 100, или число типа float в диапазоне от 0 до 1,
# или True/False. Выбор значения должен быть равновероятным. Т.е. вероятность того, что значение будет целым
# такая же, как и вероятность того, что будет типа float или типа bool.
def create_rnddict():
    import json
    import random
    import string
    filename="res2.json"
    keys_len = random.randint(5, 20)
    value=[]
    data=[]
    ft= 1
    while ft <= keys_len:
        key = ''.join(random.choice(string.ascii_lowercase) for _ in range(5))
        znach = random.choice([random.randint(-100, 100), random.random(), random.choice([True, False])])
        data.append(key)
        value.append( znach )
        ft += 1
        dict = {data[i]: value[i] for i in range(len(data))}
    return dict
newdict=create_rnddict()
print(newdict)
# 3. Написать функцию generate_and_write_json которая принимает один параметр - полный путь к файлу.
# Cгенерировать данные для записи с помощью функции из пункта 2 и записать в данный файл.
def generate_and_write_json(path):
    import json
    filename=path
    with open(filename, 'w') as js_file:
        json.dump(create_rnddict(),js_file, indent=2)
generate_and_write_json(r"C:\Users\anast\PycharmProjects\HillelDZ\res3.json")
