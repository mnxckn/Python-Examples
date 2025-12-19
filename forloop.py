# -*- coding: utf-8 -*-
"""
Created on Fri Nov 14 09:41:03 2025

@author: HP
"""
list(range(0,11,2))
list(range(100,0,-1))
list(range(1,10))
list(range(1,10,2))
list(range(1,10,4))
list(range(20,1,-1))
list(range(10,1,-2))

print(0)
list1=[1,2,3,4,5]
print(list1[0])

for value in list1:
    print(value)
    
for index in range(0,5):
    print(list1[index])
   
    
list2=[5,6,7,8,9,10]
print(2)
for value in list2:
    print(value)
for index in range(0,6):
    print(list2[index])
    
list3=[3,2,5,4,7,6,8,9]    
for value in list3:
    print(value)
for index in range(0,8):
    print(list3[index])
    
list5=[1,3,5,7,9,2,4,6,8,0]    
for value in list5
    print(value)


list6=['*','**','***','****']
for value in list6:
    print(value)
for index in range(0,4):
    print(list6[index])

for value in range(1,6):
    print(value*'*')
for value in range(1,8):
    print(value*'*')

for value in range(1,10):
    print(value*"*")
for value in range(10,0,-1):
    print(value*"*")
for value in range(1,6):
    print((6-value)*' ',value*"* ")            
for value in range(10,0,-1):
    print((10-value)*'  ',value*" *  ")
for row in range(1,6):
    for col in range(0,row):
        print(row,end=" ")
    print( ) 
for row in range(10,0,-1):
     for col in range(0,row):
        print(col,end="")
     print()        
for row in range(1,6):
    for col in range (0,row):
        print(row,end="")
    print()    
for row in range(5,0,-1):
    for col in range(0,row):
        print(row,end="")
    print()    
for row in range(5,0,-1):
    for col in range(0,row):
        print(5,end="")
    print()
for row in range(6,1,-1):
    for col in range(0,row):
        print(col,end="")
    print()    
for row in range(1,10,2):
    for col in range(0,row):
        print(row,end="")
    print()    
for row in range(5,0,-1):
    for col in range(0,row):
        print(row,end="")
    print()   
for row in range(1,6):
    for col in range(row,0,-1):
        print(col,end="")
    print()
for row in range(1,9):
    for col in range(1,row+1):
        print(col*row,end=" ")
    print()    
for values in range(5,0,-1):
    print(values*"*")
    
for row in range(1,5):
    for col in range(5,row,-1):
        print(" ",end="")
    for col in range(0,row):
        print(" * ",end="")
    print()  
    
    
for row in range(6,0,-1):
    for col in range(6,row,-1):
        print(" ",end="")
    for col in range(0,row):
        print("*",end="")
    print()    
for row in range(1,6):
    for col in range(6,row,-1):
        print("",end="")
    for col in range(0,row):
        print("*",end="")
    print()   
    
    
for row in range(6,0,-1):
    for col in range(6,row,-1):
        print("",end="")
    for col in range(0,row):
        print("*",end="")
    print()    
for row in range(1,7):
    for col in range(7,row,-1):
        print("",end="")
    for col in range(0,row):
        print("*",end="")
    print()   
for row in range(7,0,-1):
    for col in range(7,row,-1):
        print("",end="")
    for col in range(0,row):
        print("*",end="")
    print()    
    
    
for row in range(5,0,-1):
    for col in range(5,row,-1):
        print(" ",end="")
    for col in range(0,row):
        print("*",end=" ")
    print()    
for row in range(1,6):
    for col in range(5,row,-1):
        print(" ",end="")
    for col in range(0,row):
        print("*",end=" ")
    print()    
    

list1=[1,2,3,4,5,6]

result=0
for value in list1:
    result=result+value
result
result=0
for index in range(0,9):
    result=result+list1[index]
result 

result=0
for index in range(0,6):
    result=result+list1[index]
result    