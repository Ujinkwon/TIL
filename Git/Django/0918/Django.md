# Framework    
   * 서비스 개발에 필요한 기능들을 미리 구현해서 모아 놓은 것
   * 특정 프로그램을 개발하기 위한 여러 도구들과 규약을 제공하는 것
   * 소프트웨어의 생산성과 품질을 높임

# Django
* 파이썬으로 작성된 프레임워크
* 여러 유용한 기능들
* 검증된 웹 프레임워크
* 클라이언트 : 서비스를 요청하는 주체
* 서버 : 요청에 대해 서비스를 응답하는 주체
  * django는 서버를 구현하는 웹 프레임워크
* 웹 브라우저 : 웹 페이지 파일을 `렌더링` 하는 프로그램
* 웹 페이지 : 우리가 보는 화면 각각 한 장 한 장
  * 정적 웹 페이지  
    * 있는 그대로를 제공하는 것
    * 작성된 html 파일의 내용이 변하지 않고 모든 사용자에게 동일한 모습으로 전달되는 것
  * 동적 웹 페이지
    * 사용자의 요청에 따라 웹 페이지에 추가적인 수정이 되어 클라이언트에게 전달되는 웹 페이지
    * 웹 페이지의 내용을 바꿔주는 주체 : 서버

* www (World Wide Web) : 전 세계에 퍼져 있는 거미줄 같은 연결망
* 유선 연결의 한계 
  * 히말라야 정상이나 밀림까지 케이블 까는 것은 어려움
  * 개발 도상국 같은 나라에서는 충분한 인프라 기대 어려움
* 무선 연결 
  * 스타링크 프로젝트 : 지구를 많은 소형 위성으로 감싸서, 위성끼리 데이터를 교환
  * 문제점 : Starlink Train, 우주 쓰레기
* 결국, 우리가 인터넷을 이용한다는 것은 전세계의 컴퓨터가 연결되어 있는 하나의 인프라를 이용하는 것

# MTV Design Pattern
* Design Pattern
  * 자주 사용되는 구조를 일반화해서 하나의 공법으로 만들어 둔 것
* 소프트웨어 디자인 패턴
  * 다수의 엔지니어들이 일반화된 패턴으로 소프트웨어 개발을 할 수 있도록 한 규칙
  * `복잡한 커뮤니케이션이 간단해짐`
* MVC
  * Model : 데이터와 관련된 로직 관리
  * View : 레이아웃과 화면을 처리
  * Controller : 명령을 model과 view 부분으로 연결
  * 독립적 개발 가능
  * 개발 효율성, 유지보수 쉬워짐
  * 다수의 멤버로 개발하기 용이해짐
* `MTV`
  * Model 
    * 데이터와 관련된 로직 처리
    * 응용프로그램의 데이터 구조를 정의, DB의 기록 관리
  * Template 
    * 레이아웃과 화면을 처리
    * 화면상의 사용자 인터페이스 구조와 레이아웃 정의
  * View 
    * 명령을 model과 template 부분으로 연결
    * 클라이언트의 요청에 대해 처리를 분기하는 역할

# Django 기본 설정
* 설치 전 가상환경 설정, 활성화 마치고 진행
* 4.0 릴리즈로 인해 3.2(LTS) 버전을 명시해서 설치
  * LTS (Long Term Support) : 장기적, 안정적 지원 보장

## Project
* 생성 명령어 : `django-admin startproject 프로젝트이름`
* project 이름에는 python이나 django에서 사용 중인 키웓, 하이픈(-) 사용 불가
* 프로젝트 구조
  * __init__.py : 이 디렉토리를 하나의 python 패키지로 다루도록 지시
  * asgi.py (Asynchronous Server Gateway Interface) : 배포 시 사용
  * settings.py : django 프로젝트 설정 관리
  * urls.py : 사이트의 url과 적절한 views의 연결 지정
  * manage.py : 프로젝트와 다양한 방법으로 상호작용하는 커맨드라인 유틸리티
  * 배포 시 사용
    * wsgi.py (Web Server Gateway Interface) : 앱이 웹서버와 연결, 소통하는 것을 도움
    * asgi.py (Asynchronous Server Gateway Interface) : 앱이 비동기식 웹서버와 연결, 소통하는 것을 도움

## Application
* 생성 명령어 : `python manage.py startapp 앱이름`
* app 이름은 `복수형`으로 작성하는 것을 권장
* 프로젝트에서 앱 사용하기 위해서 settings.py의 `INSTALLED_APPS` 리스트에 앱 이름을 반드시 추가 (`반드시 생성 후 등록`)
* 애플리케이션 구조
  * admin.py : 관리자용 페이지 설정
  * apps.py : 앱의 정보가 작성된 곳 (추가 코드 작성 X)
  * models.py : 애플리케이션에서 사용하는 model을 정의하는 곳
  * views.py : view 함수들이 정의 되는 곳
  * tests.py : 프로젝트의 테스트 코드 작성하는 곳

# 요청과 응답
* `URL => VIEW => TEMPLATE (데이터 흐름)`
* View
  * http 요청을 수신하고 응답을 반환하는 함수 작성
  * template에게 응답 서식을 맡김
  * render() : 템플릿을 컨텍스트 데이터와 결합하고 렌더링 된 텍스트와 응답 객체를 반환하는 함수
* Templates 
  * app 폴더 안의 templates 폴더
  * 템플릿 폴더 이름은 반드시 `templates`
* 참고 (settings.py)
  * `LANGUAGE_CODE` 
    * 번역 언어 결정
    * `USE_I18N` 이 활성화 되어 있어야 적용
  * `TIME_ZONE`
    * DB 연결의 시간대를 나타내는 문자열 지정
    * `USE_TZ` 이 활성화 되지 않으면 에러 발생

# Template
* 데이터 표현을 제어하는 도구이자 표현에 관련된 로직
* Django Template Language (DTL)
  * Django template에서 사용하는 built-in template system
  * 조건, 반복, 변수 치환, 필터 등 기능 제공
  * `python 코드로 실행되는 것이 아님`
  * 프로그래밍적 로직이 아니라, `프레젠테이션을 표현하기 위한 것`
1. `Variable`
* {{ variable }}
* 변수명은 밑줄로 시작 X, 공백, 구두점 문자 사용 X
* dot(.)으로 변수 속성에 접근 가능
* render() 세번째 인자로 넘겨주는 딕셔너리의 key에 해당하는 문자열이 template에서 사용 가능한 변수명
2. `Filters`
* {{ variable|filter }}
* 표시할 변수를 수정할 때 사용
3. `Tags`
* {% tag %}
* 출력 텍스트를 만들거나, 반복 or 논리를 수행해 제어 흐름을 만드는 등, 복잡한 일 수행
* 일부 태그는 시작, 종료 태그 필요 ex) if, endif
4. `Comments`
* {# #} : 한 줄 주석
* {% comment %}{% endcomment %} : 여러 줄 주석
* django template에서 주석 표현하기 위해 사용

## Template inheritance
* 템플릿 상속은 `코드의 재사용성`에 초점
* {% extends '부모템플릿' %} : 자식 템플릿이 부모 템플릿을 확장한다는 것을 알림
* {% block content %}{% endblock content %} : 하위 템플릿이 채울 수 있는 공간
* 스켈레톤 템플릿을 앱안의 template이 아니라, 프로젝트의 template 내에 위치하고 싶으면, settings.py 의 `TEMPLATES의 DIRS 값에 [BASE_DIR / 'templates']` 코드 작성

`01_121` HTTP, GET

# URLs
* django 에서는 모든 주소가 '/'(trailing slash)로 끝나도록 구성 => 복수의 페이지에서 같은 콘텐츠가 존재하는 것을 방지

## `Valiable routing`
* routing : 어떤 네트워크 안에서 통신 데이터를 보낼 때 최적의 경로를 선택하는 과정
* url 일부를 변수로 지정해 view 함수의 인자로 넘길 수 있음
* 'hello/<name>/' (기본 타입은 str) or 'hello/<int:age>/'
* variable routing으로 할당된 변수를 인자로 받고 템플릿 변수로 사용 가능

## App URL mapping 
* 앱이 많아졌을 때 urls.py를 각 app에 매핑
* `각각의 app 안에 urls.py를 만들고`, 프로젝트 urls.py에서 각 앱의 urls.py 파일로 URL 매핑을 위탁
* `include되는 앱의 url.py에 urlpatterns 리스트가 작성되지 않으면 에러 발생`

## Naming URL patterns
* path()함수의 name 인자를 정의해서 사용
* DTL의 Tag 중 URL 태그를 사용해 path() 함수에 작성한 name을 사용 가능 : {% url '' %}
* view 함수와 템플릿에서 특정 주소를 쉽게 참조할 수 있도록 도움

## `DRY 원칙`
* Don't Repeat Yourself
* 소스 코드에서 동일한 코드를 반복하지 말자
* 동일 코드 반복시, 버그 증가 및 프로젝트 규모가 커질수록 애플리케이션의 유지 보수 비용이 커짐

# Django의 설계 철학 (Templates System)
* 표현과 로직(view)을 분리
* 중복을 배제
# Framework 성격
* 독선적 : 올바른 방법에 대한 분명한 규약이 있음
* 관용적 : 올바른 방법에 대한 제약이 거의 없음
## Django Framework 성격
* `다소 독선적`
* 프레임워크는 온전히 만들고자 하는 것에만 집중할 수 있게 도와주는 것

------

# Namespace
## URL namespace
* URL namespace를 사용하면 서로 다른 앱에서 동일한 url 이름을 사용하는 경우에도 이름이 지정된 url을 고유하게 사용 가능
* app_name = 'app_name'  => {% url 'app_name:url_name' %}
* url 태그에서 형식 지키지 않으면 `NoReverceMatch` 에러 발생

## Template namespace
* 여러 앱에서 템플릿 파일 이름이 겹치는 경우 필요
* Django templates의 기본 경로에 app과 같은 이름의 폴더를 생성해, 폴더 구조를 `app_name/templates/app_name/` 형태로 변경

# Database
* 체계화된 데이터 모임
* 검색, 구조화 작업을 쉽게 하기 위해 조직화된 데이터를 수집하는 저장 시스템
* Schema 스키마
  * 뼈대
  * 자료의 구조, 표현 방법, 관계 등을 정의한 구조
* Table 테이블
  * 관계
  * 필드(속성, Column) + 레코드(튜플, Row)
  * PK (Primary Key) : 각 레코드의 고유한 값
    * `다른 항목과 절대로 중복되어 나타날 수 없는 단일 값`
* Query 
  * 데이터를 조회하기 위한 명령어
  * 조건에 맞는 데이터를 추출, 조작하는 명령어
  * 'Query를 날린다' => '데이터베이스를 조작한다'

# Model
* `웹 애플리케이션의 데이터를 구조화하고 조작하기 위한 도구`
* Django는 Model을 통해서 데이터에 접속, 관리
* 일반적으로 각각 모델은 하나의 데이터베이스 테이블에 매핑
* models.py 작성
  * 모델 클래스 == `테이블 스키마`
  * 클래스 변수명 = DB 필드 이름
  * 클래스 변수값 (models 모듈의 Field 클래스) = DB 필드의 데이터 타입
  * Field 
    * CharField(max_lenght=None) : 길이 제한 있는 문자열
    * TextField : 글자 수 많을 때 사용
    * DateTimeField()
      * python의 datetime.datetime 인스턴스로 표시되는 날짜, 시간을 값으로 사용하는 필드
      * DateField를 상속받는 클래스
      * `auto_now_add` : 최초 생성 일자, Django ORM이 최초 데이터 입력 시에만 현재 날짜와 시간으로 갱신
      * `auto_now` : 최종 수정 일자, Django ORM이 저장을 할 때마다 현재 날짜와 시간으로 갱신
  * id 컬럼은 테이블 생성시 Django가 자동으로 생성
  * 각 모델은 django.models.Model 클래스의 서브 클래스로 표현
  * `클래스 상속 기반 형태의 Django 프레임워크 개발`
* `Migrations` : Django가 모델에 생긴 변화를 DB에 반영하는 방법
  * `python manage.py makemigrations` : 테이블을 만들기 위한 설계도를 생성하는 것
  * `python manage.py migrate` : 모델과 DB의 동기화
  * python manage.py showmigrations : migrations 파일들의 migrate 여부 확인 용도
  * python manage.py sqlmigrate articles 0001 : 해당 migrations 파일이 SQL 문으로 어떻게 해석 될지 미리 확인 가능

* 표준 파이썬 클래스의 메서드인 str()을 정의해 각각의 object가 사람이 읽을 수 있는 문자열을 반환하도록 할 수 있음
```python 
def __str__(self):
    return self.title
```

# ORM (Object-Relational-Mapping)
* SQL만 알아들을 수 있는 DB가 makemigrations로 만들어진, 파이썬으로 작성된 설계도를 이해하기 위해 중간에서 해석을 담당
* 객체 지향 프로그래밍에서 DB를 연동할 때, DB와 객체 지향 프로그래밍 언어 간의 호환되지 않는 데이터를 변환하는 프로그래밍 기법
* 장점 : SQL을 잘 알지 못해도 객체지향 언어로 DB 조작 가능, `객체 지향적 접근으로 높은 생산성`
* 단점 : ORM 만으로 완전한 서비스 구현하기 어려움

# QuerySet API
* 외부 라이브러리 설치
  * pip install ipython : 파이썬 기본 쉘보다 강력한 파이썬 쉘
    * 쉘 : 운영체제 상에서 다양한 기능과 서비스를 구현하는 인터페이스를 제공하는 프로그램
    * python shell : 파이썬 코드를 실행해주는 인터프리터
    * django shell : django 환경 안에서 진행할 수 있는 쉘
    * python manage.py shell_plus
  * pip install django-extensions : Django 확장 프로그램 모음
    * 이후 settings.py의 INSTALLED_APPS에 추가
* 패키지 목록 업데이트
* Database API 구문
  * Model class.Maneger.Queryset API => Article.objects.all()
  * 'objects' manager
    * `DB를 python class로 조작할 수 있도록 여러 메서드를 제공하는 manager`
  * `QuerySet` : 파이썬 코드가 ORM에 의해 SQL로 변환되어 DB에 전달되고, DB의 응답 데이터를 ORM이 QuerySet이라는 자료형태로 변환해 우리에게 전달
    * 데이터베이스에게서 전달받는 객체 목록
    * DB가 단일한 객체를 반환 할 때는 모델의 인스턴스로 반환됨
  * QuerySet API : QuerySet과 상호작용하기 위해 사용하는 도구

## CREATE 
```python
# 클래스를 통한 인스턴스 생성
article = Article()
# 클래스 변수명과 같은 이름의 인스턴스 변수 생성 후 값 할당
article.title = 'first'
article.content = 'django'
# 인스턴스로 save 메서드 호출
article.save()
```
```python
#인스턴스 생성 시 초기 값 같이 작성하여 생성
article = Article(title='second', content='django')
article.save()
```
```python
# QuerySet API 중 create() 메서드 활용
# 바로 생성된 데이터가 반환됨
Article.objects.create(title='third', content='django')
```
* 데이터 생성 시 save 호출전까지는 객체의 id 값이 None
* id 값은 django가 아니라 DB에서 계산되기 때문에

## READ 
* Article.objects.`all()`
  * QuerySet return
  * 전체 데이터 조회
* Article.objects.`get(pk=1)`
  * 단일 데이터 조회
  * `고유성을 보장하는 조회에서 사용`
  * 객체를 찾을 수 없으면 DoesNotExist 예외 발생
  * 둘 이상의 객체를 찾으면 MultipleObjectsReturned 예외 발생
* Article.objects.`filter(title='first')`
  * 지정된 조회 매개 변수와 일치하는 객체를 포함하는 새 QuerySet을 반환
  * 조회된 객체가 없어도 QuertSet 반환
* Field lookups 
  * 특정 레코드에 대한 조건을 설정하는 방법
  * ex) Article.objects.filter(content__contains='dj') : content 컬럼에 dj가 포함된 모든 데이터 조회

## UPDATE
```python
# 수정하고자 하는 모델의 인스턴스 객체를 조회 후 반환 값을 저장
article = Article.objects.get(pk=1)
# 인스턴스 변수를 변경
article.title = 'byebye'
# save() 인스턴스 메서드 호출
article.save()
```

## DELETE
```python
# 삭제하고자 하는 모델의 인스턴스 객체를 조회 후 반환 값을 저장
article = Article.objects.get(pk=1)
# delete() 인스턴스 메서드 호출
article.delete()
```

## HTTP response status code
* 클라이언트에게 특정 HTTP 요청이 성공적으로 완료되었는지 여부를 알려줌
* Informational responses : 1xx
* Successful responses : 2xx
* Redirection responses : 3xx
* Client error responses : 4xx
* Sever error responses : 5xx

## HTTP request method 
* GET
  * 특정 리소스를 가져오도록 요청할 때 사용
  * 반드시 `데이터를 가져올 때`만 사용
  * DB에 변화 X
  * R 담당
* POST
  * 서버로 `데이터를 전송할 때` 사용
  * 서버에 변경사항을 만듦
  * 데이터를 HTTP body에 담아서 전송
  * GET 쿼리 스트링 파라미터랑 다르게 URL로 보내지 않음
  * C, U, D 담당
  * CSRF (Cross-Site-Request-Forgery)
    * 사이트 간 요청 위조
    * 사용자가 자신의 의지와 무관하게 공격자가 의도한 행동을 하여, 특정 웹페이지를 보안에 취약하게 하거나 수정, 삭제 등의 작업을 하게 만드는 공격 방법
  * `CSRF Token`
    * 해당 POST 요청이 내가 보낸 것인지를 검증하는 것
    * 사용자의 데이터에 임의의 난수 값(token)을 부여해 매 요청마다 해당 난수 값을 포함시켜 전송 시키도록 함
    * 서버에서 요청을 받을 때마다 전달된 token 값이 유효한지 검증
    * django에서 {% csrf_token %}이 없으면 요청에 대해 403 forbidden으로 응답

# Admin site
* 서버의 관리자가 활용하기 위한 페이지
* 모델 class를 admin.py에 등록하고 관리     
  * admin.site.register(모델class)
* python manage.py createsuperuser : 관리자 계정 생성