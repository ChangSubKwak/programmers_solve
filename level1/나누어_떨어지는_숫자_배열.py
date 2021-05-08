def solution(arr, divisor):
    answer = []
    for i in arr:
        #print(str(i) + ' ' + str(i % divisor))
        if (i % divisor) == 0:
            answer.append(i)
    #print(answer)
    answer.sort()
    return [-1] if len(answer) == 0 else answer
