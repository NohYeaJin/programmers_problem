def solution(d,budget):
    answer = 0
    d.sort()
    for i in d:
        if(i<=budget):
            answer = answer + 1
            budget = budget - i
        else:
            return answer
    return answer


