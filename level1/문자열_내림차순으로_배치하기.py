def solution(s):
    s = [ch for ch in s]
    s.sort(reverse=True)
    answer = ''.join(s)
    return answer
