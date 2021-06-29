N=int(input())
ans=0
while True:
    if not N%5: # 5로 딱 떨어지면 끝
        ans+=N//5
        break
    # 끝이 아니면 3빼주고 다시 돌려보기
    N-=3
    ans+=1
    # 근데 3뺏는데 -되면 그건 못구하는거
    if N<0:
        ans=-1
        break
print(ans)