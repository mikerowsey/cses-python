import sys

n = int(input())
result = []
while True:
    result.append(str(n))
    if n == 1:
        break
    if n & 1 == 0:
        n //= 2
    else:
        n = 3 * n + 1

sys.stdout.write(" ".join(result))
