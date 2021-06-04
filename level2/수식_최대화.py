from itertools import permutations
import re

def solution(expression):
    permute = permutations(['*','-','+'],3)
    opLists = list(permute)
    
    max = 0
    resVal = ''
    for opList in opLists:
        i = 0
        j = 0
        exList = re.split('(?=\*|\+|\-)|(?<=\*|\+|\-)', expression);
        while(True):
            element = exList[i]
            if element == '*' and opList[j] == '*':
                resVal = str(int(exList[i-1]) * int(exList[i+1]));
                for _ in range(3): del exList[i-1]
                exList.insert(i-1, resVal)
                i-=1
                continue
            elif element == '-' and opList[j] == '-':
                resVal = str(int(exList[i-1]) - int(exList[i+1]))
                for _ in range(3): del exList[i-1]
                exList.insert(i-1, resVal)
                i-=1
                continue;
            elif element == '+' and opList[j] == '+':
                resVal = str(int(exList[i-1]) + int(exList[i+1]))
                for _ in range(3): del exList[i-1]
                exList.insert(i-1, resVal)
                i-=1
                continue;        

            i+=1
            if i >= len(exList):
                i = 0
                j += 1
                
            if j >= 3:
                break
        if max < abs(int(exList[0])):
            max = abs(int(exList[0]))
        
    return max
