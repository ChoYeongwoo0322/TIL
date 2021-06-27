'''
3 3
DDD
DDD
DDD
'''

def maze(y,x):
    global cnt,check
    stack=list()
    stack.append((y,x))
    sub_cnt=0
    visited = [[0]*M for _ in range(N)]
    failed = [[0]*M for _ in range(N)]
    flag=0 # 탈출 여부
    while stack:
        cy,cx=stack.pop()

        if check[cy][cx]==1:
            cnt+=1
            break
        if check[cy][cx]==2:
            return
        visited[cy][cx] = 1
        failed[cy][cx] = 1

        if arr[cy][cx]=='U':
            if 0<=cy-1 and not visited[cy-1][cx]:
                sub_cnt+=1
                stack.append((cy-1,cx))
            elif 0>cy-1:
                flag=1
                break

        elif arr[cy][cx]=='R':
            if cx+1<M and not visited[cy][cx+1]:
                sub_cnt+=1
                stack.append((cy,cx+1))
            elif cx+1>=M:
                flag=1
                break

        elif arr[cy][cx]=='D':
            if cy+1<N and not visited[cy+1][cx]:
                sub_cnt+=1
                stack.append((cy+1,cx))
            elif cy+1>=N:
                flag=1
                break

        elif arr[cy][cx]=='L':
            if 0<=cx-1 and not visited[cy][cx-1]:
                sub_cnt+=1
                stack.append((cy-1,cx))
            elif cy-1<0:
                flag=1
                break
    if flag==1:
        cnt+=(sub_cnt+1)
        for i in range(N):
            for j in range(M):
                if visited[i][j]==1 and check[i][j]==0:
                    check[i][j]=1
    if flag==0:
        for i in range(N):
            for j in range(M):
                if failed[i][j]==1 and check[i][j]==0:
                    check[i][j]=2



N,M=map(int,input().split())
arr=[list(input()) for _ in range(N)]
cnt=0
visited=[[0]*M for _ in range(N)]
check=[[0]*M for _ in range(N)]
for i in range(N):
    for j in range(M):
        # if check[i][j]==2:
        #     continue
        # if check[i][j]==1: # 성공한 길들
        #     continue
        if check[i][j]==0: # 아직 지나가보지 않은 길들
            maze(i,j)
        # check[i][j]==2 실패한 길들

print(cnt)