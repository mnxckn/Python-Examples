# -*- coding: utf-8 -*-
"""
Created on Tue Dec  2 10:52:44 2025

@author: HP
"""


    
    
list2=[1,2,3,4,5]
index=4
while index>-1:
    print(list2[index])
    index=index-1
    

list=[50,100]
index=50
while index<=1000:
    print(index)
    index+=1


index=20
while index<=100:
    print(index)
    index+=100
    
    
index=100
while index>20:
    print(index)
    index-=1
    
value=1
while value<6:
    print(value*" * ")
    value+=1
    
    
    
row=1
while row<6:
    col=6
    while col>row:
        print("",end="")
        col-=1
    col=0
    while col<row:
        print("*",end="")
        col+=1
    print()
    row+=1
    
row=6
while row>1:
    col=6
    while col