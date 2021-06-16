'''
7
6
1 2
2 3
1 5
5 2
5 6
4 7
'''

def dfs(n):
    global cnt
    visited[n]=1
    q=list()
    q.append(n)
    while q:
        v=q.pop(0)
        for i in computer[v]:
            if visited[i]==0:
                visited[i]=1
                cnt+=1
                q.append(i)

c=int(input())
computer=[[] for _ in range(c+1)]
visited=[0]*(c+1)
network=int(input())
for _ in range(network):
    c1,c2=map(int,input().split())
    computer[c1].append(c2)
    computer[c2].append(c1)

cnt=0
dfs(1)

print(cnt)