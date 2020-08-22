
def solution(board, moves):
    dolls=[]
    answer = 0
    for i in moves:
        print(dolls)
        n = 0
        while((board[n][i-1]==0)&(n<=len(board)-2)):
            n = n + 1
        if(board[n][i-1]!=0):
            if((len(dolls)>=1)):
                if(dolls[len(dolls)-1]==board[n][i-1]):
                    dolls.pop()
                    answer = answer + 2
                else:
                    dolls.append(board[n][i-1])
            else:
                dolls.append(board[n][i-1])
        board[n][i-1] = 0
    return answer


print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],[1,5,3,5,1,2,1,4]))


        


