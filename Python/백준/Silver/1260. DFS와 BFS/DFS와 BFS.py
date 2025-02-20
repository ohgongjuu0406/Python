from collections import deque
import sys
n,m,v = map(int,sys.stdin.readline().split())

graph = [[] for i in range(n+1)]

for i in range(m):
    s,e = map(int,sys.stdin.readline().split())
    graph[s].append(e)
    #그래프는 양방향
    graph[e].append(s)

#단, 방문할 수 있는 정점이 여러 개인 경우에는 정점 번호가 작은 것을 먼저 방문하고,
# 더 이상 방문할 수 있는 점이 없는 경우 종료한다. 정점 번호는 1번부터 N번까지이다.
for i in range(1,n+1):
    graph[i].sort()
# print(graph)

dfs_visited = []
def dfs_recursive(start_node,graph,visited):
    visited.append(start_node)
    for node in graph[start_node]:
        if node not in visited:
            dfs_recursive(node,graph,visited)
    return visited
                  
def bfs_recursive(start_node,graph):
    need_visit = deque([start_node])
    visited = []
    while need_visit:
        node = need_visit.popleft()
        if node not in visited:
            visited.append(node)
            need_visit.extend(graph[node])
    return visited

result = dfs_recursive(v,graph,dfs_visited) 
result2= bfs_recursive(v,graph)
for i in range(len(result)):
    print(result[i],end=' ')
print()
for i in range(len(result2)):
    print(result2[i], end = ' ')



