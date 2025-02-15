num=list(input())



num.sort(reverse=True)

sum=''
for i in range(len(num)):
    sum+=num[i]

print(int(sum)) 