'''
3
2 3
0 1 1
0 2 1
1 2 6
4 7
0 1 9
0 2 3
0 3 7
1 4 2
2 3 8
2 4 1
3 4 8
4 6
0 1 10
0 2 7
1 4 2
2 3 10
2 4 3
3 4 10
'''
INF=float('inf')
T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())  # V(Vertex): 정점은 0번부터 V까지, E(Edge): 간선의 수
    G = [[0]*(V+1) for _ in range(V+1)]

    for _ in range(E):
        u, v, w = map(int, input().split())
        G[u][v]=G[v][u]=w

    MST = [0] * (V + 1) # 방문
    key = [INF] * (V + 1) # 값비교
    key[0] = 0
    ans = 0

    for _ in range(V + 1):  # 0 ~ V 까지 모든 정점을 돌아봅니다.
        u, min_key = 0, INF  # 값을 초기화 합니다.
        for i in range(V + 1): # 점 하나 골라서
            if not MST[i] and min_key > key[i]: # 방문안했고, 값이 더 작으면
                u, min_key = i, key[i] # 출발점을 i로 바꿔주고
        MST[u] = 1
        ans += key[u]

        for v, w in enumerate(G[u]):
            if not MST[v] and G[u][v] and key[v] > w:
                key[v] = w

    print('#{} {}'.format(tc, ans))