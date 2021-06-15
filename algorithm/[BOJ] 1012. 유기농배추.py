'''
2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5
'''
dir=[[-1,0],[1,0],[0,-1],[0,1]]
def search(i,j):
    global cnt,visited
    cnt+=1
    visited[i][j]=1
    arr[i][j]=0
    stack=list()
    stack.append((i,j))
    while stack:
        nowy,nowx=stack.pop(-1)
        for dy,dx in dir:
            ny=nowy+dy
            nx=nowx+dx
            if 0<=ny<N and 0<=nx<M and visited[ny][nx]==0 and arr[ny][nx]==1:
                visited[ny][nx]=1
                arr[ny][nx]=0
                stack.append((ny,nx))

for tc in range(int(input())):
    M,N,K=map(int,input().split())
    arr=[[0]*M for _ in range(N)]
    visited=[[0]*M for _ in range(N)]
    cnt=0

    for _ in range(K):
        X,Y=map(int,input().split())
        arr[Y][X]=1

    for y in range(N):
        for x in range(M):
            if arr[y][x]==1:
                search(y,x)

    print(cnt)