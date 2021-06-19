'''
3
5
8
10
'''
def square(N):
    memo[0]=1
    memo[1]=1
    memo[2]=3
    for i in range(3,N+1):
        memo[i]=memo[i-1]+memo[i-2]*2+memo[i-3]
    return memo[N]

for tc in range(1,int(input())+1):
    N=int(input())
    memo=[-1]*31
    print("#{} {}".format(tc,square(N)))