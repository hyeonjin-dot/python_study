x = int(input())

lst1 = input()
lst1 = lst1.split()
lst = list(map(int, lst1))
mx = max(lst)
sum = 0
for j in range(x):
    lst[j] = (lst[j] / mx) * 100
    sum = sum + (lst[j])
ave = sum / x
print(ave)