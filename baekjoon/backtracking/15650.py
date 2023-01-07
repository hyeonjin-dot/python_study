x,y = map(int, input().split())

a = []

def check(s):
    if len(a) == y:
        print(' '.join(map(str,a)))
        return
    else:
        for i in range(s, x+1):
            if i not in a:
                a.append(i)
                check(i + 1)
                a.pop()
check(1)
