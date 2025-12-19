# -*- coding: utf-8 -*-
"""
Created on Sun Nov 16 13:04:47 2025

@author: HP
"""

dict1={'name':'akthar','age':'23','occupation':'student','place':'anakkayam'}
id(dict1)
type(dict1)
dir(dict1)
dict1['name']
dict1['age']
dict1['country']='india'
dict1
dict1['country']='usa'
dict1
dict2=dict1.copy()
dict2
dict2.clear()
dict1.popitem()
dict1.pop('age')
dict1
dict1['age']=23
dict1['country']='india'
dict1
dict1.items()
dict1.keys()
dict1.setdefault('country','india')
dict1.values()
