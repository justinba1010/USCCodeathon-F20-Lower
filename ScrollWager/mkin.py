#!/usr/local/bin/python3
from random import randint
xVal = randint(4, 120)
yVal = int(input())
if yVal <= 15:
    yVal = 2** yVal
else:
    yVal = 2 ** (24 +(yVal % 5)) + (yVal * 100000)
print(xVal)
print(yVal)