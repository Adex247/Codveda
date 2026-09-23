def solve_n_queens(n):
    """
    Solve the N-Queens problem using backtracking.
    Returns all valid board configurations as lists of column positions,
    where board[row] = column of the queen in that row.
    """
    solutions = []
    board = [-1] * n  # board[row] = column where queen is placed

    def is_safe(row, col):
        for r in range(row):
            c = board[r]
            # Same column
            if c == col:
                return False
            # Same diagonal (either direction)
            if abs(c - col) == abs(r - row):
                return False
        return True

    def backtrack(row):
        if row == n:
            solutions.append(board[:])  # found a full valid placement
            return
        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1  # undo (backtrack)

    backtrack(0)
    return solutions


def print_board(solution, n):
    """Print a solution as an N x N chessboard."""
    for row in range(n):
        line = ""
        for col in range(n):
            line += "Q " if solution[row] == col else ". "
        print(line)
    print()


if __name__ == "__main__":
    n = 4  # try 4, 8, etc.
    solutions = solve_n_queens(n)
    print(f"Found {len(solutions)} solutions for N={n}\n")
    for sol in solutions:
        print_board(sol, n)