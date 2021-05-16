def solution(n):
    answer = 0
    prime = [1] * (n + 1)
    prime[0] = 0
    prime[1] = 0
    
    for i in range(2, n+1):
        if prime[i] == 0: continue
        
        for j in range(2 * i, n + 1, i):
            prime[j] = 0
    answer = prime.count(1)
    return answer
