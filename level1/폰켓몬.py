def solution(nums):
    list = []
    for n in nums:
        if n not in list:
            list.append(n)
    length = len(list)
    half = len(nums) / 2
    answer = min (length, half)
    return answer
