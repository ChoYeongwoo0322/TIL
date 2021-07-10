# :boot: Bootstrap

:one: CSS,JS 복붙

- [bootstrap]: https://getbootstrap.kr/docs/5.0/getting-started/introduction

![image-20210710115958111](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210710115958111.png)

:walking: CSS, JS 복붙해서 html에 복사

:whale: html은 어디에??

![image-20210710131728687](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210710131728687.png)

- public/index.html
  - CSS는 head
  - JS는 body끝

> 단점이라함은 사이트에있는걸 끌어와서 사용하는거라, 사이트이용안될때는 로딩이 오래걸림... 그래서 다운받아서 쓰던가해도됨

---

:two: npm으로 bootstrap설치(5.x)

```vue
npm install bootstrap@next @popperjs/core
```

- main.js

  ```vue
  import 'bootstrap'
  import 'bootstrap/dist/css/bootstrap.min.css'
  ```

