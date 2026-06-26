# Pattern: Mathematical Invariants
# Technique: Constant-time feasibility check
# Time: O(t)
# Space: O(1) (excluding output)
# Insight:    Each move removes exactly three coins (2 from one pile, 1 from the other),
#             so the total number of coins must be divisible by 3. Additionally, neither
#             pile can ever contain more than twice as many coins as the other, or the
#             smaller pile would be exhausted before the larger one.


import sys


def solve(it) -> str:
    result = []
    n = ni(it)

    for _ in range(n):
        a, b = (ni(it), ni(it))
        if a > 2 * b or b > 2 * a or (a + b) % 3 != 0:
            result.append('NO')
        else:
            result.append('YES')

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
