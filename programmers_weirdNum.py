def solution(s):
    answer = ""
    num = 0
    for i in range(len(s)):
        if(s[i]==" "):
            num = 0
            answer = answer + " "
        else:
            if(num % 2 != 0):
                if(ord(s[i])<97):
                    answer = answer + chr(ord(s[i])+32)
                else:
                    answer = answer + s[i]
            else:
                if(ord(s[i])>=97):
                    answer = answer + chr(ord(s[i])-32)
                else:
                    answer = answer + s[i]
            num = num + 1

    return answer