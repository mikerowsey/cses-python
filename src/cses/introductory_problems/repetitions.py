# Pattern: Linear Scan
# Technique: Run-length counting
# Time: O(n)
# Space: O(1)
# Insight: Traverse the string once, counting consecutive identical
#          characters. Reset the count when the character changes and
#          track the maximum run length seen.

import sys


def solve(it) -> str:
    s = ns(it)
    reps = best = 1

    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            reps += 1
            best = max(best, reps)
        else:
            reps = 1

    return str(best)


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
