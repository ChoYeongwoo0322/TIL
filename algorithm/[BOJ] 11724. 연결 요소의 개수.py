'''
6 5
1 2
2 5
5 1
3 4
4 6
'''
def bfs(i):
    global cnt,node,visited
    cnt+=1
    q=list()
    q.append(i)
    visited[i]=1

    while q:
        now=q.pop(0)
        for next in range(1,N+1):
            if node[now][next]==1 and visited[next]==0:
                visited[next]=1
                q.append(next)

N,M=map(int,input().split())
node=[[0]*(N+1) for _ in range(N+1)]
cnt=0
visited=[0]*(N+1)

for i in range(M):
    s,e=map(int,input().split())
    node[s][e]=node[e][s]=1

for i in range(1,N+1):
    if visited[i]==0:
        bfs(i)

print(cnt)