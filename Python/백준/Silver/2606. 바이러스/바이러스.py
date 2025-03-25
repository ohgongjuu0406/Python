import sys
from collections import deque
#컴퓨터의 수
n = int(sys.stdin.readline())
#컴퓨터 쌍의 수
m = int(sys.stdin.readline())
ma = []
for i in range(n+1):
    ma.append([])

for i in range(m):
    x,y = sys.stdin.readline().split()
    ma[int(x)].append(int(y))
    ma[int(y)].append(int(x))

#시작점은 1
cnt = 0
#방문한 노드
visited = []
#방문할 노드
start = 1
need = deque([start])

while True:
    node = need.popleft()
    if node not in visited:
        visited.append(node)
        cnt+=1
        need.extend(ma[node])
    if len(need)==0:
        #1번 컴퓨터를 통해 감영되는 컴퓨터의 수이므로 1을 빼야함
        print(cnt-1)
        break

