import sys
sys.setrecursionlimit(50000)
class Board:
    def __init__(self, playerhealth, monsterhealth, move, index, cooldown, previousmoves):
        self.playerhealth = playerhealth
        self.monsterhealth = monsterhealth
        self.move = move
        self.index = index
        self.children = []
        self.cooldown = cooldown
        self.previousmoves = previousmoves
    def generate_children(self):
        if self.monsterhealth <= 0:
            return self.previousmoves
        children = []
        newindex = self.index + 1
        playerhealth = self.playerhealth
        monsterhealth = self.monsterhealth
        cooldown = max(self.cooldown - 1, 0)
        previousmoves = self.previousmoves[:]
        previousmoves.append(self.move)
        # Generate monster move deterministic
        if newindex % 20 == 0:
            playerhealth = (playerhealth+1)//2
        if newindex > 10 and newindex % 14 in [0,1,2]:
            playerhealth -= 6
        if newindex % 5 == 0:
            playerhealth -= 11
        if playerhealth > 0:
            # Always make a move if possible
            if newindex % 2 == 0 and cooldown == 0:
                newChild = Board(playerhealth, monsterhealth - 9, 1, newindex, cooldown, previousmoves)
                results = newChild.generate_children()
                if results:
                    return results
            if newindex % 3 == 0 and cooldown == 0:
                cooldown = 2
                newChild = Board(min(playerhealth+15, 100), monsterhealth, 2, newindex, 3, previousmoves)
                results = newChild.generate_children()
                if results:
                    return results
            if children == []:
                newChild = Board(playerhealth, monsterhealth, 0, newindex, cooldown, previousmoves)
                results = newChild.generate_children()
                if results:
                    return results
        return None

initialBoard = Board(100, int(input()), 1, 0, 0, [])
results = initialBoard.generate_children()
results_reversed = results[::-1]
x = results_reversed.index(1)
p = results[:-x]
for i in p:
    print(i)
print(len(p))
