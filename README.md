# Sudoku solver and generator

In this project I practice the sudoku solver and generator using backtracking concept/algorithm

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
