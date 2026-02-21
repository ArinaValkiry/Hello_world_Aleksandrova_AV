# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 23:41:56 2026

@author: Lenovo A
"""
# Запросим у пользователя название питательной среды

medium_name = input("Введите название питательной среды: ")
agar_conc = input("Укажите концентрацию агара (%): ")
ster_temp = input("Укажите температуру стерилизации (градусы цельсия): ")

with open("recipe.txt", "w", encoding="utf-8") as recipe:
    recipe.write(f"Среда {medium_name}\n{agar_conc}\n{ster_temp}\n")

print(f"Файл 'recipe.txt' успешно сформирован!")
