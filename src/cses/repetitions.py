s = input()
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

print(reps)
