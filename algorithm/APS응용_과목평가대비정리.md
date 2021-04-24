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

