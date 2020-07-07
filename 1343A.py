#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 17:08:12 2020

@author: f4him
"""
t=int(input())
for i in range(t):
    num=int(input())
    for k in range(2,30):
        if num%(pow(2,k)-1)==0:
            print(num//(pow(2,k)-1))
            break

