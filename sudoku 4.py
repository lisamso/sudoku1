import random
board = []
blanks = []

def emptyCell():
    cell = [[0,0,0],[0,0,0],[0,0,0]]
    return cell

def emptyBoard():
    board = []
    for i in range(9):
        board.append(emptyCell())
    return board

def generateNumber(poss):
    a = random.choice(poss)
    return a

def printBoard(board):
    print("         SUDOKU          ")
    print("|-----------------------|")
    for cellRow in range (3):
        for row in range (3):
            s = "| "
            for cell in range(3):
                for element in range(3):
                    s+=str(board[(cellRow*3) + cell][row][element])
                    s+= " "
                s+=("| ")
            print(s)
        print("|-----------------------|")
    


def generateCell():
    cell = emptyCell()
    p = [1,2,3,4,5,6,7,8,9]
    for row in cell:
        for i in range(3):
            a = random.choice(p)
            row[i] = a
            p.remove(a)
    return cell

def generateSeed(board):
    print("Loading...")
    for i in range(9):
        board[i] = generateCell()
    board = correctBoard(board)
    for i in range(8):  
        board = fillBoardX(board)
        board = correctBoard(board)
        board = fillBoardY(board)
        board = correctBoard(board)
        board = fillBoardCell(board)
        board = correctBoard(board)
    while errorChecksum(board):
        for i in range(9):
            board[i] = generateCell()
        board = correctBoard(board)
        for i in range(8):  
            board = fillBoardX(board)
            board = correctBoard(board)
            board = fillBoardY(board)
            board = correctBoard(board)
            board = fillBoardCell(board)
            board = correctBoard(board)
        
        
    



    print("Loading complete!\nError checksum: ",errorChecksum(board), "\n\n")
    return board


def correctBoard(board):
    for boardRow in range(3):
        for row in range(3):
            p = [1,2,3,4,5,6,7,8,9]
            for cell in range(3):
                for element in board[(3*boardRow) + cell][row]:
                    if element in p:
                        p.remove(element)
                    elif element not in p:
                        board[(3*boardRow) + cell][row][board[(3*boardRow) + cell][row].index(element)] = 0
    for boardCol in range(3):
        for col in range(3):
            p = [1,2,3,4,5,6,7,8,9]
            for cell in range(3):
                for row in board[(cell*3) + boardCol]:
                    if row[col] in p:
                        p.remove(row[col])
                    elif row[col] not in p:
                        board[(cell*3) + boardCol][board[(cell*3) + boardCol].index(row)][col] = 0
    for cell in board:
        p = [1,2,3,4,5,6,7,8,9]
        for row in cell:
            for element in row:
                if element in p:
                    p.remove(element)
                elif element not in p:
                    cell[cell.index(row)][row.index(element)] = 0
    
    return board


def errorChecksum(board):
    error = 0
    for cell in board:
        for row in cell:
            for element in row:
                if element == 0:
                    error += 1
    return error


def fillBoardX(board):
    for boardRow in range(3):
        for row in range(3):
            p = [1,2,3,4,5,6,7,8,9]
            for cell in range(3):
                for element in range(3):
                    if board[(boardRow*3) + cell][row][element] in p:
                        p.remove(board[(boardRow*3) + cell][row][element])
            for cell in range(3):
                for element in range(3):
                    if board[(boardRow*3) + (2-cell)][row][2-element] == 0:
                        a = random.choice(p)
                        board[(boardRow*3) + (2-cell)][row][2-element] = a
                        p.remove(a)                
    return board

def fillBoardY(board):
    for boardCol in range(3):
        for col in range(3):
            p = [1,2,3,4,5,6,7,8,9]
            for cell in range(3):
                for element in range(3):
                    if board[(cell * 3) + boardCol][element][col] in p:
                        p.remove(board[(cell * 3) + boardCol][element][col])
            for cell in range(3):
                for element in range(3):
                    if board[((2-cell) * 3) + boardCol][(2-element)][col] == 0:
                        a = random.choice(p)
                        board[((2-cell) * 3) + boardCol][(2-element)][col] = a
                        p.remove(a)
    return board
                
                
                
def fillBoardCell(board):
    for cell in board:
        p = [1,2,3,4,5,6,7,8,9]
        for row in cell:
            for element in row:
                if element in p:
                    p.remove(element)
        for row in cell:
            for element in row:
                if element == 0:
                    a = random.choice(p)
                    cell[cell.index(row)][row.index(element)] = a
                    p.remove(a)
    return board

def mirrorPair(board):
    cell = random.randint(0,8)
    row = random.randint(0,2)
    element = random.randint(0,2)
    dig = board[cell][row][element]
    return [cell, row, element, dig]

def createPuzzleSeed(board):
    antall = 18
    while antall != 0:
        r = mirrorPair(board)
        if r[3] != " ":
            board[r[0]][r[1]][r[2]] = " "
            board[8 - r[0]][2 - r[1]][2 - r[2]] = " "
            antall -= 1
            blanks.append([r[0],r[1],r[2]])
            blanks.append([8 - r[0], 2 -r[1], 2 -r[2]])
    
    
    return board

def convertUserInput(x,y):
    x -= 1
    y -= 1
    cellX = x//3
    cellY = y//3
    elementX = x%3
    elementY = y%3
    cell = 3*cellY + cellX
    row = elementY
    element = elementX
    return [cell,row,element]
    
    
                    

def userInput():
    x = int(input("x(1-9): "))
    while x > 9 or x < 1:
        print("Your x-value must be an integer between 1 and 9!\n")
        x = int(input("x(1-9): "))
    y = int(input("y(1-9): "))
    while y > 9 or y < 1:
        print("Your y-value must be an integer between 1 and 9!\n")
        y = int(input("y(1-9): "))
    return convertUserInput(x,y)

def userDigit():
    dig = int(input("Enter a value between 1 and 9: "))
    while dig < 1 or dig > 9:
        print("Must be a value between 1 and 9! \n")
        dig = int(input("Enter a value between 1 and 9: "))
    return dig

    
        
def main(board, boardSolution):
    print("")
    while board != boardSolution:
        r = userInput()
        while r not in blanks:
            print("This cell is a given and can not be changed.")
            print("Enter the coordinates of a changable cell \n\n")
            printBoard(board)
            print("")
            r = userInput()
        board[r[0]][r[1]][r[2]] = userDigit()
        printBoard(board)
    s =input("Congratulations. Play again? y = yes, n = no: ")
    if s == "yes" or s == "y" or s == "Yes" or s == "Y" or s == "YEs" or s == "YeS" or s == "YES":
        initiate()
    else:
        exit()
            
        
        
        
    
    
    
def initiate():
    blanks = []
    board = emptyBoard()
    board = generateSeed(board)
    boardSolution = []
    for cell in board:
        c = []
        for row in cell:
            r = []
            for element in row:
                r.append(element)
            c.append(r)
        boardSolution.append(c)
    board = createPuzzleSeed(board)
    printBoard(board)
    main(board,boardSolution)
    

initiate()

