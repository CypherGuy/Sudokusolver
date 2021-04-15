#We define the board here. Remember to replace any gaps in the puzzle with 0's.
board = [
     [0, 9, 0, 0, 0, 3, 6, 0, 0],
     [0, 0, 0, 1, 0, 0, 2, 0, 0],
     [3, 0, 2, 0, 0, 6, 0, 9, 8],
     [0, 0, 0, 0, 0, 0, 1, 2, 5],
     [0, 0, 4, 0, 0, 0, 8, 0, 0],
     [5, 2, 9, 0, 0, 0, 0, 0, 0],
     [2, 4, 0, 7, 0, 0, 5, 0, 3],
     [0, 0, 3, 0, 0, 2, 0, 0, 0],
     [0, 0, 8, 3, 0, 0, 0, 1, 0]
 ] 
def findEmpty(board): #Function to find empty squares.
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) #row, column
    return None

def valid(board, num, pos): #Function to determine if the number to place there is valid.
    row = pos[0] #X coordinate
    column = pos[1] #Y coordinate
     
    #checking rows for the same number
    for i in range(len(board[0])):
        if board[row][i] == num and column != i:
            return False
    #checking columns
    for i in range(len(board)):
        if board[i][column] == num and row != i:
            return False
    
    #checking each box
    startRowBox = row//3 
    startColumnBox= column//3
    for i in range(startRowBox*3, (startRowBox*3)+3):
        for j in range(startColumnBox*3, (startColumnBox*3)+3):
            if board[i][j] == num and row != i and column != j:
                return False
    return True

def printBoard(board): #This print the start and end product
    if not findEmpty(board):
        print("\nFinished puzzle\n")
    else:
        print("\nUnsolved puzzle\n")
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")
            
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            
            print(str(board[i][j])+" ", end="")
        print("\b") #Convert to bytes object, making everything neater
    
    
        
def solve(board):
    find = findEmpty(board) #First we look for empty spaces.
    
    if not find:
        return True
    else:
        row, col = find #We get the 'coordinates' of the box that's empty
    
    for i in range(1,10):
        if valid(board, i, find):
            board[row][col] = i
            
            if solve(board):
                return True
            
            board[row][col] = 0
    return False
             
printBoard(board)      #printing the board before solving the puzzle
solve(board)           #solving the puzzle
printBoard(board)      #printing the puzzle after solving
