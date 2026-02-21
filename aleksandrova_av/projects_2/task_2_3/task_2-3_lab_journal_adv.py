# -*- coding: utf-8 -*-
"""
Created on Sat Feb 21 08:58:50 2026

@author: Lenovo A
"""

# Сбор данных
sci_name = input("Введите ФИО исследователя: ")
date = input("Введите дату проведения эксперимента: ")
exp_name = input("Введите название эксперимента: ")
result = input("Введите вывод: ")


def print_framed(lines, width=50):
    def border():
        return "+" + "-" * width + "+"

    def format_line(text=""):
        return "| " + text.ljust(width - 2) + " |"

    print(border())
    for line in lines:
        print(format_line(line))
    print(border())


text = ["Электронный лабораторный журнал", "", f"ФИО исследователя : {
    sci_name}", f"Дата : {date}", f"Эксперимент : {exp_name}", "", f"Вывод : {result}"]

print_framed(text)
