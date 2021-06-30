'''
3
5 1
2 1 2 5 1 6 5 3 6 4
5 1
2 6 6 4 6 5 4 1 5 3
10 5
7 6 7 4 6 9 4 11 9 5 11 8 5 3 5 2 8 1 8 10
'''
# 전위순회
def tree(N):
    global cnt
    if N==0:
        return
    cnt+=1
    tree(ln[N])
    tree(lr[N])

for tc in range(1,int(input())+1):
    E,N=map(int,input().split())
    nodes=list(map(int,input().split()))
    ln=[0 for i in range(E+2)]
    lr=[0 for i in range(E+2)]

    for i in range(0,2*E,2):

        if not ln[nodes[i]]:
            ln[nodes[i]]=nodes[i+1]
        else:
            lr[nodes[i]]=nodes[i+1]

    cnt=0
    tree(N)

    print("#{} {}".format(tc, cnt))