def solution(answers):
    answer = []
    a=[1,2,3,4,5] * 2000
    b = [2,1,2,3,2,4,2,5] *1250
    c = [3,3,1,1,2,2,4,4,5,5] *1000
    ans_a = a[:len(answers)]
    ans_b = b[:len(answers)]
    ans_c = c[:len(answers)]
    cnt_a = 0
    cnt_b = 0
    cnt_c = 0
    for i in range(len(answers)):
        if ans_a[i]==answers[i]:
            cnt_a+=1
        if ans_b[i]==answers[i]:
            cnt_b+=1
        if ans_c[i]==answers[i]:
            cnt_c+=1
            
    answer.append((cnt_a,1))
    answer.append((cnt_b,2))
    answer.append((cnt_c,3))
    
    answer.sort()
    max_=answer[-1][0]
    li = []
    for i in range(3):
        if answer[i][0]==max_:
            li.append(answer[i][1])
        
    return li
        
    
    
        
        
    # return answer