# -*- coding: utf-8 -*-
"""
Created on Wed Dec 17 09:24:28 2025

@author: HP
"""

def hello():
    for value in range(0,6):
        print(value*"*")
        
hello()

def hello(a=2):
    for value in range(a,10):
        print(value*"*")
        
        
hello()

def beat():
    for row in range(0,6):
        for col in range(0,row):
            print(row,end="")
        print()
            
            
beat()


def prime(num):
    for value in range(2,num):
        if num%value==0:
            break
    if value==num-1:
            print("prime")
    else:
            print("non prime")    
         
            
prime(8)      

def list_fun(*args):
    print(args)
    result=0
    for value in args:
        result+=value
    return result
list_fun(1)
list_fun(1,2,3,56,123,34)
        

def list_fun(*args):
    print(args)
    result=0
    for value in args:
        if value%2==0: 
            result+=value
    return result


list_fun(1,2,3,56,123,34)


def list_fun(*args):
    print(args)
    result=[]
    for value in args:
        if value%2==0:  
            result.append(value)
    return result
       
list_fun(1,2,3,4,5,6)

args=[1,2,3,4,5]
result=[]
for value in args:
    if value%2==0:  
        result.append(value)
result


def list_fun(*args):
    num=args 
    for value in range(2,num):
        if num%value==0:
            break
    if value==num-1:
            print("prime")
    else:
            print("non prime")    
         
list_fun(1,2,3,4,5,6,7,8) 
list1=[3,4,5,6,7,8]
primelist=[]
for values in list1:    
    num=values
    for value in range(2,num):
        if num%value==0:
            break
    if value==num-1:
        print("prime")
        primelist.append(num)
    else:
        print("non prime")
primelist

def primechecking(*list1):
    primelist=[]
    for values in list1:    
        num=values
        for value in range(2,num):
            if num%value==0:
                break
        if value==num-1:
            print("prime")
            primelist.append(num)
        else:
            print("non prime")
    return primelist

primechecking(3,4,5,6,7,8,9)


num=15
result=0
for values in range(1,num):
    if num%value==0:
        print(values)
        result=result+value
if num==result:
    print("perfect number")
else:
    print("non perfect")    
    
def perfectchecking(*list2):
    perfectlist=[]
    for values in list2:
        num=values
        for values in range(1,num):
             if num%value==0:
                 print(values)
                 result=result+value
        if num==result:
            print("perfect number")
            list2.append(perfectlist)
    else:
        print("non perfect")    
        

def perfect(num):
    result=0
    for values in range(1,num):
        if num%values==0:
            print(values)
            result=result+values
    if num==result:
        print("perfect number")
    else:
        print("non perfect") 
        
perfect(6)
list1=[6,7,8,9,12]
list2=[]
for value in list1:
    num=value
    result=0
    for values in range(1,num):
        if num%values==0:
            print(values)
            result=result+values
    if num==result:
        print("perfect number")
        list2.append(num)
    else:
        print("non perfect") 
        
list2

def perfectstar(*list1):
    list2=[]
    for value in list1:
        num=value
        result=0
        for values in range(1,num):
            if num%values==0:
                print(values)
                result=result+values
        if num==result:
            print("perfect number")
            list2.append(num)
        else:
            print("non perfect") 
    return list2
perfectstar(6,9)
