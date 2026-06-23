n = int(input())

if n % 4 in (1, 2):
    print("NO")
    exit()
    
a = []
b = []

for i in range(n):
    if i % 4 in (0, 3):
        a.append(n - i)
    else:
        b.append(n - i)

result = [
    "YES",
    str(len(a)),
    " ".join(map(str, a)),
    str(len(b)),
    " ".join(map(str, b)),
]

print("\n".join(result))
