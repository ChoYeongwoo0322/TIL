# 21.02.03.

<p>lorem => 더미데이터출력
 너무 많다싶으면 lorem3   
</p>

#### float : 공간차지하면서 위치설정해주기

float로 설정된 elem가 일반적인 문서 흐름으로 부터 빠져서 텍스트 및 인라인 요소가 그 주위를 감싸는 형태로 배치되게 하는 것

  .left {

   float: left;

  }  => 왼쪽으로(상자를)

  .right {

   float: right;

  }  => 오른쪽으로(상자를)

#### float clear

clear: both; => float를 해제하겠다. ? 강제로 막는거라고 하는데, 도통 뭔소린지..;?

float된 요소를 다시 내려주는 역할을 수행

left right both none

#### CSS Flexbox

flex  :  박스를 정렬하기 위한것..

자식에만 영향을 끼침, 자손은 x

요소 간 공간 배분 정렬을 1차원 레이아웃 : 한방향으로만

- 요소
  
- Flex Container안의 item들
  
- 축 main, cross(교차축)

  - 1-1 Flex Container : 제일 큰 박스 컨테이너

  기본방향은 왼쪽에서 오른쪽으로

시작..!

.flex-container { display: flex; }

- 배치 방향 설정: flex-direction : 메인의 축을 가로로 할거냐, 세로로할거냐

  - 기본적으로 row값을 가지고있음(왼 > 오) / row-reversse(오 > 왼)
  - 세로로 바꾸게되면, 메인축이 세로로... column : 위 > 아래,  column-reverse: 아래 > 위

- 메인축 방향 정렬 : justify-content 

  - justify : 메인축정렬
  - align : 교차축정렬

- 교차축 방향 정렬: align items(한 줄), self(개별요소를 선택), content(여러줄을 컨트롤하겠다)

  - 여기서 조합하면됨,

    justify-content : 메인축기준 여러줄 정렬

    - start, end, /center/, between, around, evenly

    align-items: 교차축 기준 한 줄 정렬

    - start, end, /center/, 

    align-content:

    - start, end, /center/, 

    align-self: 교차축 기준 선택한 요소 기준 정렬

- 기타... flex- wrap flow grou, shrink basis/ order



실습

   display: flex; = 기본값이 왼> 오 정렬

display: inline-flex; => 자기본인만큼의 너비를 가짐

flex-wrap: wrap; 초과분에 대해서는 아래로 떨궈버림

flex-wrap: wrap-reverse; = 반대로

flex-direction: row; = 왼오 정렬

flex-direction: row-reverse; = 오왼 정렬

flex-direction: column; = 상하 정렬

flex-direction: column-reverse; = 하상 정렬

justify-content: flex-end; = 왼오정렬이긴한데, 끝을 end에 맞춰줌

justify-content: space-between; = 양쪽으로 찢고 간격을 동일하게

justify-content: space-around; = 아이템들과의 너비가 처음과 그 다음의 너비 차가 2배, ex) 1,2222,1

justify-content: space-evenly; = 너비가 같음 1,1111,1

align-items: stretch; = align의 기본값

align-items: flex-start; = 위로 올라가버림

align-items: flex-end; = 밑으로 내려가버림

align-items: center; 중간으로 (+ 완전 중앙으로 해주고싶으면 justify-content: center;랑 합쳐주기)

 align-items: baseline; = 글자 중간거 크게해줌..?



align-self: flex-start; = 개별요소 선택해서



order: 0; = 기본값

oder: 1; = 기본값0들보다 1이 당연 더 크니까 2가 나오기 전으로 이동할듯



flex-grow: 1; = 주축에서 남는 부분의 비율을 각각 나눠주는거임, 1,2,3이라고해서 아~ 얘가 2. 1보다 2배니까 크기가 2배구나. 가 아니라, 나머지공간을 1:2비율로 나눠서 배분하는겅





# Bootstrap

프론트에서 유명하다고함, 빠른디자인, ..~

grid system, responsive..! 가장 중요한것. One source, multi use.

....

실습중.. 너무어렵다 엉엉엉 ㅠㅠㅠㅠ

과제제출도 제시간에 못했네 아이고..

