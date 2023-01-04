import sys
from collections import Counter

n = int(sys.stdin.readline())
a = list(map(int, sys.stdin.readline().split()))
b = sorted(list(set(a)))
d = {b[i]:i for i in range(len(b))}
for i in (a):
    print(d[i],end=' ')