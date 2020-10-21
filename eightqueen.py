chessboard = [[0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0],
              [0, 0, 0, 0, 0, 0, 0, 0]]


def validate_range(i, j):
    return 0 <= i < 8 and 0 <= j < 8


def validate_actual_position(chess_board, i, j):
    return chess_board[i][j] != 1


def validate_right_down(chess_board, i, j):
    is_valid = True
    k = 0
    while i + k < 8 and j + k < 8:
        is_valid = is_valid and chess_board[i + k][j + k] != 1
        k += 1

    return is_valid


def validate_right_up(chess_board, i, j):
    is_valid = True
    k = 0
    while i - k > -1 and j + k < 8:
        is_valid = is_valid and chess_board[i - k][j + k] != 1
        k += 1

    return is_valid


def validate_left_down(chess_board, i, j):
    is_valid = True
    k = 0
    while i + k < 8 and j - k > -1:
        is_valid = is_valid and chess_board[i + k][j - k] != 1
        k += 1

    return is_valid


def validate_left_up(chess_board, i, j):
    is_valid = True
    k = 0
    while i - k > -1 and j - k > -1:
        is_valid = is_valid and chess_board[i - k][j - k] != 1
        k += 1

    return is_valid


def validate_down(chess_board, i, j):
    is_valid = True
    k = 0
    while i + k < 8:
        is_valid = is_valid and chess_board[i + k][j] != 1
        k += 1

    return is_valid


def validate_up(chess_board, i, j):
    is_valid = True
    k = 0
    while i - k > -1:
        is_valid = is_valid and chess_board[i - k][j] != 1
        k += 1

    return is_valid


def validate_left(chess_board, i, j):
    is_valid = True
    k = 0
    while j - k > -1:
        is_valid = is_valid and chess_board[i][j - k] != 1
        k += 1

    return is_valid


def validate_right(chess_board, i, j):
    is_valid = True
    k = 0
    while j + k < 8:
        is_valid = is_valid and chess_board[i][j + k] != 1
        k += 1

    return is_valid


def validate_attemp(chess_board, i, j):
    return validate_actual_position(chess_board, i, j) and validate_right_down(chess_board, i, j) and validate_right_up(chess_board, i, j) and validate_left_down(chess_board, i, j) and validate_left_up(chess_board, i, j) and validate_down(chess_board, i, j) and validate_up(chess_board, i, j) and validate_right(chess_board, i, j) and validate_left(chess_board, i, j)


def verify_end(chess_board):
    queens_number = 0
    for i in range(0, 8):
        for j in range(0, 8):
            if chess_board[i][j] == 1:
                queens_number += 1
    return queens_number == 8


def print_solution(chess_board):
    print("SOLUTION FOUND")
    for i in range(0, 8):
        print(chess_board[i])
    print


def calculate_eight_queen(chess_board, j):
    if j == 8:  # GOAL
        if verify_end(chess_board):
            print_solution(chess_board)
    else:
        for i in range(0, 8):
            if validate_attemp(chess_board, i, j):      # CHOICE
                chess_board[i][j] = 1
                calculate_eight_queen(chess_board, j + 1)
            chess_board[i][j] = 0   # BACKTRACK


if __name__ == "__main__":
    calculate_eight_queen(chessboard, 0)
