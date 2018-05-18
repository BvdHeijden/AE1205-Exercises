# -*- coding: utf-8 -*-
"""
Created on Fri May  4 14:38:02 2018

@author: vdhei
"""

time=input("enter a time (hh:mm): ")

hour=int(time[:2])
minute=int(time[3:])

angle_h=hour/12%1
angle_m=minute/60%1

angle=abs(angle_h-angle_m%1)*360

print("angle=",angle)