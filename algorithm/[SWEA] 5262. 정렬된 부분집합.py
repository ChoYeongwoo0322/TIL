'''
3
5 1 5 3 4 2
5 4 3 5 1 2
10 2 9 5 1 10 6 3 4 8 7
'''
# LIS
for tc in range(1,int(input())+1):
    arr=list(map(int,input().split()))
    n=arr[0]
    a = arr[1:]
    DP = [1] * (n)

    for i in range(n):
        for j in range(i):
            if a[i] > a[j]:
                DP[i] = max(DP[j]+1, DP[i])
    print("#{} {}".format(tc, max(DP)))