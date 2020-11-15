""" board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
] """
board = [
    [0,0,0,4,0,0,1,2,0],
    [0,0,0,0,7,0,0,0,0],
    [0,0,0,0,0,1,0,0,0],
    [0,0,7,0,4,0,2,0,0],
    [0,0,1,0,0,0,0,0,0],
    [9,0,0,0,0,0,0,0,0],
    [0,0,0,3,0,0,0,1,2],
    [0,0,0,0,0,0,4,0,0],
    [0,0,0,0,0,6,0,0,7]
]
def sudokuSolve(board):
    empty_cell = getemptycell(board)
    if empty_cell == None:
        return True
    else: 
        row, col = empty_cell
    
    for i in range(1, 10): #check num (1-9) if it fits our validcell function
        if validcell(board, (row, col), i):
            board[row][col] = i
            #Recursion Start
            if sudokuSolve(board):
                return True
            #reset board if we get a False Return from checking all numbers from 1-9 and None are Valid
            board[row][col] = 0
    return False

def printboard(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0: #does not have ---- lines for first row
            print("- - - - - - - - - - - -")
        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0: 
                print(" | ", end = "")
            if j == 8: # goes to newline and prints last cell in row
                print(board[i][j])
            else:
                print(str(board[i][j]), end = " ")
    return " "
                
def getemptycell(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j) #return row and column index or pos*
    return None

def validcell(board, pos, num): #pos(i,j) is position of given (num)
    #row
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i: #checks for every element in row(pos[0]) and doesnt check itself
            return False
    #column
    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False
    #3x3
    a = pos[0] // 3
    b = pos[1] // 3 #gives you x, y coordinate of current cell location within the 3x3 box as you want to iterate through box
    # board[a][b], (6,8) == (2,2)
    for i in range(a*3, a*3 + 3):
        for j in range(b*3, b*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False
    return True


sudokuSolve(board)
print(printboard(board))

