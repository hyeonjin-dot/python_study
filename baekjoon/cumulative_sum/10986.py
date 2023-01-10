x,y = map(int,(input().split()))
lst = list(map(int, input().split()))

# res = 1
# for i in range(x):
#     for j in range(i + 1, x):
#         if sum(lst[i:j+1]) % y == 0:
#             res += 1

sum = 0
tmp = [0] * y
for i in range(x):
    sum += lst[i]
    tmp[sum % y] += 1
res = tmp[0]
for i in tmp:
    res += (i * (i - 1)) // 2
print(res)