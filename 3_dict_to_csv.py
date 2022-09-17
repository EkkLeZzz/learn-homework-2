"""

Домашнее задание №2

Работа csv

1. Создайте список словарей с ключами name, age и job и значениями по вашему выбору. 
   В списке нужно создать не менее 4-х словарей
2. Запишите содержимое списка словарей в файл в формате csv

"""
import csv
lib = [
    {'name': 'ivan', 'age': '20', 'job':'writter'},
    {'name': 'kirill', 'age':'24', 'job':'driver'},
    {'name': 'artem', 'age':'27', 'job':'programmer'},
    {'name': 'alex', 'age':'34', 'job':'director'},
]


with open ('user_info.csv', 'w', encoding='utf-8') as info:
    heading = ['name', 'age', 'job']
    inside = csv.DictWriter(info, heading, delimiter = ',')
    inside.writeheader()
    for var in lib:
        inside.writerow(var)


