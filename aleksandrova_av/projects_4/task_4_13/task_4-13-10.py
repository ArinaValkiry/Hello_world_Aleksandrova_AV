# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 15:47:52 2026

@author: arina
"""

array = list(map(int, input("Введите ваш массив: ").split()))

summa = 0

for i in range(len(array)):
    if i % 2 == 0 :
        summa = summa + array[i]
        #print(summa)
        
        
print(f"Сумма всех элементов с нечетными индексами = {summa}")