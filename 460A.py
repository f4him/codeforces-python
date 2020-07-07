#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 18:24:13 2020

@author: f4him
"""
import math
socks,day=map(int, input().split())


print( socks + math.floor((socks-1)/(day-1)))