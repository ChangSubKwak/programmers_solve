def solution(left, right):
    answer = 0
    
    count = [0] * (right + 1)
    for i in range(1, right + 1):
        for j in range(1, int(right / i) + 1):
            count[i*j] += 1
    
    for i in range(left, right + 1):    
        if count[i]%2 == 0: answer += i
        else:               answer -= i

    return answer

