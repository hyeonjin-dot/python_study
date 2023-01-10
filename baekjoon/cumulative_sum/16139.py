# for i in range(n):
#     a = list(map(str,input().split()))
#     tmp = st[int(a[1]):(int(a[2])+1)]
#     res = 0
#     for j in tmp:
#         if j == a[0]:
#             res += 1
#     print(res)
# for i in range(n):
#     a = list(map(str,input().split()))
#     tmp = st[int(a[1]):(int(a[2])+1)].split(a[0])
#     print(len(tmp) - 1)

import sys
input = sys.stdin.readline

st = input()
n = int(input())
#ord() - 97 -> a=0
tmp = [[0] * 26]
tmp[0][ord(st[0]) - 97] = 1
for i in range(1, len(st)):
    tmp.append(tmp[-1][:])
    tmp[i][ord(st[i]) - 97] += 1
for i in range(n):
    c, start, end = (input().split())
    start, end = map(int, [start, end])
    if (start) == 0:
        print(tmp[(end)][ord(c)-97])
    else:
        print(tmp[(end)][ord(c)-97] - tmp[(start) - 1][ord(c)-97])