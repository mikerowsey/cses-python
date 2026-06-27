# Pattern: Constructive Algorithm
# Technique: Even-odd partitioning
# Time: O(n)
# Space: O(n)
# Insight: Place all even numbers first, then all odd numbers. This
#          guarantees adjacent values differ by at least 2 for all
#          n ≥ 4, producing a valid permutation without backtracking.

import sys


def solve(it) -> str:
    n = ni(it)

    if n == 1:
        return "1"

    if n == 2 or n == 3:
        return "NO SOLUTION"

    result: list[str] = []

    for i in range(2, n + 1, 2):
        result.append(str(i))

    for i in range(1, n + 1, 2):
        result.append(str(i))

    return " ".join(result)


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
