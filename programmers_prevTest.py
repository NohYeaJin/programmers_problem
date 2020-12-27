def solution(answers):
    answer1 = [1,2,3,4,5]*2000
    answer2 = [2,1,2,3,2,4,2,5]*1250
    answer3 = [3,3,1,1,2,2,4,4,5,5]*1000
    num1 = 0
    num2 = 0
    num3 = 0
    for i in range(len(answers)):
        if(answers[i]==answer1[i]):
            num1 = num1 + 1
        if(answers[i]==answer2[i]):
            num2 = num2 + 1
        if(answers[i]==answer3[i]):
            num3 = num3 + 1
    if((num1>num2)and(num1>num3)):
        return [1]
    if((num2>num3)and(num2>num1)):
        return [2]
    if((num3>num2)and(num3>num1)):
        return [3]
    if((num1==num2)and(num1>num3)):
        return [1,2]
    if((num2==num3)and(num2>num1)):
        return [2,3] 
    if((num1==num3)and(num1>num2)):
        return [1,3] 
    if((num1==num3)and(num1==num2)):
        return [1,2,3]
    
