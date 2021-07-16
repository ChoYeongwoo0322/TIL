from heapq import heappush, heappop

def solution(jobs):
    jobs.sort(key=lambda x: x[0])
    nums = len(jobs)
    workingTime = 0
    heap = []
    time = 0

    while jobs:
        while jobs and jobs[0][0] <= time:
            start, duration = jobs.pop(0)
            heappush(heap, (duration, start))
        if not heap:
            start, duration = jobs.pop(0)
            heappush(heap, (duration, start))
            time = start
        duration, start = heappop(heap)
        time += duration
        workingTime += time - start

    while heap:
        duration, start = heappop(heap)
        time += duration
        workingTime += time - start

    return workingTime//nums
solution([[0, 9], [0, 4], [0, 5], [0, 7], [0, 3]])