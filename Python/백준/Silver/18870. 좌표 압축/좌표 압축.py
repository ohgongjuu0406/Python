import sys

n = int(sys.stdin.readline())

li = list(map(int,sys.stdin.readline().strip().split()))

result = list(set(li))


result.sort()

dic = {}

for i in range(len(result)):
    dic[result[i]]=i

for i in range(len(li)):
    print(dic[li[i]],end=' ')


    




