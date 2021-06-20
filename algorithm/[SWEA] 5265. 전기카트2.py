'''
3
3
0 18 34
48 0 55
18 7 0
4
0 83 65 97
82 0 78 6
19 19 0 82
6 34 94 0
5
0 9 26 85 42
14 0 84 31 27
58 88 0 16 46
83 61 94 0 17
40 71 24 38 0
'''
# TSP
from tsp_solver.greedy import solve_tsp

for tc in range(1,int(input())+1):
    n=int(input())
    arr=[list(map(int,input().split())) for _ in range(n)]
    ans=987654321

    for i in range(0,n):
        result = solve_tsp(arr, endpoints=(i, None))
        result.append(result[0])
        temp=0
        for j in range(n):
            temp+=arr[result[j]][result[j+1]]
        if temp<ans:
            ans=temp

    print("#{} {}".format(tc,ans))





