# -*- coding: utf-8 -*-
"""
Created on Sat Feb 21 11:58:58 2026

@author: arina
"""

all_capsules = int(input("Введите общее количество произведенных капсул: "))
in_one_blister = int(input("Введите количество капсул в одной упаковке: "))

full_blisters = all_capsules // in_one_blister
left_capsules = all_capsules % in_one_blister

print("--- Отчет фасовочного цеха ---", f"\nПолных упаковок:\t{full_blisters}",
      f"\nОстаток капсул:\t\t{left_capsules}")