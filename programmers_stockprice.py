def solution(prices):
    num = len(prices)
    answer = []
    for i in range(num):
        answer.append(stock(i,prices))

    return answer

def stock(i,prices):
    price = 0
    for j in range(i+1,len(prices),1):
        if(prices[i]<=prices[j]):
            price = price+ 1
        else:
            return price+1
    return price

print(solution([1,2,3,2,3]))