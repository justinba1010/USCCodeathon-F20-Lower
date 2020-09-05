n = int(input())
l = [int(x) for x in input().split()]
average = sum(l)//n
sorted(l)
median = int(l[n//2] + l[(n-1)//2])//2

def letter(x):
    if x >= 90:
        return "A"
    if x >= 80:
        return "B"
    if x >= 70:
        return "C"
    if x >= 60:
        return "D"
    return "F"

print(letter(average) + " " + letter(median))
