"""Eight queens"""

N = 8 # no. of queens

board = [[0] * N for _ in range(N)] # creating chessboard [8 X 8] matrix initially set to 0.

def N_queens(n): #function to place the queens
    #replace the value 0 in the board with 1 value if the queen can be placed there
    if n == 0:
        return True

    for i in range(0, N):
        for j in range(0, N):
            if (not(attack(i,j))) and (board[i][j] != 1):
                board[i][j] = 1

                #backtrack
                if N_queens(n-1):
                    return True
                board[i][j] = 0

    return False       


#function to check the position of the queen to be placed.
def attack(i, j): 
    #horizontal and vertical check
    for k in range(0, N):
        #if queen is already placed in that position return true
        if board[i][k] == 1 or board [k][j] == 1:
            return True
        
    #diagonal check
    for k in range(0, N):
        for l in range(0, N):
            if (k+l == i+j) or (k-l == i-j):
                if board[k][l] == 1:
                    return True
    
    return False

N_queens(N)

for i in board:
    print(i)

# if queen is already placed in that position return true

# display the board ater placing all the queens