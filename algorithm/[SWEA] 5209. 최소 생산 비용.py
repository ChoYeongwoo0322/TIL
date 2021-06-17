'''
1
3
73 21 21
11 59 40
24 31 83
'''

def search(p):
    global cnt, sub_cnt
    if p==N:
        if sub_cnt<cnt:
            cnt=sub_cnt

    if sub_cnt>=cnt: return # 가지치기

    for i in range(N): # 회사
        if visited[i]==0:
            sub_cnt+=arr[p][i]
            visited[i]=1
            search(p+1)
            sub_cnt-=arr[p][i]
            visited[i]=0
    return

for tc in range(1,int(input())+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    visited=[0]*N
    cnt=float('inf')
    sub_cnt=0
    search(0)

    print("#{} {}".format(tc,cnt))