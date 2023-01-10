#https://school.programmers.co.kr/learn/courses/30/lessons/12916

def solution(s):
    s = s.lower()
    a = len(s.split('p'))
    b = len(s.split('y'))
    return(a == b)