# -*- coding: utf-8 -*-
"""
Created on Fri May  4 15:06:30 2018

@author: vdhei
"""
from math import sin,cos,acos,radians,degrees

A_lat=radians(float(input("Point A Latitude: ")))
A_lon=radians(float(input("Point A Longitude: ")))
B_lat=radians(float(input("Point B Latitude: ")))
B_lon=radians(float(input("Point B Longitude: ")))

dist=6371*acos(cos(A_lat)*cos(B_lat)*cos(B_lon-A_lon)+sin(A_lat)*sin(B_lat))
dir_AB=degrees(acos(cos(A_lat)*sin(B_lat)-sin(A_lat)*cos(B_lat)*cos(B_lon-A_lon)))%360
dir_BA=degrees(acos(cos(B_lat)*sin(A_lat)-sin(B_lat)*cos(A_lat)*cos(A_lon-B_lon)))%360
               
print("Dist= ",dist)  
print("A to B: ",dir_AB)
print("B to A: ",dir_BA)             