# Vuex
## State Management
* 상태 (현재에 대한 정보) : 현재 app이 가지고 있는 data로 표현
* 각 컴포넌트는 독립적 => 각각의 상태(data)를 가짐 => 컴포넌트들이 모여서 하나의 app을 구성
* 여러 개의 컴포넌트가 같은 상태를 유지할 필요가 있음 => 상태 관리 필요
* Centralized Store 
  * `중앙 저장소(store)에 데이터를 모아서 상태 관리`
  * 컴포넌트의 계층에 상관없이 중앙 저장소에 접근해서 데이터를 얻거나 변경할 수 있음
  * 중앙 저장소의 데이터가 변경되면 각각의 컴포넌트는 해당 데이터의 변화에 반응해 새로 변경된 데이터를 반영
* Vuex
  * state management pattern + Library
  * 중앙 저장소를 통해 상태 관리를 할 수 있도록 하는 라이브러리
  * 데이터가 예측 가능한 방식으로만 변경 될 수 있도록 하는 규칙을 설정
  * Vue의 반응성을 효율적으로 사용하는 상태 관리 기능을 제공

## Vuex 시작
```
vue create vuex-app   Vue 프로젝트 생성
cd vues-app           디렉토리 이동
vue add vuex          Vue CLI를 통해 vuex plugin 적용
```

```javascript
// Vue 인스턴스
export default {
    name: 'VueInstance',
    data: function() {
        return{

        }
    },
    computed: {

    },
    methods: {

    },
}


// Vuex 인스턴스
export default new Vuex.Store({
    state: {

    },
    getters: {

    },
    mutations: {

    },
    actions: {

    },
    modules: {

    }
})

```
* src / store / index.js 생성
* vuex 핵심 컨셉 
  * state
    * vue 인스턴스의 data에 해당
    * `중앙에서 관리하는 모든 상태 정보`
    * 개별 컴포넌트는 state에서 데이터를 가져와서 사용
    * state 데이터가 변화하면 해당 데이터를 공유하는 컴포넌트도 자동으로 다시 렌더링
    * `$store.state`로 state 데이터에 접근
  * getters
    * vue 인스턴스의 computed에 해당
    * state를 활용해 `계산한 새로운 변수 값`
    * `state를 활용해 계산된 값을 얻고자 할 때 사용`
    * getters 의 결과는 캐시(cache)되며, 종속된 값이 변경된 경우에만 재계산
    * 계산된 값은 state에 영향 x
    * 첫번째 인자로 state, 두번째 인자로 getters
  * mutations
    * `실제로 state를 변경하는 유일한 방법`
    * vue 인스턴스의 methods에 해당하지만, 호출되는 핸들러 함수는 반드시 `동기적`이어야 함
    * 첫 번째 인자로 state, 두번째 인자로 payload를 받으며 컴포넌트 or actions에서 `commit()` 메서드로 호출됨
  * actions
    * mutations와 비슷하지만 `비동기` 작업을 포함할 수 있음
    * `state를 직접 변경하지 않고 commit() 메서드로 mutations를 호출해서 변경`
    * commit(A, B) : A(호출하고자 하는 mutations 함수), B(payload)
    * context 객체를 인자로 받으며, 이 객체를 통해 store.js의 모든 요소와 메서드에 접근 가능
    * 첫번째 인자 context, 두번째 인자 payload
    * component에서 `dispatch()` 메서드에 의해 호출
    * dispatch(A, B) : A(호출하고자 하는 actions 함수), B(넘겨주는 데이터 payLoad)

* component에서 데이터 조작 : component => (actions) => mutations => state
* component에서 데이터 사용 : state => (getters) => component

# Lifecycle Hooks
* 각 Vue 인스턴스는 생성과 소멸의 과정 중 단계별 초기화 과정을 거침
* 각 단계가 트리거가 되어 특정 로직 실행 가능 => Lifecycle Hooks
* 특징 
  * 컴포넌트별로 정의 가능
  * 부착 여부가 부모-자식 관계에 따라 순서를 가지고 있지 않음 => `instance마다 각각의 lifecycle을 가지고 있음`

* created   
  * vue instance가 생성된 후 호출
  * data, computed 등 설정이 완료된 상태
  * 서버에서 받는 데이터를 vue instance의 data에 할당하는 로직을 구현하기 적합
  * mount되지 않아 요소에 접근할 수 없음 => HTML과 DOM 연결 X
* mounted
  * vue instance가 요소에 mount된 후 호출
  * mount된 요소 조작 가능
* updated
  * 데이터가 변경되어 DOM에 변화를 줄 때 호출


# Local Storage
* 브라우저에서 제공하는 저장공간 중 하나
* 브라우저의 Local Storage에 데이터를 저장해서 브라우저를 종료하고 다시 실행해도 데이터가 보존될 수 있도록 함
* Window.localStorage
  * 만료되지 않고 브라우저를 종료하고 다시 실행해도 데이터가 보존됨
  * 데이터가 문자열 형태로 저장됨
  * 관련 메서드
    * `setItem(key, value)` : key, value 형태로 데이터 저장
    * `getItem(key)` : key에 해당하는 데이터 조회
* 데이터가 문자열 형태로 저장되어야 하기 때문에 `JSON.stringify`로 변환 필요
* state 변경 작업이 아니므로 actions에 작성
* 생성, 수정, 삭제시 saveTodosToLocalStorage action 메서드가 실행 되도록 함

* vuex-persistedstate
  * vuex state를 자동으로 브라우저의 Local Storage에 저장해주는 라이브러리
  * 페이지가 새로고침 되어도 vuex state를 유지시킴
  * local storage에 저장된 data를 자동으로 state로 불러옴
  * 설치 : npm i vuex-persistedstate
  * 적용
    ``` js
    // index.js
    import createPersistedState from 'vuex-persistedstate'

    export default new Vuex.Store({
        plugins: [
            createPersistedState(),
        ],
    })
    ```

* vuex 사용
  * Vuex는 공유된 상태 관리를 처리하는 데 유용하지만, 개념에 대한 이해와 시작하는 비용이 큼
  * app이 단순하다면 vuex가 없는 것이 더 효율적일 수 있음
  * 그러나 중대형 규모의 SPA를 구축하는 경우 Vuex는 자연스럽게 선택할 수 있는 단계가 오게 됨
  * 결과적으로 역할에 적절한 상황에서 활용 했을 때, Vuex 라이브러리 효용을 극대화 할 수 있음 => 필요한 순간이 왔을 때 사용하는 것을 권장