import sys
n = int(sys.stdin.readline())

li = []
for i in range(n):
    x,y = map(int,sys.stdin.readline().split())
    li.append((x,y))

li.sort()

for x,y in li:
    print(x,y)
