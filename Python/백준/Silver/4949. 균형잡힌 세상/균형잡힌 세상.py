import sys
s = sys.stdin.readlines()

for i in range(len(s)-1):
    stack = []
    sen = s[i].strip().split()
    result = True
  
    for j in range(len(sen)):
        for k in range(len(sen[j])):
            if '(' == sen[j][k]:
                stack.append('(')
            elif ')' in sen[j][k]:
                if len(stack)!=0:
                    a = stack.pop()
                    if a!='(':
                        result=False
                        break
                else:
                    result=False
                    break
            elif '[' == sen[j][k]:
                stack.append('[')
            elif ']' == sen[j][k]:
                if len(stack)!=0:
                    a = stack.pop()
                    if a!='[':
                        result=False
                        break
                else:
                    result = False
                    break
        if result == False:
            break
    
        
    if len(stack)==0 and result==True:
        print('yes')
    else:
        print('no')
