import sys


def solve(it) -> str:
    n = ni(it)

    if n == 1:
        return "1"

    if n == 2 or n == 3:
        return "NO SOLUTION"

    result: list[str] = []

    for i in range(2, n + 1, 2):
        result.append(str(i))

    for i in range(1, n + 1, 2):
        result.append(str(i))

    return " ".join(result)


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
