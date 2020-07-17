#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 22:01:10 2020

@author: RobinHood
"""
a = int(input())

for i in range(0,a):
    x,y,n=map(int,input().split())
    if x*(n//x)+y<=n:
        print(x*(n//x)+y)
    else:
        print(x*(n//x-1)+y)