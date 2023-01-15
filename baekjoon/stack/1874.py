import sys
input = sys.stdin.readline

n = int(input())
lst = []
for _ in range(n):
    lst.append(int(input()))

stack = []
rtn = []
stack.append(0)
k = 1
a = 0
for i in range(n):
    while lst[i] != stack[-1]:
        if lst[i] > stack[-1]:
            stack.append(k)
            k += 1
            rtn.append('+')
        elif lst[i] < stack[-1]:
            if lst[i] < k :
                print('NO')
                a = 1
                quit()
            stack.pop()
            rtn.append('-')
    stack.pop()
    rtn.append('-')
    
if a == 0:
    for _ in rtn:
        print(_)