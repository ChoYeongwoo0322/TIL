# 21.02.05

#### 01_nav_footer.html

항상 처음 시작은 네비게이션탭을 위에 고정한다고한다. 이건 어느 웹사이트를 가던 똑같은것 같은데,

```
<nav class="fixed-top">
```

네이게이션바에 툴? 같은게 붙어있길래

```
<nav class="navbar navbar-expand-lg navbar-light bg-light">
  <div class="container-fluid">
    <a class="navbar-brand" href="#">Navbar</a>
    <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavDropdown" aria-controls="navbarNavDropdown" aria-expanded="false" aria-label="Toggle navigation">
      <span class="navbar-toggler-icon"></span>
    </button>
    <div class="collapse navbar-collapse" id="navbarNavDropdown">
      <ul class="navbar-nav">
        <li class="nav-item">
          <a class="nav-link active" aria-current="page" href="#">Home</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Features</a>
        </li>
        <li class="nav-item">
          <a class="nav-link" href="#">Pricing</a>
        </li>
        <li class="nav-item dropdown">
          <a class="nav-link dropdown-toggle" href="#" id="navbarDropdownMenuLink" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            Dropdown link
          </a>
          <ul class="dropdown-menu" aria-labelledby="navbarDropdownMenuLink">
            <li><a class="dropdown-item" href="#">Action</a></li>
            <li><a class="dropdown-item" href="#">Another action</a></li>
            <li><a class="dropdown-item" href="#">Something else here</a></li>
          </ul>
        </li>
      </ul>
    </div>
  </div>
</nav>
```

이 양식을 주워왔다. component - navbar에 들어가면 쉽게 양식을 구할수 있다. 이런식으로

필요한 양식들을 하나씩 하나씩 줍다보면 뭔가의 양식은 만들어지게된다.

햄버거를 만들어줘야되는데.. 흠, 일단 드롭다운을 삭제하고 뭘 뒤적뒤적 하다보면

```
      <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
        <span class="navbar-toggler-icon"></span>
      </button>
```

버튼을 하나 발견하게될거다. 이걸 살포시 넣어주면 얼추 틀이 잡히는데, 여기서 내가겪은 문제가 있다.

오른쪽정렬이 안되는거다. 아휴ㅠㅠ... 그런데,  항목들이 들어간 ul에다가 ms-auto를 추가해주니, 마진스타트부분이 오토로 늘어나면서, 쭉 오른쪽으로 밀리는것이 아니겠는가. 그렇게 해결

그다음 login에 modal을 적용해줄차례인데

```
<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal" data-bs-whatever="@mdo">Open modal for @mdo</button>
<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal" data-bs-whatever="@fat">Open modal for @fat</button>
<button type="button" class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#exampleModal" data-bs-whatever="@getbootstrap">Open modal for @getbootstrap</button>

<div class="modal fade" id="exampleModal" tabindex="-1" aria-labelledby="exampleModalLabel" aria-hidden="true">
  <div class="modal-dialog">
    <div class="modal-content">
      <div class="modal-header">
        <h5 class="modal-title" id="exampleModalLabel">New message</h5>
        <button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>
      </div>
      <div class="modal-body">
        <form>
          <div class="mb-3">
            <label for="recipient-name" class="col-form-label">Recipient:</label>
            <input type="text" class="form-control" id="recipient-name">
          </div>
          <div class="mb-3">
            <label for="message-text" class="col-form-label">Message:</label>
            <textarea class="form-control" id="message-text"></textarea>
          </div>
        </form>
      </div>
      <div class="modal-footer">
        <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Close</button>
        <button type="button" class="btn btn-primary">Send message</button>
      </div>
    </div>
  </div>
</div>
```

가장 비슷해보이는 아이로 또 복붙을 시도한다. 그러고 내가원하는 틀에맞게 변형을 해주는데,

여기서 또 문제발생. 패스워드는 칠떄 문자로 표현되어야한다. 누가훔쳐볼수없게 ^^;

```
input type="password"
```

그래서, 그부분은 password로 인풋을 설정해주면된다.

이정도까지하면 얼추 1페이지는 완성



