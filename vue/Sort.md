# :arrow_down_small: Sort

- list().sort()

  ```vue
  priceSort(){
        this.roomdata.sort(function(a,b){
          return a-b
        })
      }
  ```

  > a,b는 숫자들을 의미해주고 a-b했을때 양수가 나오면 자리를 바꿔주고 뭐 무튼 그런식으로 정렬을 해준다고함.. (???)

---

:sos: 원본을 보존하면서 새로운 변수를 만들어주려면

```vue
      originalroomdata:[...roomdata],
      roomdata,
```

> [...data]를 같이 작성하면 각각 별개의 사본을 만들어줌

##### BUT!!!

몇번 쓰다보면 멈춰버림...

```vue
    sortBack(){
      this.roomdata=this.originalroomdata;
    }
```

> 값을 갈아치워주세요~ 가 아니라, =로 넣어주게되면 값공유해주세요~ 가 되버림

```vue
      this.roomdata=[...this.originalroomdata];
```

> 그럴땐, 이것도 사본을 복사해서 넣어주기