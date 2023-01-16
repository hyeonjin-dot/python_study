import sys
input = sys.stdin.readline
import collections
from collections import deque

lst = deque()
def push_front(n):
    lst.appendleft(n)
    
def push_back(n):
    lst.append(n)

def pop_front():
    if len(lst) == 0:
        print(-1)
    else:
        print(lst.popleft())
        
def pop_back():
    if len(lst) == 0:
        print(-1)
    else:
        print(lst.pop())
        
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
    if com[0] == 'pop_front':
        pop_front()
    elif com[0] == 'pop_back':
        pop_back()
    elif com[0]  == 'front':
        front()
    elif com[0]  == 'back':
        back()
    elif com[0]  == 'size':
        size()
    elif com[0]  == 'empty':
        empty()
    else:
        if com[0] == 'push_front':
            push_front(com[1])
        else:
            push_back(com[1])