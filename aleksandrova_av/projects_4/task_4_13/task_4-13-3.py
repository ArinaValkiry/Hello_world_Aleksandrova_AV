# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 08:25:16 2026

@author: arina
"""

a = int(input("Введите число: "))

i = 1
fact = 1

for i in range(1, a+1):
    fact = fact * i
        
print(f"Факториал числа {a} равен {fact}")