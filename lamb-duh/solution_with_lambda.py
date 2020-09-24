'''input
2
4 7
2 6 9 -7
5 6 8 -3 2 -8 12
5 3
8 4 7 6 12
2 -4 7
'''
cases = int(input())
for i in range(cases):
    _ = input()
    n = list(map(int, input().split()))
    k = list(map(int, input().split()))
    # total = sum(k)
    # n = list(map(lambda x: x+total, n))
    for op in k:
        n = list(map(lambda x: x+op, n))
        # print(n)
    print(sum(n))