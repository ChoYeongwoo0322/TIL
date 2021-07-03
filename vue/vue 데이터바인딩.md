### ✔ vue 데이터바인딩

```vue
<script>
export default {
  name: 'App',
  data(){
    return{
      price1:100,
      price2:200,
      price3:300
    }
  },
  components: {
  }
}
</script>
```

👉 data통을 만들어서 return {여기에다가 데이터 다 집어넣어주기}

👉 데이터들은 object형식으로 = key:value

그리고 template에 연결시켜주려면

```vue
  <div>
    <h4>영우원룸</h4>
    <p>{{price1}}만원</p>
  </div>
```

👉 중괄호 2개를 활용해서 값 삽입

🎇 이 문법을 왜쓰느냐??

- html에 하드코딩해놓으면 나중에 변경이 어려움
- Vue의 실시간 자동 렌더링을 위헤
  - data를 변경하면 바로 자동반영됨, key값에 해당하는 것들을 자동으로!!
  - 실시간 자동 렌더링을 하면 웹앱같은 것을... 구현가능하다고함
  - 자주 변경할거 같은거는 꽂아넣어라
  - 자주 변경 안되는 항목은 굳이 데이터바인딩 해줄필요가 없음

❗❗ html 속성도 데이터바인딩이 가능!!

대신 속성 앞에 `:` 를 써준다.

```vue
      roomstyle:'color:blue',
```

```vue
    <h4 class="" :style="roomstyle">영우원룸</h4>
```

---

###  ✔ 반복문

```vue
<a href="" v-for="작명 in 횟수" :key="작명">Home</a>
```

⭕ :key="" 는 필수

💨 숫자 대신 데이터를 집어넣을 수도 있음

```vue
# data
menus:['Home', 'Shop', 'About']
```

```vue
<a href="" v-for="작명 in menus" :key="작명">Home</a>
```

🔅 menus의 길이만큼 반복을 수행

```vue
<a href="" v-for="value in menus" :key="value">{{value}}</a>
```

🔆 작명 부분을 value라고 지정하고 {{}}로 값 출력하면 menus의 데이터들이 출력됨

