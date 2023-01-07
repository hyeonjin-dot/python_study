def cnt2(n):
    i = 0
    while n != 0:
        n = n // 2
        i += n
    return i

def cnt5(n):
    i = 0
    while n != 0:
        n = n // 5
        i += n
    return i

x,y = map(int, input().split())
print(min(cnt2(x) - cnt2(x - y) - cnt2(y),cnt5(x) - cnt5(x - y) - cnt5(y)))