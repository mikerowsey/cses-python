import sys


def ni(it) -> int:
    return int(next(it))


def nil(it, n: int) -> list[int]:
    return [ni(it) for _ in range(n)]


def ns(it) -> str:
    return next(it).decode()


def solve(it) -> str:
    s = ns(it)

    freq = [0] * 26
    for ch in s:
        freq[ord(ch) - ord('A')] += 1

    odd = sum(f & 1 for f in freq)

    if odd > 1:
        print("NO SOLUTION")
        exit()

    left = []
    middle = ""

    for i, f in enumerate(freq):
        ch = chr(ord('A') + i)

        left.append(ch * (f // 2))

        if f % 2:
            middle = ch

    left = "".join(left)
    return left + middle + left[::-1]


def main() -> None:
    it = iter(sys.stdin.buffer.read().split())
    sys.stdout.write(solve(it) + "\n")


if __name__ == "__main__":
    main()
