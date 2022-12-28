def checkhansu(a):
    if a < 10:
        return 1
    elif a < 100:
        return 1
    else:
        if a == 1000:
            return 0
        tmp = str(a)
        tmp = list(map(int,tmp))
        if (tmp[1] - tmp[0]) != (tmp[2]-tmp[1]):
            return 0
        else:
            return 1

x = input()
rtn = 0
for i in range(1, int(x) + 1):
    if checkhansu(i) == 1:
        rtn = rtn + 1
if int(x) == 1:
    rtn = 1
print(rtn)