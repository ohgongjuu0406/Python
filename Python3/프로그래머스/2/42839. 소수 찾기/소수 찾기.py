import itertools

#소수 찾기
def find(num):
    if num==1 or num==0:
        return 0
    lis = [2,3,5,7]
    if num in lis:
        return 1
    
    for i in range(2,num//2+1):
        if num%i==0:
            break
        if i==num//2 and num%i!=0:
            return 1
        
def solution(numbers):
    answer = 0
    li = list(numbers)
    #가능한 모든 조합을 찾기->소수 판단
    per = []
    for i in range(1,len(li)+1):
        for p in itertools.permutations(li, i):
            per.append(int(''.join(p)))
    per = set(per)
    per = list(per)
    print(per)
    for i in range(len(per)):
        num = int(per[i])
        if find(num)==1:
            answer+=1
    return answer 

                
    