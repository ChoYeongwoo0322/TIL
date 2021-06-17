'''
3
5 2 3 1 1
10 2 1 3 2 2 5 4 2 1
10 1 1 2 1 2 2 1 2 1
'''

def bus(n):
    global cnt, sub_cnt
    if n>=N:
        if sub_cnt<cnt:
            cnt=sub_cnt
        return
    if sub_cnt>cnt: return

    start=n
    gas=arr[start]
    for i in range(start+gas,start,-1):
        sub_cnt+=1
        bus(i)
        sub_cnt-=1

for tc in range(1,int(input())+1):
    arr=list(map(int,input().split()))
    N=arr[0]
    cnt=float('inf')
    sub_cnt=0
    bus(1) # 시작
    print("#{} {}".format(tc,cnt))