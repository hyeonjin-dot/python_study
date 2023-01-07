def fac(a,b):
    res = 1
    for i in range(a):
        res = res * (b - i) / (i + 1)
    return (int(res))
        
    
x = int(input())
for i in range(x):
    a,b = map(int, (input().split()))
    if a == b:
        print(1)
    elif a == 1:
        print(b)
    else:
        print(fac(a,b))