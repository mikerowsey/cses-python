# Pattern: Backtracking
# Technique: DFS with frequency counts (pruning duplicates)
# Time: O(U × n)
# Space: O(U × n) (including output)
# Insight:    Maintain a frequency count for each character and recursively build the string.
#             Each recursive call chooses only from characters that still have remaining
#             copies, guaranteeing that every unique permutation is generated exactly once.
#             This avoids producing duplicate permutations and eliminates the need for a set.

from collections import Counter
import sys


def solve(it) -> str:
    s = b"".join(it).decode()
    cnt = Counter(s)
    chars = sorted(cnt)

    out = []

    def dfs(path):
        if len(path) == len(s):
            out.append("".join(path))
            return

        for c in chars:
            if cnt[c]:
                cnt[c] -= 1
                path.append(c)
                dfs(path)
                path.pop()
                cnt[c] += 1

    dfs([])

    return str(len(out)) + "\n" + "\n".join(out)


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
