'''
5 5
WBWWW
WWWWW
BBBBB
BBBWW
WWWWW
'''
dir=[[-1,0],[1,0],[0,-1],[0,1]]
def bfs(y,x,color):
    global white_power,black_power
    cnt=0
    s=list()
    s.append([y,x])

    while s:
        noy,nox=s.pop(0)
        for dy,dx in dir:
            ny=noy+dy
            nx=nox+dx
            if 0<=ny<M and 0<=nx<N and arr[ny][nx]==color:
                cnt+=1
                s.append([ny,nx])
                arr[ny][nx]='N'

    if color=='W':
        if cnt!=0: white_power+=cnt*cnt
        else: white_power+=1
    else:
        if cnt!=0: black_power+=cnt*cnt
        else: black_power+=1

N,M=map(int,input().split())
arr=[list(input()) for _ in range(M)]

# White
white_power=0
for i in range(M):
    for j in range(N):
        if arr[i][j]=='W':
            bfs(i,j,'W')

# Black
black_power=0
for i in range(M):
    for j in range(N):
        if arr[i][j]=='B':
            bfs(i,j,'B')

print(white_power,black_power)