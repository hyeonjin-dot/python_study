l = int(input())
a = []
for i in range(l):
    a = list(map(int, input().split()))
    b = ((a[0] - a[3]) ** 2 + (a[1] - a[4]) ** 2) ** (1/2)
    if (a[0] == a[3] and a[1] == a[4]):
        if a[2] == a[5]:
            print(-1)
        else:
            print(0)
    elif b > (a[2] + a[5]):
        print(0)
    elif b == (a[2] + a[5]):
        print(1)
    else:
        if abs(a[2] - a[5]) < b and b < a[2] + a[5]:
            print(2)
        elif abs(a[2] - a[5]) == b:
            print(1)
        else:
            print(0)