# :arrow_right_hook: Lifecycle Hook

- lifecycle 사이에서 갈고리Hook을 걸어 실행시켜주세요.

  ![image-20210709235722658](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210709235722658.png)

  ```vue
    mounted(){
    },
  ```

  :star: UI 만드는법

  ![image-20210709235907242](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210709235907242.png)

  :star: 몇초 뒤에 실행시키기 위한 함수 : `setTimeout`

  ```vue
    mounted(){
      setTimeout(()=>{
        this.showDiscount=false;
      },1000);
    },
  ```

  > this.를 사용할때 function대신 `()=>` 애로우타입으로 작성해야함

