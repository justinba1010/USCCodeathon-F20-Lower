#!/usr/bin/env python3
DATES = {
        's': 1,
        'm': 60,
        'h': 60*60,
        'd': 60*60*24,
        'w': 60*60*24*7,
        'mo': 60*60*24*30,
        'y': 60*60*24*365,
}

for _ in range(int(input())):
    n, d = input().split()
    print(int(n)*DATES[d])
