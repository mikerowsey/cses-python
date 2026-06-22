def solve(pairs: list[tuple[int, int]]) -> str:
    result = []
    for i in range(len(pairs)):
        a, b = pairs[i]
        mx = max(a, b)
        dif = a - b
        p = mx * mx - mx + 1
        if mx % 2 == 0:
            result.append(p + dif)
        else:
            result.append(p - dif)
    return "\n".join(map(str, result))



def main():
    _n = int(input())
    tokens = input().split()
    pairs = [(int(tokens[i]), int(tokens[i+1])) for i in range(0, len(tokens), 2)]
    print(solve(pairs))


if __name__ == "__main__":
    main()
