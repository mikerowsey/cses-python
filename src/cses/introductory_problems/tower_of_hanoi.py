# Pattern: Recursion
# Technique: Divide and conquer
# Time: O(2ⁿ)
# Space: O(n)
# Insight: Move the top n-1 disks to the auxiliary peg, move the largest
#          disk to the destination, then move the n-1 disks onto it.

import sys


def solve(it) -> str:
    n = ni(it)
    out = [str((1 << n) - 1)]

    def hanoi(disks: int, src: int, aux: int, dst: int) -> None:
        if disks == 1:
            out.append(f"{src} {dst}")
            return

        hanoi(disks - 1, src, dst, aux)
        out.append(f"{src} {dst}")
        hanoi(disks - 1, aux, src, dst)

    hanoi(n, 1, 2, 3)

    return "\n".join(out)


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
