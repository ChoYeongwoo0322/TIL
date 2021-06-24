'''
3
3 2
1 5 3
8 3
5 10
2 12 13 11 18
17 4 7 20 3 9 7 9 20 5
10 12
10 13 14 6 19 11 5 20 11 14
5 18 17 8 9 17 18 4 1 16 15 13
'''

def search():
    total=0
    now = N-1
    for i in range(M-1,-1,-1):
        while now>=0:
            if T[i]>=W[now]:
                total+=W[now]
                now-=1
                break
            now-=1
    return total

for tc in range(1,int(input())+1):
    N,M=map(int,input().split())
    W=list(map(int,input().split()))
    T=list(map(int,input().split()))
    W.sort()
    T.sort()

    print("#{} {}".format(tc, search()))

