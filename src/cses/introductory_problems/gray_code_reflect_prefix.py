# Pattern: Constructive Algorithm
# Technique: Reflect-and-prefix generation
# Time: O(n · 2ⁿ)
# Space: O(2ⁿ)
# Insight: Generate Gray codes iteratively by reflecting the previous
#          sequence. Prefix '0' to the original order and '1' to the
#          reversed order, ensuring adjacent codes differ by one bit.

import sys


def solve(it) -> str:
    n = ni(it)
    a = ["0", "1"]

    for i in range(1, n):
        b = []
        for e in a:
            s = '0' + e
            b.append(s)
        for e in reversed(a):
            s = '1' + e
            b.append(s)
        a = b

    return "\n".join(a)


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
