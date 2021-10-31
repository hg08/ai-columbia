#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 14 17:01:53 2018

@author: huang
"""

# To compare two lists
li1 = [1,2,3]
li2 = [2,1,3]
print(li1==li2) 
# To compare two tuples
tup0 = (1,2,3)
tup1 = 1,2,3
tup2 = (1,2,3)
tup3 = (2,3,1)

print(tup1 == tup2)
print(tup0 == tup1)
print(tup0 == tup3)