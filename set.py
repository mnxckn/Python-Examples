# -*- coding: utf-8 -*-
"""
Created on Sun Nov 16 12:09:01 2025

@author: HP
"""
data1={10,2.6,'akthar',40+5j,True}
data2={10,2.6,'akthar',True,5,6.0,'beat',40+5j}
data1.difference(data2)
data2.difference(data1)
data1.intersection(data2)
data1.issuperset(data2)
data2.issubset(data1)
data2.issuperset(data1)
data1.issubset(data2)
data2.pop()
data1.union(data2)
data1
data3=data1.copy()
data3
data3.clear()
data3
data1.isdisjoint(data2)
data4={5,7,3,False,50+3j,6.9}
data1.isdisjoint(data4)
data1.symmetric_difference(data2)
