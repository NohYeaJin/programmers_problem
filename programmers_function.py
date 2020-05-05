def solution(progresses, speeds):
    answer = []
    while(len(progresses)>0):
        for i in range(len(progresses)):
            if(progresses[i]<100):
                progresses[i] += speeds[i]

        if(progresses[0]>=100):
            answer.append(function(progresses,speeds))

    return answer

def function(progresses,speeds):
    num = 0
    num2 = 0
    if(len(progresses)==1):
        progresses.pop(0)
        speeds.pop(0)
        return 1
    while((len(progresses)>=1)&(progresses[num]>=100)):
        num2 = num2 + 1
        progresses.pop(0)
        speeds.pop(0)
        if(len(progresses)==0):
            break
    return num2






