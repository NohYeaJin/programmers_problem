def solution(n, words):
    num = len(words)
    answer = []
    for i in range(1,num,1):
        if(words[i][0]!=words[i-1][len(words[i-1])-1]):
            i = i + 1
            num1 = i % n
            if(num1==0):
                num1 = n
                num2 = int(i / n)
            else:
                num2 = i/n+1
                num2 = int(num2)
            answer = [num1,num2]
            return answer

        else:
            for j in range(i):
                if(words[i]==words[j]):
                    i = i + 1
                    num1 = i % n
                    if(num1==0):
                        num1 = n
                        num2 = int(i / n)
                    else:
                        num2 = i/n+1
                        num2 = int(num2)
                    answer = [num1,num2]
                    return answer
    return [0,0]

print(solution(2,["hello", "one", "even", "never", "now", "world", "draw"]))