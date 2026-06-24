import sys


def ni(it) -> int:
    return int(next(it))


def nil(it, n: int) -> list[int]:
    return [ni(it) for _ in range(n)]


def ns(it) -> str:
    return next(it).decode()


def solve(it) -> str:
    result = []
    n = ni(it)

    for _ in range(n):
        a, b = (ni(it), ni(it))
        if a > 2 * b or b > 2 * a or (a + b) % 3 != 0:
            result.append('NO')
        else:
            result.append('YES')

    return "\n".join(result)


def main() -> None:
    it = iter(sys.stdin.buffer.read().split())
    sys.stdout.write(solve(it) + "\n")


if __name__ == "__main__":
    main()
