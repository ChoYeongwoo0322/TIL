# def solution(phone_book):
#     answer = True
#     N=len(phone_book)
#     while True:
#         for i in range(N-1):
#             for j in range(i+1,N):
#                 a=list(phone_book[i])
#                 b=list(phone_book[j])
#                 c=a+b
#                 d=set(c)
#                 if max(len(a),len(b))==len(d):
#                     answer = False
#                     break
#         break
#
#     return answer
phone_book=["123","456","789"]
answer = True
N = len(phone_book)
for i in range(N-1):
    for j in range(i + 1, N):
        if len(phone_book[i]) <= len(phone_book[j]):
            cnt=0
            for l in range(len(phone_book[i])):
                if phone_book[i][l]!=phone_book[j][l]:
                    continue
                else:
                    cnt+=1
            if cnt==len(phone_book[i]):
                answer=False
                break
        if len(phone_book[j]) <= len(phone_book[i]):
            cnt=0
            for l in range(len(phone_book[j])):
                if phone_book[j][l]!=phone_book[i][l]:
                    continue
                else:
                    cnt+=1
            if cnt==len(phone_book[j]):
                answer=False
                break

print(answer)