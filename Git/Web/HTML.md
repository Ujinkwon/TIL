# Web이란?
* 웹 사이트 : 브라우저를 통해 접속하는 웹 페이지(문서)들의 모음
* 링크를 통해 여러 웹 페이지를 연결한 것을 웹 사이트라고 함
* HTML => 구조
* CSS => 표현
* Javascript => 동작
* 웹사이트는 브라우저를 통해 동작
* 브라우저마다 동작이 약간씩 달라 생기는 문제를 해결하기 위해 웹 표준이 등장
* 웹 표준을 만드는 곳은 W3C, WHATWG
* 웹 표준 : 웹에서 표준적으로 사용되는 기술이나 규칙
  
# HTML (Hyper Text Markup Language)
* Hyper Text : 참조(하이퍼링크)를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트
* Markup Language : 태그 등을 이용해 문서나 데이터의 구조를 명시하는 언어
* HTML : 웹 페이지를 작성(구조화)하기 위한 언어
* 기본 구조
  * html : 문서의 최상위 요소
  * head : 문서 메타데이터 요소
    * 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등
    * 일반적으로 브라우저에 나타나지 않는 내용
    * <title> : 브라우저 상단 타이틀
    * <meta> : 문서 레벨 메타데이터 요소
    * <link> : 외부 리소스 연결 요소
    * <script> : 스크립트 요소 
    * <style> : CSS 직접 작성
  * body : 문서 본문 요소
    * 실제 화면 구성과 관련된 내용
* 요소
  * 태그로 내용을 감싸는 것으로 그 정보의 성격과 의미를 정의
  * 내용이 없는 태그들도 존재(닫는 태그가 없음)
    * br, hr, img, input, link, meta
  * 요소는 중첩될 수 있음
    * 요소의 중첩을 통해 하나의 문서를 구조화
    * 여는 태그 닫는 태그 쌍 잘 확인
* 속성
  * <a href="https://google.com"></a>
  * href 는 속성명, 뒤의 값은 속성값
  * 공백 X, 쌍따옴표 사용
  * 태그의 부가적인 정보(경로, 크기) 설정
  * 태그랑 상관업이 사용 가능한 속성들도 있음(HTML Global Attribute)
    * id : 문서 전체에서 유일한 고유 식별자 지정
    * class : 공백으로 구분된 해당 요소의 클래스의 목록
    * data-* : 페이지에 개인 사용자 정의 데이터 저장
    * style : inline 스타일
    * title : 요소에 대한 추가 정보 지정
    * tabindex : 요소의 탭 순서
* 시맨틱 태그
  * HTML 태그가 특정 목적, 역할 및 의미적 가치를 가지는 것
  * Non semantic 요소로는 div, span, a, form, table 등이 있음
  * header : 문서 전체나 섹션의 헤더
  * nav : 내비게이션
  * aside : 사이드에 위치한 공간, 메인 콘텐츠와 관련성이 적은 콘텐츠
  * section : 문서의 일반적인 구분, 컨텐츠의 그룹을 표현
  * article : 문서, 페이지, 사이트 안에서 독립적으로 구분되는 영역
  * footer : 문서 전체나 섹션의 마지막 부분
  * 사용해야 하는 이유 : 의미론적 마크업  
    * 의미 있는 정보의 그룹을 태그로 표현
    * 가독성 높이고 유지보수 쉬움
    * 검색 엔진 최적화
  * 렌더링 (Rendering) : 웹사이트 코드를 사용자가 보게 되는 웹 사이트로 바꾸는 과정 
  * DOM (Document Object Model) 트리 : 텍스트 파일인 HTML 문서를 브라우저에서 렌더링 하기 위한 구조
    * HTML 문서에 대한 모델 구성
    * HTML 문서 내의 각 요소에 접근 / 수정에 필요한 프로퍼티와 메서드를 제공

# HTML 문서 구조화
* 인라인 요소는 글자 취급 / 블록 요소는 한 줄 모두 사용
* 텍스트 요소
  * <a></a> : href 속성을 활용하여 다른 URL로 연결하는 하이퍼링크 생성
  * <b></b> / <strong></strong> : 굵은 글씨 요소 / 중요한 강조
  * <i></i> / <em></em> : 기울임 글씨 요소 / 중요한 강조
  * <br> : 텍스트 내에 줄 바꿈 생성
  * <img> : src 속성을 활용해 이미지 표현
  * <span></span> : 의미 없는 인라인 컨테이너

* 그룹 컨텐츠
  * <p></p> : 하나의 문단
  * <hr> : 문단 레벨 요소에서의 주제의 분리 (수평선으로 표현)
  * <ol></ol> : 순서가 있는 리스트
  * <ul></ul> : 순서가 없는 리스트
  * <pre></pre> : HTML에 작성한 내용을 그대로 표현
  * <blockquote></blockquote> : 텍스트가 긴 인용문 (주로 들여쓰기를 한 것으로 표현 됨)
  * <div></div> : 의미 없는 블록 레벨 컨테이너

* form 태그
  * 정보를 서버에 제출하기 위해 사용하는 태그
  * 기본 속성
    * action : form을 처리할 서버의 URL (데이터를 보낼 곳)
    * method : form을 제출할 때 사용할 HTTP 메서드 (GET or POST)
    * enctype : method가 post인 경우 데이터의 유형
* input 태그
  * 다양한 타입을 가지는 입력 데이터 유형과 위젯 제공
  * 대표 속성
    * name : form control에 적용되는 이름 (이름/값 페어로 전송)
    * value : form control에 적용되는 값 (이름/값 페어로 전송)
    * required, readonly, autofocus, autocomplete, disabled 등
  * input label
    * label을 클릭해 input 자체의 초점을 맞추거나 활성화 시킬 수 있음
    * 사용자는 선택할 수 있는 영역이 늘어나 웹 / 모바일 환경에서 편하게 사용 가능
    * 화면리더기에서도 label을 읽어 쉽게 내용을 확인 할 수 있도록 함
    * <input>에 id 속성을, <label>에는 for 속성을 활용해 상호 연관을 시킴
  ```html
  <label for="agreement">개인정보 수집에 동의합니다.</label>
  <input type="checkbox" name="agreement" id="agreement">
  ```

  * input 유형 - `일반`
    * text : 일반 텍스트 입력
    * password : 입력 시 값이 보이지 않고 문자를 특수기호(*)로 표현
    * email : 이메일 형식이 아닌 경우 form 제출 불가
    * number : min, max, step 속성을 활용해 숫자 범위 설정 가능
    * file : accept 속성을 활용해 파일 타입 지정 가능
  * input 유형 - `항목 중 선택`
    * 일반적으로 label 태그와 함께 사용해 선택 항목을 작성함
    * 동일 항목에 대해서는 name을 지정하고 선택된 항목에 대한 value를 지정해야 함
      * checkbox : 다중 선택
      * radio button : 단일 선택
  * input 유형 - `기타`
    * color : color picker
    * date : date picker
    * hidden : 사용자에게 보이지 않는 input