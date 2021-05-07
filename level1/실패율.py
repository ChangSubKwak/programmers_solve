def solution(N, stages):
    answer = [0] * N
    
    stages.sort()
    for i in stages:
        if i <= N: 
            answer[i-1]+=1
    print(answer)
    
    size = len(stages)
    temp = []
    for i in range(len(answer)):
        if answer[i] == 0:
            temp.append( (i+1, 0))
            continue
        failRatio = answer[i] / size
        size -= answer[i]
        answer[i] = failRatio
        temp.append( (i+1, answer[i]))
    
    print(temp)
    temp2 = sorted(temp, key = lambda x : -x[1])
    print(temp2)
    
    answer = []
    for i in temp2:
        answer.append(i[0])
    
    return answer
