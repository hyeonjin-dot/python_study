n = int(input())

def solution(n):
    if n == 0:
        return 0
    sol = set()
    for i in range(2, int(n**1/2) + 1):
        if n % i == 0:
            sol.add(i) 
            sol.add(n//i)
    sol.add(1)
    sol.add(n)
    sol = list(sol)
    return (sum(sol))

print(solution(n))

#https://www.notion.so/Lv-1-f3cf9b6cf8fc4913baacb6bbaba01592#7244ddd97bf549a1bfb5510684f68c07