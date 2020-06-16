def solution(n, words):
    answer = []
    num = len(words)
    for i in range(1,num,1):
        if(words[i][0]!=words[i-1][len(words[i-1])-1]):
            a = (i+1) % n
            if(a==0):
                a = n
            b = int((i) /n + 1)
            return [a,b]
        else:
            for j in range(i):
                if(words[j]==words[i]):
                    a = (i+1) % n
                    if(a==0):
                        a = n
                    b = int((i) /n + 1)
                    return [a,b]
    return [0,0]

print(solution(

  
3, ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]))

  

                

