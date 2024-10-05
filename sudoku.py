import copy
from sudokuGenerator import get_sudoku


def main():
    original_sudoku = get_sudoku()
    sudoku_to_change = copy.deepcopy(original_sudoku)
    new_i, new_j = next_cell(0, -1,original_sudoku)
    print("Starting algorithm with cell", new_i, new_j)
    board = backtracking_algorithm(sudoku_to_change, original_sudoku, new_i, new_j)

    print_board(original_sudoku)
    print("\n\n")
    print_board(board)


def validate_sudoku(board):
    """Tests if sudoku board is valid"""

    # Analysing rows
    for row in board:
        nums_seen = []
        for num in row:
            if num != 0:
                if num in nums_seen:  # repeat number in row
                    return False
                nums_seen.append(num)

    # Analysing columns
    for i in range(9):
        nums_seen = []
        for row in board:
            if row[i] != 0:
                if row[i] in nums_seen:  # repeat number in column
                    return False
                nums_seen.append(row[i])

    # Analysing 3x3 boxes
    for i in range(3):
        for j in range(3):
            nums_seen = []

            for k in range(3):

                for l in range(3):

                    if board[3 * i + k][3 * j + l] != 0:

                        if (
                            board[3 * i + k][3 * j + l] in nums_seen
                        ):  # repeat number in 3x3 box
                            return False

                        nums_seen.append(board[3 * i + k][3 * j + l])

    return True  # Passed all tests


def backtracking_algorithm(board, original_sudoku, i=0, j=0):
    """
    With backtracking algorithm, resolves sudoku board
    Returns None if no possible valid number is found (so need to backtrack)
    Otherwise returns the completed board

    """
    if i == 9:
        return board

    for num in range(1, 10):
        board[i][j] = num
        if validate_sudoku(board) == True:
            i_temp, j_temp = next_cell(i, j, original_sudoku) # Get next free cell to work on
            result_of_board = backtracking_algorithm(board, original_sudoku, i_temp, j_temp)
            if result_of_board is not None:
                return result_of_board

    board[i][j] = 0
    return None  # No valid number was found for this cell


def print_board(board):
    for row in board:
        print(row)


def next_cell(i, j,original_sudoku):
    """Finds the next free cell (i, j) to process"""
    if j == 8:
        i = i + 1
        j = 0
    else:
        j = j + 1

    if i == 9:
        return i, j

    if original_sudoku[i][j] != 0:  # If cell is not empty, find next cell
        i, j = next_cell(i, j, original_sudoku)

    return i, j


if __name__ == "__main__":
    main()
