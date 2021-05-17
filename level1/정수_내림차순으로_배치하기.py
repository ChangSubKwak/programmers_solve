def solution(n):
    answer = ''.join(sorted(''.join(str(n)), reverse = True))
    return int(answer)
