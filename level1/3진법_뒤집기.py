def solution(n):
    answer = 0
    
    threeNary = []
    
    remain = n % 3
    n = int(n / 3)
    threeNary.append(remain)
    while n != 0:
        remain = n % 3
        n = int(n / 3)
        threeNary.append(remain)
    
    threeNary.reverse()
    for i in range(len(threeNary)):
        answer += threeNary[i] * 3 ** i
    
    return answer
