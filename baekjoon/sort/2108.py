import sys
from collections import Counter

n = int(sys.stdin.readline())
a = []
for i in range(n):
    a.append(int(sys.stdin.readline()))

print(round(sum(a)/n))#1

a.sort()
print(a[int(n/2)])#2

#두번째 최빈값
cnt = Counter(a).most_common(2)
if len(a) > 1:
    if cnt[0][1] == cnt[1][1]:
        print(cnt[1][0])
    else:
        print(cnt[0][0])
else:
    print(cnt[0][0])
        
print(a[-1] - a[0])#4
