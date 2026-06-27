# Pattern: Mathematical Formula
# Technique: Factor counting
# Time: O(log₅ n)
# Space: O(1)
# Insight: Each trailing zero comes from a factor of 10 = 2 × 5. Since
#          factorials contain more 2s than 5s, count the number of factors
#          of 5 by repeatedly dividing n by 5.

import sys


def solve(it) -> str:
    n = ni(it)
    result = 0
    while n:
        n //= 5
        result += n
    return str(result)


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
