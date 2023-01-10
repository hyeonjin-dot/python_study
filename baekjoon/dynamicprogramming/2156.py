n = int(input())
lst = [0]
for i in range(n):
    lst.append(int(input()))

res = [0]#0
res.append(lst[1])#1
if n > 1:
    res.append(lst[1] + lst[2])#2

for i in range(3,n+1): #110 101 011 
   res.append(max(res[i - 1], res[i - 2] + lst[i], res[i - 3] + lst[i - 1] + lst[i])) 
print(res[n])