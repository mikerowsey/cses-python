# Pattern: Permutation Generation
# Technique: Brute-force enumeration with duplicate removal
# Time: O(n! × n)
# Space: O(n! × n)
# Insight:    Generate every possible permutation, remove duplicates using a set, then sort
#             the unique strings before output. This is feasible because n ≤ 8, making the
#             maximum number of permutations (8! = 40,320) small enough to enumerate. Performs
#             well for CSES.

import itertools
import sys


def solve(it) -> str:
    p = itertools.permutations(b"".join(it).decode())
    s = set()
    for i in p:
        s.add("".join(i))
    l = sorted(s)
    return str(len(l)) + "\n" + "\n".join(l)


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
