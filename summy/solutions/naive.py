(n, k) = [int(x) for x in input().split()]
listy = [int(x) for x in input().split()]
maxes = listy[:]
mins = listy[:]
maxy = 0
miny = 0


for i in range(k):
    a = max(maxes)
    b = min(mins)
    maxy += a
    miny += b
    maxes.remove(a)
    mins.remove(b)
print(miny)
print(maxy)
