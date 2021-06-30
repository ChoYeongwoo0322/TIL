'''
3
6
7 2 5 3 4 6
6
3 1 4 16 23 12
8
18 57 11 52 14 45 63 40
'''

import heapq

for tc in range(1,int(input())+1):
    N=int(input())
    nums=list(map(int,input().split()))
    h=[]
    for i in range(N):
        heapq.heappush(h,nums[i])

    ans=0
    while N//2>0:
        N//=2
        ans+=h[N-1]

    print("#{} {}".format(tc, ans))
