def solution(skill, skill_trees):
    answer = 0
    pos = {}
    for i in skill:
        pos[i] = 26
    
    for st in skill_trees:
        for i in skill:
            pos[i] = 26
        
        for i in skill:
            if st.find(i) < 0:
                continue
            pos[i] = st.find(i)
        
        isMatch = True
        for i in range(len(skill) - 1):
            if pos[skill[i]] > pos[skill[i+1]]:
                isMatch = False
                break
        if isMatch:
            answer += 1
    return answer
