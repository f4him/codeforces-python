#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  7 16:26:06 2020

@author: f4him
"""
song=input()
pattern="WUB"

new = song.replace("WUB", " ").strip()
print(new)