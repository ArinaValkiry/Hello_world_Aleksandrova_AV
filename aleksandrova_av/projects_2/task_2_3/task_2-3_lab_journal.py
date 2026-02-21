# -*- coding: utf-8 -*-
"""
Created on Sat Feb 21 23:37:05 2026

@author: arina
"""
from datetime import datetime

# Ввод данных
sci_name = input("Введите ФИО исследователя: ")
date = input("Введите дату проведения эксперимента: ")
exp_name = input("Введите название эксперимента: ")
result = input("Введите вывод: ")

# Переменные для вывода
width = 50
text = "Электронный лабораторный журнал"
text_11 = f"ФИО исследователя : {sci_name}"
text_12 = f"Дата : {date}" 
text_13 = f"Эксперимент : {exp_name}"
text_2 = f"Вывод : {result}"

# Вывод данных в рамке

current_datetime = datetime.now()
print(f"\n\n{current_datetime}\n")

print("+" + "-" * width + "+")
print("| " + text.ljust(width - 2) + " |")
print("| " + "*" * (width - 2) + " |")
print("| " + text_11.ljust(width - 2) + " |")
print("| " + text_12.ljust(width - 2) + " |")
print("| " + text_13.ljust(width - 2) + " |")
print("| " + "*" * (width - 2) + " |")
print("| " + text_2.ljust(width - 2) + " |")
print("+" + "-" * width + "+")