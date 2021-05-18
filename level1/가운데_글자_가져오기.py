def solution(s):
    midPos = int(len(s) / 2)
    return s[midPos] if len(s) % 2 != 0 else s[midPos-1:midPos+1]
