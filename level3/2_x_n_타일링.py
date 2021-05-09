def solution(n):
    if n == 1: return 1
    elif n == 2: return 2
    
    answer = 0
    
    data = [0] * (n+1)
    data[1] = 1
    data[2] = 2
    
    for i in range(3, n+1):
        data[i] += data[i-1] + data[i-2]
        data[i] %= 1000000007
        #print(data[i])

    answer = data[n]
    
    return answer
