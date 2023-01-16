import sys
input = sys.stdin.readline
import collections
from collections import deque

lst = deque()
def push(n):
    lst.append(n)

def pop():
    if len(lst) == 0:
        print(-1)
    else:
        print(lst.popleft())
        
def size():
    print(len(lst))

def empty():
    if len(lst) == 0:
        print(1)
    else:
        print(0)
    
def front():
    if len(lst) == 0:
        print(-1)
    else:
        print(lst[0])

def back():
    if len(lst) == 0:
        print(-1)
    else:
        print(lst[-1])

i = int(input())
for _ in range(i):
    com = input().rsplit()
    if com[0] == 'pop':
        pop()
    elif com[0]  == 'front':
        front()
    elif com[0]  == 'back':
        back()
    elif com[0]  == 'size':
        size()
    elif com[0]  == 'empty':
        empty()
    else:
        push(com[1])