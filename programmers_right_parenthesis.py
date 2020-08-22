def solution(s):
    answer = True
    stack = []
    for i in s:
        if (i=='('):
            stack.append(i)
        else:
            if(len(stack)>0):
                if(stack[len(stack)-1]=='('):
                    stack.pop()
                else:
                    return False
            else:
                return False
    if(len(stack)>0):
        return False
    return True
