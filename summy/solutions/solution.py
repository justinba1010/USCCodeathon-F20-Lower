(_n, k) = [int(x) for x in input().split()]
l = [int(x) for x in input().split()]
l.sort()
print(sum(l[:k]))
print(sum(l[-k:]))
