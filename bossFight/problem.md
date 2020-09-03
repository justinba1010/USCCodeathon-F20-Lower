A monster is attacking! It has predictable movements, so maybe you can predict its future movements in order defeat it!

during timestep 0, the monster is charging up, and does not use any attacks

if a timestep is divisible by 5, the monster fires an attack that deals 15 damage.

<!-- if a timestep is divisible by 7, the monster fires an attack that stays on the ground for 3 time steps. While on the ground, the player loses 10 health each timestep -->

if a timestep is divisible by 20, the monster fires an attack that deals damage equal to half of your current health, rounded down (i.e. if you have 60 health and get hit by this attack, you go to 30 health. If you had 21 health, you would lose 10 health, bringing you to 11)


if a timestep is divisible by two, you have the option to fire a shot from your anti-monster gun, which deals 9 damage to the monster

if a timestep is divisible by three, you have the option to heal yourself by 15 health (if the player health is increased above 100, the health is reduced back to 100), but at the cost of resting (not doing anything) for the next two time steps 


first line is boss health

