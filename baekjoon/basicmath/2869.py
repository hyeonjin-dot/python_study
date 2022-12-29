a,b,c = map(int,input().split())
z = ((c - b) / (a - b))
print(int(z) if z == int(z) else int(z) + 1)