import sys
sys.stdin=open("[SWEA] 5202. 화물 도크.txt")

for tc in range(1,int(input())+1):
    N=int(input())
    t=[0]*24
    w=[]
    ans=0
    for _ in range(N):
        w.append(list(map(int,input().split())))
    W=sorted(w, key=lambda x:x[1])
    for i in W:
        start,end=i
        cnt=0
        for j in range(start,end):
            if t[j]==0:
                cnt+=1
        if cnt==(end-start):
            ans+=1
            for k in range(start, end):
                t[k]=1
    print("#{} {}".format(tc, ans))