def solution(A,B):
    answer = 0
    A.sort()
    B.sort(reverse = True)
    num = len(A)
    for i in range(num):
        answer = answer + A[i]*B[i]
    return answer