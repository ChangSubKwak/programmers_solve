def solution(n):
    ans = 0
    
    if n == 1: return 1
    
    while (n > 1):
        if n % 2 == 0:
            n /= 2
        else:
            ans+=1
            n -= 1
    
    return ans + 1
