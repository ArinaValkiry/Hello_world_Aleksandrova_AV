# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 15:30:43 2026

@author: arina
"""

number = int(input("Введите ваше число: "))

summa = 0

for i in range(number + 1):
    q = i**2
    summa = summa + q
    
print(f"Сумма квадратов = {summa}")