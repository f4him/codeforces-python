#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 13:56:01 2020

@author: f4him
"""

a,b = map(int,input().split())
year=0
while a<=b:
    a=3*a
    b=2*b
    year+=1
print(year)