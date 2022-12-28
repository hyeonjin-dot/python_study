x = input()
x = x.upper()
y = [0 for i in range(1000)]
for i in range(len(x)):
    j = ord(x[i])
    y[j] += 1
max = 0
rtn = 0
for i in range(1000):
    if y[i] > max:
        max = y[i]
        rtn = i
for i in range(1000):
    if i != rtn and max == y[i]:
        rtn = ord('?')
print(chr(rtn))