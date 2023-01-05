import sys

res = []

def merge(a, p, q, r):
    tmp = []
    i = p
    j = q + 1
    while(i <= q and j <= r):
        if (a[i] <= a[j]):
            tmp.append(a[i])
            i += 1
        else:
            tmp.append(a[j])
            j += 1
    while(i <= q):
        tmp.append(a[i])
        i += 1
    while(j <= r):
        tmp.append(a[j])
        j += 1
    i = p
    t = 0
    while (i <= r):
        a[i] = tmp[t]
        res.append(tmp[t])
        t += 1
        i += 1
        
def merge_sort(a, p, r):
    if(p < r):
        q = int((p + r)/2)
        merge_sort(a, p, q)
        merge_sort(a, q + 1, r)
        merge(a, p, q, r)
        

x,y = map(int, sys.stdin.readline().split())
b = [int(i) for i in sys.stdin.readline().split()]

merge_sort(b, 0, x - 1)

if len(res) < y:
    print(-1)
else:
    print(res[y - 1])