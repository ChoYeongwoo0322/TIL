'''
10 4200
1
5
10
50
100
500
1000
5000
10000
50000
'''
N,K=map(int,input().split())
coins=[]
for i in range(N):
    coins.append(int(input()))
ans=0
idx=N-1

while K!=0:
    coin = coins[idx]
    if K//coin > 0:
        ans+=K//coin
        K-=((K//coin)*coin)
    idx-=1

print(ans)




