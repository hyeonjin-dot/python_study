def findemi(x):
    if (x == 1):
        return False
    for i in range(2, int(x**0.5)+1):
        if (x % i == 0):
            return False
    return True

x,y = map(int, input().split())
for i in range(x,y+1):
    if findemi(i):
        print(i)