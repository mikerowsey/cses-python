def solve(n: int) -> str:
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


def main():
    n = int(input())
    print(solve(n))


if __name__ == '__main__':
    main()
