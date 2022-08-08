# Float
* CSS 원칙
  * Nomal Flow
  * 모든 요소는 박스모델이고, 위에서 아래로, 왼쪽에서 오른쪽으로 쌓임
  * Float : 박스를 좌우로 이동시켜 인라인요소들이 주변을 wrapping 하도록 함
    * none : 기본값
    * left : 요소를 왼쪽으로 띄움
    * right : 요소를 오른쪽으로 띄움

# Flexbox
* 행과 열 형태로 아이템들을 배치하는 1차원 레이아웃 모델
* 축
  * main axis [direction : row]
  * cross axis (교차 축)
* 구성 요소
  * Flex Container (부모 요소)
    * Flex item들이 놓여있는 영역
    * display 속성을 flex or inline-flex로 지정
  * Flex item (자식 요소)

* 시작
  * 부모 요소에 display:flex / inline-flex

* 속성
  * 배치 설정
    * flex-direction
      * main axis 기준 방향 설정
      * row / column
    * flex-wrap
      * 아이템이 컨테이너를 벗어나는 경우 해당 영역 내에 배치되도록 설정
      * 요소들이 강제로 한 줄에 배치 되게 할 것인지 여부 설정
      * wrap : 넘치면 그 다음 줄로 배치
      * nowrap(기본값) : 한 줄에 배치
    * flex-flow
      * flex-direction과 flex-wrap의 shorthand
      * flex-flow:row nowrap;
  
  * 공간 나누기
    * justify-content (main axis)
      * main axis를 기준으로 공간 배분
      * flex-start (시작점으로) / flex-end (끝 쪽으로) / center (중앙으로) 
      * space-between (사이의 간격을 균일하게 분배) / space-around (둘러싼 영역을 균일하게 분배) / space-evenly (전체 영역에서 아이템 간 간격을 균일하게 분배)
    * align-content (cross axis)
      * cross axis를 기준으로 공간 배분 (아이템이 한 줄로 배치되는 경우 확인 X)
      * flex-start / flex-end / center 
      * space-between / space-around / space-evenly
  
  * 정렬
    * align-items 
      * 모든 아이템을 cross axis 기준으로 정렬
      * stretch (컨테이너를 가득 채움) / baseline (텍스트 baseline에 기준선을 맞춤)
      * flex-start (위) / flex-end (아래) / center (가운데)
    * align-self
      * 개별 아이템을 cross axis 기준으로 정렬
      * 컨테이너에 적용하는 것이 아니라 개별 아이템에 적용 !!!
      * stretch / flex-start / flex-end / center
    * flex-grow : 남은 영역을 아이템에 분배
    * order : 배치 순서