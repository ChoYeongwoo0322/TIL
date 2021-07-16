# :round_pushpin: Router

- Router 설치

  ```
  npm install vue-router@4
  ```

- router.js 생성

  ![image-20210710155822614](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210710155822614.png)

- 경로, component 설정

  ```vue
  const routes = [
    {
      path: "/유저가 입력",
      component: 보여주는 .vue,
    },
  ```

  ```vue
  import List from './components/List.vue';
  ```

  ![image-20210710162241329](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210710162241329.png)

- App.vue에 표현

  ```vue
  <router-view :blogfeed="blogfeed"></router-view>
  ```

  :checkered_flag: 중간에 props같은 부분은 데이터를 전달하고싶을 때

---

:flags: router-link

```vue
<router-link to="/list">List Page</router-link>
```

:new: route에 param

```
path: "/detail/:id",
```

```
$route.params.id
```

주소의 :값 을 params.값 으로 호출