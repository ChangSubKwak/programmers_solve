def solution(s):
    answer = True
    if len(s) not in [4, 6]:
        return False
    
    if not s.isdigit():
        return False
    
    return answer
