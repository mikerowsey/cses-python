import sys

MOD = 1_000_000_007


def ni(it) -> int:
    return int(next(it))


def nil(it, n: int) -> list[int]:
    return [ni(it) for _ in range(n)]


def ns(it) -> str:
    return next(it).decode()


def mul(a, b):
    return (
        (a[0] * b[0] + a[1] * b[2]) % MOD,
        (a[0] * b[1] + a[1] * b[3]) % MOD,
        (a[2] * b[0] + a[3] * b[2]) % MOD,
        (a[2] * b[1] + a[3] * b[3]) % MOD,
    )


def mpow(a, n):
    result = (1, 0, 0, 1)

    while n > 0:
        if n & 1:
            result = mul(result, a)

        a = mul(a, a)
        n >>= 1

    return result


def solve(it) -> str:
    n = ni(it)
    if n == 0:
        return "0"

    t = (0, 1, 1, 1)
    t = mpow(t, n - 1)

    return str(t[3])


def main() -> None:
    it = iter(sys.stdin.buffer.read().split())
    sys.stdout.write(solve(it) + "\n")


if __name__ == "__main__":
    main()
