def solution(s):
    numbers = {"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9}
    num_str = ""
    answer = ""
    for i in s:
        if 48<= ord(i) <=57:
            answer += i
        else:
            num_str += i
            if num_str in numbers:
                answer += str(numbers[num_str])
                num_str = ""
    return answer