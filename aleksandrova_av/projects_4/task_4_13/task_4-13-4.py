# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 08:32:33 2026

@author: arina
"""

a = int(input("Введите число: "))
summa = 0

for i in range(a+1):
    summa = summa + i
    
print(f"Сумма первых {a} натуральных чисел равна {summa}")