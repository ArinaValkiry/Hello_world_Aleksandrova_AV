# -*- coding: utf-8 -*-
"""
Created on Sun Feb 22 23:50:52 2026

@author: arina
"""

destination = input("Куда изволите направиться: направо, налево али прямо? \n")

up_destination = destination.upper()

if up_destination == "НАПРАВО":
    print("\nПравильный выбор")
elif up_destination == "ПРЯМО":
    answer = int(input("\nСколько будет 2*2? "))
    if answer == 4 or answer == 5:
        print("\nДа Вы математик!")
    else:
        print("\nВам бы подучить Высшую математику")
elif up_destination == "НАЛЕВО":
    print("\nНе ходите налево")
     