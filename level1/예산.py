def solution(d, budget):
    d.sort()
    sum = 0
    count = 0
    answer = 0
    
    for i in d:
        if sum+i <= budget:
            sum += i
            count+=1
            continue
        break
    
    answer = count
    return answer
