x,y = map(int, input().split())
a = list(map(int, input().split()))

s = 0
mx = 0
sorted(a)
for i in range(x):
    for j in range(i + 1, x):
        for k in range(j + 1, x):
            s = a[i] + a[j] + a[k]
            if (s <= y):
                mx = max(mx, s)
            elif (s > y):
                continue
print(mx)