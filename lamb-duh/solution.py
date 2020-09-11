caseCount = int(input())
for i in range(caseCount):
    a, b = list(map(int, input().split()))
    n = list(map(int, input().split()))
    k = list(map(int, input().split()))
    n_total = sum(n)
    k_total = sum(k)
    answer = n_total + k_total*len(n)
    print(answer)

