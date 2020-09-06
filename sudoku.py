from random import randint, shuffle

""" 
sudoku puzzles to test
board has 2 solutions
board1 has 1 solution
board3 has 8 solutions
"""

board = [
    [9, 0, 6, 0, 7, 0, 4, 0, 3],
    [0, 0, 0, 4, 0, 0, 2, 0, 0],
    [0, 7, 0, 0, 2, 3, 0, 1, 0],
    [5, 0, 0, 0, 0, 0, 1, 0, 0],
    [0, 4, 0, 2, 0, 8, 0, 6, 0],
    [0, 0, 3, 0, 0, 0, 0, 0, 5],
    [0, 3, 0, 7, 0, 0, 0, 5, 0],
    [0, 0, 7, 0, 0, 5, 0, 0, 0],
    [4, 0, 5, 0, 1, 0, 7, 0, 8]
]

board1 = [
    [6, 8, 5, 0, 3, 0, 4, 0, 7],
    [0, 0, 0, 8, 0, 0, 0, 2, 0],
    [0, 1, 0, 4, 0, 0, 5, 0, 0],
    [0, 9, 0, 3, 0, 0, 0, 0, 5],
    [0, 4, 0, 0, 0, 0, 6, 0, 0],
    [5, 0, 8, 0, 0, 4, 0, 3, 0],
    [9, 2, 6, 0, 7, 8, 3, 0, 0],
    [8, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 3, 0, 0, 0, 0, 1, 9]
]

board3 = [
    [0, 0, 9, 8, 0, 0, 0, 0, 2],
    [0, 0, 0, 3, 1, 2, 8, 9, 0],
    [2, 0, 8, 0, 6, 9, 0, 0, 0],
    [0, 5, 0, 6, 2, 0, 0, 0, 1],
    [0, 0, 1, 4, 0, 8, 0, 2, 0],
    [6, 0, 0, 0, 9, 1, 0, 4, 0],
    [0, 0, 0, 0, 7, 6, 4, 0, 3],
    [0, 0, 7, 0, 8, 5, 0, 0, 9],
    [1, 0, 0, 9, 0, 0, 2, 0, 0]
]

"""
Sudoku solver logic:
1. Find the empty cell on the grid
- Find from top to bottom, left to right
2. Using backtracking to find the right number
- Check whether the number is satisfy the sudoku requirements
- If yes then move on to the next cell
- If no then move to the next number. If all the options are not valid, 
move back to the previous cell and chose the next option
- Continue until the sudoku board is filled

Sudoku generator logic:
1. Generate the normal 9x9 board/grid
2. Fill the grid with the sudoku requirements
- Each row, column and block is filled with number from 1-9, without repeating any number within them.
2.1 Randomly chose the number from 1 to 9 and fill it into the grid
2.2 Each time the number is chosen, check whether it satisfy the requirements. If not, choose another one
2.3 Repeat the process until the board is filled
3. Start to remove each cell one by one to create a sudoku puzzle
- Randomly remove a cell in the board (if it is not removed yet)
- Use the sudoku solver to check how many solution the puzzle has.
- If there are more than 1 solution, then return the value to the removed cell, and start the process again
- If there is only 1 solution, then move on and continue to randomly remove another cell.
"""


def generate_board():
    empty_board = []
    i=0
    while i < 9:
        empty_board.append([0,0,0,0,0,0,0,0,0])
        i+=1
    return empty_board


def print_board(bo):
    count = 0
    for r in range(len(bo)):
        if r % 3 == 0 and r != 0:
            print('----------------------------------')
        for c in range(len(bo)):
            if c % 3 == 0 and c != 0:
                print(' | ', end=' ')
            print(str(bo[r][c]) + ' ', end=' ')
            count += 1
            if count % 9 == 0 and count != 0:
                print('')


def find_empty(bo):
    for r in range(len(bo)):
        for c in range(len(bo)):
            if bo[r][c] == 0:
                return (r, c)
    return None


def valid(bo, num, pos):
    # check row
    for c in range(len(bo)):
        if bo[pos[0]][c] == num and pos[1] != c:
            return False

    # check column
    for r in range(len(bo)):
        if bo[r][pos[1]] == num and pos[0] != r:
            return False

    # check block
    row_box = pos[0] // 3
    col_box = pos[1] // 3

    for r in range(row_box * 3, row_box * 3 + 3):
        for c in range(col_box * 3, col_box * 3 + 3):
            if bo[r][c] == num and (r, c) != pos:
                return False
    return True


def count_solutions(bo):
    global counter
    find = find_empty(bo)
    if not find:
        counter +=1
        return None
    else:
        r, c = find

    for num in range(1, 10):
        if valid(bo, num, (r, c)):
            bo[r][c] = num
            if count_solutions(bo):
                return True
            else:
                bo[r][c] = 0
    return False


def solve(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        r, c = find

    for num in range(1, 10):
        if valid(bo, num, (r, c)):
            bo[r][c] = num
            if solve(bo):
                return True
            else:
                bo[r][c] = 0
    return False


def fill_board(bo):
    find = find_empty(bo)
    if not find:
        return True
    else:
        r, c = find

    shuffle(numberList)
    for value in numberList:
        if valid(bo,value,(r,c)):
            bo[r][c] = value
            if fill_board(bo):
                return True
            else:
                bo[r][c] = 0
    return False


def sudoku_gen(bo, attempts):
    """
    :param attempts: the number of time the fuction try to remove the cell, more attempt means more cells are removed
    """
    global counter
    while attempts > 0:
        # Select a random cell
        row = randint(0, 8)
        col = randint(0, 8)
        while bo[row][col] == 0:
            row = randint(0, 8)
            col = randint(0, 8)
        # Backup the cell value
        backup = bo[row][col]
        bo[row][col] = 0

        # Copy the board
        copyBoard = []
        for r in range(0, 9):
            copyBoard.append([])
            for c in range(0, 9):
                copyBoard[r].append(bo[r][c])

        counter = 0
        count_solutions(copyBoard)
        # if there are more than 1 solution, return the value to the cell
        if counter != 1:
            bo[row][col] = backup
            attempts -= 1

if __name__ == "__main__":
    # create a list for fill grid
    numberList = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    # Now start to generate the sudoku puzzle and solve it
    grid = generate_board()
    fill_board(grid)
    print('full grid')
    print_board(grid)
    print('\n')


    sudoku_gen(grid, 5)
    print('sudoku')
    print_board(grid)
    print('\n')

    solve(grid)
    print('solved')
    print_board(grid)
