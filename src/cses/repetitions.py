import sys


def ni(it) -> int:
    return int(next(it))


def nil(it, n: int) -> list[int]:
    return [ni(it) for _ in range(n)]


def ns(it) -> str:
    return next(it).decode()


def solve(it) -> str:
    s = ns(it)
    current = s[0]
    n = 1
    reps = 1

    for next_val in s[1:]:
        if next_val == current:
            n += 1
            reps = max(reps, n)
            continue
        n = 1
        current = next_val

    return str(reps)


def main() -> None:
    it = iter(sys.stdin.buffer.read().split())
    sys.stdout.write(solve(it) + "\n")


if __name__ == "__main__":
    main()
