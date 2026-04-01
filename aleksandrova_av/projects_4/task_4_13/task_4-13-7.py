# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 15:36:38 2026

@author: arina
"""

array = list(map(int, input("Введите ваш массив: ").split()))

average = 0

for i in range(len(array)):
    average = average + array[i]
    
average = average / len(array)    
print(f"Среднее арифметическое элементов массива = {average}")