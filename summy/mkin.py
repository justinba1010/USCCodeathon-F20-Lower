import random
(n, k) = [int(x) for x in input().split()]
x = [str(random.randint(-100, 100)) for _ in range(n)]

print(n, k)
print(" ".join(x))
