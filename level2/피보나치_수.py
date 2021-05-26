def solution(n):
    answer = 0
    if n == 1: return 0
    if n == 2: return 1
    
    start = 3
    f0 = 0
    f1 = 1
    for _ in range(start, n + 2):
        f2 = f0 + f1
        f0, f1 = f1, f2
    answer = f2 % 1234567
    
    return answer
