def solution(n, arr1, arr2):
    answer = []
    list = [0]*n
    for i in range(n):
        list[i] = arr1[i] | arr2[i]
        val = (('%' + str(n) + 's') % bin(list[i])[2:]).zfill(n).replace('1','#').replace('0',' ')
        answer.append(val)
    
    return answer
