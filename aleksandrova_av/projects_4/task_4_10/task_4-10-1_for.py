# -*- coding: utf-8 -*-
"""
Created on Mon Mar 30 23:09:49 2026

@author: arina
"""

sum_even = 0

for i in range(1, 16):
    if i % 2 == 0:
        sum_even = sum_even + i

print("Сумма чётных чисел:", sum_even)