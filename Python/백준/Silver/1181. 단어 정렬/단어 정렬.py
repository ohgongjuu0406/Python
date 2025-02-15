import sys
n = int(sys.stdin.readline())

li = []
for i in range(n):
    word = sys.stdin.readline().strip()
    if word in li:
        continue
    li.append((len(word),word))
li=list(set(li))
li.sort()

for x,y in li:
    print(y)
    
