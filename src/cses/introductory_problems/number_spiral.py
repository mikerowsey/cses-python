import sys


def solve(it) -> str:
    result = []

    for _ in range(ni(it)):
        row, col = (ni(it), ni(it))
        layer = max(row, col)
        layer_end = layer * layer
        previous_layer_end = (layer - 1) * (layer - 1)

        if layer & 1:
            if row == layer:
                result.append(str(previous_layer_end + col))
            else:
                result.append(str(layer_end - row + 1))
        else:
            if col == layer:
                result.append(str(previous_layer_end + row))
            else:
                result.append(str(layer_end - col + 1))

    return "\n".join(result)


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
