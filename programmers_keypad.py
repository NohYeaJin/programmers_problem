def solution(numbers, hand):
    answer = ''
    Lpos = (3,0)
    Rpos = (3,2)
    key_pos = [(3,1),(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
    keypad_num = [[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    for i in numbers:

        if i == 1 or i == 4 or i == 7:
            answer+= "L"
            Lpos = key_pos[i]
        elif i == 3 or i == 6 or i == 9:
            answer += "R"
            Rpos = key_pos[i]
        else:
            a1,b1 = Lpos
            a2,b2 = key_pos[i]
            a3,b3 = Rpos
            a,b = a1 - a2, b1 - b2
            c,d = a3 - a2, b3 - b2

            if abs(a) + abs(b) > abs(c) + abs(d):
                Rpos = key_pos[i]
                answer += "R"
            elif abs(a) + abs(b) == abs(c) + abs(d):
                if hand == "right":
                    Rpos = key_pos[i]
                    answer += "R"
                else:
                    Lpos = key_pos[i]
                    answer += "L"
            else:
                Lpos = key_pos[i]
                answer += "L"

    return answer

#print(solution([7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2],"left"))