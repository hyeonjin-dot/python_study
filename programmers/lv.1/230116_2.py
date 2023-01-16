# https://school.programmers.co.kr/learn/courses/30/lessons/77884

def solution(left, right):
    sum = 0
    for i in range(left, right + 1):
        if (i ** 0.5).is_integer() == True:
            sum -= i
        else:
            sum += i
    return sum