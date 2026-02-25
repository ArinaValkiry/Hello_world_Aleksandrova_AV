# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 22:55:08 2026

@author: Lenovo A
"""

reagent_name = input("Введите название реагента: ")
reagent_amount = input("Введите количество реагента: ")

resume = print(f"Реактив {reagent_name} поступил на склад в количестве {reagent_amount} шт..")

with open('inventory.txt', "w", encoding="utf-8") as f:
    print(f"Реактив {reagent_name} поступил на склад в количестве {reagent_amount} шт..", file=f)
