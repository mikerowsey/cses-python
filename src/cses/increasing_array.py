def solve(n: int, array: list[int]):
    result = 0
    for i in range(1, n):
        if array[i] >= array[i - 1]:
            continue
        diff = array[i - 1] - array[i]
        result += diff
        array[i] += diff
    return result


def main():
    n = int(input())
    array = list(map(int, input().split()))
    print(solve(n, array))


if __name__ == "__main__":
    main()
