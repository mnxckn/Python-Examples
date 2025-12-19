# -*- coding: utf-8 -*-
"""
Created on Thu Dec 11 20:19:07 2025

@author: HP
"""
for value in range(1,6):
    print("*"*value)
    
    
#funcion definition:
    
def hello():
    for value in range(1,6):
        print("*"*value)
hello()    #function calling

def beat(a):
    for value in range(1,a):
        print("*"*value)
        
beat(9)
def beat(a,b):
    for value in range(1,a):
        print(b*value)

beat(6,"&")

def beat(a=5,b="*"):
    for value in range(1,a):
        print(b*value)
        
beat(8,"%")


def starpattern(a,b):
    for row in range(a,0,-1):
        for col in range(a,row,-1):
            print(" ",end="")
        for col in range(0,row):
            print(b,end=" ")
        print()
    
    
starpattern(10,"^")

#for default
def key(a, b=10):
    for value in range(a,b):
        print(value*"*")
        
key(3)

key(3,15)


def pro(): 
    list=[]
    for  values in range(0,6):
        data=int(input("enter any value"))
        list.append(data)
        
         
pro()

def pro(a): 
    list1=[]
    for  values in range(0,a):
        data=int(input("enter any value"))
        list1.append(data)
    return list1
        
pro(3)

list6=[1,56,77,89,88,95,80]
def hp(list8):
    list2=[]
    list3=[]
    for values in list8:
        if values%2==0:  
            list2.append(values)
        else:
            list3.append(values)
    return list2,list3    
    
        

hp(list6)


#prime numbers
def prime(num): 
    
    for values in range(2,num):
        if num%values==0:
            break
    if values==num-1:
            print('prime')
    else:
            print('not prime')
    
    
prime(16)    


def sum(list1):
    result=0
    for values in list1:
        result=result+value
    returnresult    
    
list1=[1,2,3,4,5]    
sum(list1)+77
