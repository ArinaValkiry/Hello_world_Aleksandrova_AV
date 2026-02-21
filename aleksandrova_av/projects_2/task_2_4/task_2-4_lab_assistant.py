# -*- coding: utf-8 -*-
"""
Created on Sat Feb 21 18:29:34 2026

@author: arina
"""

volume = float(input("Введите итоговый объём раствора (в мл): "))

nacl_mass = volume * 0.009
water_volume = volume

with open("recipe.txt", "w", encoding="utf-8") as file:
        file.write("ОТЧЁТ ПО ПРИГОТОВЛЕНИЮ\n")
        file.write("-" * 23)
        file.write(f"\nОбщий объём: {volume} мл")
        file.write(f"\nМасса соли:  {nacl_mass} г")
        file.write(f"\nОбъем воды:  {water_volume} мл")
        
print("Итоговый отчёт находится в файле recipe.txt")