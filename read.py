# -*- coding: utf-8 -*-
"""
Created on Tue Aug 30 13:41:37 2022

@author: OASoft
"""

file = open(
    'dics/random.txt',
    'r',
    encoding = 'utf_8'
    )

data = file.read()
file.close()

lines = data.split('\n')
for line in lines:
    print(line)