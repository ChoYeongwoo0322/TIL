from bisect import bisect_left, bisect_right
import heapq
def solution(scoville, K):
    # answer = 0
    # scoville.sort()
    # temp_sco=scoville.copy()
    #
    # for i in range(len(temp_sco)-1):
    #     a = temp_sco.pop(0)
    #     b = temp_sco.pop(0)
    #     ab = a + b * 2
    #     idx = bisect_left(temp_sco, ab)
    #     temp_sco.insert(idx, ab)
    # if temp_sco[0]<K:
    #     answer=-1
    #     return answer
    #
    #
    # while True:
    #     if scoville[0]>=K:
    #         break
    #     else:
    #         a=scoville.pop(0)
    #         b=scoville.pop(0)
    #         ab=a+b*2
    #         idx=bisect_left(scoville,ab)
    #         scoville.insert(idx,ab)
    #         answer+=1
    answer = 0
    h=[]
    for i in range(len(scoville)):
        heapq.heappush(h,scoville[i])
    while len(h)>=2 and h[0]<K:
        a=heapq.heappop(h)
        b=heapq.heappop(h)
        temp=a+2*b
        heapq.heappush(h,temp)
        answer+=1

    if sum(h)<K:
        answer=-1
    return answer


solution([1,2,3,9,10,12],7)