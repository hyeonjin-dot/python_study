a = []
max = 0
for i in range(0,9):
    a = list(map(int, input().split()))
    for j in range(0,9):
        if a[j] >= max:
            max = a[j]
            r1 = i
            r2 = j

print(max)
print(r1 + 1, r2 + 1)