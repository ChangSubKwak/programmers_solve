import math

def solution(n):
    answer = 0
    sq = int(math.sqrt(n))
    if sq**2 == n:
        return (sq + 1) ** 2
    return -1
