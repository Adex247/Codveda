# Task 3: N-Queens Problem

## Description

A classic backtracking problem: place **N** queens on an **N × N** chessboard such that no two queens threaten each other (i.e., no two queens share the same row, column, or diagonal).

## Objectives

- Represent the chessboard as a 2D array.
- Use backtracking to place queens one by one in safe positions.
- Ensure that no two queens are on the same row, column, or diagonal.

## Approach

The board is represented as a 1D array `board`, where `board[row] = col` gives the column of the queen placed in that row. Since each row can hold at most one queen, this is a natural and efficient way to represent the board without needing a full N × N grid internally.

The algorithm places queens row by row:

1. For the current row, try each column from left to right.
2. Check if placing a queen at `(row, col)` is safe — no queen in the same column or diagonal as any previously placed queen.
3. If safe, place the queen and recurse to the next row.
4. If the recursive call fails to find a solution, remove the queen (backtrack) and try the next column.
5. If all N queens are placed successfully, record the solution.

### Safety check

A placement at `(row, col)` is unsafe if, for any previously placed queen at `(r, c)`:

- `c == col` → same column
- `abs(c - col) == abs(r - row)` → same diagonal (in either direction)

Rows never need to be checked, since only one queen is placed per row.

## Usage

```bash
python n_queens.py
```

Edit the `n` value in the `if __name__ == "__main__":` block to solve for a different board size.

**Example output for N = 4:**

```
Found 2 solutions for N=4

. Q . .
. . . Q
Q . . .
. . Q .

. . Q .
Q . . .
. . . Q
. Q . .
```

## Files

| File           | Description                                  |
|----------------|-----------------------------------------------|
| `n_queens.py`  | Backtracking solver and board printer         |

## Complexity

- **Time:** Worst case O(N!), since each row tries up to N columns and the safety check is O(N).
- **Space:** O(N) for the board array plus recursion depth.

## Challenges

- **Designing an efficient backtracking solution** — pruning invalid placements as early as possible (checking safety before recursing) avoids exploring dead-end branches.
- **Correctly handling constraints** — the diagonal check is the easiest part to get wrong; using `abs(c - col) == abs(r - row)` correctly covers both diagonal directions in a single comparison.

## Possible Extensions

- Track used columns/diagonals with sets for O(1) safety checks instead of O(N) scans.
- Visualize solutions with a GUI or a chessboard-style image output.
- Count solutions only, without storing full boards, to handle larger N efficiently.
