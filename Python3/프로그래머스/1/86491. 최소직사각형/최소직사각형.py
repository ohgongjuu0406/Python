def solution(sizes):
    
    li_w=[]
    li_h=[]
    answer = []
    for i,(w,h) in enumerate(sizes):
        li_w.append(w)
        li_h.append(h)
        
    # print(li_w)
    # print(li_h)
    min_ = min(min(li_w),min(li_h))
    max_ = max(max(li_w),max(li_h))
    
    
    for j in range(min_,max_+1):
        cnt=0
        for i in range(len(li_w)):
            w,h = li_w[i],li_h[i]
            if (w<=max_ and h<=j) or (h<=max_ and w<=j):
                cnt+=1
        if cnt==len(li_h):
            answer.append(max_*j)
        
    return min(answer)
    
    
        
            

    return min(answer)
                
        
    
    
    