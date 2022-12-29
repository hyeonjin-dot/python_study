x = input()
x = x.split()
a = int(x[0])
b = int(x[1])
c = int(x[2])

if (c - b) <= 0:
    print(-1)
else:
    y = c - b
    tmp = a / y
    rtn = int(tmp) + 1
    print(rtn)