'''
3
3
0 27 44
-5 0 62
0 99 0
5
0 0 1 0 0
88 0 39 0 75
71 56 0 43 0
23 0 -21 0 92
22 -1 48 0 0
10
0 94 98 0 23 0 31 0 85 0
10 0 78 19 83 0 91 0 82 -7
70 0 0 24 0 66 0 0 46 0
0 40 90 0 82 77 0 0 0 0
72 0 61 16 0 99 0 58 -9 44
82 84 61 76 29 0 30 28 20 72
39 78 76 0 0 11 0 54 58 39
0 0 25 40 10 0 57 0 19 38
68 5 81 78 87 54 60 -7 0 0
67 56 83 74 0 36 0 55 0 0
'''
# 플로이드와샬
for tc in range(1,int(input())+1):
    n=int(input())
    arr=[list(map(int,input().split())) for _ in range(n)]
    ans=0

    for i in range(n):
        for j in range(n):
            if arr[i][j]==0:
                arr[i][j]=float('inf')


    for k in range(n):
        for i in range(n):
            for j in range(n):
                arr[i][j]=min(arr[i][j], arr[i][k]+arr[k][j])

    ans=0
    for i in range(n):
        for j in range(n):
            if not i==j and arr[i][j]>ans:
                ans=arr[i][j]
    print("#{} {}".format(tc, ans))