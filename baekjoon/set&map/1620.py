import sys

x,y = map(int, sys.stdin.readline().split())
a = {}

for i in range(1, x+1):
    k = sys.stdin.readline().rstrip()
    a[i] = k
    a[k] = i
    
for i in range(y):
    k = sys.stdin.readline().rstrip()
    if k.isdigit():
        print(a[int(k)])
    else:
        print(a[k])