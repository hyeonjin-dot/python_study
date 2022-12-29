x = int(input())
for i in range(x):
    h,w,n = map(int, input().split())
    z = n / h
    if (z == int(z)):
        z -= 1
    z = int(z) + 1
    y = n % h
    if y == 0:
        y = h
    if (z < 10):
        print(y,'0',z, sep='')
    elif (z > 9):
        print(y,z, sep='')