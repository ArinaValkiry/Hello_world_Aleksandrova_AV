# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 08:20:16 2026

@author: arina
"""

a = float(input("Введите число: "))
b = float(input("Введите число: "))
c = float(input("Введите число: "))
d = float(input("Введите число: "))

if a < b :
    if a < d :
        if a < c :
            min = a
        else:
            min = c
    else:
        if d < c :
            min = d
        else:
            min = c
else:
    if b < d:
        if b < c:
            min = b
        else:
            min = c
    else:
        if d < c:
            min = d
        else:
            min = c
            
print(f"Наименьшее число = {min}")