# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

files = ["seq1", "seq2", "seq3", "seq4"]

for name in files:
    data_name = name + "_22.02.2026" 
    names = [data_name]
    
    for data_name in names: 
        new_name = data_name + ".fasta" 
        
        print(f"{new_name}")