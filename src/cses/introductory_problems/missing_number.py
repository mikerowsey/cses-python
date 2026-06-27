# Pattern: Mathematical Formula
# Technique: Arithmetic sum comparison
# Time: O(n)
# Space: O(1)
# Insight: Compute the expected sum of 1..n using the arithmetic series
#          formula, subtract the actual sum, and the difference is the
#          missing number.

import sys


def solve(it) -> str:
    n = ni(it)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(map(int, it))
    return str(expected_sum - actual_sum)


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
