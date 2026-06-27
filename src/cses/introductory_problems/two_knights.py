# Pattern: Mathematical Formula
# Technique: Combinatorial counting
# Time: O(n)
# Space: O(1)
# Insight: Count all ways to place two knights, then subtract the pairs
#          that attack each other. Each 2×3 or 3×2 rectangle contributes
#          four attacking pairs.

import sys


def solve(it) -> str:
    n = ni(it)
    result = []

    for i in range(1, n + 1):
        attacking = 4 * (i - 1) * (i - 2)
        total = i * i * (i * i - 1) // 2
        result.append(str(total - attacking))

    return "\n".join(result)


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
