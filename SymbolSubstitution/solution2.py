x = int(input())
seen = []
for i in range(x):
    line = input().split(" ")
    (a,b,c) = (int(line[0]), int(line[2]), int(line[4]))
    output = ""
    if line[1] in seen:
        print("seen")
        continue
    seen.append(line[1])
    if a + b == c:
        output += "+"
    if a - b == c:
        output += "-"
    if a * b == c:
        output += "*"
    if b != 0 and a / b == c:
        output += "/"
    print(output)
