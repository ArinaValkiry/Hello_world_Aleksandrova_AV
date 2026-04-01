# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 15:40:06 2026

@author: arina
"""

array = list(map(int, input("Введите ваш массив: ").split()))

count = 0

for i in range(len(array)):
    if array[i] > 0:
        count = count + 1
        
print(f"Количество положительных элементов в вашем массиве = {count}")