## Indexing

### Point) item 위치에 숫자를 쓰자.

​	![indexing](Indexing & slicing.assets/indexing-1611026863842.png)

* 리스트 요소의 각각의 위치를 숫자로 접근을 한다.

* 리스트 길이 보다 큰 인덱스 번호로 접근할 수 없다. (에러 발생)

* 시작은 0 부터 이다.

* 리스트의 가장 우측의 값을 접근을 하려면 `-1` 을 인덱스 값으로 넣어주면 된다.

  ```python
  num_list = [10, 20, 30, 40, 50, 60]
  
  print(num_list[3])  # 40
  print(num_list[6])  # IndexError: list index out of range
  print(num_list[0])  # 10
  print(num_list[-1]) # 60
  print(num_list[-3]) # 40
  ```

------

## Slicing

### Point) 콤마 위치에 숫자를 쓰자

​	![slicing](Indexing & slicing.assets/slicing-1611026873023.png)

* 기본 사용법 : `리스트_변수명[시작점:끝점:step]`

* 시작점과 끝점 그리고 몇 씩 증가할지 step 을 작성해주는 방식으로 slicing 을 할 수 있다.

  * step은 1이 기본 값으로 설정되어 있다.

* 나누는 위치는 **콤마(,) 를 기준으로 숫자를 써주면 된다**. 

  * 시작인 0은 대괄호 시작점에 맞춰주면된다. 

    (마지막 대괄호는 숫자를 안적는다. 0은 무조건 좌측 대괄호 위치 (`[`) 이다.)

* 시작점과 끝점을 생략하는 경우 

  * `시작점 생략: 처음부터` 를 의미한다. 
  * `끝점 생략: 끝까지` 를 의미한다.
  * `변수명[:]` => 처음부터 끝까지를 의미
  
  ```python
  num_list = [10, 20, 30, 40, 50, 60]
  
  print(num_list[0:3])  # [10, 20, 30]
  print(num_list[:3])   # [10, 20, 30] 처음부터 3번점 까지
  print(num_list[2:])   # [30, 40, 50, 60]  2번점 부터 끝까지
  print(num_list[:])    # [10, 20, 30, 40, 50, 60]  처음부터 끝까지
print(num_list[-3:-1])# [40, 50] -3번점 부터 -1번점 까지
  print(num_list[:-1])  # [10, 20, 30, 40, 50] 처음부터 -1번점 까지
print(num_list[2:-2]) # [30, 40] 2번점 부터 -2번점 까지
  print(num_list[-1:])  # [60] -1번점 부터 끝까지
  ```
  
  * 스텝이 주어지는 경우 시작점에 증가하는 숫자만큼 더해서 그 숫자의 뒷 요소를 찾으면 된다.
  
    ```python
    print(num_list[1::2]) # [20, 40, 60] 1번점 부터 끝까지 2씩 증가한다.
    # 1번점, 3번점, 5번점, 순으로 2씩 증가를 하게 되는데
    # 이때 1번 점의 뒤에 있는 값 20
    # 3번점의 뒤에 있는 값 40
    # 5번점의 뒤에 있는 값 60
    # 이 선택이 되게 된다.
    ```



---

다음과 같은 형태로 index, slice 가 이루어 지니 궁금한 부분이 있다면 **직접 타이핑**을 해서 비교해 보시기 바랍니다. 