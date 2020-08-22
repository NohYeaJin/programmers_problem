def solution(a, b):
    months=[0,31,29,31,30,31,30,31,31,30,31,30,31]
    days=["FRI","SAT","SUN","MON","TUE","WED","THU"]
    total = 0
    for i in range(a):
        total = total + months[i]
    total = total + b - 1
    total = total % 7
    answer = days[total]
    return answer

print(solution(12,31))
