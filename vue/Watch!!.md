# :watch: Watch!!

데이터를 감시하기 위해 사용하는것

```vue
export default {
    name:'Modal',
    data(){
      return{
        month:1,
      }
    },
```

input에 month데이터를 입력하는데, 이것이 옳게 들어가는지를 감시하기위해

```vue
    watch:{
      month(){
        
      }
    },
```

```vue
watch:{감시할데이터(){}}
```

```
    watch:{
      month(a,b){
        if (a>12){
          alert('13이상 입력하지 마세요')
```

:watermelon: b는 변경전, a가 변경 후

---

# :open_mouth: transition

```vue
  <div class="start" :class="{end:modal}">
    <Modal @modal="modal=false" :roomdata="roomdata" :putroom="putroom" :modal="modal"/>
  </div>
```

```vue
.start {
  opacity: 0;
  transition: all 1s;
}
.end {
  opacity: 1;
}
```

:exclamation: 스페셜한 vue의 기능!

```vue
  <transition name="fade"> //name="작명"
    <Modal @modal="modal=false" :roomdata="roomdata" :putroom="putroom" :modal="modal"/>
  </transition>
```

:goal_net: 등장

```vue
.fade-enter-from {
  opacity: 0;
}
.fade-enter-active {
  transition: all 1s;
}
.fade-enter-to {
  opacity: 1;
}
// .작명-XXX-XXX
```

:outbox_tray: 퇴장

```
.fade-leave-from {
  opacity: 1;
}
.fade-leave-active {
  transition: all 1s;
}
.fade-leave-to {
  opacity: 0;
}
```

