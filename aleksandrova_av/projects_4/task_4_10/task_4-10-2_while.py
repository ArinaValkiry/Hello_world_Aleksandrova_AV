# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 23:10:09 2026

@author: arina
"""

i = 1
sum_even = 0

while i <= 15:
    if i % 2 == 0:
        sum_even = sum_even + i
    i = i + 1

print("Сумма чётных чисел:", sum_even)