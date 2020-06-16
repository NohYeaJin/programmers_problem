def solution(heights):
    num = len(heights)
    answer = []
    for i in range(num):
        answer.append(check(heights,i))
    return answer

def check(heights,i):
    num = len(heights)
    for j in range(i-1,0,-1):
        if(heights[i]<heights[j]):
            return j+1
    return 0


print(solution([3,9,9,3,5,7,2]))