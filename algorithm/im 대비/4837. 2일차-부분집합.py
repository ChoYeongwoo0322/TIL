'''
3
3 6
5 15
5 10
'''
from itertools import permutations,combinations

for tc in range(1, int(input())+1):
    N,K=map(int,input().split())
    A=[i for i in range(1,13)]

    cnt=0
    for i in combinations(A,N):
        if sum(i)==K:
            cnt+=1
    print("#{} {}".format(tc,cnt))