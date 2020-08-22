def solution(s):
    answer=""
    if(len(s)%2==0):
        list1 = s[int(len(s)/2-1):int(len(s)/2)+1]

        return list1
    else:
        num = int((len(s)-1)/2)
        return s[num]


print(solution("abcdee"))
