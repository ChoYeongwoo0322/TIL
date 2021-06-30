'''
3
6
8
15
'''
def search(n):
    global i
    if n<=N:
        search(2*n)
        tree[n]=i+1
        i+=1
        search(2*n+1)

for tc in range(1,int(input())+1):
    N=int(input())
    tree=[0]*(N+1)
    i=0
    search(1)

    print("#{} {} {}".format(tc, tree[1], tree[N//2]))