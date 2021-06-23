'''
3
3
0 2 1
0 1 1
1 1 1
5
0 0 0 0 0
0 1 2 3 0
0 2 3 4 0
0 3 4 5 0
0 0 0 0 0
5
0 1 1 1 0
1 1 0 1 0
0 1 0 1 0
1 0 0 1 1
1 1 1 1 1
'''
from collections import deque
dir=[[-1,0],[1,0],[0,-1],[0,1]]
def search():
    global D
    D[0][0]=0
    Q=deque()
    Q.append((0,0))
    visited=[[0]*n for _ in range(n)]
    while Q:
        y,x=Q.popleft()
        visited[y][x]=1
        for dy,dx in dir:
            ny=y+dy
            nx=x+dx
            if 0<=ny<n and 0<=nx<n:
                if arr[y][x]>=arr[ny][nx]:
                    D[ny][nx]=min(D[ny][nx],D[y][x]+1)
                else:
                    D[ny][nx]=min(D[ny][nx],(arr[ny][nx]-arr[y][x])+D[y][x]+1)
                if not visited[ny][nx]:
                    Q.append((ny,nx))

for tc in range(1,int(input())+1):
    n=int(input())
    arr=[list(map(int,input().split())) for _ in range(n)]
    D=[[987654321]*n for _ in range(n)]
    search()
    print("#{} {}".format(tc,D[n-1][n-1]))