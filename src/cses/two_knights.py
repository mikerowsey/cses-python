import sys

n = int(input())
result = []

for i in range(1, n + 1):
    attacking = 4 * (i - 1) * (i - 2)
    total = i * i * (i * i - 1) // 2
    result.append(str(total - attacking))

sys.stdout.write("\n".join(result))
