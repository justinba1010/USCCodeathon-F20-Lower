#!/usr/local/bin/python3
from random import *
numCommands = randint(10, 10)
# numCommands = int(input())
print(numCommands)
maxVal = 20
for i in range(numCommands):
    a = randint(0, maxVal)
    letter = chr(randint(65, 90))
    b = randint(0, maxVal)
    hiddenSymbol = choice(["+", "-", "*", "/"])
    if hiddenSymbol == "/" and b == 0:
        hiddenSymbol = choice(["+", "-", "*"])
    if hiddenSymbol == "/":
        a = randint(0, maxVal) * b
    
    answer = eval(str(a)+hiddenSymbol+str(b))
    print(a, letter, b, "=", int(answer))


