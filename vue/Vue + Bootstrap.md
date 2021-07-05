# Vue + Bootstrap

:new: 설치해주기

```
npm install vue bootstrap-vue bootstrap
```

:star: main.js 추가

```vue
import BootstrapVue from 'bootstrap-vue'
import 'bootstrap/dist/css/bootstrap.min.css'
import 'bootstrap-vue/dist/bootstrap-vue.css'

Vue.use(BootstrapVue)
```

:x: vue3에서는 지원되지 않는다고함 아직까진

:x: 프로젝트 이름을 bootstrap같은 뭔가 이런 유사한걸로 하면안됨

:x: vue2에서는 아직까지 root를 하나만 가지기 때문에 무조건 div로 감싸줘야하나봄 안그럼 에러

