#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 14:26:02 2020

@author: f4him
"""

word = input()
u=0
l=0
for i in word:
    if i.isupper():
        u+=1
if u>(len(word)/2):
    print(word.upper())
else:
    print(word.lower())
