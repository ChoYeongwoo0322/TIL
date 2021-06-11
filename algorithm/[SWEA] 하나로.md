#### 하나로

```python
def search(): # 이것이 프림인것같은데 맞는지 모르겠음...
    global D, visited, p
    total=0 # 합구하는거니까 total=0
    u=0 # 시작점
    D[u]=0 # 시작은 거리가 0
 
    for i in range(N):
        # 가중치가 최소인 정점 찾기
        min=float('inf')
        for v in range(N): # 연결된것 돌려주기
            if visited[v]==0 and min>D[v]: # 방문안했고 min값보다 작다면?
                min=D[v] # min값에 넣어주고
                u=v # 그 값을 u로 설정
        visited[u]=1 # u는 방문
        total+=island[p[u]][u] # total에 min값 넣어주기
        
 		### 업데이트!!!!!!!!!!
        for v in range(N): # 업데이트해주기
            if island[u][v] !=0 and visited[v]==0 and island[u][v] < D[v]: 
            # 거리가 0보다크고, 방문안했고
                D[v]=island[u][v] # v거리에다 업데이트해주기
                p[v]=u # 부모노드업데이트?
    return total
 
for tc in range(1, int(input())+1):
    N=int(input())
    X=list(map(int, input().split())) # X좌표받아주기
    Y=list(map(int, input().split())) # Y좌표받아주기
    E=float(input()) # E받기
    island = [[0] * N for _ in range(N)] # 행열만들어서 거리 넣어주기
 
    for i in range(N):
        for j in range(i + 1, N):
            island[i][j] = island[j][i] = ((X[i] - X[j])**2 + (Y[i] - Y[j])**2) * E
 
    D=[float('inf')]*N # 최소값찾으려고 N개 만들어주기
    visited=[0]*N # visited체크
    p=list(range(N)) # 부모찾아주기? 일단 만들어줌
 
    print("#{} {}".format(tc, round(search())))
About
```

