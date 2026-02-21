# -*- coding: utf-8 -*-
"""
Created on Sat Feb 21 11:52:12 2026

@author: arina
"""

weight = float(input("Введите вес (кг): "))
height = float(input("Введите рост (м): "))

bmi = weight / (height ** 2)

print("--- Отчет о состоянии здоровья ---", f"\nРост:\t{height} см\nВес:\t{weight} кг")
print(f"Индекс массы тела пациента: {bmi:.2f}")