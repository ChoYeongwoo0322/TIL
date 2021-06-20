'''
2
10 4
6 12
5 10
5 15
4 6
12 5
7 20
3 10
5 3
3 8
6 15
'''
# knapsack
def search(N,M):
    global maxV

    if N==0 or M==0:
        return 0
    if size[M-1]>N:
        return search(N,M-1)
    else:
        return max(value[M-1]+search(N-size[M-1],M-1),search(N,M-1))

for tc in range(1,int(input())+1):
    N,M=map(int,input().split())
    size=[]
    value=[]
    maxV=0
    for _ in range(M):
        s,v=map(int,input().split())
        size.append(s)
        value.append(v)

    search(N,M)
    print("#{} {}".format(tc, search(N,M)))