# -*- coding: utf-8 -*-
"""
Created on Thu Dec  4 10:04:58 2025

@author: HP
"""

list1=[]
for value in range(0,5):
    data=int(input("enter a value"))
    list1.append(data)
list1
result=0
for values in list1:
    result=result+values
result    





list


list2=[]
value=1
while value<7:
    data=int(input("enter a number"))
    list2.append(data)
    value+=1
print()    

list2

result=1
for index in range(0,5):
    result=result*list1[index]
result

result=1
value=1
while value<6:
    result=result+list2[value]
    value+=1
print()    
result

list=[]
value=1
while value<6:
    data=int(input("enter any value"))
    list.append(data)
    value+=1
print()

list
result=1
value=1
while value<5:
    result=result*list[value]
    value+=1
print()    
result
 
list4=[]
value=int(input("enter any value or 0 for exit"))
while value!=0:
    list4.append(value)
    value=int(input("enter any value or 0 for exit"))
print(list4)

list4

list=[]
result=0
for value in range(0,5):
    data=int(input("enter a value"))
    list.append(data)
    if data%2==0:
        result=result+data
list
result


list1=[]
list2=[]
value=int(input("enter any value or 0 for exit"))
while value !=0:
    if value%2==0:
        list1.append(value)
    else:
        list2.append(value)
    value=int(input("enter   any value or 0 for exit"))
print(list1)    



list1=[]
list2=[]
result1=0
result2=0
value=int(input("enter any value or 0 for exit"))
while value !=0:
    if value%2==1:
        result1=result1+value
        list1.append(value)
    else:
        result2=result2+value
        list2.append(value)
    value=int(input("enter   any value or 0 for exit"))
print(list1)    
print(list2)
result1
result2


list3=[]
list4=[]
value=int(input("enter any value or 0 for exit"))
while value!=0:
    if value%2==0:
       list3.append(value)
    else:   
       list4.append(value)
       value=int(input("enter any value or 0 for exit"))
print(list3)
print(list4)


