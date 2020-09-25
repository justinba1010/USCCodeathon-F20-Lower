#since the max value is 120, the pattern will repeat every 125
width = int(input())
height = int(input()) % 125
board = [[0 for i in range(width)] for j in range(height)]
# cornerStart = 5
board[0] = [i%10 for i in range(width)]

for i in range(1, height):
    #must be 1 so that 
    for j in range(0, width):
        #it wraps
        # board[i][j] = (board[i-1][j] + board[i][j-1] + board[i-1][j-1]) % 10 
        value = 0
        value += board[i-1][j]
        if j - 1 >= 0:
            value += board[i][j-1]
            value += board[i-1][j-1]
        board[i][j] = value % 10 

# [print(*i,sep="") for i in board]
print(*board[height-1])
