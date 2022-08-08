# CSS (Cascading Style Sheets)
* 스타일을 지정하기 위한 언어
* 선택자 {속성:값;}
* 선택자를 통해 스타일을 지정할 HTML 요소를 선택
* 속성 : 어떤 스타일 기능을 변경할지 결정
* 값 : 어떻게 스타일 기능을 변경할지 결정

# CSS 정의 방법
## 인라인 
* 해당 태그에 직접 style 속성을 활용
* 실수가 잦아짐 (중복, 찾기 어려움)
## 내부 참조
* <head> 태그 내에 <style> 에 지정
* 내부 참조를 쓰게 되면 코드가 너무 길어짐
## 외부 참조
* 외부 CSS 파일을 <head> 내 <link>를 통해 불러오기
* 가장 많이 쓰는 방식

# CSS Selectors
## 선택자 유형
* 기본 선택자
  * 전체 선택자 : *
  * 요소 선택자 : h1. h2 (HTML 태그를 직접 선택)
  * 클래스 선택자 : .green
  * 아이디 선택자 : #purple (단일 id 사용)
  * 속성 선택자 

* 결합자
  * 자손 결합자 : .box p [선택자 box 하위의 모든 p 요소]
  * 자식 결합자 : .box > p [선택자 box  바로 아래의 p 요소]
  * 일반 형제 결합자 : p ~ span [선택자 p 뒤에 위치하는 span 요소를 모두 선택]
  * 인접 형제 결합자 : p + span [선택자 p 바로 뒤에 위치하는 span 요소를 선택]

* 의사 클래스/요소
  * 링크, 동적 의사 클래스
  * 구조적 의사 클래스, 기타 의사 클래스, 의사 엘리먼트, 속성 선택자
* 우선순위 : !important > 인라인 > id > class, 속성, pseudo-class > 요소, pseudo-element > CSS 파일 로딩 순서
  
* CSS 상속
  * 속성 중에는 상속이 되는 것과 되지 않는 것들이 있다.
  * 되는 것 : text 관련 요소, opacity, visibility 등
  * 안되는 것 : box model 관련 요소, position 관련 요소 등

# CSS 기본 스타일
* 크기 단위
  * PX 픽셀
    * 모니터 해상도의 한 화소 기준
    * 고정적인 단위
  * %
    * 백분율 단위
    * 가변적인 레이아웃에서 자주 사용
  * em
    * 상속의 영향을 받음
    * 배수 단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐
  * rem 
    * 상속의 영향을 받지 않음
    * 최상위 요소 html 의 사이즈를 기준으로 배수 단위를 가짐
  * viewport
    * 디바이스의 viewport를 기준으로 상대적인 사이즈가 결정됨
    * vw, vh, vmin, vmax
* 색상 단위
  * 색상 키워드
    * 대소문자 구분 X
    * 특정 색을 직접 글자로 나타냄
  * RGB 색상
    * 16진수 표기법 (#) or 함수형 표기법 (rgb) 으로 특정 색을 표현
  * HSL 색상
    * 색상, 채도, 명도를 통해 특정 색을 표현하는 방식
    * hsla : a는 투명도

* 문서 표현
  * 텍스트
    * 서체 (font-family)
    * 서체 스타일 (font-style, font-weight)
    * 자간 (letter-spacing)
    * 단어 간격 (word-spacing)
    * 행간 (line-height)
    * 컬러 (color)
    * 배경 (background-image, background-color)
    * 목록 (li) , 표 (table)

# Box model
* 모든 HTML 요소는 box 형태로 되어있음
* 하나의 박스는 네 부분으로 이루어짐
  * margin / border / padding / content
  * margin / padding의 shorthand
    * 1개 = 상하좌우
    * 2개 = 상하 / 좌우
    * 3개 = 상 / 좌우 / 하
    * 4개 = 상 / 우 / 하 / 좌
  * border의 shorthand
    * width style color
* 기본적으로 모든 요소의 box-sizing은 content-box
* padding을 제외한 순수 contents 영역만을 box로 지정
* 우리가 일반적으로 영역을 볼 때는 border까지의 너비를 보는 것을 원함
  * box-sizing을 border-box로 설정

# CSS Display
* display에 따라 크기와 배치가 달라진다.
* block 
  * 줄 바꿈이 일어나는 요소
  * 화면 크기 전체의 가로 폭을 차지한다.
  * 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음
  * `div / ul, ol, li / p / hr / form` 등
* inline
  * 줄 바꿈이 일어나지 않는 행의 일부 요소
  * content 너비만큼 가로 폭 차지
  * width, height, margin-top, margin-botton을 지정할 수 없다.
  * 상하 여백은 line-height으로 지정
  * `span / a / img / input, label / b, em, i, strong` 등
* display: inline-block
  * block과 inline 레벨 요소의 특징을 모두 가짐
* display: none
  * 화면에 표시하지 않고 공간조차 부여되지 않음
  * hidden은 공간은 차지함

# CSS position
* 문서 상에서 요소의 위치 지정
* static 
  * 모든 태그의 기본 값
  * 일반적인 요소의 배치 순서에 따름
  * 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치됨
* 좌표 프로퍼티 (top, bottom, left, right) 로 이동 가능한 position
  * relative : 상대 위치
    * 자기 자신의 static 위치를 기준으로 이동
    * 요소가 차지하는 공간은  static일 때와 같음
  * absolute : 절대 위치
    * normal flow에서 벗어남
    * 가장 가까이 있는 부모를 기준으로 이동 (없는 경우 화면 기준으로)
  * fixed : 고정 위치
    * normal flow에서 벗어남
    * 부모 요소와 관계없이 viewport를 기준으로 이동
  * sticky : 스크롤에 따라 static -> fixed로 변경
    * 속성을 적용한 박스는 평소에 일반적인 흐름이지만, 스크롤 위치가 임계점에 이르면 박스를 화면에 고정


# CSS 원칙
* 1, 2 : Normal flow
  * 모든 요소는 박스모델, 좌측상단에 배치
  * diplay에 따라 크기와 배치가 달라짐
* 3 : position으로 위치의 기준을 변경
  * relative : 본인의 원래 위치
  * absolute : 특정 부모의 위치
  * fixed : 화면의 위치
  * sticky : 기본적으로 static이나 스크롤 이동에 따라 fixed로 변경