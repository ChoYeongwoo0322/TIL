'''
2
8
3 2 7 8 1 4 5 6
10
2 1 3 4 5 6 7 9 10 8
'''
def search(n):
    global cnt,visited
    visited[n]=1
    num_stack=list()
    num_stack.append(n)

    while num_stack:
        now=num_stack.pop()

        if visited[change[now]]==0:
            init[change[now]] = 0
            visited[change[now]]=1
            num_stack.append(change[now])
    cnt+=1

for i in range(1,int(input())+1):
    N=int(input())
    arr=[]
    init=[0]+[i for i in range(1,N+1)]
    change=[0]+list(map(int,input().split()))
    visited=[0]*(N+1)
    cnt=0

    for i in range(1,N+1):
        if init[i] !=0:
            search(init[i])

    print(cnt)