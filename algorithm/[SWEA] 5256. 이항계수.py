'''
3
2 1 1
3 2 1
5 3 2
'''

# def dp(i):
#     # global n_lst
#     if i<=2: return
#
#     now=3
#     while now<=i:
#         for j in range(1,now):
#             n_lst[now-1][j]=n_lst[now-2][j-1]+n_lst[now-2][j]
#         now+=1
#
# for tc in range(1,int(input())+1):
#     n,a,b=map(int,input().split())
#     n_lst=[[1]*(n+1) for _ in range(n)]
#     # 기본
#     n_lst[1][1]=2
#     dp(n)
#     print(n_lst)
#     print("#{} {}".format(tc, n_lst[n-1][b]))

def bi(n, a, b):
    if a == 0 or b == 0:
        return 1
    else:
        return bi(n-1, a, b-1) + bi(n-1, a-1, b)

T = int(input())
for tc in range(1, T+1):
    n, a, b = map(int, input().split())

    print('#{} {}'.format(tc, bi(n, a, b)))