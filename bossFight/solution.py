bossHealth = 10000
# bossHealth = int(input())
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
        # if timestep % 3 == 0 and playerHealth < 60: # any number from 58 to 66 works in a decent amount of time
        #     restCooldown = 3
        #     playerHealth = min(100, playerHealth + 15)
        # elif timestep % 2 == 0 and restCooldown == 0:
        #     bossHealth -= 9

        #this is a second solution 
        if timestep % 3 == 0 and timestep % 20 != 0: #uses 20 because that is when the monster halves the player health
            restCooldown = 3
            playerHealth = min(100, playerHealth + 15)
        elif timestep % 2 == 0:
            bossHealth -= 9


    if timestep != 0:
        if timestep % 20 == 0:
            playerHealth -= playerHealth//2
        if timestep % 5 == 0:
            playerHealth -= 11
        if timestep % 17 == 0:
            poisonCooldown = 3


    timestep += 1
    # print("timestep", timestep)
    # print("playerHealth:", playerHealth)
    # print("bossHealth:", bossHealth)

print("playerHealth:", playerHealth)
print("bossHealth:", bossHealth)
print("timestep", timestep)

