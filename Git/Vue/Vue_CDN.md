# Vue intro

## Front-end Development
* Back-end 개발 : Django
* Front-end 개발 : Javascript
  * Vue.js === JavaScript Front-end Framework

* `SSR` (Server Side Rendering) : 기존의 요청 처리 방식
  * 서버가 사용자의 요청에 적합한 HTML을 렌더링하여 제공하는 방식
  * 전달 받은 새 문서를 보여주기 위해 브라우저는 새로고침을 진행

* SPA (Single Page Application) : 서버에서 최초 1장의 HTML만 전달받아 모든 요청에 CRS 방식으로 요청을 처리
  * `CRS` (Client Side Rendering)
    * 각 요청에 대한 대응을 JS를 사용하여 필요한 부분만 다시 렌더링
    * 1. 새로운 페이지를 서버에 AJAX로 요청
    * 서버는 화면을 그리기 위해 필요한 데이터를 JSON 방식으로 전달
    * JSON 데이터를 JS로 처리, DOM 트리에 렌더링
  * CRS 방식을 사용하는 이유
    * 1. 모든 HTML 페이지를 서버로부터 받는 것이 아니기 때문에
      * 클라이언트 - 서버간 통신 즉, 트래픽이 감소
      * 트래픽이 감소한다 => 응답 속도가 빨라진다.
    * 2. 매번 새 문서를 받아 새로고침하는 것이 아니라 필요한 부분만 고쳐 나가므로 각 요청이 끊김없이 진행
    * 3. BE와 FE의 작업 영역을 명확히 분리 할 수 있음
      * 협업이 용이해짐
    * 단점 
      * 첫 구동 시 필요한 데이터가 많을수록 최초 작동 시작까지 오랜 시간이 소요
      * 모바일에 설치된 Web-App을 실행 하게 되면 잠깐의 로딩 시간이 필요
      * `검색 엔진 최적화` (SEO)가 어려움
        * 서버가 제공하는 것은 빈 HTML
        * 내용을 채우는 것은 AJAX 요청으로 얻은 JSON 데이터로 클라이언트가 진행
        * SEO (Search Engine Optimization)
          * 서비스나 제품 등이 효율적으로 검색 엔진에 노출되도록 개선하는 과정을 일컫는 작업
          * 검색 : 각 사이트가 운용하는 검색 엔진에 의해 이뤄지는 작업
          * 검색 엔진 : 웹 상에 존재하는 가능한 모든 정보들을 긁어 모으는 방식으로 동작
      * 대체적으로 HTML에 작성된 내용을 기반으로 하는 검색 엔진에 빈 HTML을 공유하는 SPA 서비스가 노출되기는 어려움

* CSR VS SSR
  * 서비스에 적합한 렌더링 방식을 적절히 활용
  * SPA 서비스에서도 SSR을 지원하는 프레임워크도 발전 중

# Why Vue
* 입문자가 시작하기 좋은 프레임워크
* 가볍고 간편하게 사용할 수 있는 프레임워크
* 구조가 직관적
* FE 프레임워크를 빠르고 쉽게 학습하고 활용 가능

* 헷갈리지 말 것
  * Django == Python Web Framework
    * pip install
  * Vue === JS Front-end Framework
    * CDN 방식

* Vue로 코드 작성
``` javascript
// 1. Vue CDN 가져오기
// 2. Vue instance 생성
const app = new Vue({
    // 3. el, data 설정
    // 4. 선언적 렌더링 : {{ }}
    el: '#app',
    data: {
        message: 'Hello, Vue!',
    },
    methods: {
        print: function() {
            console.log(this.message)
        },
        bye: function() {
            this.message = 'Bye, Vue!'
        },
    }
})
```
```html
<!--  4. input tag에 v-model 작성 -->
<input type='text' v-model='message'>
```
* `생성자 함수`
  * 함수 이름은 반드시 대문자로 시작
  * new 연산자 사용
* `el` 
  * Vue instance와 DOM을 연결하는 옵션
    * View와 Model을 연결하는 역할
    * HTML id or class와 연결 가능
  * Vue instance와 연결되지 않은 DOM 외부는 Vue 영향을 받지 않음
* `data`
  * Vue instance의 데이터 객체 or 인스턴스 속성
  * 데이터 객체는 반드시 기본 객체 {} 여야 함
  * 객체 내부의 아이템들은 value로 모든 타입의 객체를 가질 수 있음
  * 정의된 속성은 interpolation {{}}을 통해 view에 렌더링 가능
* `methods`
  * Vue instance의 method를 정의
  * 객체 내 print method 정의
    * print method 실행 시 Vue instance의 data내 message 출력
    * ex) 콘솔창에서 app.print() 실행 => Hello, Vue!
  * method를 호출하여 data 변경 가능
    * 객체 내 bye method 정의 => print method 실행 시 Vue instance의 data내 message 변경
    * ex) 콘솔창에서 app.bye() 실행 => Bye, Vue!
  * `메서드 정의 시, Arrow Function 사용 금지`
    * Arrow Function에서 this는 window (상위 객체)를 가리킴
    * this로 Vue의 data를 변경하지 못함


# Vue instance
* MVVM Pattern
  * 소프트웨어 아키텍처 패턴의 일종
  * 마크업 언어로 구현하는 그래픽 사용자 인터페이스(`view`)의 개발을 Back-end(`model`)로부터 분리시켜 view가 어느 특정한 모델 플랫폼에 종속되지 않도록 함
  * view : 우리 눈에 보이는 부분 => DOM
  * Model : 실제 데이터 => JSON
  * View Model : Vue
    * View를 위한 모델
    * View와 연결되어 Action을 주고 받음
    * 모델이 변경되면 View Model도 변경되고 바인딩된 View도 변경됨
    * View에서 사용자가 데이터를 변경하면 View Model의 데이터가 변경되고 바인딩된 다른 View도 변경됨

# Basic of syntax
* Template Syntax
  * 렌더링 된 DOM을 기본 Vue instance의 data에 선언적으로 바인딩할 수 있는 HTML 기반 template syntax를 사용

* Template Interpolation
  * HTML을 일반 텍스트로 표현
  * `v-html` directive을 사용해 data와 바인딩
``` html
<!-- <div id='app'>
    <p>메시지: {{ msg }}</p>
    <p>HTML 메시지: {{ rawHTML }}</p>
</div> -->

<div id='app'>
    <p>HTML 메시지: <span v-html='rawHTML'></span>
    </p>
</div>

<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
<script>
    const app = new Vue({
        el: '#app',
        data: {
            msg: 'Text interpolation',
            rawHTML: '<span style='color:red'> 빨간 글씨 </span>'
        }
    })
</script>
```


# Directives
* 기본 구성
  * v-접두사가 있는 특수 속성에는 값을 할당 할 수 있음
  * 값에는 JS 표현식을 작성 할 수 있음
  * directive 역할 : 표현식의 값이 변경될 때 반응적으로 DOM에 적용하는 것
  * v-on:submit.prevent="onSubmit"
    * `:` : 전달인자 받을 수 있음
    * `.` : directive를 특별한 방법으로 바인딩 해야 함
## `v-text`
* 가장 기본적인 바인딩 방법
* {{ }} 와 같은 역할 (정확히 동일한 것은 아님)
```html
<div id='app'>
    <p v-text='message'></p>
    <p>{{ message }}</p>
</div>

<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
<script>
    const app = new Vue({
        el: '#app',
        data: {
            message: 'Hello'
        }
    })
</script>
```

## `v-html`
* RAW HTML을 표현할 수 있는 방법
* 단 사용자가 입력하거나 제공하는 컨텐츠에는 절대 사용 금지
```html
<div id='app'>
    <p v-html='html'></p>
</div>

<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
<script>
    const app = new Vue({
        el: '#app',
        data: {
            html: '<a href="https://www.google.com">GOOGLE</a>'
        }
    })
</script>
```

## `v-show`
* 표현식에 작성된 값에 따라 element를 보여 줄 것인지 결정
* boolea 값이 변경 될 때 마다 반응
* 대상 element의 display 속성을 기본 속성과 none으로 toggle
* 화면에서만 사라졌다 보였다 하는 것일 뿐, DOM에는 항상 존재
* `표현식 결과와 관계 없이 렌더링 되므로 초기 렌더링에 필요한 비용은 v-if 보다 높을 수 있지만, display 속성 변경으로 표현 여부를 판단하므로 렌더링 후 toggle 비용은 적다`
```html
<div id='app'>
    <p v-show='isActive'>보임? 안보임?</p>
</div>

<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
<script>
    const app = new Vue({
        el: '#app',
        data: {
            isActive: false
        }
    })
</script>
```

## `v-if`
* v-show와 사용 방법은 동일
* isActive 값이 변경 될 때 반응
* 단, 값이 false인 경우 `DOM에서 사라짐`
* `표현식 결과가 false인 경우, 렌더링조차 되지 않으므로 초기 렌더링 비용은 v-show보다 낮을 수 있지만 표현식 값이 자주 변경되는 경우 잦은 재 렌더링으로 비용이 증가할 수 있음`
```html
<div id='app'>
    <p v-if='isActive'>보임? 안보임?</p>
</div>

<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
<script>
    const app = new Vue({
        el: '#app',
        data: {
            isActive: false
        }
    })
</script>
```

## `v-for`
* 반복한 데이터 타입에 모두 사용 가능
  * 문자열, 배열 ..
* index를 함께 출력 => (char, index) 형태로 사용 가능
* 각 요소가 객체라면 `dot notation`으로 접근 가능
* v-for 사용 시 반드시 `key 속성을 각 요소에 작성`
  * vue 화면 구성 시 이전과 달라진 점을 확인 하는 용도로 활용
  * 따라서 key가 중복되면 안됨
  * 각 요소가 고유한 값을 가지고 있지 않다면 생략 가능
```html
<h2>Array</h2>
<div v-for="(item, index) in myArr"
    :key="`arry-${index}`">
    <p>{{ index }}번째 아이템</p>
    <p>{{ item.name }}</p>
</div>

<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
<script>
    const app = new Vue({
        data: {
            myArr: [
                { id: 1, name: 'python'},
                { id: 2, name: 'django'},
                { id: 3, name: 'javascript'},
            ]
        }
    })
</script>
```

## `v-on`
* `:` 을 통해 전달받은 인자를 확인
* 값으로 JS 표현식 작성
* addEventListener의 첫 번째 인자와 동일한 값들로 구성
* 대기하고 있던 이벤트가 발생하면 할당된 표현식 실행
* method를 통한 data 조작도 가능
  * ex) v-on:keyup.enter
  * shortcut 제공 `@` : @keyup.click
```html
<div id='app'>
    <button v-on:click='number++'>
        increase Number
    </button>
    <p>{{ number }}</p>
</div>

<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
<script>
    const app = new Vue({
        el: '#app',
        data: {
            number: 0,
        }
    })
</script>
```

## `v-bind`
* HTML 기본 속성에 Vue data를 연결
* class의 경우 다양한 형태로 연결 가능
  * `조건부 바인딩`
    * {'class Name': '조건 표현식'}
    * 삼항 연산자도 가능
  * `다중 바인딩`
    * ['JS 표현식', 'JS 표현식', ..]
* Vue data의 변환에 반응하여 DOM에 반영하므로 상황에 따라 유동적 할당 가능
* shortcut 제공 `:` : :class
```html
<div id='app'>
    <a v-bind:href="url">Go To GOOGLE</a>
</div>

<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
<script>
    const app = new Vue({
        el: '#app',
        data: {
            url: 'https://www.google.com/',
        },
    })
</script>
```

## `v-model`
* Vue instance와 DOM의 `양방향 바인딩`
* Vue data 변경 시 v-model로 연결된 사용자 입력 element에도 적용
```html
<div id='app'>
    <h3>{{ myMessage }}</h3>
    <input v-model="myMessage" type="text">
    <hr>
</div>

<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
<script>
    const app = new Vue({
        el: '#app',
        data: {
            maMessage: '',
        },
    })
</script>
```


# Vue advanced
## computed
* Vue instance가 가진 옵션 중 하나
* computed 객체에 정의한 함수를 페이지가 최초로 렌더링 될 때 호출해 계산
* 계산 결과가 변하기 전까지 함수를 재호출하는 게 아니라 값을 반환
* computed VS method
  * method 
    * 호출 될 때마다 함수를 실행
    * 같은 결과여도 매번 새로 계산
  * computed
    * 함수의 종속 대상의 변화에 따라 계산 여부가 결정됨
    * 종속 대상이 변하지 않으면 항상 저장된 값을 반환

## watch
* 특정 데이터의 변화를 감지하는 기능
  *1. watch 객체를 정의
  *2. 감시할 대상 data를 지정
  *3. data가 변할 시 실행 할 함수를 정의
* 첫 번째 인자는 변동 전 data, 두 번째 인자는 변동 후 data
* 실행 함수를 Vue method로 대체 가능
  * 1. 감시 대상 data의 이름으로 객체 생성
  * 2. 실행하고자 하는 method를 handler에 문자열 형태로 할당
  * Array, Object의 내부 요소 변경을 감지하기 위해서는 `deep` 속성 추가 필요
```html
<button @click='number++'></button>

<script src="https://cdn.jsdelivr.net/npm/vue@2/dist/vue.js"></script>
<script>
    const app = new Vue({
        data: {
            number: 0,
        },
        watch: {
            number: function(val, oldval) {
                console.log(val, oldval)
            },
        }
    })
</script>
```

## filters
* 텍스트 형식화를 적용할 수 있는 필터
* interpolation 혹은 v-bind를 이용할 때 사용 가능
* 필터는 JS 표현식 마지막에 `|`(파이프)와 함께 추가되어야 함