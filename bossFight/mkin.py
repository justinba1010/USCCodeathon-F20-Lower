#!/usr/local/bin/python3
from random import *
# numCommands = randint(2, 30)
startHealth = int(input())
if startHealth <= 6:
    startHealth *= 25
elif startHealth <= 20:
    startHealth *= 250
elif startHealth == 30:
    startHealth = 10000
else:
    startHealth *= 330

print(startHealth)



