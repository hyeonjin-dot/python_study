import sys
input = sys.stdin.readline

bra1 = ['(', '[' ]
bra2 = [ ')', ']']
n = []

def check(tmp):
    n.clear()
    l = len(tmp)
    for i in range(l):
        k = tmp.pop()
        if k in bra2:
            n.append(k)
        else:
            if len(n) == 0:
                return ('no')
            elif bra1.index(k) != bra2.index(n[len(n) - 1]):
                return ('no')
            else:
                n.pop()
    if len(n) == 0:
        return ('yes')
    else:
        return ('no')
        
lst = []   
i = 0     
while True:
    lst.append(list(input().rstrip()))
    if len(lst[i]) == 1 and (lst[i][0] == '.'):
        break
    i += 1
    
tmp = []
for q in range(i):
    for j in range(len(lst[q])):
        if lst[q][j] in bra1:
            tmp.append(lst[q][j])
        if lst[q][j] in bra2:
            tmp.append(lst[q][j])
    if len(tmp) == 0:
        print('yes')
    elif tmp[0] in bra2: 
        print('no')
    else:
        print(check(tmp))
    tmp.clear()