#this is a sudoku solver in python by Alexander Gilman and Chris Gilman, using tkinter as the GUI to display the board.
import tkinter as tk
window = tk.Tk()
#blocks is for checking the values in the same box
blocks={0,1,2,6,7,8}
def solvePuzzle():
#called when you click "solve" on the GUI
    possibleValues = [1,2,3,4,5,6,7,8,9]
    coord = getNext(dataguesses)

    if not coord:
        #if there are no more empty spaces
        return True
    else:
        x,y = coord

    for guess in possibleValues:
        if checkValues(guess, x, y):
            #if it follows the rules of sudoku, input the guess
            text = "inserted {0} in coordinates {1} , {2}".format(guess,x,y)
            print(text)
            tk.Label(text=guess).grid(row=x, column=y)
            dataguesses[x][y] = guess
            #this is the backtracking part
            if solvePuzzle():
                return True
            dataguesses[x][y] = 0
    return False
def checkValues(guess, x, y):
    #checks for sudoku rules of no same numbers in column, row, and square
    #returns true if value is valid guess
    if checkXvalues(guess, x) and checkYvalues(guess, y) and checksquarevalue(guess, x, y):
        return True
    else:
        return False
def getNext(dataguesses):
    #returns coordinates of next empty value
    for i in range(9):
        for j in range(9):
            if dataguesses[i][j] == 0:
                return(i,j)
    return False
def checkXvalues(guess, x):
    #returns true if no same values in row
    if guess in dataguesses[x]:
        return False
    else:
        return True

def checkYvalues(guess, x):
    #returns true if no same values in column
    for i in range(9):
        if guess == dataguesses[i][x]:
            return False
        else:
            pass
    return True
def checksquarevalue(guess, x, y):
    #returns true if no same values in 3x3 square
    if x < 3:
        if y<3:
            for i in range(3):
                for j in range(3):
                    if guess == dataguesses[i][j]:
                        return False
                    else:
                        pass
            return True
        elif y < 6:
            for i in range(3):
                for j in range(3,6):
                    if guess == dataguesses[i][j]:
                        return False
                    else:
                        pass
            return True
        else:
            for i in range(3):
                for j in range(6,9):
                    if guess == dataguesses[i][j]:
                        return False
                    else:
                        pass
            return True
    elif x < 6:
        if y<3:
            for i in range(3,6):
                for j in range(3):
                    if guess == dataguesses[i][j]:
                        return False
                    else:
                        pass
            return True
        elif y < 6:
            for i in range(3,6):
                for j in range(3,6):
                    if guess == dataguesses[i][j]:
                        return False
                    else:
                        pass
            return True
        else:
            for i in range(3,6):
                for j in range(6,9):
                    if guess == dataguesses[i][j]:
                        return False
                    else:
                        pass
            return True
    else:
        if y<3:
            for i in range(6,9):
                for j in range(3):
                    if guess == dataguesses[i][j]:
                        return False
                    else:
                        pass
            return True
        elif y < 6:
            for i in range(6,9):
                for j in range(3,6):
                    if guess == dataguesses[i][j]:
                        return False
                    else:
                        pass
            return True
        else:
            for i in range(6,9):
                for j in range(6,9):
                    if guess == dataguesses[i][j]:
                        return False
                    else:
                        pass
            return True

#creating a 9x9 sudoku board
for i in range(9):
    window.columnconfigure(i, weight=1, minsize=40)
    window.rowconfigure(i, weight=1, minsize=40)
    for j in range(9):
        if i in blocks:
            if j not in blocks:
                frame = tk.Frame(
                    master=window,
                    relief=tk.RAISED,
                    borderwidth=1.25,
                    bg="grey75"
            )
            else:
                frame = tk.Frame(
                    master=window,
                    relief=tk.RAISED,
                    borderwidth=1
                )
        elif i not in blocks:
            if j in blocks:
                frame = tk.Frame(
                    master=window,
                    relief=tk.RAISED,
                    borderwidth=1,
                    bg="grey75"
            )
            else:
                frame = tk.Frame(
                    master=window,
                    relief=tk.RAISED,
                    borderwidth=1
                )
        else:
            frame = tk.Frame(
                master=window,
                relief=tk.RAISED,
                borderwidth=1
            )
        frame.grid(row=i, column=j, sticky="nsew")
#unsolved sudoku puzzles, varying in difficulty.
data= [
        [7, 8, 0, 4, 0, 0, 1, 2, 0],
        [6, 0, 0, 0, 7, 5, 0, 0, 9],
        [0, 0, 0, 6, 0, 1, 0, 7, 8],
        [0, 0, 7, 0, 4, 0, 2, 6, 0],
        [0, 0, 1, 0, 5, 0, 9, 3, 0],
        [9, 0, 4, 0, 6, 0, 0, 0, 5],
        [0, 7, 0, 3, 0, 0, 0, 1, 2],
        [1, 2, 0, 0, 0, 7, 4, 0, 0],
        [0, 4, 9, 2, 0, 6, 0, 0, 7]
    ]
data3 = [
    [5,3,0,0,7,0,0,0,0],
    [6,0,0,1,9,5,0,0,0],
    [0,9,8,0,0,0,0,6,0],
    [8,0,0,0,6,0,0,0,3],
    [4,0,0,8,0,3,0,0,1],
    [7,0,0,0,2,0,0,0,6],
    [0,6,0,0,0,0,2,8,0],
    [0,0,0,4,1,9,0,0,5],
    [0,0,0,0,8,0,0,7,9]
]
data2 = [
    [0,0,7,1,0,0,0,5,0],
    [0,6,0,0,0,0,0,7,0],
    [0,0,0,7,0,0,3,0,4],
    [3,0,0,4,0,0,5,2,0],
    [0,2,0,8,0,5,0,4,0],
    [0,8,4,0,0,3,0,0,6],
    [1,0,5,0,0,2,0,0,0],
    [0,7,0,0,0,0,0,6,0],
    [0,4,0,0,0,9,1,0,0]
    ]
dataguesses = data.copy()
for x in range(9):
    #filling the 9x9 board with the given values of the puzzle
    for y in range(9):
        if data[x][y] == 0:
            pass
        else:
            label= tk.Label(text=dataguesses[x][y]).grid(row=x, column=y)
button = tk.Button(window, text="Solve", fg="red", command=solvePuzzle).grid(row=10, column=4)
window.mainloop()
