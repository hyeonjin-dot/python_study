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

n = int(input())
a = []
b = []
for i in range(n):
    a.append(int(input()))
sorted(a)
tmp = [a[i] - a[i - 1] for i in range(1, n)]
res = tmp[0]

for i in range(1, n - 1):
    res = gcd(res, tmp[i]) #최대 공약수

for i in range(1, int(res ** 1/2) + 1):
    if res % i == 0:
        b.append(i)
        b.append(res // i)
b.remove(1)
b = list(set(b))
sorted(b)
for i in b:
    print(i, end=' ')