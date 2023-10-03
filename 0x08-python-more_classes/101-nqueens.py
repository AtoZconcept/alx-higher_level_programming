#!/usr/bin/python3
import sys

def is_safe(board, row, col):
    # Check if a queen can be placed at board[row][col] without attacking others
    N = len(board)

    # Check the row on the left side
    for i in range(col):
        if board[row][i] == 1:
            return False

    # Check the upper diagonal on the left side
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check the lower diagonal on the left side
    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    return True

def solve_nqueens(board, col):
    N = len(board)

    if col >= N:
        print_solution(board)
        return True

    res = False
    for i in range(N):
        if is_safe(board, i, col):
            board[i][col] = 1
            res = solve_nqueens(board, col + 1) or res
            board[i][col] = 0

    return res

def print_solution(board):
    N = len(board)
    solution = []
    for i in range(N):
        row = ""
        for j in range(N):
            if board[i][j] == 1:
                row += "Q"
            else:
                row += "."
        solution.append(row)
    print("\n".join(solution))
    print()

def nqueens(N):
    if not N.isdigit():
        print("N must be a number")
        sys.exit(1)
    N = int(N)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    if not solve_nqueens(board, 0):
        print("No solution found")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    nqueens(sys.argv[1])
