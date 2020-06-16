def solution(n, t, m, p):
    i = 0
    A=""
    answer = ''
    if(n==2):
        while(len(A)<=m*(t)):
            B = str(bin(i))
            print(B)
            print(A,"AA")
            A= A.join(B[2:])
            i = i + 1


    elif(n==8):
        while(len(A)<=m*(t+1)):
            B = str(oct(i))
            A= A.join(B[2:])
            i = i + 1

    elif(n==10):
        while(len(A)<=m*(t+1)):
            B = str(i)
            A= A.join(B[2:])
            i = i + 1


    elif(n==16):
        while(len(A)<=m*(t+1)):
            B = str(hex(i))
            A= A.join(B[2:])
            i = i + 1

    print(A)
    num = p - 1 + m
    for i in range(t):
        if(t==0):
            answer = answer.join(A[p-1])
        else:
            answer = answer.join(A[num])
            num = num + m

    
    return answer

print(solution(2,4,2,1))
