def solution(nums):
    result = 0
    length = int(len(nums)/2)
    poketmon=[]
    for i in nums:
        if(result<length):
            if(i not in poketmon):
                poketmon.append(i)
                result = result + 1
        else:
            return len(poketmon)
    return len(poketmon)