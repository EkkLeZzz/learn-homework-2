"""
Домашнее задание №2

Дата и время

1. Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
2. Превратите строку "01/01/20 12:10:03.234567" в объект datetime

"""
from datetime import date, timedelta, datetime


def print_days():
    date_now=date.today()
    dt1=timedelta(days=1)
    dt3=timedelta(days=30)
    dt4=date_now-dt3
    dt2=date_now - dt1
    print(f" Вчера: {dt2} \n Сегодня: {date_now} \n 30 Дней назад: {dt4}")


def str_2_datetime(date_string):
    date= datetime.strptime(date_string, '%d/%m/%y %H:%M:%S.%f')
    print(date)

if __name__ == "__main__":
    print_days()
    print(str_2_datetime("01/01/20 12:10:03.234567"))
