def solution(arr1, arr2):
    answer = []
    rowNum = len(arr1)
    colNum = len(arr1[0])
    
    for y in range(rowNum):
        answer.append([])
        for x in range(colNum):
            answer[y].append(arr1[y][x] + arr2[y][x])
    return answer
