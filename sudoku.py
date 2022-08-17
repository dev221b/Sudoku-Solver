def find_next_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == 0:
                return r,c
    return None, None #if no spaces are there in the puzzle  

def is_valid(puzzle, guess, row, col):

    #starts solving with checking rows
    row_vals = puzzle[row]
    if guess in row_vals:
        return False

    #checking columns
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    
    #checking the grid
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    row_end = row_start + 3
    col_end = col_start + 3
    for i in range(row_start, row_end):
        for j in range(col_start, col_end):
            if guess == puzzle[i][j]:
                return False

    return True

def solve_sudoku(puzzle):
    row, col = find_next_empty(puzzle)

    if row is None:
        return True

    for guess in range(1,10):
        if is_valid(puzzle, guess, row, col):
            puzzle[row][col] = guess
            if solve_sudoku(puzzle):
                return True
        
        puzzle[row][col] = 0

    return False

if __name__ == '__main__':
    sudoku_board = [
        [0, 0, 0,   0, 9, 7,   6, 0, 2],
        [0, 0, 0,   0, 0, 3,   1, 0, 0],
        [3, 0, 0,   0, 2, 0,   0, 0, 0],
        [0, 0, 1,   4, 0, 0,   0, 0, 6],
        [0, 0, 0,   6, 0, 0,   0, 0, 3],
        [0, 7, 0,   0, 0, 0,   0, 0, 0],
        [4, 0, 0,   0, 0, 0,   2, 5, 0],
        [0, 0, 9,   2, 1, 0,   0, 0, 0],
        [0, 6, 5,   0, 0, 9,   0, 7, 0]
    ]
    print(solve_sudoku(sudoku_board))
    print(sudoku_board)