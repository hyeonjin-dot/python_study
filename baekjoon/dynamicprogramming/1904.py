# def make2(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 2
#     return (make2(n-1) + make2(n-2))%15746
    
# print(make2(int(input())))


n = int(input())
a = [0] * 1000000
a[0] = 1
a[1] = 2
for i in range(2, n):
    a[i] = (a[i - 2] + a[i - 1]) % 15746
print(a[n - 1])