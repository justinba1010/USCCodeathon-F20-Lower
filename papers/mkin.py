import random
n = int(input())
x = [str(random.randint(0, 100)) for _ in range(n)]

print(n)
print(" ".join(x))
