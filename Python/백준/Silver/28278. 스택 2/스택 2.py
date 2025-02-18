import sys
n = int(sys.stdin.readline())
stack = []
for i in range(n):
    x = list(map(int,(sys.stdin.readline().split())))
    for j in range(len(x)):
        if x[j]==1:
            stack.append(x[j+1])
            break
        elif x[j]==2:
            if len(stack)!=0:
                a = stack.pop()
                print(a)
            else:
                print(-1)
        elif x[j]==3:
            print(len(stack))
        elif x[j]==4:
            if len(stack)==0:
                print(1)
            else:
                print(0)
        elif x[j]==5:
            if len(stack)!=0:
                print(stack[-1])
            else:
                print(-1)

    

