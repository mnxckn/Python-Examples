# -*- coding: utf-8 -*-
"""
Created on Tue Nov 18 09:19:13 2025

@author: HP
"""

list1=[1,2,3,4,5]

result=0
for values in list1:
    result=result+values
result

result=0
for index in range(0,5):
    result=result+list1[index]
result    


list=[2,4,6,8,10]

result=0
for values in list:
    result=result+values
result

result=0
for index in range(0,5):
    result=result+list[index]
result    

list2=[2,2,2,2,2]

result=0
for values in list2:
    result=result+values
result    

result=0
for index in range(0,5):
    result=result+list2[index]
result    

result=1
for values in list2:
    result=result*values
result    

result=1
for values in list1:
    result=result*values
result

result=1
for index in range(0,5):
    result=result*list1[index]
result
