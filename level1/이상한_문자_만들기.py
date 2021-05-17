def solution(s):
    answer = ''
    i = 0
    wordPos = 0
    while i < len(s):
        if s[i].isalpha():
            if wordPos % 2 == 0: answer += s[i].upper()
            else               : answer += s[i].lower()
            wordPos += 1
        else:
            answer += s[i]
            wordPos = 0
        i += 1
    
    return answer
