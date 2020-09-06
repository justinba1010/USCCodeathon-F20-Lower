from sys import argv
monster = int(argv[1])
x = open(argv[2]).read().split()[:-1]
player = 100
cooldown = 0
minhealth = 100
for (i, move) in enumerate(x):
    cooldown = max(0, cooldown - 1)
    print("timestep: %s, move: %s, player health: %s, monster health: %s" % (i, move, player, monster))
    if move == "0":
       pass 
    elif move == "1" and i % 2 == 0 and cooldown <= 0:
        monster -= 9
    elif move == "2" and i % 3 == 0 and cooldown <= 0:
        cooldown = 2
        player = min(player+15, 100)
    else:
        print("invalid move")
        break
    if monster <= 0:
        print("defeated the monster")
        break
    if player <= 0:
        print("killed")
        break
    if i % 20 == 0 and i > 10:
        player = (player+1)//2
    if i % 14 in [0,1,2] and i > 10:
        player -= 6
    if i % 5 == 0 and i > 1:
        player -= 11
    minhealth = min(player, minhealth)
print("The lowest the player health gets is: %s" % minhealth)


