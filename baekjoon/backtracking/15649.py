x,y = map(int, input().split())

a = []

def check():
    if len(a) == y:
        print(' '.join(map(str,a)))
        return
    else:
        for i in range(1, x+1):
            if i not in a:
                a.append(i)
                check()
                a.pop()
check()
