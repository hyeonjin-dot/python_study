def dis(x):
    y = x
    while True:
        for i in range(2, x+1):
            if y % i == 0 and y >= i:
                print(i)
                y = y / i
                break
        if (y == 1):
            return

dis(int(input()))
