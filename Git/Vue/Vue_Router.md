# UI & UX
* UX 
  * 유저와 가장 가까이에 있는 분야
  * 데이터를 기반으로 유저를 조사, 분석해서 개발자와 디자이너가 이해할 수 있게 소통
  * 유저가 느끼는 느낌, 태도, 행동을 디자인
* UI 
  * 유저에게 보여지는 화면을 디자인
  * UX를 고려한 디자인을 반영
  * 프론트엔드 개발자와 가장 많이 소통

# Vue Router
## Routing
* 네트워크에서 경로를 선택하는 프로세스
* 웹 서비스에서의 라우팅 : 유저가 방문한 url에 대해 적절한 결과를 응답하는 것
* Routing in SSR
  * 서버가 모든 라우팅을 통제
  * URL로 요청이 들어오면 응답으로 완성된 HTML 제공
* Routing in SPA/ CSR
  * 서버는 하나의 HTML만을 제공
  * 이후에 모든 동작은 하나의 HTML 문서 위에서 JS 코드 활용
  * 하나의 URL만 가질 수 있음

## Vue Router
* SPA 상에서 라우팅을 쉽게 개발할 수 있는 기능 제공
* 라우트에 컴포넌트를 매핑한 후, 어떤 URL에서 렌더링 할지 알려줌
* 설치
  * vue create vue-router-app  => Vue 프로젝트 생성
  * cd vue-router-app          => 디렉토리 이동
  * vue add router             => Vue CLI를 통해 router plugin 적용
  * 프젝 진행 중, router를 추가하게 되면 App.vue를 덮어쓰므로 필요한 경우 명령을 실행하기 전에 파일을 백업해둬야 함
* History mode
  * 브라우저의 History API를 활용한 방식 => 새로고침 없이 URL 이동 기록 남길 수 있음
  * 우리에게 익숙한 URL 구조로 사용 가능
  * <=> Hash mode : # 을 통해 URL을 구분하는 방식
* `router-link`
  * a 태그와 비슷한 기능 => URL 이동
  * routes에 등록된 컴포넌트와 매핑됨
  * 히스토리 모드에서 router-link는 클릭 이벤트를 차단해 a 태그와 달리 브라우저가 페이지를 다시 로드하지 않도록 함
  * 목표 경로는 `to` 속성으로 지정됨
  * 기능에 맞게 HTML에서 a태그로 렌더링되지만, 필요에 따라 다른 태그로 바꿀 수 있음
* `router-view`
  * 주어진 URL에 대해 일치하는 컴포넌트를 렌더링 하는 컴포넌트
  * 실제 컴포넌트가 DOM에 부착되어 보이는 자리
  * router-link를 클릭하면 routes에 매핑된 컴포넌트를 렌더링
  * `App.view는 base.html의 역할, router-view는 block 태그로 감싼 부분`
* src/router/index.js
  * 라우터에 관련된 정보, 설정 작성
  * django에서 urls.py에 해당
  * routes에 URL과 컴포넌트를 매핑
* src/Views
  * router-view에 들어갈 컴포넌트 작성
  * views/ 
    * routes에 매핑되는 컴포넌트
    * 다른 컴포넌트와 구분하기 위해 View로 끝나도록 만드는 것을 권장
  * components/
    * routes에 매핑된 컴포넌트의 하위 컴포넌트를 모아두는 폴더


* 선언적 방식 네비게이션
  * router-link의 `to` 속성으로 주소 전달
  * routes에 등록된 주소와 매핑된 컴포넌트로 이동
* 프로그래밍 방식 네비게이션
  * Vue 인스턴스 내부에서 라우터 인스턴스에 `$router`로 접근 가능
  * 다른 URL로 이동은 `this.$router.push` 사용
* lazy-loading
  * 미리 로드를 하지 않고 특정 라우트에 방문할 때 매핑된 컴포넌트의 코드를 로드하는 방식 
  * 최초에 로드하는 시간이 빨라짐
  * `당장 사용하지 않을 컴포넌트는 먼저 로드하지 않음`

# Navigation Guard
* Vue router를 통해 특정 URL에 접근할 때 다른 url로 redirect 하거나 URL로의 접근을 막는 방법

## 전역 가드
* 애플리케이션 전역에서 동작
* 다른 url 주소로 이동할 때 항상 실행
* router/index.js에 `router.beforeEach()`를 사용하여 설정
* 콜백 함수의 값으로 3개의 인자
  * to : 이동할 URL 정보가 담긴 Route 객체
  * from : 현재 URL 정보가 담긴 Route 객체
  * next : 지정한 URL로 이동하기 위해 호출하는 함수
* 변경된 URL로 라우팅하기 위해서는 next()를 호출해줘야 함
* next()가 호출되기 전까지 화면이 전환되지 않음

## 라우터 가드
* 특정 URL에서만 동작
* `beforeEnter()`
  * route에 진입했을 때 실행됨
  * 라우터를 등록한 위치에 추가
  * 다른 경로에서 탐색할 때만 실행됨
  * ex) 이미 로그인 되어있는 경우 HomeView로 이동하기
  
## 컴포넌트 가드
* 라우터 컴포넌트 안에 정의
* 특정 컴포넌트 내에서 가드를 지정하고 싶을 때 사용
* `beforeRouteUpdate()`
  * 해당 컴포넌트를 렌더링하는 경로가 변경될 때 실행
  * params 변화 감지 => url은 변하는데 페이지는 변하지 않는 것 해결

# 404 Not Found
* 사용자가 요청한 리소스가 존재하지 않을 때 응답
* 모든 경로에 대해서 404 page로 redirect => routes에 최하단부에 작성