#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 18:24:13 2020

@author: f4him
"""
import math
socks,day=map(int, input().split())

def day_counter(socks,day):
    days=0
    days+= socks    
    if (math.floor(socks/day)) >= day:
        days+=day_counter(math.ceil(socks/day),day)
    else:
        days+=math.floor(socks/day)
        
    return days


print(day_counter(socks, day))