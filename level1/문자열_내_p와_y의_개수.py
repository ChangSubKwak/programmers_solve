def solution(s):
    answer = True
    
    countP = 0
    countY = 0
    
    for i in range(len(s)):
        if s[i] in ['P', 'p']: countP += 1
        if s[i] in ['Y', 'y']: countY += 1
    
    return True if countP == countY else False
