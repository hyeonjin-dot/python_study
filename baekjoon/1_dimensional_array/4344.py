x = int(input())

for i in range(x):
    lst = str(input())
    lst = lst.split()
    len = int(lst[0])
    sum = 0
    for j in range(1,len+1):
        sum = sum + int(lst[j])
    ave = sum / len
    z = 0
    for j in range(1, len+1):
        if int(lst[j]) > ave:
            z = z + 1
    k = (z / len) * 100
    print(f'{k:.3f}%');
