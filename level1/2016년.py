def solution(a, b):
    day = ['FRI','SAT','SUN','MON','TUE','WED','THU']
    dayNum = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    daySum = 0
    daySum += b - 1
    for i in range(a-1): daySum += dayNum[i]
    daySum %= 7
    
    return day[daySum]
