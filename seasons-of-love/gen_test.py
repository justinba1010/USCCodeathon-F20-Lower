import os
import random
from random import randint
import subprocess

os.makedirs("input", exist_ok=True)
os.makedirs("output", exist_ok=True)

cases = randint(1, 200)
print(cases)
for t in range(cases):
    s = randint(0, 2**32)
    DATES = {
        's': 1,
        'm': 60,
        'h': 60*60,
        'd': 60*60*24,
        'w': 60*60*24*7,
        'mo': 60*60*24*30,
        'y': 60*60*24*365,
    }
    d, frac = random.choice(list(DATES.items()))
    print("{} {}".format(s//frac, d))
    #input = "{} {}".format(s//frac, d)
    #with open("input/{}".format(i), 'w') as f:
        #f.write(input)
    #output = subprocess.run(["python3", "solutions/solution.py"], capture_output=True, input=input, check=True, text=True).stdout
    #with open("output/{}".format(i), 'w') as f:
        #f.write(output)
