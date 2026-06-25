import sys


def solve(it) -> str:
    n = ni(it)
    a = ["0", "1"]

    for i in range(1, n):
        b = []
        for e in a:
            b.append('0' + e)
        for e in reversed(a):
            b.append('1' + e)
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
