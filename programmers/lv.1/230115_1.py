# https://school.programmers.co.kr/learn/courses/30/lessons/12933

def solution(n):
    tmp = list(str(n))
    tmp.sort(reverse=True)
    tmp = ''.join(tmp)
    return (int(tmp))