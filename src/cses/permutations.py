import sys

it = iter(sys.stdin.buffer.read().split())
n = int(next(it))

if n == 1:
    print("1")
    exit(0)

if n == 2 or n == 3:
    print("NO SOLUTION")
    exit(0)

result: list[str] = []

for i in range(2, n + 1, 2):
    result.append(str(i))

for i in range(1, n + 1, 2):
    result.append(str(i))

sys.stdout.write(" ".join(result))
