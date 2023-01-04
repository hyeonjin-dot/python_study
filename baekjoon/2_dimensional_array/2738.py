x,y=map(int,input().split())
a,b = [],[]
for i in range(x):
    i = list(map(int, input().split()))
    a.append(i)

for j in range(x):
    j = list(map(int, input().split()))
    b.append(j)

for i in range(x):
    for j in range(y):
        print(a[i][j] + b[i][j], end=' ')
    print()    
