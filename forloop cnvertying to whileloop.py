# -*- coding: utf-8 -*-
"""
Created on Wed Dec  3 10:22:54 2025

@author: HP
"""

    
for row in range(1,6):
    for col in range(5,row,-1):
        print(" ",end="")
    for col in range(0,row):
        print("*",end=" ")
    print()  
    
row=1
while row<6:
    col=5
    while col>row:
        print(" ",end="")
        col-=1
    col=0
    while col<row:
        print("*",end=" ")
        col+=1
    print()
    row+=1
    
for row in range(5,0,-1):
    for col in range(5,row,-1):
        print(" ",end="")
    for col in range(0,row):
        print("*",end=" ")
    print()
    
row=5
while row>0:
    col=5
    while col>row:
        print(" ",end=" ")
        col-=1
    col=0
    while col<row:
        print("2",end=" ")
        col+=1
    print()
    row-=1
    
    
    
 for row in range(1,7):
     for col in range(7,row,-1):
         print("",end="")
     for col in range(0,row):
         print("*",end="")
     print()      
     

row=1
while row<7:
    col=7
    while col>row:
        print("",end=" ")
        col-=1
    col=0
    while col < row:
        print("*",end=" ")
        col+=1
    print()
    row+=1    

for row in range(1,10,2):
    for col in range(0,row):
        print(row,end="")
    print()    
 
row=1
while row<10:
    col=0
    while col<row:
        print(row,end="")
        col+=1
    print()
    row+=2    
    
for row in range(1,7):
    for col in range(7,row,-1):
        print("",end="")
    for col in range(0,row):
        print("*",end="")
    print()       

row =1
while row <7:
    col=7
    while col>1:
        print("",end="")
        col-=1
    col=0
    while col<row:
        print("*",end="")
        col+=1
    print()
    row+=1    
    
    
for row in range(1,5):
    for col in range(5,row,-1):
        print(" ",end="")
    for col in range(0,row):
        print(" * ",end="")
    print()  
    
row=1
while row<5:
    col=5
    while col>row:
        print(" ",end="")
        col-=1
    col=0
    while col<row:
        print(" * ",end="")
        col+=1
    print()
    row+=1     
    
    
for row in range(1,6):
    for col in range(row,0,-1):
        print(col,end="")
    print()

row=1
while row<6:
    col=row
    while col>0:
        print(col,end="")
        col-=1
    print()
    row+=1    