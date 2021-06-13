'''
1 1
0
2 2
0 1
1 0
3 2
1 1 1
1 1 1
5 4
1 0 1 0 0
1 0 0 0 0
1 0 1 0 1
1 0 0 1 0
5 4
1 1 1 0 1
1 0 1 0 1
1 0 1 0 1
1 0 1 1 1
5 5
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0 0 0 0
1 0 1 0 1
0 0
'''
dir=[[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]
def island(x,y):
    global cnt, arr,visited
    cnt+=1
    q=list()
    q.append((x,y))
    arr[x][y]=0
    while q:
        sy,sx=q.pop(0)

        for dy,dx in dir:
            ny=sy+dy
            nx=sx+dx
            if 0<=ny<h and 0<=nx<w and visited[ny][nx]==0 and arr[ny][nx]==1:
                visited[ny][nx]=1
                arr[ny][nx]=0
                q.append((ny,nx))
for _ in range(100):
    w,h=map(int,input().split())
    if w==0 and h==0:
        exit()
    arr=[list(map(int,input().split())) for _ in range(h)]

    visited=[[0]*w for _ in range(h)]
    cnt=0
    for i in range(h):
        for j in range(w):
            if arr[i][j]==1:
                island(i,j)
    print(cnt)