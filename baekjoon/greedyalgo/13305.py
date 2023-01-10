import sys
input = sys.stdin.readline

# def findmin(price):
#     tmp = sorted(price)
#     return price.index(tmp[0])

# n = int(input())
# length = list(map(int, input().split()))
# price = list(map(int, input().split()))
# price.pop()
# min = findmin(price)
# sump = 0
# while min != 0:
#     sump += price[min] * sum(length[min:])
#     price = price[:min]
#     length = length[:min]
#     min = findmin(price)
# sump += price[0] * sum(length)
# print(sump)

n = int(input())
length = list(map(int, input().split()))
price = list(map(int, input().split()))
sump = 0
min_cost = 1000000000 
for i in range(n-1):
    if price[i] < min_cost:
        min_cost = price[i]
    sump += length[i] * min_cost
print(sump)