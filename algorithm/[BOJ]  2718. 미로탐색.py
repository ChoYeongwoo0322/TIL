'''
4 6
101111
101010
101011
111011
'''
# 최소칸수 = BFS

dir=[[-1,0],[1,0],[0,-1],[0,1]]
def bfs(sy,sx,ey,ex,visited):
    q=list()
    q.append([sy,sx])

    while q:
        now_y,now_x=q.pop(0)
        for dy,dx in dir:
            ny=now_y+dy
            nx=now_x+dx
            if 0<=ny<N and 0<=nx<M and arr[ny][nx]==1:
                arr[ny][nx]+=arr[now_y][now_x]
                q.append([ny,nx])

N,M=map(int,input().split())
arr=[list(map(int,input())) for _ in range(N)]
visited=[[0]*M for _ in range(N)]
bfs(0,0,N-1,M-1,visited)

print(arr[N-1][M-1])