import sys


def solve(it) -> str:
    n = ni(it)

    if n % 4 in (1, 2):
        print("NO")
        exit()

    a = []
    b = []

    for i in range(n):
        if i % 4 in (0, 3):
            a.append(n - i)
        else:
            b.append(n - i)

    result = [
        "YES",
        str(len(a)),
        " ".join(map(str, a)),
        str(len(b)),
        " ".join(map(str, b)),
    ]

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
