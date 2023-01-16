# https://school.programmers.co.kr/learn/courses/30/lessons/150370

def solution(today, terms, privacies):
    ans = []
    term = dict()
    today = today.replace('.','')
    for i in terms:
        term[i[0]] = i[2:]
    for i in privacies:
        date = i[:10]
        pri = i[-1]
        date = date.replace('.', '')
        tmp = int(date) + (int(term[pri]) * 100)
        q = (tmp % 10000) // 100
        while (q > 12):
            if q > 12:
                tmp = tmp + 10000 - 1200
            q = (tmp % 10000) // 100
        if int(today) >= tmp:
            ans.append(privacies.index(i) + 1)
    return ans