def solution(numbers):
    answer2=[]
    for i in numbers:
        j = str(i)
        answer2.append(j)
    answer2.sort(reverse=True)
    print(answer2)
    answer = ''
    answer = ''.join(str(v) for v in answer2)
    return answer
numbers=[6,10,2]
print(solution(numbers))
