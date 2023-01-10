import sys
input = sys.stdin.readline

n = int(input())
lst = []
for i in range(n):
    a,b= (map(int, input().split()))
    c = b - a
    lst.append([a,b,c])
lst = sorted(lst, key=lambda x:(x[1],x[0],x[2])) #끝, 시작, 걸리는 시간

res = 1
min = lst[0][1]
for i in range(1, n):
    if min > lst[i][0]:
        continue
    else:
        min = lst[i][1]
        res += 1
print(res)