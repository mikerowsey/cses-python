def solve(n: int, numbers: list[int]) -> int:
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(numbers)

    return expected_sum - actual_sum


def main() -> None:
    n = int(input())
    numbers = list(map(int, input().split()))

    print(solve(n, numbers))


if __name__ == "__main__":
    main()