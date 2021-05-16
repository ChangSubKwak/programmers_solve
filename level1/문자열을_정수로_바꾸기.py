def solution(s):
    #return int(s)
    length = len(s)
    answer = 0
    if s[0] in ('-', '+'):
        sign = 1 if s[0] == '+' else -1
        s = s[1:]
        length -= 1
        for i in s:
            answer += (ord(i) - ord('0')) * pow(10, length - 1)
            length -= 1
        answer *= sign
    else:
        for i in s:
            answer += (ord(i) - ord('0')) * pow(10, length - 1)
            length -= 1
    return answer
