def same(i,k,phone_book):
    answer = True
    for j in range(len(phone_book[i])):
        if(phone_book[i][j]==phone_book[k][j]):
            answer = False
        else:
            return True
    return answer


def solution(phone_book):
    for i in range(len(phone_book)):
        for k in range(len(phone_book)):
            if(len(phone_book[i])<len(phone_book[k])):
                if(same(i,k,phone_book)==False):
                    return False

    return True




