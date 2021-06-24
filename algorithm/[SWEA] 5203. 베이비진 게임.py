'''
3
9 9 5 6 5 6 1 1 4 2 2 1
5 3 2 9 1 5 2 0 9 2 0 0
2 8 7 7 0 2 2 2 5 4 0 3
'''
def babygin(player1,player2):
    flag=0
    temp1=[0]*10
    temp2=[0]*10
    for i in range(6):
        temp1[player1[i]]+=1
        if i>=2 and check(temp1)==1:
            flag=1
            return flag
        temp2[player2[i]]+=1
        if i>=2 and check(temp2)==1:
            flag=2
            return flag
    return flag

def check(player):
    # triplet
    for j in range(10):
        if player[j] == 3:
            return 1
    # run
    for j in range(8):
        if player[j] and player[j+1] and player[j+2]:
            return 1

for tc in range(1,int(input())+1):
    player1=[]
    player2=[]
    card=list(map(int,input().split()))

    for i in range(0,12,2):
        player1.append(card[i])
        player2.append(card[i+1])

    print("#{} {}".format(tc, babygin(player1,player2)))
