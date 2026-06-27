# Pattern: Linear Scan
# Technique: Running maximum
# Time: O(n)
# Space: O(1)
# Insight: Traverse the array once, keeping track of the minimum allowed
#          value (the previous element). When a value is too small, add the
#          required increment; otherwise, update the running maximum.

import sys


def solve(it) -> str:
    length = ni(it)
    previous = ni(it)
    moves = 0

    for _ in range(length - 1):
        current = ni(it)

        if current < previous:
            moves += previous - current
        else:
            previous = current

    return str(moves)


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
