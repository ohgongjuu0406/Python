from collections import deque
import sys
n,m = map(int,sys.stdin.readline().split())
map = []
for i in range(n):
    map.append(list(sys.stdin.readline().strip()))

# print(map)

graph = [[] for i in range(n*m)]

#이어져있는 걸 바탕으로 graph 구하기
for i in range(n):
    for j in range(m):
        if map[i][j] == '1':
            #상
            if (i!=0) and map[i-1][j]=='1':
                #1차원 인덱스 기준으로 넣을거임
                graph[m*i+j].append(m*(i-1)+j)
            #하
            if (i!=n-1) and map[i+1][j]=='1':
                #1차원 인덱스 기준으로 넣을거임
                graph[m*i+j].append(m*(i+1)+j)
            #좌
            if j!=0 and map[i][j-1]=='1':
                #1차원 인덱스 기준으로 넣을거임
                graph[m*i+j].append(m*i+j-1)
            #우
            if j!=m-1 and map[i][j+1]=='1':
                #1차원 인덱스 기준으로 넣을거임
                graph[m*i+j].append(m*i+j+1)

for i in range(n):
    graph[i].sort()



def bfs(graph,start,target):
    dist = 1
    queue = deque([(start,dist)])
    visited = []
    
    
    while queue:
        node,dist = queue.popleft()
        if node not in visited:
            if node == target:
                return dist
            visited.append(node)
            for child in graph[node]:
                queue.append((child,dist+1))
        


print(bfs(graph,0,n*m-1))