# -*- coding: utf-8 -*-
"""
Created on Sat Feb 21 11:43:58 2026

@author: arina
"""

m_proteins = input("Введите массу белков в продукте (г): ")
m_lipids = input("Введите массу жиров в продукте (г): ")
m_glucose = input("Введите массу углеводов в продукте (г): ")

int_m_proteins = int(m_proteins)
int_m_lipids = int(m_lipids)
int_m_glucose = int(m_glucose)

print(f"Кал =", int_m_proteins * 4 + int_m_lipids * 9 + int_m_glucose * 4)