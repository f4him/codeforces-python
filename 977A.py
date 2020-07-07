#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 14:20:59 2020

@author: f4him
"""

num, time = map(int,input().split())

for i in range(time):
    if num%10==0:
        num=num/10
    else:
        num-=1
print(int(num))
    