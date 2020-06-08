def solution(citations):
    num = len(citations)
    answer = 0
    for i in range(1,num+1,1):
        print(i)
        cite = 0
        for j in range(num):
            if(citations[j]>=i):
                cite = cite + 1
        if(cite>=i):
            answer = i

            
    return answer

