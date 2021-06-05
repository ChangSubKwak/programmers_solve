from itertools import permutations
import re

def solution(expression):
    permute = permutations(['*','-','+'], 3)
    opLists = list(permute)
    
    max = 0
    resVal = ''
    for opList in opLists:
        i = 0
        j = 0
        exList = re.split('(?=\*|\+|\-)|(?<=\*|\+|\-)', expression);
        while(True):
            if exList[i] in ['*','-','+'] and exList[i] == opList[j]:
                resVal = eval(exList[i-1] + exList[i] + exList[i+1]);
                for _ in range(3): del exList[i-1]
                exList.insert(i-1, str(resVal))
                i-=1
                continue
            i+=1
            if i >= len(exList):
                i = 0
                j += 1
                
            if j >= 3:
                break
        # end of while                
        if max < abs(int(exList[0])):
            max = abs(int(exList[0]))
        
    # print(exList)
    return max
