'''
3
5 3 2
4 1
5 2
3 3
10 5 2
8 42
9 468
10 335
6 501
7 170
17 9 4
16 479
17 359
9 963
10 465
11 706
12 146
13 282
14 828
15 962
'''
for tc in range(1,int(input())+1):
    N,M,L=map(int,input().split())
    tree=[0]*(N+1)
    for i in range(M):
        node,value=map(int,input().split())
        tree[node]=value

    while N>=2*L:
        tree[N//2]+=tree[N]
        N-=1
    print("#{} {}".format(tc, tree[L]))