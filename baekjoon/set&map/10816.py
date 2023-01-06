x = int(input())
a = list(map(int, input().split()))
b = {}
for i in a:
    if i in b:
        b[i] += 1
    else:
        b[i] = 1
        
y = int(input())
c = list(map(int, input().split()))
for i in c:
    if i in b:
        print(b[i])
    else:
        print(0)