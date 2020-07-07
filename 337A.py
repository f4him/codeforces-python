#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 15:54:44 2020

@author: f4him
"""
s,p =map(int,input().split())
size =[int(i) for i in input().split()]

size.sort()
diff=[]
for i in range(len(size)-s+1):
    diff.append(size[i+s-1]-size[i])
diff.sort()
print(diff[0])