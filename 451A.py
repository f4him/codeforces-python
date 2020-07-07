#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 16:56:12 2020

@author: f4him
"""

m,n=map(int,input().split())
count=0
while m>0 and n>0:
    count+=1
    m-=1
    n-=1
if count%2==0:
    print("Malvika")
else:
    print("Akshat")