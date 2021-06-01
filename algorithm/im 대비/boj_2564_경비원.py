'''
10 5
3
1 4
3 2
2 8
2 3
'''
w,h=map(int,input().split())
N=int(input())
arr=[list(map(int,input().split())) for _ in range(N)]
dong_dir,dong_spot=map(int,input().split())
distance=0
for i in arr:
    # 나랑 같은 방향일때
    if i[0]==dong_dir:
        distance+=abs(dong_spot-i[1])
    # 나의 반대방향일 때
    if (i[0]==1 and dong_dir==2) or (i[0]==2 and dong_dir==1):
        distance+=min(h+dong_spot+i[1],h+(w-dong_spot)+(w-i[1]))
    if (i[0]==3 and dong_dir==4) or (i[0]==4 and dong_dir==3):
        distance+=min(w+dong_spot+i[1],w+(h-dong_spot)+(h-i[1]))
    # 나의 옆방향일 때
    if (dong_dir==1 and i[0]==3):
        distance+=dong_spot+i[1]
    if (dong_dir==1 and i[0]==4):
        distance+=(w-dong_spot)+i[1]
    if (dong_dir==2 and i[0]==3):
        distance+=dong_spot+(h-i[1])
    if (dong_dir==2 and i[0]==4):
        distance+=(w-dong_spot)+(h-i[1])
    if (dong_dir==3 and i[0]==1):
        distance+=dong_spot+i[1]
    if (dong_dir==3 and i[0]==2):
        distance+=(w-dong_spot)+i[1]
    if (dong_dir==4 and i[0]==1):
        distance+=dong_spot+(w-i[1])
    if (dong_dir==4 and i[0]==2):
        distance+=(h-dong_spot)+(w-i[1])

print(distance)