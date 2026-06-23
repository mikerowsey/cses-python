import sys

it = iter(sys.stdin.buffer.read().split())
ni = lambda: int(next(it))

n = ni()
expected_sum = n * (n + 1) // 2
actual_sum = sum(map(int, it))

print(expected_sum - actual_sum)