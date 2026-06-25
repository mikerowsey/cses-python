import sys


def hanoi(n, src, aux, dst, out):
    if n == 1:
        out.append(f"{src} {dst}")
        return
    hanoi(n - 1, src, dst, aux, out)
    out.append(f"{src} {dst}")
    hanoi(n - 1, aux, src, dst, out)


def solve(it) -> str:
    n = ni(it)
    out = [str((1 << n) - 1)]
    hanoi(n, 1, 2, 3, out)
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
