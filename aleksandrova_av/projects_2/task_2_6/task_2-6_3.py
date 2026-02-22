# -*- coding: utf-8 -*-
"""
Created on Sun Feb 22 23:36:36 2026

@author: arina
"""

donor = input("Введите группу крови донора (I, II, III, IV): ")
recepient = input("Введите группу крови пациента (I, II, III, IV): ")

if donor == recepient or donor == "I" or recepient == "IV":
    print("Переливание крови возможно")

else:
    print("Переливание крови не рекоммендуется")
