'''
3 4 5
3 2
2 2
3 1
2 3
1 1
'''
dir=[[-1,0],[1,0],[0,-1],[0,1]]
def trash(i,j):
    global cnt,arr,visited
    sub_cnt=1
    q=list()
    q.append([i,j])

    while q:
        nowy,nowx=q.pop(0)
        visited[nowy][nowx]=1
        for dy,dx in dir:
            ny=dy+nowy
            nx=dx+nowx
            if 0<=ny<N and 0<=nx<M and arr[ny][nx]==1 and visited[ny][nx]==0:
                q.append([ny,nx])
                sub_cnt+=1
                visited[ny][nx]=1

    if sub_cnt>cnt:
        cnt=sub_cnt

N,M,K=map(int,input().split())
arr=[[0]*M for _ in range(N)]
visited=[[0]*M for _ in range(N)]

cnt=0
for _ in range(K):
    r,c=map(int,input().split())
    arr[r-1][c-1]=1

for i in range(N):
    for j in range(M):
        if arr[i][j]==1:
            trash(i,j)
print(cnt)