#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 17:27:27 2020

@author: f4him
"""
x = int(input())

if x<0:
    m=abs(x)
    if (m%10)>int(m/10)%10:
        print(int((-1)*m/10))
    else:
        print((-1)*(int(m/100)*10+m%10))



else:
    print(x)
    