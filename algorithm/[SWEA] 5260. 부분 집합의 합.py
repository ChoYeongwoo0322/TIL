'''
3
10 7
10 53
100 5050
'''
# 시간초과

def search(capacity,number):
    global ans

    if M==0:
        ans+=1
    elif M<0:
        return
    elif M>0:
        return
    else:
        search(M-value[N-1],N-1)
        search(M,N-1)


for tc in range(1,int(input())+1):
    N,M=map(int,input().split())
    value=[i for i in range(1,N+1)]
    ans=0

    print("#{} {}".format(tc, search(M,N)))


# def part_sum(k, cnt):
#     global result
#     a = sum(visit[k:N+1])+cnt
#     if cnt > M:
#         return
#     if a < M:
#         return
#     if a == M:
#         result += 1
#         return
#     if k == N+1:
#         return
#     part_sum(k+1, cnt+k)
#     part_sum(k+1, cnt)
#
#
# T = int(input())
# for tc in range(1, T+1):
#     N, M = map(int, input().split())
#     visit = [i for i in range(101)]
#     result = 0
#     part_sum(1, 0)
#     print('#{} {}'.format(tc, result))