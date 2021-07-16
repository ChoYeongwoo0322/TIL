'''
5
3 1 4 3 2
'''
N=int(input())

lst=list(map(int,input().split()))
lst.sort()
ans=0

for i in range(N):
    ans+=lst[i]*(N-i)
print(ans)