# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 15:10:32 2026

@author: arina
"""

array = list(map(int, input("Введите ваш массив: ").split()))

maxi = 0

for i in range(len(array)):
    if array[i] > maxi:
        maxi = array[i]
        
print(f"Максимум = {maxi}")
        
    

