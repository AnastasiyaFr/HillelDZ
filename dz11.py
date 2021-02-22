# data.json - файл с данными о некоторых математиках прошлого.
# 1. Необходимо написать функцию, которая считает эти данные из файла. Параметр функции - имя файла.
import json
import re
filename="dz11.json"
def read_json(path):
    with open(filename, "r") as json_file:
        data=json.load(json_file)
    return data
data=read_json(filename)
# 2. Написать функцию сортировки данных по ФАМИЛИИ в поле "name" (у тех у кого она есть).
# Например для Rene Descartes фамилия это Descartes, у Pierre de Fermat - Fermat и т.д.
# Если фамилии нет, то использовать имя, например Euclid.
def sort_key_by_surname(sort_dict):
    value = sort_dict["name"].split(" ")[-1]
    return value
result2 = sorted(data, key=sort_key_by_surname)

# 3. Написать функцию сортировки по дате смерти из поля "years".
# Обратите внимание на сокращение BC. - это означает до н.э.
def sort_by_dday(sort_dict):
    age = sort_dict["years"].split("–")
    if age[-1].find("BC")>=0:
        years = -int(re.findall(r'[0-9]+', age[-1])[-1])
    else:
        years = int(re.findall(r'[0-9]+', age[-1])[-1])
    return years
result3 = sorted(data, key=sort_by_dday)
# 4. Написать функцию сортировки по количеству слов в поле "text"
def sort_key_by_len_name(sort_dict):
    return len(sort_dict["text"])
result4 = sorted(data, key=sort_key_by_len_name)
