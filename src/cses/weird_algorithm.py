def solve(n: int) -> str:
    result = []
    while True:
        result.append(str(n))

        if n == 1:
            break

        if n & 1 == 0:
            n //= 2
        else:
            n = 3 * n + 1

    return " ".join(result)


def main():
    n = int(input())
    print(solve(n))

if __name__ == "__main__":
    main()