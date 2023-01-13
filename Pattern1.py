# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 10:16:46 2022

@author: dell
"""

rows = int(input("Enter number of rows: "))

for i in range(rows):
    for j in range(i+1):
        print("* ", end="")
    print("\n")
    