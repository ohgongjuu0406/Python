import sys
t = int(sys.stdin.readline())


for i in range(t):
    stack = []
    result = True
    n = list(sys.stdin.readline().strip())
    for j in range(len(n)):
        if n[j] =='(':
            stack.append('(')
        else:
            if len(stack)==0:
                result=False
                break
            else:
                stack.pop()
    
    if len(stack)!=0 or result==False:
        print('NO')
    else:
        print('YES')