x = int(input())
playerhealth = 100
monsterhealth = x
healthbar = 50
take_break = 0
debug = False
for i in range(8*x):
    if debug:
        print("i: %s, playerhealth: %s, monsterhealth: %s"% (i, playerhealth, monsterhealth))
    # 0   1 2 3 4 5
    # 2/1 0 0 0 1 0
    if i % 6 == 3:
        if playerhealth < healthbar:
            print("2")
            take_break = 2
        elif take_break == 0:
            monsterhealth -= 9
            print("1")
        else:
            print("0")
            take_break -= 1
    elif i % 6 == 0:
        if playerhealth < healthbar:
            print("2")
            take_break = 2
        elif take_break <= 0:
            monsterhealth -= 9
            print("1")
        else:
            print("0")
            take_break -= 1
    elif i % 6 in [2,4]:
        if take_break <= 0:
            monsterhealth -= 9
            print("1")
        else:
            print("0")
            take_break -= 1
    else:
        print("0")
        take_break -= 1

    if i > 0:
        if i % 5 == 0:
            playerhealth -= 11
        if i % 14 in [0,1,2]:
            playerhealth -= 6
        if i % 20 == 0:
            playerhealth /= 2
    if monsterhealth <= 0:
        break
