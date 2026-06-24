import sys

it = iter(sys.stdin.buffer.read().split())
ni = lambda: int(next(it))
np = lambda: (ni(), ni())

result = []
n = ni()

for _ in range(n):
    a, b = np()
    if a > 2 * b or b > 2 * a or (a + b) % 3 != 0:
        result.append('NO')
    else:
        result.append('YES')

sys.stdout.write("\n".join(result))
