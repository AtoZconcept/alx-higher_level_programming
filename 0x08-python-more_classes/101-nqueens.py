#!/usr/bin/python3
import sys


def is_safe(board, row, col):
    # Check if a queen can be placed at board[row][col]
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
    sol = []
    N = len(board)
    result = []
    for i in range(N):
        row = []
        for j in range(N):
            if board[i][j] == 1:
                row.append(i)
                row.append(j)
        result.append(row)
    sol.append(result)

    for r in sorted(sol):
        print(r)


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
