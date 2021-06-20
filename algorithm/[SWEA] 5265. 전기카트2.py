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

#Prepare the square symmetric distance matrix for 3 nodes:
#  Distance from A to B is 1.0
#                B to C is 3.0
#                A to C is 2.0
D = [[],
     [1.0],
     [2.0, 3.0]]

path = solve_tsp(D)

#will print [1,0,2], path with total length of 3.0 units
print(path)

# for tc in range(1,int(input())+1):
#     n=int(input())
#     arr=[list(map(int,input().split())) for _ in range(n)]
#     ans=float('inf')
#
#     for i in range(n):





