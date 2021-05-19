def solution(x):
    answer = True
    digitList = [ int(i) for i in str(x) ]
    digitSum = sum(digitList)
    if x%digitSum != 0:
        answer = False
    return answer
