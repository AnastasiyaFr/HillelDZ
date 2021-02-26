#Task1

import requests
import csv
import random
import json
import re

#Create function for csv write
def write_csv(path,data):
    csv_file = open(path, 'w',newline='')
    with csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(["Author","Quote","URL"])
        writer.writerows(data)
    return print("Your file for task 1 is written")

#Create main function
def create_citates_csv(path,number):
    url = "http://api.forismatic.com/api/1.0/"
    author=[]
    quote=[]
    link=[]
    while len(quote)<=number-1:
        params = {"method": "getQuote",
                      "format": "json",
                      "key": random.randint(0,99999),
                      "lang": "ru"}
        responce = requests.get(url, params=params)
        result = responce.json()
        if result["quoteAuthor"]:
                quotei = str(result["quoteText"])
                quote.append(quotei)
                if len(set(quote))==len(quote):
                    authori = str(result["quoteAuthor"])
                    linki = str(result["quoteLink"])
                    author.append(authori)
                    link.append(linki)
                else:
                    quote.remove(quotei)
    data = list(zip(sorted(author), quote, link))
    write_csv(path,data)


#Example
path="dz12_authors.csv"
number=5
create_citates_csv(path,number)
#_________________________________________________________________________________________________________________
#Task 2

#Function for 2.1.
def read_txt_list(path):
    with open(path, "r") as text_file:
        alllist=text_file.readlines()
        result21=[]
        for line in alllist:
            if "'s" in line:
                result21.append(line)
    return result21

#Function for 2.2.
def result21todict(result21):
    result22=[]
    months = dict(January="01", February="02", March="03", April="04", May="05", June="06", July="07", August="08", September="09", October="10", November="11", December="12")
    for data in result21:
        date=data.split(" - ")[0]
        dd=re.findall(r"[0-9]+",date)
        month=date.split(" ")[1]
        mm=months[month]
        year= date.split(" ")[2]
        forauthor=data.split("-")[1]
        author=forauthor.split("'s")[0]
        formatdate=dd[0]+"/"+mm+"/"+year
        d={"name":author, "date":formatdate}
        result22.append(d)
    return result22

#Function for write json task 2.3
def write_json(path, adddata):
    with open(path, "w") as json_file:
        json.dump(adddata,json_file)
        return print ("File for task2 is successfully created")
#_____________________________________________________________________________________________________
#Example:
path="authors12.txt"
result21=read_txt_list(path)
result22=result21todict(result21)
write_json("authors12.txt", result22)