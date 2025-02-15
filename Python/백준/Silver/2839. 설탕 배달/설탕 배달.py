n = int(input())
result = []


if n % 3 == 0:
    result.append(n//3)

   
if n % 5 == 0:
    result.append(n//5)


i=1


while True:
    n1 = n
    n1=n1-5*i
    if n1>0 and n1 % 3 ==0:
        result.append(i+n1//3)

    elif n1<=0:
        break
    i+=1


j=1
while True:
    n2 = n
    if n2 <= 0:
        break
    n2 = n2 - 3*j
    if n2>0 and n2 % 5 == 0:
        result.append(j+n2//5)

    elif n2<=0:
        break
    j+=1

if len(result)==0:
    print(-1)
else:
    print(min(result))



