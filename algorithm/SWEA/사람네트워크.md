#### 사람네트워크

```python
for tc in range(1, int(input())+1):
    arr=list(map(int,input().split())) # 리스트 받아주고
    N=arr[0] # 사람의 숫자는 N
    adj=[] # 사람숫자빼고 이제 나머지들을 담아둘 리스트
    for i in range(1,len(arr),N): # N번씩뛰면서, 1부터시작!(0은 이미 N으로 빠짐), 길이만큼해서
        adj.append(arr[i:i+N]) # 슬라이싱으로 N명씩 빼서 넣어준다
        # 만들고나면 N열의 N행의 2차행열이 만들어짐
 
    for i in range(N): # 리스트의 인접하지 않은 부분들은 무수히큰수로 만들어주기위함?
        for j in range(N):
            if adj[i][j]==0: # 0이면
                adj[i][j]=987654321 # 존나크게
            if i==j: # 근데 만약같은아이들은 거리가 0이니까
                adj[i][j]=0 # 0으로 다시 설정해주기
 #플로이드마샬
    for k in range(N): # k
        for i in range(N): # 접점가져오기
            for j in range(N):
                adj[i][j]=min(adj[i][j], adj[i][k]+adj[k][j]) # 접점에다가 그 접점이랑 뒤에 요상한아이랑 비교해서 작은거 넣어줌
    ans = 987654321 # 작은값찾기니까 큰값넣어두고
    for i in range(N): # N만큼 돌려주면서
        if ans > sum(adj[i]): # 그 행값 합이랑 비교해서
            ans=sum(adj[i]) # 더 작으면 넣어주기
    print("#{} {}".format(tc, ans))
     
    # 플로이드마샬?????
```

