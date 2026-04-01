# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 15:52:35 2026

@author: arina
"""

array = list(map(int, input("Введите ваш массив: ").split()))

summa = 0
count = 0

for i in range(len(array)):
    if i % 2 != 0 :
        summa = summa + array[i]
        count = count + 1 
    
    
average = summa / count   
print(f"Среднее арифметическое элементов массива с четными индексами = {average}")