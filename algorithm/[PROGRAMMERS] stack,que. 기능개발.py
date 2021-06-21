from collections import deque
def solution(progresses, speeds):
    n=len(progresses)
    answer = []

    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]

        cnt=0
        while progresses and progresses[0]>=100:
            progresses.pop(0)
            speeds.pop(0)
            cnt+=1

        if cnt>0: answer.append(cnt)

    return answer


print(solution([93, 30, 55],[1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99],[1, 1, 1, 1, 1, 1]	))

