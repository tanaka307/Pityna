# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 13:46:07 2022

@author: OASoft
"""

file = open(
    'dics/random.txt',
    'r',
    encoding = 'utf_8'
    )

lines = file.readlines()
file.close()
    
for line in lines:
    print(line)