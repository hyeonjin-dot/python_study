# n = int(input())
# a = []
# b = []
# for i in range(n):
#     a.append(int(input()))
# sorted(a)
# for i in range(2, a[0] + 1):
#     k = a[0] % i
#     for j in range(1, n):
#         if (k != a[j] % i):
#             break
#     if j == n - 1:
#         b.append(i)
# print(b)

from math import *
import sys

n = int(sys.stdin.readline())
a = [int(sys.stdin.readline()) for i in range(n)]
b = []
a.sort()
tmp = [(a[i] - a[i - 1]) for i in range(1, n)]
res = tmp[0]

for i in range(0, len(tmp)):
    res = gcd(res, tmp[i]) #최대 공약수

for i in range(2, int(sqrt(res)) + 1):
    if res % i == 0:
        b += [i, res//i]
            
b.append(res)
b = list(set(b))
b.sort()
print(*b)