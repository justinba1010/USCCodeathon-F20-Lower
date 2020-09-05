player = 100
monster = int(input())
bar = 56
cooldown = -1

for i in range(monster*8):
    if player <= 0:
        break
    if monster <= 0:
        break
    if i % 3 == 0 and player < bar:
        player = min(100, player+15)
        print("2")
        cooldown = i+2
    elif i > cooldown and i % 2 == 0:
        print("1")
        monster -= 9
    else:
        print("0")
    if i % 20 == 0 and i > 10:
        player = (player+1)//2
    if i % 5 == 0 and i > 0:
        player -= 11
    if i % 14 in [1,2,0] and i > 10:
        player -= 6
    print("%s %s %s" % (i, player, monster))


