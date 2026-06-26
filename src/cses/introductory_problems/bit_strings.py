# Pattern: Modular Arithmetic
# Technique: Built-in modular exponentiation (pow(base, exp, mod))
# Time: O(log n)
# Space: O(1)
# Insight: Python's three-argument pow() performs exponentiation by
#          squaring and applies the modulus during computation, avoiding
#          huge intermediate integers.

import sys


def solve(it) -> str:
    n = ni(it)
    result = pow(2, n, 1000000007)
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
