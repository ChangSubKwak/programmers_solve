def solution(lottos, win_nums):
    answer = []
    
    matchCnt = 0
    zeroCnt = 0
    for num in lottos:
        if num in win_nums:
            matchCnt += 1
            continue
        
        if num == 0:
            zeroCnt += 1

    max = 7 - matchCnt - zeroCnt 
    min = 7 - matchCnt - (1 if zeroCnt == 6 else 0)
    
    if (matchCnt + zeroCnt) == 0: return [6, 6]
    
    answer.append(max)
    answer.append(min)
    
    return answer
