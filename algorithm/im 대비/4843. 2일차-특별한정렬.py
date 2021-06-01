'''
3
10
1 2 3 4 5 6 7 8 9 10
10
67 39 16 49 60 28 8 85 89 11
20
3 69 21 46 43 60 62 97 64 30 17 88 18 98 71 75 59 36 9 26
'''
for tc in range(1, int(input())+1):
    N=int(input())
    nums=list(map(int,input().split()))
    nums.sort()
    result=[]
    for i in range(N-1,N//2-1,-1):
        result.append(nums[i])
        result.append(nums[-i-1])
    print("#{}".format(tc), end=" ")
    print(*result[:10])