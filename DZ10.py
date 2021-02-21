# 1. Написать функцию read_file которая принимает один параметр - полный путь к файлу.
# В зависимости от расширения файла (txt, csv, json) считывает и возвращает данные из файла.
# Для csv использовать reader.
# Если расширение не соответствует заданным, то вывести текст "Unsupported file format"
import os
import json
import csv
# Создаём три функции для чтения трёх различных файлов
def read_txt(path):
    with open(path, "r") as text_file:
        data=text_file.read()
    return data
def read_json(path):
    with open(path, "r") as json_file:
        data=json.load(json_file)
    return data
def read_csv(path):
     with open(path, "r") as csv_file:
        data=[]
        reader=csv.reader(csv_file)
        for raw in reader:
             data.append(raw)
     return data
# # Функция, которая требуется в задачи
def read_file(path):
    extention=path.split(".")
    if extention[-1]=="txt":
        return read_txt(path)
    if extention[-1]=="json":
        return read_json(path)
    if extention[-1]=="csv":
        return read_csv(path)
    else:
        print("Unsupported file format")
# 2. Написать функцию write_file которая принимает два параметра - полный путь к файлу и данные.
# В зависимости от расширения файла (txt, csv, json) записывает данные в данный файл.
# Для csv использовать DictWriter.
# Если расширение не соответствует заданным, то вывести текст "Unsupported file format"
#
# Данные для записи и файлы создать самим. Файлы с результатами добавить в гит.
def write_txt(path, adddata):
    with open(path, "w") as text_file:
       text_file.writelines(str(adddata))
    return text_file
def write_json(path, adddata):
    with open(path, "w") as json_file:
        json.dump(adddata,json_file)
        return json_file
def write_csv(path, adddata):
    with open(path, 'w', newline='') as csvfile:
        fieldnames = adddata.keys()
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerow(adddata)
    return writer
# Функция, которая требуется в задачи
def write_file(path,newdata):
    extention=path.split(".")
    if extention[-1]=="txt":
        return write_txt(path,newdata)
    if extention[-1]=="json":
        return write_json(path,newdata)
    if extention[-1]=="csv":
        return write_csv(path,newdata)
    else:
        print("Unsupported file format")
# Example
path="dz10.txt"
adddata={"Name":"Anastasiya", "Surname":"Pyatnitsa","DZ":"10","Result":"100" }
write_file(path, adddata)
result=read_file(path)
print(result)