# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from math import factorial

n=range(100)
s=[0]

for i in n:
    s.append(s[-1]+(((2**i)*factorial(i))/i**i))

s=s[1:]
plt.plot(n,s)
