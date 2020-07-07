#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 16:18:19 2020

@author: f4him
"""

a = int(input())
b = [int(i) for i in input().split()]


b.sort()
for i in b:
    print(i,end=" ")