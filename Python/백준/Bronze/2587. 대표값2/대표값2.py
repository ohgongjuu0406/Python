li=[]
sum=0
for i in range(5):
    num = int(input())
    li.append(num)
    sum += num

mean = sum//5
li.sort()
print(mean)
print(li[2])