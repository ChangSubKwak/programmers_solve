def solution(seoul):
    answer = ''
    pos = 0
    for i in range(len(seoul)):
        if seoul[i] == 'Kim':
            pos = i
            break
    answer = '김서방은 ' + str(pos) + '에 있다'
    
    return answer
