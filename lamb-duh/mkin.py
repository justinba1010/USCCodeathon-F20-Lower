#!/usr/local/bin/python3
from random import *
# numCommands = int(input())
numTestCases = 8
# numTestCases = (numCommands)*6
print(numTestCases)
# maxNK = 100000
# maxVal = 10
maxNK = 10000
maxVal = 1000
for i in range(numTestCases):
    n = maxNK
    k = maxNK
    n = randint(1, maxNK)
    k = randint(1, maxNK)
    print(n, k)
    n_list = [randint(-maxVal, maxVal) for j in range(n)]
    k_list = [randint(-maxVal, maxVal) for j in range(k)]
    print(*n_list)
    print(*k_list)