#abc + a + b + c = k
n = int(input())

for i in range(1, n+1):
    a = list(map(int,str(i)))
    if sum(a) + i == n:
        print(i)
        break
    elif i == n:
        print(0)