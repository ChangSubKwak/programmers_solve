def solution(nums):
    answer = -1
    l = len(nums)
    count = 0
    for i in range(l):
        sum = nums[i]
        for j in range(i+1, l):
            sum += nums[j]
            for k in range(j+1, l):
                sum += nums[k]
                
                isPrime = True
                for m in range(2, sum):
                    if sum % m == 0:
                        isPrime = False
                        break
                if isPrime:
                    count+=1
                sum -= nums[k]
            sum -= nums[j]

    print('Hello Python')
    answer = count
    return answer
