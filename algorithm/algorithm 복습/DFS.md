# DFS

- 탐색 시작 노드를 스택에 삽입하고 방문처리
- 스택의 최상단 노드에 방문하지 않은 인접한 노드가 하나라도 있으면 그 노드를 스택에 넣고 방문처리
- 방문하지 않은 인접노드가 없으면 스택에서 최상단 노드를 꺼내기
- 더이상 앞의 과정을 수행할 수 없을 때까지 반복

```python
# 인접노드를 표현
graph=[
[],
[2,3,8],
[1,7],
[1,4,5],
[3,5],
[3,4],
[7],
[2,6,8],
[1,7],
]

# 각 노드가 방문된 정보를 표현(1차원 리스트)
visited=[]*len(graph)

# 함수호출(인접노드, 시작점, 방문표시)
#dfs(graph,1,visited)

# dfe함수
def dfs(graph, v, visited):
	# 현재 노드 방문처리
	visited[v]=1
	print(v, end=" ")
	# 현재 노드와 연결된 다른 노드를 재귀적으로 방문
	for i in graph[v]: # v노드의 인접노드들 반복문 돌려주기
		if visited[i]==0: # 방문하지 않았다면
			dfs(graph, i, visited) # 다시 돌려주기
>> 1 2 7 6 8 3 4 5
```



> DFS는 한경로로 쭉쭉쭉 들어가고 못가면 돌아와서 가지않았던 인접한길로 다시또 쭉쭉쭉 들어간다.
>
> 그래서 깊이경로탐색? 이라고 부르는가보다.



#### BOJ) 1260. DFS와 BFS

```python
'''
example)
4 5 1
1 2
1 3
1 4
2 4
3 4
answer)
1 2 4 3
1 2 3 4

example)
5 5 3
5 4
5 2
1 2
3 4
3 1
answer)
3 1 2 5 4
3 1 4 2 5
'''
def dfs(graph,visited,V):

    visited[V]=True
    dfs_list.append(V)
    graph[V].sort()
    for i in graph[V]:
        if not visited[i]:
            dfs(graph,visited,i)

def bfs(graph,visited,V):
    q=[]
    q.append(V)
    while q:
        node=q.pop(0)
        bfs_list.append(node)
        visited2[node]=True
        graph[node].sort()
        for i in graph[node]:
            if not visited2[i]:
                visited2[i]=True
                q.append(i)


N,M,V=map(int,input().split())
graph=[[] for _ in range(N+1)]
visited1=[False]*(N+1)
visited2=[False]*(N+1)
for i in range(M):
    s,e=map(int,input().split())
    graph[s].append(e)
    graph[e].append(s)
dfs_list=[]
bfs_list=[]
dfs(graph,visited1,V)
bfs(graph,visited2,V)

print(*dfs_list)
print(*bfs_list)
```

