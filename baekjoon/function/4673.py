selfnum = set(range(1, 10001))
noself = set()

for i in range(1, 10000):
    sum = i
    tmp = str(i)
    for j in range(len(tmp)):
        sum = sum + int(tmp[j])
    noself.add(sum)

rtn = sorted(selfnum - noself)
for i in rtn:
    print(i)