import sys
input = sys.stdin.readline

lst = []

def push(n):
    n = int(n)
    lst.append(n)
    
def pop():
    if len(lst) != 0:
        print(lst.pop())
    else:
        print(-1)

def size():
    print(len(lst))
    
def empty():
    if len(lst) == 0:
        print(1)
    else:
        print(0)

def top():
    if len(lst) == 0:
        print(-1)
    else:
        print(lst[len(lst) - 1])
        
i = int(input())
for _ in range(i):
    com = input().rsplit()
    if com[0] == 'pop':
        pop()
    elif com[0]  == 'top':
        top()
    elif com[0]  == 'size':
        size()
    elif com[0]  == 'empty':
        empty()
    else:
        push(com[1])