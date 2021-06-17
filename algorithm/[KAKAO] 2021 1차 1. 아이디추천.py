'''
"...!@BaT#*..y.abcdefghijklm"
"z-+.^."
"=.="
"123_.def"
"abcdefghijklmn.p"
'''
def step_1(l):
    global letter
    N=len(letter)
    for i in range(N):
        # print(ord(letter[i]))
        if 65<=ord(letter[i])<=90:
            letter[i]=chr(ord(letter[i])+32)

def step_2(l):
    global letter
    lst=[]
    for i in letter:
        if i=='-' or i=='_' or i=='.':
            lst.append(i)
        elif 97<=ord(i)<=122:
            lst.append(i)
        elif '0'<=i<='9':
            lst.append(i)
    letter=lst

def step_3(l):
    global letter
    lst=[]
    for i in letter:
        if not lst:
            lst.append(i)
        elif i=='.' and lst[-1]=='.':
            continue
        else:
            lst.append(i)
    letter=lst

def step_4(l):
    global letter
    N=len(letter)
    if N!=0:
        if letter[0]=='.':
            del letter[0]
    if len(letter)!=0:
        if letter[-1]=='.':
            del letter[-1]

def step_5(l):
    global letter
    if not letter:
        letter.append('a')

def step_6(l):
    global letter
    if len(letter)>=16:
        letter=letter[:15]
    if letter[-1]=='.':
        del letter[-1]

def step_7(l):
    global letter
    while len(letter)<=2:
        letter.append(letter[-1])

letter=list(input())[1:-1]
step_1(letter)
step_2(letter)
step_3(letter)
step_4(letter)
step_5(letter)
step_6(letter)
step_7(letter)

print(f'"{"".join(letter)}"')
