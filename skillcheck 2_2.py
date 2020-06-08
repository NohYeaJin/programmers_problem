def solution(n):
    answer = 0
    i = 2
    if((n==2)or(n==3)):
        return -1
    elif(n==1):
        return 4
    elif(n==4):
        return 9
    while((i*i)<=50000000000000):
        num1 = i * i
        num2 = (i+1)*(i+1)
        print(i)
        if((n<=num2 and n>=num1)):
            if(n==num2):
                return (i+2)*(i+2)
            else:
                return -1
        else:
            i = i + 1
    return -1


