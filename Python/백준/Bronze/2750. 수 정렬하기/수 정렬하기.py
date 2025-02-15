import math
#선택 정렬 : 최소값 찾아서 리스트 맨 앞과 교환(그 다음 인덱스부터도 다시 진행)
n = int(input())
li = []
for i in range(n):
    li.append(int(input()))

for i in range(len(li)):
    min_num = min(li[i:])
    idx = li.index(min_num)
    li[idx] = li[i]
    li[i] = min_num



for i in range(len(li)):
    print(li[i])
            

