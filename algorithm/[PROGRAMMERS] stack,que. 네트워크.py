from collections import deque
def solution(n, computers):
    answer = 0
    visited=[0]*n
    for i in range(n):# 출발점
        if not visited[i]:
            q=deque()
            q.append(i)
            while q:
                a=q.popleft()
                visited[a]=1
                for b in range(n):
                    if a!=b and computers[a][b]==1 and not visited[b]:
                        q.append(b)
            answer+=1

    return answer


solution(3,[[1, 1, 0], [1, 1, 0], [0, 0, 1]])