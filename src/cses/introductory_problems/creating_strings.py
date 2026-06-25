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
