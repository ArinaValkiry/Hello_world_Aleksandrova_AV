# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

print("***\tАнализ последовательности ДНК\t***")

# Ввод данных пользователем
dna = input("\nВведите последовательность ДНК: ")

# Анализ последовательности

dna_upper = dna.upper()

count_A = dna_upper.count("A")
count_T = dna_upper.count("T")
count_G = dna_upper.count("G")
count_C = dna_upper.count("C")

dna_length = len(dna_upper)

perc_A = (count_A / dna_length) * 100
perc_T = (count_T / dna_length) * 100
perc_G = (count_G / dna_length) * 100
perc_C = (count_C / dna_length) * 100

# Вывод данных
print(f"\nПоследовательность в верхнем регистре: {dna_upper}")
print(f"\nПодсчёт нуклеотидов:\nA: {count_A}\nT: {count_T}\nG: {count_G}\nC: {count_C}")
print(f"\nОбщая длина: {dna_length} нуклеотидов")
print(f"\nПроцентное содержание нуклеотидов в последовательности:", 
      f"\nA - {perc_A:.2f}%\nT - {perc_T:.2f}%\nG - {perc_G:.2f}%\nC - {perc_C:.2f}%")