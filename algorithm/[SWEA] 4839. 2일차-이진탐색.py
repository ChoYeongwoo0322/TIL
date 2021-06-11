'''
3
400 300 350
1000 299 578
1000 222 888
'''

for tc in range(1,int(input())+1):
    P,A,B=map(int,input().split())

    cnt_A=0
    cnt_B=0
    l_A,r_A=1,P
    l_B,r_B=1,P
    result=""
    # A
    while True:
        m=(l_A+r_A)//2
        cnt_A+=1
        if m==A:
            break
        elif m > A: r_A=m
        elif m < A: l_A=m
    # B
    while True:
        m=(l_B+r_B)//2
        cnt_B+=1
        if m==B:
            break
        elif m > B: r_B=m
        elif m < B: l_B=m

    if cnt_A<cnt_B: result="A"
    if cnt_A>cnt_B: result="B"
    if cnt_A==cnt_B: result="0"

    print("#{} {}".format(tc, result))
