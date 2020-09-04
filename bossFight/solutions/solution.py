# bossHealth = 15
bossHealth = int(input())
playerHealth = 100
timestep = 0
restCooldown = 0
poisonCooldown = 0

while bossHealth > 0 and playerHealth > 0:
    restCooldown = max(restCooldown - 1, 0)
    if poisonCooldown:
        playerHealth -= 6
        # print("poison damage")
        poisonCooldown -= 1
        if playerHealth <= 0:
             break
    if restCooldown == 0:
        #this block is one potential solution
        if timestep % 3 == 0 and playerHealth < 60 and timestep % 50 != 0: # any number from 58 to 66 works in a decent amount of time
            restCooldown = 3
            playerHealth = min(100, playerHealth + 15)
            print(2)
        elif timestep % 2 == 0 and restCooldown == 0:
            bossHealth -= 9
            print(1)
        else:
            print(0)


        #this is a second solution, seems most optimal, even without playerHealth < 60
        if timestep % 3 == 0 and timestep % 40 != 0 and playerHealth < 60: #uses 40 because that is when the monster halves the player health (20 is too frequent)
            restCooldown = 3
            playerHealth = min(100, playerHealth + 15)
            print(2)
        elif timestep % 2 == 0:
            bossHealth -= 9
            print(1)
        else:
            print(0)


        
        #naive solution 1, works on low boss health
        # if timestep % 6 == 0 and playerHealth < 40: 
        #     restCooldown = 3
        #     playerHealth = min(100, playerHealth + 15)
        #     print(2)
        # elif timestep % 2 == 0:
        #     bossHealth -= 9
        #     print(1)
        # else:
        #     print(0)

        #naive solution 2
        # if timestep % 3 == 0 and playerHealth < 60: 
        #     restCooldown = 3
        #     print(2)
        #     playerHealth = min(100, playerHealth + 15)
        # elif timestep % 2 == 0:
        #     bossHealth -= 9
        #     print(1)
        # else:
        #     print(0)

        # if timestep % 3 == 0 and timestep  % 10 != 0: 
        #     restCooldown = 3
        #     playerHealth = min(100, playerHealth + 15)
        #     print(2)
        # elif timestep % 2 == 0:
        #     bossHealth -= 9
        #     print(1)
        # else:
        #     print(0)
        
        # if bossHealth <= 0:
        #     break
    else:
        print(0)


    if timestep != 0:
        if timestep % 20 == 0:
            playerHealth -= playerHealth//2
        if timestep % 5 == 0:
            playerHealth -= 11
        if timestep % 14 == 0: # was 17, but that was too easy
            poisonCooldown = 3


    timestep += 1
    # print("timestep", timestep)
    # print("playerHealth:", playerHealth)
    # print("bossHealth:", bossHealth)

# print("playerHealth:", playerHealth)
# print("bossHealth:", bossHealth)
# print("timestep", timestep)

