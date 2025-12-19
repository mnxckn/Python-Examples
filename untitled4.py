# -*- coding: utf-8 -*-
"""
Created on Thu Nov 13 09:29:09 2025
@author: HP
"""

data1={2,"akthar",40+3j,10.5,"akthar",40+3j,2,10.5}

id(data1)
type(data1)
dir(data1)
data1.update()
data1
data2={5,"beat",40+3j,"beat",10.5,40+3j,10.5,5}
data1.union(data2)
data1.difference(data2)
data2.difference(data1)
data1.intersection(data2)
data1.union(data2)
data1.symmetric_difference(data2)
data1.update(data2)
data1
data1.discard(4)
data1.pop()
data1
