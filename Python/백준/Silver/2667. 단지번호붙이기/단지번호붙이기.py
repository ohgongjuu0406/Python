import sys
n = int(sys.stdin.readline())
ma = []
for i in range(n):
    ma.append(list(sys.stdin.readline().strip()))

answer = []

from collections import deque
while True:    
    #1을 찾기 위해 탐색

    
    for a in range(n):
        for b in range(n):
            if ma[a][b] == '1':
                visited = []
                need_visit = deque([(a,b)])
                cnt = 0
                
                while True:
                    x,y = need_visit.popleft()
                    if (x,y) not in visited:
                        visited.append((x,y))
                        cnt += 1
                        #방문처리한 x,y는 0으로 바꿈
                        ma[x][y]='0'
                            
                        
                        #상,하,좌,우
                        dx = [0,0,-1,1]
                        dy = [-1,1,0,0]
                        for i in range(4):
                            nx = x + dx[i]
                            ny = y + dy[i]
                        #벽을 넘지 않고, 1인 경우 방문할 리스트에 추가
                            if 0<=nx<=n-1 and 0<=ny<=n-1 and ma[nx][ny]=='1':
                                need_visit.append((nx,ny))
                    if len(need_visit) == 0 :
                        answer.append(cnt)
                        # print(cnt)
                        break
            
    if all('1' not in row for row in ma):
        break
print(len(answer))
answer.sort()
for i in range(len(answer)):
    print(answer[i])
 






    

