def solution(dartResult):
    answer = 0
    i = 0
    length = len(dartResult)
    
    score = [0] * 3
    bonus = {'S':1, 'D':2, 'T':3}
    setIdx = 0
    while setIdx < 3:
        if dartResult[i] == '1' and dartResult[i+1] == '0':
            score[setIdx] = 10
            i+=2
        else:
            score[setIdx] = int(dartResult[i])
            i+=1
        score[setIdx] = pow(score[setIdx], bonus[dartResult[i]])
        i+=1
        
        if i < length and dartResult[i] == '*':
            start = 0 if setIdx == 0 else setIdx - 1
            for j in range(start, setIdx+1):
                score[j]*=2
            i+=1
        if i < length and dartResult[i] == '#':
            score[setIdx]*=-1
            i+=1
        setIdx+=1
    
    for i in range(3):
        print(score[i])
    answer = score[0] + score[1] + score[2]
    
    return answer
