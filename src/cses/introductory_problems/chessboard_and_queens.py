# Pattern: Recursive Backtracking
# Technique: Depth-first search with pruning
# Time: O(8!) worst case
# Space: O(8)
# Insight: One queen per row eliminates row checks; columns and
#          diagonals become simple set lookups.
# CSES best with CPython3

import sys


def solve(it) -> str:
    board = [ns(it) for _ in range(8)]
    cols = set()
    diag1 = set()
    diag2 = set()

    def dfs(row: int) -> int:
        if row == 8:
            return 1

        total = 0

        for col in range(8):
            if board[row][col] == '*':
                continue

            if col in cols:
                continue

            if row - col in diag1:
                continue

            if row + col in diag2:
                continue

            cols.add(col)
            diag1.add(row - col)
            diag2.add(row + col)

            total += dfs(row + 1)

            cols.remove(col)
            diag1.remove(row - col)
            diag2.remove(row + col)

        return total

    return str(dfs(0))


def ni(it) -> int:
    return int(next(it))


def nil(it, n: int) -> list[int]:
    return [ni(it) for _ in range(n)]


def ns(it) -> str:
    return next(it).decode()


def main() -> None:
    it = iter(sys.stdin.buffer.read().split())
    sys.stdout.write(solve(it) + "\n")


if __name__ == "__main__":
    main()
