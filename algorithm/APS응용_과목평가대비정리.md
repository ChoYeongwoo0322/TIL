#### 순열

itertools를 활용하면, 시간도 단축되고 빠르게 설정할 수 있다. 난.... 그 순열만들고 하는 함수의 과정을 이해하지 못했기 때문에, 그냥 이걸로 사용할 것이다.

* 순열은 N개 중에서 순서상관있게 r개 고르면 된다. AB와 BA는 다른걸로 취급함 항상 튜플로나오니까 리스트로 바꿔서 쓰는것을 생활화하는걸로~

```python
from itertools import permutations
A = [i for i in range(5)]
nPr = itertools.permutations(A,len(A))
nPr_list = []
for i in nPr:
    nPr_list.append(list(i))
print(nPr_list)
```

```python
from itertools import permutations
N=6
initial_comb = [i for i in range(1, N)]
lst1 = []
for i in list(permutations(initial_comb, len(initial_comb))):
    lst1.append(list(i))
print(lst1)
```

#### 조합

* 조합은 N개 중에서 r개를 뽑는데, 이건 순서가 상관없다 그냥 r개만 뽑으면 된다. ABC나 CBA나 3개뽑힌건 매한가지이다.

```python
from itertools import combinations
A = [i for i in range(5)]
nCr = itertools.combinations(A,3)
nCr_list=[]
for i in nCr:
    nCr_list.append(list(i))
print(nCr_list)
```



##### lambda로 정렬하기

가끔 이것을 까먹긴한데, 리스트가 있으면 그 리스트의 몇번째 항으로 정렬을 시켜줄때 사용함.

따로 설정을 안하면 기본적으로 첫번째 항으로 정렬이될것임

```
using_time.sort(key=lambda x:x[1])
# using_time리스트를 [1]인덱스1의 항으로 정렬해줄것임.
# 이것을 보면 1은 끝나는 시간을 나타내는것임.
```



------

#### 병합정렬

병합정렬이라고해서 쪼개고쪼개고쪼개서 두개비교한다음 합쳐주고, 그렇게 또 합쳐주고합쳐주고 쭉쭉쭉 올라가면서 계속 합쳐주는것을 의미한다

```python
# 일단 기본세팅을해주자.
def merge_sort(a): # 리스트 하나 받아서
    # 길이가 1일때까지 굴려주니까
    if len(a) == 1:
        return a
    else:
        mid = len(a)//2 # 반으로 쪼개기
        low = a[:mid] # 왼쪽
        high = a[mid:] # 오른쪽
        low = merge_sort(low)
        high = merge_sort(high)
        # 이 과정이 끝나게 되면 return a를 통해서 길이가 1 이하인 아이가 나오게됨
        return merge(low, high) # 나온 low와 high를 merge해준다.

def merge(low, high):
    global cnt
    merge_list=[] # 작은거부터 하나씩 넣어주려면 리스트0으로 안만들어도됨
    i,j=0,0
    while i < len(low) or j < len(high): # 두개 리스트의 인덱스가 범위안일때
        if i < len(low) and j < len(high):
            if low[i] < high[j]: # 만약 low가 더 작다면?
                merge_list.append(low[i]) # list에 추가해주기
                i+=1 # 그러고 low의 인덱스인 i는 한칸 전진
            else:
                merge_list.append(high[j])
                j+=1
        elif i < len(low): # 왼쪽만 남았을때
            merge_list.append(low[i])
            i+=1
        elif j < len(high):
            merge_list.append(high[j])
            j+=1
    return merge_list

for tc in range(1, int(input())+1):

    arr=list(map(int, input().split())) # 정렬해줄 리스트 받아주기
    cnt = 0
    ans = merge_sort(arr) # 병합정렬을 함수로 돌려준다.

    print(ans)
```

---

##### 퀵정렬

pivot을 활용해서 왼쪽오른쪽으로 나뉘어진채로 pivot과 비교해서 정렬해주는방식

```python
def Quick(temp,start,end):
    if start>=end:
        return
    pivot=start
    left=start+1
    right=end
    while left <= right:
        while left<=end and temp[left] <= temp[pivot]:
            left+=1
        while right>start and temp[right] >= temp[pivot]:
            right-=1

        if left > right: # 엇갈린거
            temp[right], temp[pivot] = temp[pivot], temp[right]
        else:
            temp[left],temp[right]=temp[right],temp[left]
    Quick(temp,start,right-1)
    Quick(temp,right+1,end)


for tc in range(1, int(input())+1):
    N=int(input())
    temp=list(map(int, input().split()))
    start, end = 0, len(temp)-1
    Quick(temp, start, end)

    print("#{} {}".format(tc, temp[N//2]))
```

---

#### 이진수

```
for tc in range(1, int(input())+1):
    l,w=map(str,input().split()) # 몇자리인지, 16진수
    result='' # 여기에 차곡차곡 넣어줄예정
    for i in range(len(w)): # l이랑 같은거같음, w의길이
        result+="{:04b}".format(int(w[i],16))
		# result에다가 format을 활용해 16진수를 2진수b로 바꿔서 하나씩 차곡차곡 넣어줌 04는 아마도 0의 4자리를 의미하는것 같음. 필요없으면 안해줘도될듯
    print("#{} {}".format(tc, result))
```

```
for tc in range(1, int(input())+1):
    num=float(input()) # 소수받아주기
    result="" #결과값담아주기
    while True: # 계속돌릴거양~~
        num*=2 # 곱하기2
        result+=str(int(num)) # 실수부분만 담아주기
        num-=int(num) # 그리고 실수빼주기
  # 이것을 반복반복 하다가
        if not num%2: # 만약 2로 나눴을때 나머지가 없다면?
            break # 멈춰라
        elif len(result)>13: # 만약 길이가 13이상이라면? 
            result="overflow" # overflow를 출력해라
            break # 그리고멈춰
    print("#{} {}".format(tc, result)) # 결과값출력
```

