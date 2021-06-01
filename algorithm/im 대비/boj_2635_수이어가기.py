'''
100
'''
first=int(input())
lst=[first]

for i in range(1,first+1):
    sub_lst = [first]
    sub_lst.append(i)
    while True:
        temp=sub_lst[-2]-sub_lst[-1]
        if temp <0:
            if len(sub_lst) >= len(lst):
                lst=sub_lst
            break

        else:
            sub_lst.append(temp)
print(len(lst))
print(*lst)