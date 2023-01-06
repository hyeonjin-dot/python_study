x,y = map(int, input().split())

a = set()
b = set()
for i in range(x):
    a.add(input())
for i in range(y):
    b.add(input())

res = sorted(a & b)

print(int(len(res)))
for i in res:
    print(i)