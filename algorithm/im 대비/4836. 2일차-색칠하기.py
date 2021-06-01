'''
3
2
2 2 4 4 1
3 3 6 6 2
3
1 2 3 3 1
3 6 6 8 1
2 3 5 6 2
3
1 4 8 5 1
1 8 3 9 1
3 2 5 8 2
'''

for tc in range(1,int(input())+1):
    arr=[[0]*10 for _ in range(10)]
    for _ in range(int(input())):
       r1,c1,r2,c2,color=map(int,input().split())
       for i in range(r1,r2+1):
           for j in range(c1,c2+1):
               arr[i][j]+=color

    cnt=0
    for i in range(10):
        for j in range(10):
            if arr[i][j]>=3:
                cnt+=1
    print("#{} {}".format(tc, cnt))