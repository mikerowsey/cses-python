# Pattern: Subset Enumeration (2^n)
# Technique: Iterative subset generation
# Time: O(n * 2^n)
# Space: O(2^n)
# Insight: Each new weight creates a second copy of every existing subset.

import sys


def solve(it):
    count = ni(it)
    weights = nil(it, count)
    total = sum(weights)
    subset_sums = [0]
    for weight in weights:
        subset_sums += [s + weight * 2 for s in subset_sums]
    result = min(abs(i - total) for i in subset_sums)
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
