def solution(n, m):
    if n > m: n, m = m, n
    maxVal, minVal = m, n
    
    while maxVal % minVal != 0:
        maxVal = maxVal - minVal
        if maxVal < minVal:
            maxVal, minVal = minVal, maxVal
    gcd = minVal
    
    maxVal, minVal = m, n
    if m % n == 0: lcm = m
    else         : lcm = m*n/gcd
    
    answer = [gcd, lcm]
    return answer
