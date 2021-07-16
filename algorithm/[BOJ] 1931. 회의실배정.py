'''
11
1 4
3 5
0 6
5 7
3 8
5 9
6 10
8 11
8 12
2 13
12 14
'''
N=int(input())
works=[]
ans=0
for i in range(N):
    work=list(map(int,input().split()))
    works.append(work)
works.sort(key=lambda x:x[1])
finish=0
for i in range(N):
    start,end=works[i]
    if start>=finish:
        ans+=1
        finish=end
print(ans)