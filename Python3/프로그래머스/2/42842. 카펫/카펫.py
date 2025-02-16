def solution(brown, yellow):
    answer = []
    all = brown + yellow
    #무조건 3 이상(갈색 최소가 8개이기 때문)
    li =[]
    for i in range(3,all//2+1):
        if all % i !=0:
            continue
        h = i
        w = all // h
        if h<w:
            li.append((w,h))
        elif h<3 or w<3:
            continue
        else:
            li.append((h,w))
    li = list(set(li))
    print(li)
    
    yellow_list=[]
    for i in range(1,yellow//2+1):
        if yellow % i !=0:
            continue
        h = i
        w = yellow // h
        if w>h:
            w,h = (w,h)
        else:
            w,h = (h,w)
        yellow_list.append((w,h))
    yellow_list = set(yellow_list)
    yellow_list=list(yellow_list)
    
    if len(li)==1:
        answer.append(li[0][0])
        answer.append(li[0][1])
    else:
        for w,h in li:
            for y_w,y_h in yellow_list:
                if w-y_w==2 and h-y_h==2:
                    answer = [w,h]
                    
                    
        
    
    return answer