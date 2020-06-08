def solution(s):
    stack = []
    s= list(s)
    if((len(s)%2)==1):
        return 0

    for i in range(len(s)):
        if(i==0):
            stack.append(s[0])
        else:
            if(len(stack)>0):
                if(s[i]==stack[len(stack)-1]):
                    stack.pop()
                else:
                    stack.append(s[i])
            else:
                stack.append(s[i])
    if(len(stack)>0):
        return 0
    else:
        return 1