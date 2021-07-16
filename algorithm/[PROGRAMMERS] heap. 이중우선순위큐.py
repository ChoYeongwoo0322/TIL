'''
["I 16","D 1"]
["I 7","I 5","I -5","D -1"]
'''
import heapq
def solution(operations):
    answer = []
    h=[]
    for i in range(len(operations)):
        command,number=operations[i].split()
        if command=='I':
            h.append(int(number))
        else:
            if len(h)>1:
                if number=='1':
                    h.remove(int(max(h)))
                elif number=='-1':
                    h.remove(int(min(h)))
            else:
                h=[]
    if not h:
        answer=[0,0]
    else:
        answer=[int(max(h)),int(min(h))]

    return answer

solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"])