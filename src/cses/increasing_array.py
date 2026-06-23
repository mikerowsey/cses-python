import sys

it = iter(sys.stdin.buffer.read().split())
ni = lambda: int(next(it))

length = ni()
previous = ni()
moves = 0

for _ in range(length - 1):
    current = ni()

    if current < previous:
        moves += previous - current
    else:
        previous = current

sys.stdout.write(str(moves))
