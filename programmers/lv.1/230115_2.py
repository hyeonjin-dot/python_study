# https://school.programmers.co.kr/learn/courses/30/lessons/12919

def solution(seoul):
    if "Kim" in seoul:
        return ("김서방은 %d에 있다" %(seoul.index("Kim")))