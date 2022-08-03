# Bootstrap
* bootstrap 사이트에서 예제 하나씩 해보기

* spacing (Margin and Padding)
  * {property}{sides}-{size} => 
    * mt-3 (margin top 3)
    * mx-auto : 가로 가운데 정렬
  * <div class="mt-3 ms-5">bootstrap-spacing</div>

  * {property} : margin or padding?
    * m - margin
    * p - padding
  
  * {sides} : 위, 아래, 왼, 오
    * t - top
    * b - bottom
    * s - start / left
    * e - end / right
    * x - 양 옆 (left, right)
    * y - 양 위아래 (top, bottom)
    * blank - 4 sides
  
  * {side} : 크기
    * [ 1 rem = 16px ]
    * 0 - 0
    * auto - aito
    * 1 - *0.25rem = 4px
    * 2 - *0.5rem = 8px
    * 3 - *1rem = 16px
    * 4 - *1.5rem = 24px
    * 5 - *3rem = 48px

* Color
  * <div class="bg-primary">이건 파랑</div>
  * <div class="text-danger">텍스트 빨강</div>

* Text
  * 텍스트 위치
    * <p class="text-start">text-start</p>
    * <p class="text-center">text-center</p>
    * <p class="text-end">text-end</p>
  * 링크 밑줄, 색 변경
    * <a href="#" class="text-decoration-none text-dark">Non-underline-Link</a>
    * a.text-decorantion-none.text-dark 로 사용하면 자동 완성 
      * 클래스가 자동 생성 되기 때문에 실수 확률 낮음!
    * text-decoration : 밑줄 없애기
    * text-dark : 글씨 색상 어둡게
    * p.fw-bold : 글씨 굵게
    * p.fw-nomal : 글씨 보통
    * p.fw-light : 글씨 얇게
    * p.fst-italic : 폰트 스타일 이탈릭

* Position (top, start, bottom, end)
  * relative
  * static
  * absolute
    * 부모가 static이 아니여야 함 `relative`로 해주면 됨
    * 브라우저를 기준으로 이동
  * fixed
  * sticky

* Display
  * <div class="d-inline p-2 text-bg-primary">d-inline</div>
    * 인라인
  * <span class="d-block p-2 text-bg-primary">d-block</span>
    * 블록
  * .d-none : 사라지도록

* Components
  * Buttons
  * Dropdowns
  * Form control
  * `Navbar`
  * Carousel
  * Modal 
    * 팝업창이랑 다름 : 모달은 페이지 이동 시 사라짐
    * 중첩 사용 X 
  * Card - Grid Cards

* Layout - Grid System
  * flexbox로 제작
  * 1. 12개의 column
  * 2. 6개의 grid breakpoints : 구간마다 어떤 디자인을 보여줄건지
    * ~576px / ~768px / ~992px / ~1200px / ~1400px

  * box col-2 / box col-8 / box col-2
    * column 은 총 12칸이므로 2 / 8 / 2 칸씩 나눔
  * box col-1 * 13
    * 12칸까지 하나씩 나오고 남은 한칸은 다음줄에
  * box col-9 / box col-4 / box col-4
    * 9칸 할당하고, 9+4는 12를 넘기 때문에, 뒤의 4칸, 4칸은 다음줄에

  * 크기에 따라 비율이 변경되도록 (break point 사용)
    ``` html
    <div class="row">
      <div class="box col-2 col-sm-8 col-md-4 col-lg-5">1</div>
      <div class="box col-8 col-sm-2 col-md-4 col-lg-2">1</div>
      <div class="box col-2 col-sm-2 col-md-4 col-lg-5">1</div>
    ```
    * 2 + 8 + 2 = 12칸
    * sm (스몰 사이즈) = 8 : 2 : 2
    * md (미디움 사이즈) = 4 : 4 : 4
    * lg (라지 사이즈) = 5 : 2 : 5

  * 중첩 가능

  * <div class="box col-md-4 offset-md-4 offset-lg-2"></div>
    * offset : 띄우고 싶은 칸 수