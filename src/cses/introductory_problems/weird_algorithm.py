# Pattern: Simulation
# Technique: Iterative State Update
# Time: O(k)   # k = number of terms generated
# Space: O(1)
# Insight: Repeatedly apply the Collatz rules until reaching 1.
#          Each iteration updates the current value in place, so only
#          constant extra memory is required.

import sys


def solve(it) -> str:
    result = []
    n = ni(it)
    while True:
        result.append(str(n))
        if n == 1:
            break
        if n & 1 == 0:
            n //= 2
        else:
            n = 3 * n + 1
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
