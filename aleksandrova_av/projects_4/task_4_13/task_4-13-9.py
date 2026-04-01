# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 15:44:07 2026

@author: arina
"""

array = list(map(int, input("Введите ваш массив: ").split()))

summa = 0

for i in range(len(array)):
    if array[i] % 2 != 0:
        summa = summa + array[i]
        
print(f"Сумма всех нечетных элементов в вашем массиве = {summa}")