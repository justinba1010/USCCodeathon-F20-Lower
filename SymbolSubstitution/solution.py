caseCount = int(input())
seen = []
for i in range(caseCount):

    equation = input().split()
    # print(equation)
    # print(equation)
    if equation[1] in seen:
        print("seen")
        continue
    else:
        seen.append(equation[1])
    b = int(equation[2])
    a = int(equation[0])
    c = int(equation[4])
    symbols = ["+", "-", "*", "/"]
    for i in symbols:
        if i == "/" and b == 0:
            continue
        eq = eval(str(a)+i+str(b))
        eq = int(eq)
        # print(str(a)+i+str(b), "=", eq)

        if eq == c:
            print(i,end="")
    # if a + b == c:
    #     print("+", end=" ")
    # if a - b == c:
    #     print("-", end=" ")
    # if a * b == c:
    #     print("*", end=" ")
    # if a / b == c:
    #     print("/", end=" ")
    print()