'''
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
'''
dir=[[-1,0],[1,0],[0,-1],[0,1]]
def search(y,x):
    global cnt, houses
    cnt+=1
    house=1
    visited[y][x]=1
    s=list()
    s.append((y,x))
    while s:
        nowy,nowx=s.pop()
        for dy,dx in dir:
            ny=nowy+dy
            nx=nowx+dx
            if 0<=ny<N and 0<=nx<N and arr[ny][nx]==1 and visited[ny][nx]==0:
                s.append((ny,nx))
                arr[ny][nx]=0
                visited[ny][nx]=1 #
                house+=1
    houses.append(house)

N=int(input())
arr=[list(map(int,input())) for _ in range(N)]
visited=[[0]*N for _ in range(N)] #
cnt=0
houses=[]
for y in range(N):
    for x in range(N):
        if arr[y][x]==1:
            search(y,x)
houses.sort()
print(cnt)
for i in houses:
    print(i)