import sys
import collections
from collections import deque
input = sys.stdin.readline

lst = deque()

def D():
    if len(lst) == 0:
        return (0)
    else:
        lst.popleft()
        return (1)

def R():
    (lst).reverse()
    
def parshing(s):
    if len(s) == 0:
        return (0)
    if len(s) == 1:
        t = s[0]
        t = t[1:]
        t = t[:-2]
        s[0] = t
    else:
        t = s[0]
        t = t[1:]
        s[0] = t
        t = s[-1]
        t = t[:-2]
        s[-1] = t
    for i in s:
        lst.append(int(i))
    return(1)

    
n = int(input())
for i in range(n):
    cmm = list(map(str, input()))
    l = int(input())
    ilst = list(map(str, input().split(',')))
    if l == 0:
        if 'D' in cmm:
            print('error')
            continue
    if parshing(ilst) == 0:
        print('error')
        quit()
    for k in cmm:
        if k == 'R':
            R()
        elif k == 'D':
            if D() == 0:
                print('error')
                continue
    if len(lst) > 0:    
        print(list(lst))
    lst.clear()