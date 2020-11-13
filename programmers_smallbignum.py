def solution(s):
    numnum=[]
    num=s.split(" ")
    for i in num:
        i = int(i)
        numnum.append(i)
    numnum.sort()
    answer = str(numnum[0])+" "+str(numnum[len(numnum)-1])
    return answer
solution("1 2 3 4")