#max value that it works for is 26
#if greater, repeat is every 125, until a value of 126
'''
12
30
'''
width = int(input())
# width = 6
height = int(input())
# height = 10
board = [[0 for i in range(width)] for j in range(height)]
# cornerStart = 5
board[0] = [i%10 for i in range(width)]

for i in range(1, height):
    for j in range(0, width):
        # board[i][j] = (board[i-1][j] + board[i][j-1] + board[i-1][j-1]) % 10 
        value = 0
        value += board[i-1][j]
        if j - 1 >= 0:
            value += board[i][j-1]
            value += board[i-1][j-1]
        board[i][j] = value % 10 

[print(*i,sep="") for i in board]
# print(*board[height-1])
