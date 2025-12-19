# -*- coding: utf-8 -*-
"""
Created on Mon Nov 17 21:58:32 2025

@author: HP
"""

list=[1,2,3,4,5,6,7,8,9]
for values in list:
    print(values)
    
for index in range(0,8):
    print(list[index])
    
list1=[3,3,5,4,6,7,3,4]
for values in list1:
    print(values)

"*"*5   

for values in range(0,6):
    print(values*"*")
    

for values in range(10,0,-1):
    print(values*"*")

for values in range(0,6):
    print((6-values)*" ",values*" *")
    
for values in range(10,0,-1):
    print((10-values)*" ",values*" *"    )
    
for row in range(1,6):
    for col in range(0,row):
        print(col,end="")
    print()    

for row in range(10,0,-1):
    for col in range(0,row):
        print(row,end=" ")
    print()    