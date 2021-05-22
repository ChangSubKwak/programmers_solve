def solution(n):
    answer = []
    
    while True:
        if   (n - 1) % 3 == 0: answer.append(1)
        elif (n - 1) % 3 == 1: answer.append(2)
        elif (n - 1) % 3 == 2: answer.append(4)
        n = int(n/3) - (1 if n % 3 == 0 else 0)
        if n == 0: break
    
    answer.reverse()
    s = [ str(i) for i in answer ]
    answer = "".join(s)
    
    return answer
