x = int(input())

p = [[0 for i in range(100)] for j in range(100)]

for i in range(x):
    a,b = map(int,input().split())
    for j in range(a,a+10):
        for k in range(b, b+10):
            if p[j][k] == 0:
                p[j][k] = 1
                
res = 0  
for i in range(100):
    for j in range(100):
        if p[i][j] == 1:
            res += 1

print(res)