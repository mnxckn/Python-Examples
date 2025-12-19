# -*- coding: utf-8 -*-
"""
Created on Sat Nov 29 10:56:59 2025

@author: HP
"""

            
result=0           
data=input("enter a number for armstrong or not")
for value in data:
      result=result+int(value)**len(data)
if data==str(result):
   print("armstrong number")
else:
   print("not armstrong")

