def solution(people, limit):
    num = len(people)
    people.sort(reverse = True)
    return check(people,limit)

def check(people,limit):
    num = len(people)
    min = limit-(people[0])
    i = 0
    answer = 0
    print(people)
    while(len(people)>1):
        
        j = len(people)-1
        print(people[i],people[j])
        print(i)
        if(limit<(people[i]+people[j])):
            print(i)
            if(limit>people[i]+people[j-1]):
                people.remove(people[j-1])
                people.remove(people[i])
                answer = answer + 1
            else:
                print("dsds")
                answer = answer + 1
                people.remove(people[i])
        elif(limit==(people[i]+people[j])):
            answer = answer + 1
            people.remove(people[i])
            people[j-1]=0
        else:
            j = j - 1
    if(people[0]>0):
        answer = answer + 1
    return answer



print(solution([70, 50, 80, 50],100))




