#!/usr/local/bin/python3
from random import randint
numCommands = int(input())
# numTestCases = 8
numTestCases = (numCommands //5 + 2)
print(numTestCases)
maxNK = 1000
# maxVal = 10
if numCommands > 7:
    maxNK = 10000 * (numCommands//2 + 2)
maxVal = 10
for i in range(numTestCases):
    n = maxNK
    k = maxNK
    # n = randint(1, maxNK)
    # k = randint(1, maxNK)
    print(n, k)
    n_list = [randint(-maxVal, maxVal) for j in range(n)]
    k_list = [randint(-maxVal, maxVal) for j in range(k)]
    print(*n_list)
    print(*k_list)
