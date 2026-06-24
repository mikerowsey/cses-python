s = input().strip()

freq = [0] * 26
for ch in s:
    freq[ord(ch) - ord('A')] += 1

odd = sum(f & 1 for f in freq)

if odd > 1:
    print("NO SOLUTION")
    exit()

left = []
middle = ""

for i, f in enumerate(freq):
    ch = chr(ord('A') + i)

    left.append(ch * (f // 2))

    if f % 2:
        middle = ch

left = "".join(left)
print(left + middle + left[::-1])