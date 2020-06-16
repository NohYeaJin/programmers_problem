def solution(citations):

    num = len(citations)
    cite = 1

    while(citations):
        number = 0
        for i in range(num):           
            if(citations[i]>=cite):               
                number = number + 1
        if(number>=cite):
            cite = cite + 1
        else:
            return cite - 1
            

print(solution([2,2,2,2,2]))              
