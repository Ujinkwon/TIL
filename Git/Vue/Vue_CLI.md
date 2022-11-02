# Node.js
* JS는 브라우저 밖에서 구동 X
* Node.js : JS를 구동하기 위한 런타임 환경 => 브라우저가 아닌 환경에서도 구동 가능
* NPM (Node Package Manage)
  * 자바스크립트 패키지 관리자
  * 파이썬 (pip) / Node.js (npm)
  * 다양한 의존성 패키지 관리
  * Node.js의 기본 패키지 관리자 (Node.js 설치 시 함께 설치됨)

# Vue CLI
* Vue 개발을 위한 표준 도구
* 프로젝트의 구성을 도와주는 역할
* 확장 플러그인, GUI, Babel 등 다양한 tool 제공
## Vue CLI Quick Start
  * 설치 (git bash) => npm install -g @vue/cli
  * 프로젝트 생성 (vscode terminal) => vue create vue-cli
  * Vue 버전 선택 (Vue2) 
  * 생성한 프로젝트 폴더로 이동 => cd vue-cli
  * 서버 구동 => npm run serve
## Vue CLI 프로젝트 구조
* node_modules
  * node.js 환경의 여러 의존성 모듈
  * python의 venv와 비슷한 역할
  * 그래서, .gitignore에 넣어줘야 해서 자동으로 추가됨
* node_modules - `Babel`
  * JS compiler
  * JS의 ES6+ 코드를 구버전으로 번역/변환 해주는 도구
  * JS의 파편화, 표준화의 영향으로 작성된 코드의 스펙트럼이 매우 다양
    * 최신 문법을 사용해도 브라우저 버전 별로 동작하지 않는 상황 발생
    * 버전에 따른 같은 의미의 다른 코드를 작성하는 등의 대응 필요 => 해결하기 위한 도구
* node_modules - `Webpack`
  * static module bundler
  * 모듈 간의 의존성 문제를 해결하기 위한 도구
  * 프로젝트에 필요한 모든 모듈을 매핑하고 내부적으로 종속성 그래프를 빌드함
* `Module`
  * 파일을 여러 개로 분리하여 관리 => 분리된 파일 각각이 모듈
    * 즉, js 파일 하나가 하나의 모듈
  * 대게 기능 단위로 분리
  * 클래스 하나 or 특정한 목적을 가진 복수의 함수로 구성된 라이브러리 하나로 구성
  * 의존성 문제 
    * 모듈의 수가 많아지고 라이브러리/모듈 간 의존성이 깊어짐
    * 어떤 모듈 간의 문제인지 파악 어려움
    * `Webpack은 모듈 간의 의존성 문제를 해결하기 위함`
* `Bundler`
  * 모듈 의존성 문제를 해결해주는 작업 : Bundlig
  * 도구 : Bundler (종류 중 하나 : Webpack)
  * 모듈들을 하나로 묶어주고 묶인 파일은 하나(혹은 여러 개)로 만들어짐
  * Bundling된 결과물은 개별 모듈의 실행 순서에 영향을 받지 않고 동작
  * Vue CLI는 이런 Babel, Webpack에 대한 초기 설정이 자동으로 됨
* package.json
  * 프로젝트의 종속성 목록과 지원된는 브라우저에 대한 구성 옵션을 포함
* package-lock.json
  * node_modules에 설치되는 모듈과 관련된 모든 의존성을 설정, 관리
  * 협업 및 배포 환경에서 정확히 동일한 종속성을 설치하도록 보장하는 표현
  * 사용할 패키지 버전 고정
  * 개발 과정 간 의존성 패키지 충돌 방지
  * python의 requirements.txt 역할

* public/index.html
  * Vue 앱의 뼈대가 되는 html 파일
  * Vue 앱과 연결된 요소가 있음
* src
  * src/assets : 정적 파일을 저장하는 디렉토리
  * src/components : 하위 컴포넌트들이 위치
  * src/App.vue : 최상위 컴포넌트
    * public/index.html과 연결


# SFC
* Component
  * UI를 독립적이고 재사용 가능한 조각들로 나눈 것
  * CS에서는 다시 사용할 수 있는 범용성을 위해 개발된 소프트웨어 구성 요소를 의미
  * 하나의 앱을 구성할 때, 중첩된 컴포넌트들의 tree로 구성하는 것이 보편적
    * Vue에서는 src/App.vue를 root node로 하는 tree의 구조
  * 유지보수 쉬움 / 재사용 기능
* Component based architecture 특징
  * 관리가 용이 => 유지/보수 비용 감소
  * 재사용성
  * 확장 가능
  * 캡슐화
  * 독립적
* Component in Vue
  * 이름이 있는 재사용 가능한 Vue instance => component
  * Vue instance => new Vue()로 만든 인스턴스
* SFC (Single File Component)
  * 하나의 .vue 파일이 하나의 Vue instance이고, 하나의 컴포넌트임
  * Vue instance에서는 HTML, CSS, JS 코드를 한번에 관리
  * 컴포넌트 기반 개발의 핵심 기능

## Vue component
* 템플릿(HTML) : HTML의 body
* 스크립트(JS) : vue인스턴스를 구성하는 대부분 작성
* 스타일(CSS) : 컴포넌트의 스타일
* 컴포넌트들이 tree 구조로 하나의 페이지를 만듦
* root component => `App.vue`
* App.vue를 index.html과 연결
* index.html 파일 하나만을 rendering => 이게 SPA

## 실습
* `컴포넌트 생성 3단계`
  1. src/components/ 안에 컴포넌트 생성
  2. script에 name 등록 
  3. templates에 요소 추가
     * 비어 있으면 안됨 => 해당 요소 안에 추가 요소 작성 필요

* `component 등록 3단계`
  1. 불러오기 (script)
    * import {instance name} from {위치}
      * instance name : 인스턴스 생성 시 작성한 이름
    * import Mycomponent from './components/MyComponent.vue'
    * @ : scr 절대경로 / .vue 생략 가능
    * import Mycomponent from '@/components/MyComponent'
  2. 등록하기 (script)
    * expert default 안의 components 내에 작성
  3. 보여주기 (template)
    * <MyComponent/>


# Pass Props & Emit Events
## Data in components
* 한 페이지 내에서 같은 데이터를 공유 해야 함 
* 하지만 페이지들은 component로 구분 되어있음
* 부모-자식 관계만 데이터 주고받도록 함
  * 데이터 흐름 파악 용이
  * 유지 보수 쉬워짐
  * 부모 => 자식 : pass `props` 방식
  * 자식 => 부모 : `emit` event 방식

## `Pass Props`
  * 부모 => 자식으로의 데이터 전달 방식
  * 자식 컴포넌트는 props 옵션을 사용해 수신하는 props를 명시적으로 선언해야 함
  * 요소에 속성을 작성하듯 사용 가능 
    * `prop-data-name="value"` 
    * 주의주의 
      * 보내는 쪽은 html의 요소기 때문에 대소문자 구분 X => `kebab-case`
      * 받는 쪽은 script의 요소기 때문에 => `camelCase`
      * 받는 쪽은 props를 type과 함께 명시

  * Dynamic props
    * 변수를 props로 전달
    * v-bind directive를 사용해 데이터를 동적으로 바인딩
    * `:my-props="dynamicProps"`
      * 앞의 key값이라는 이름으로 뒤의 " "안에 오는 데이터를 전달하겠다는 뜻
      * 자식 컴포넌트에서 myProps로 데이터를 받아야 함
    * <SomeComponent num-props="1"/> 
      * static props => string으로써의 1을 전달
    * <SomeComponent :num-props="1"/>
      * dynamic props => 숫자로써의 1을 전달

  * 단방향 데이터 흐름
    * 부모 속성이 업데이트되면 자식으로 흐르지만 반대는 X
    * 하위 컴포넌트가 실수로 상위 컴포넌트 상태를 변경해 앱의 데이터 흐름을 이해하기 힘들게 만드는 것을 방지


## `Emit Event`
* 부모 컴포넌트에서 자식 컴포넌트로 데이터를 전달할 때는 이벤트를 발생시킴
  * 데이터를 이벤트 리스너의 콜백함수의 인자로 전달
  * 상위 컴포넌트는 해당 이벤트를 통해 데이터를 받음
* $emit
  * $emit 메서드를 통해 부모 컴포넌트에 이벤트를 발생
  * `$emit('event-name')`
1. 자식 컴포넌트에 있는 버튼 클릭 이벤트를 청취해 연결된 핸들러 함수(ChildToParent) 호출
2. 호출된 함수에서 $emit을 통해 상위 컴포넌트에 이벤트(child-to-parent) 발생 & 이벤트에 데이터(child data)를 함께 전달
3. 상위 컴포넌트는 자식 컴포넌트가 발생시킨 이벤트(child-to-parent)를 청취해 연결된 핸들러 함수(parentGetEvent) 호출 & 함수의 인자로 전달된 데이터(child data)가 포함되어 있음
4. 호출된 함수에서 csl 실행

* pass props와 마찬가지로 동적인 데이터도 전달 가능