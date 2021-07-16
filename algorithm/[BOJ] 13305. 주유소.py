'''
4
2 3 1
5 2 4 1
'''
N=int(input())
dist=list(map(int,input().split()))
oil=list(map(int,input().split()))
standard=987654321
ans=0
for i in range(N-1):
    if oil[i]<standard:
        standard=oil[i]
    ans+=dist[i]*standard
print(ans)