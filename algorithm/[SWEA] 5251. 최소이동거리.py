'''
3
2 3
0 1 1
0 2 6
1 2 1
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
def search():
    total=0
    start=0
    end=N
    D=[987654321]*(N+1)
    D[start]=0
    visited=[0]*(N+1)
    P=list(range(N+1))
    for i in range(N+1):
        minV=987654321
        for v in range(N+1):
            if visited[v]==0 and minV > D[v]:
                minV=D[v]
                start=v
        visited[start]=1
        total+=arr[P[start]][start]

        for v in range(N+1):
            if arr[start][v]!=0 and visited[v]==0 and arr[start][v] < D[v]:
                D[v]=arr[start][v]
                P[v]=start
    print(D)


for tc in range(1,int(input())+1):
    N,E=map(int,input().split())
    arr=[[0]*(N+1) for _ in range(N+1)]
    for _ in range(E):
        s,e,w=map(int,input().split())
        arr[s][e]=w



    print(search())