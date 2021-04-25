#### 인수의 생일잔치

```python
from collections import deque
 
def kruskal(X,adj): # 출발하는점과 접점행렬
    D=[987654321]*(N+1) # 최소값을 찾을거니까 비교해줄 큰값으로 D만들어주기
    # bfs 돌려주기위한
    q=deque() # q생성해서 popleft로 시간단축
    s=X # 스타트!
    D[s]=0 # 스타트는 거리가 0이어야지?
    q.append(s) # q에다가 스타트점을 담아서
    while q: # q가 빌때까지 돌려준다.
        s=q.popleft() # 뽑아서
        for v in range(N+1): # 접점이 뭐가있는지 돌려주기
            if adj[s][v]!=0 and D[v] > D[s]+adj[s][v]: # 접점이 0이 아니고, 거리가 더 작으면?
                D[v]=D[s]+adj[s][v] # 교환
                q.append(v) #그리고 q에 넣어주기
                # bfs로 계속 돌려주기
    return D # 그러고 D리스트를 반환한다.
 
for tc in range(1, int(input())+1):
    N,M,X=map(int, input().split()) # 값 받아주고
    parent=[i for i in range(N+1)] # 부모찾기안해도됨
    adj1=[[0]*(N+1) for _ in range(N+1)] # 접점과 거리 표시해주기 위한 리스트 생성
    adj2=[[0]*(N+1) for _ in range(N+1)] # 두개를 만들어주는 이유는, 뻗어나가고 받는것 2가지 형태를 만들어주기 위해서
    for i in range(M):
        x,y,c=map(int, input().split())
        adj1[x][y]=c # x에서 y로 가는 길 c(집으로돌아가는건가..) 
        adj2[y][x]=c # y에서 x로 돌아가는 길 c
        # 둘중 하나는 X에서 각자집으로 가는거고, 하나는 X로 가는거고....
 
    ans1=kruskal(X,adj1) # 뻗어나가는애들, 받는애들 두개를 만들어주는형태
    ans2=kruskal(X,adj2)
    # 리스트로 반환을 받았을거임
 
    ans=0
    for i in range(1,N+1): # i로 돌려주면서 합중에서 제일 큰것을 찾아주는 작업
        ans=max(ans,ans1[i]+ans2[i])
 
    print("#{} {}".format(tc, ans))

```

