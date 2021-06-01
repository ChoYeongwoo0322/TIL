'''
10 8
3
0 3
1 4
0 2
'''

def search(i,j):
    global ans
    global paper
    y=i
    x=j
    length_x=0
    length_y=0
    # 가로
    while x < n and paper[i][x]==1:
        length_x+=1
        x+=1
    while y < N and paper[y][j]==1:
        length_y+=1
        y+=1
    if length_x*length_y > ans:
        ans=length_x*length_y
    # 초기화해주기
    for a in range(i,y):
        for b in range(j,x):
            paper[a][b]=0
    return


a,b=map(int,input().split())
paper=[[1]*a for _ in range(b)]
h=[]
v=[]
for i in range(int(input())):
    dir,idx=map(int,input().split())
    if dir==0:
        h.append(idx)

    if dir==1:
        v.append(idx)

h.sort()
v.sort()
# 가로 추가
for i in range(len(h)):
    paper.insert(i+h[i],[0]*len(paper[0]))

# 세로 추가
for i in range(len(v)):
    for j in range(len(paper)):
        paper[j].insert(i+v[i],0)

ans=0
N=len(paper)
n=len(paper[0])
for i in range(N):
    for j in range(n-1):
        if paper[i][j]==1:
            search(i,j)
print(ans)