def solution(participant, completion):
    answer = ''
    for i in participant:
        if i in completion:
            completion.remove(i)
        else:
            answer=i
    return answer