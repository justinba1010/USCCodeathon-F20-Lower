A monster is attacking! It has predictable movements, so maybe you can predict its future movements in order defeat it!


If a timestep is divisible by 5, the monster fires an attack that deals 11 damage.

If a timestep is divisible by 14, the monster fires an attack that stays on the ground for 3 time steps. While on the ground, the player loses 6 health each timestep

If a timestep is divisible by 20, the monster fires an attack that deals damage equal to half of your current health, rounded down (i.e. If you have 60 health and get hit by this attack, you go to 30 health. If you had 21 health, you would lose 10 health, bringing you to 11)

If a timestep is divisible by three, you have the option to heal yourself by 15 health but at the cost of resting (not doing anything) for the next two time steps. (The player health cannot go above 100, so if you are at 90 health and heal, your health only goes to 100, not 105), 

If a timestep is divisible by two, you have the option to fire a shot from your anti-monster gun, which deals 9 damage to the monster (If you are not resting)


Note:During timestep 0, the monster is charging up, and does not use any attacks. (But you can)

first line is boss health

