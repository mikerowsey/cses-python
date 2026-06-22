def solve(s: str) -> int:
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
    return reps


def main() -> None:
    a = input()
    print(solve(a))


if __name__ == "__main__":
    main()
