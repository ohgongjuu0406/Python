import sys
from collections import deque

T = int(sys.stdin.readline())

for t in range(T):
    m,n,k = map(int,sys.stdin.readline().split())

    ma = []

    for i in range(m):
        ma.append([])
        for j in range(n):
            ma[i].append(0)

   


    for i in range(k):
        x,y = map(int, sys.stdin.readline().split())
        ma[x][y] = 1


        
    cnt = 0

    #시작점을 찾기 위해 전체 맵을 조사하여 1 검색
    while True:

        for i in range(m):
            for j in range(n):
                if ma[i][j] == 1: 
                    cnt +=1
                    need = deque([(i,j)])
                    visited = []
                    
                    while True:
                        x,y = need.popleft()
                        if (x,y) not in visited:
                            visited.append((x,y))
                            ma[x][y] = 0
                            

                            dx = [-1,1,0,0]
                            dy = [0,0,-1,1]
                            for k in range(4):

                                nx = x + dx[k]
                                ny = y + dy[k]

                                if 0<=nx<=m-1 and 0<=ny<=n-1 and ma[nx][ny] == 1:
                                    need.append((nx,ny))    

                        if len(need)==0:
                            break   


        #종료 조건:
        if 1 not in ma:
            break

    print(cnt)



