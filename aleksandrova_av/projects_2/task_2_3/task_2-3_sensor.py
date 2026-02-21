# -*- coding: utf-8 -*-
"""
Created on Thu Feb 19 23:52:01 2026

@author: Lenovo A
"""
operator = input("Введите имя оператора: ")
pressure = input("Введите текущее значение давления (Па): ")

with open("sensor_log.txt", "w", encoding="utf-8") as sensor:
    sensor.write(f"ОПЕРАТОР\tЗНАЧЕНИЕ\n{operator}\t{pressure}")

print(f"Данные успешно сохранены в sensor_log.txt")
