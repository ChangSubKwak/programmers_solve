def solution(s, n):
    answer = ''
    
    for i in s:
        if i.isalpha():
            if i.islower():
                answer += chr(ord('a') + (ord(i) - ord('a') + n) % 26)
            else:
                answer += chr(ord('A') + (ord(i) - ord('A') + n) % 26)
        else:
            answer += i
        
    return answer
