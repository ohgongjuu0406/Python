import sys

n = int(sys.stdin.readline())
li = []
for i in range(n):
    age,name = sys.stdin.readline().strip().split()
    li.append((int(age),i,name))

li.sort()

for age,i,name in li:
    print(age,name)