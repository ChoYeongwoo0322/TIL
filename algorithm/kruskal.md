#### kruskal

```python
def make_set(x):
    parent[x] = x

def find_set(x):
    if parent[x] == x:
        return x
    else:
        return find_set(parent[x])

def union(x, y):
    parent[find_set(y)] = find_set(x)

def kruskal():
    total = 0
    cnt = 0
    # make set
    for i in range(V):
        make_set(i)

    # 가중치별로 정렬
    edges.sort(key=lambda x: x[2])

    # findset 비교
    for i in range(E):
        if find_set(edges[i][0]) != find_set(edges[i][1]):
            total += edges[i][2]
            cnt += 1
            union(edges[i][0], edges[i][1])
        if cnt == V-1: break
    return total

V, E = map(int, input().split())
# 간선의 배열  : 시작 끝 가중치
edges = [list(map(int, input().split())) for _ in range(E)]
parent = [0] * V
print(kruskal())
```

