def solution(s):
    answer = -1
    
    stack = []
    for i in s:
        if len(stack) < 1:
            stack.append(i)
            continue
        
        if stack[-1] == i:
            stack.pop()
            continue
            
        if stack[-1] != i:
            stack.append(i)

    return 1 if len(stack) == 0 else 0
