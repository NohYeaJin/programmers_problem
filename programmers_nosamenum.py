def sosu(n):
    for i in range(3,(int(n/2)+1),2):
        print(i)
        if(n%i==0):
            return False
    return True

def solution(n):
    answer = 0
    for i in range(3,n+1,2):
        if(sosu(i)==True):
            answer = answer + 1
    return answer+1

print(sosu(7))