import sys

it = iter(sys.stdin.buffer.read().split())
ni = lambda: int(next(it))
np = lambda: (ni(), ni())

result = []

for _ in range(ni()):
    row, col = np()
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

sys.stdout.write("\n".join(result))
