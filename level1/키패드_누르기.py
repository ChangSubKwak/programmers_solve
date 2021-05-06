def solution(numbers, hand):
    answer = []

    pos = { 1:[-1, 1], 2:[0, 1], 3:[1, 1], 4:[-1, 0], 5:[0, 0], 6:[1, 0], 7:[-1,-1], 8:[0,-1], 9:[1,-1], '*':[-1,-2], 0:[0,-2],'#':[1,-2] }
    
    lPos = pos['*']
    rPos = pos['#']
    
    for i in range(len(numbers)):
        key = numbers[i]
        if key in [1,4,7]:
            answer.append("L")
            lPos = pos[key]
            continue;
            
        if key in [3,6,9]:
            answer.append("R")
            rPos = pos[key]
            continue;
            
        lDis = abs(pos[key][0] - lPos[0]) + abs(pos[key][1] - lPos[1])
        rDis = abs(pos[key][0] - rPos[0]) + abs(pos[key][1] - rPos[1])
        #print(str(lDis) + " : " + str(rDis))
        if lDis > rDis:
            answer.append("R")
            rPos = pos[key]
        elif lDis < rDis:
            answer.append("L")
            lPos = pos[key]
        else:
            answer.append(hand[0])
            if hand[0] == "l": lPos = pos[key]
            else:              rPos = pos[key]
            
    return "".join(answer).upper()
