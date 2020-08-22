def solution(phone_number):
    num=len(phone_number)
    listlist = phone_number[num-4::]
    list1="".join(listlist)
    list2 = "*"*(num-4)
    return list2+listlist

print(solution("12345678"))
