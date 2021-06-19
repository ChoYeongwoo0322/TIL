'''
3
10 7
10 53
20 50
'''
# 시간초과

from itertools import combinations
for tc in range(1,int(input())+1):
    N,K =map(int,input().split())
    arr = [i for i in range(1,N+1)]
    ans=0
    for i in range(1,N+1):
        for j in combinations(arr,i):
            if sum(j)==K:
                ans+=1

    print("#{} {}".format(tc,ans))