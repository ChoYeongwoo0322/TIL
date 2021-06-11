#### heapq 최대힙구하기

```
import sys, heapq
sys.stdin=open("17_힙.txt")

for tc in range(1, int(input())+1):
    n = int(input())
    heap=[]
    result = []
    for i in range(n):
        temp = list(map(int, input().split()))

        if temp[0]==1:
            heapq.heappush(heap, (-(int(temp[1])),temp[1]))
    #     elif len(heap):
    #         result.append(-heapq.heappop(heap))
    #     else:
    #         result.append(-1)
    #
    # print("#{}".format(tc), end=" ")
    # print(*result)

    print(heap[0])

    for x,y in heap:
        result.append(y)
    print(result)

```

