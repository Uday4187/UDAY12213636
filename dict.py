# -*- coding: utf-8 -*-
"""
Created on Mon Jan  2 09:43:56 2023

@author: dell
"""

emp={"Name":"Rahul",
     "Age":62,
     "Dept":"CSE",
     "Salary":6000}
print(emp["Salary"])
print(emp.get("Dept"))
print(emp.items)
print(emp.pop("Name"))
print(emp.popitem())
