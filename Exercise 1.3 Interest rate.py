# -*- coding: utf-8 -*-
"""
Created on Fri May  4 15:02:34 2018

@author: vdhei
"""

start=float(input("starting value? "))
rate=float(input("interest rate? (%) "))
years=float(input("# years? "))
            
end=start*(1+rate/100)**years

print("final amount: ",end)