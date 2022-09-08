# Django start
1. `.gitignore` 파일 생성 => python, vs code, django
2. 가상환경 실행 
    * python -m venv venv
    * source venv/Script/activate
3. 장고 설치
    * pip install django==3.2
4. 패키지 리스트 생성
    * pip freeze > requirements.txt
    * 만약 파일이 있다면 있는대로 설치
      * pip install -r requirements.txt
5. 장고 프로젝트 생성
    * django-admin startproject 프로젝트이름 .
6. 장고 앱 생성
    * python manage.py startapp 앱이름
    * settings.py 에 앱 등록
7. url 분리
    * 앱 폴더에 urls.py 생성
    ```python
    from django.urls import path
    from . import views
    app_name = '앱이름'
    urlpatterns = [

    ]
    ```
8. 기본 템플릿 생성
    * templates\base.html
    * CDN, block 태그 추가
    * settings.py 에 `BASE_DIR / 'templates'`
9. 모델 생성
    * 필드 구성
    ```python
    class 모델이름(models.Model):
        title = models.CharField(max_length=10)
        content = models.TextField()
    ```
10. ModelForm 생성
    * 필드 구성
    ```python
    from django import forms
    from .models import 모델이름
    class 모델폼이름(forms.ModelForm):
        title = forms.CharField(
            label='제목',
            widget=forms.TextInput(
                attrs={
                    'class': 'my-title', 
                    'placeholder': 'Enter the title',
                    'maxlength': 10,
                }
            ),
        )
        content = forms.CharField(
            label='내용',
            widget=forms.Textarea(
                attrs={
                    'class': 'my-content',
                    'placeholder': 'Enter the content',
                    'rows': 5,
                    'cols': 50,
                }
            ),
            error_messages={
                'required': 'Please enter your content'
            }
        )

        class Meta:
            model = 모델이름
            fields = '__all__'
    ```

11. app accounts 생성, 등록 & url 분리, 등록
12. accounts.models.py에 AbstractUser 상속받는 커스텀 유저 클래스 생성
    ```python
    from django.conrtib.auth.models import AbstractUser
    class User(AbstractUser):
        pass
    ```
    * settings.py에 `AUTH_USER_MODEL = 'accounts.User'` 등록
13. accounts.admin.py에 커스텀 유저 모델 등록
    ```python
    from django.contrib.auth.admin import UserAdmin
    from .models import User
    admin.site.register(User, UserAdmin)
    ```
14. DB에 적용
    * python manage.py makemigrations
    * python manage.py migrate

    * 만약, 프로젝트 진행 중에 accounts 생성했다면 `데이터베이스 초기화 후 마이그레이션`
      * migrations 파일(번호가 붙은 파일만) 삭제
      * db.sqlite3 삭제
      * 이후, DB 적용

15. 관리자 아이디. 비밀번호 생성
    * python manage.py createsuperuser

--------

# 게시글 crud
```python
from .models import Article
from .forms import ArticleForm
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.http import require_http_methods, require_POST, require_safe
from django.contrib.auth.decorators import login_required  
# 로그인 상태에서만 글을 작성/수정/삭제 할 수 있도록

# Create your views here.
@require_safe
# 게시글 목록
def index(request):
    # DB 불러와서 딕셔너리로 변환 후 렌더링
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)


@login_required
@require_http_methods(['GET', 'POST'])
# 게시글 작성
def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST) 
        # 폼이 유효하다면 저장
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        # 글 작성 폼 렌더링
        form = ArticleForm()
    # print(form.errors)
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)


@require_safe
# 글의 세부사항
def detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

@login_required
@require_POST
# 게시글 삭제
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    return redirect('articles:detail', article.pk)

@login_required
@require_http_methods(['GET', 'POST'])
# 게시글 수정
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        # Create a form to edit an existing Article,
        # but use POST data to populate the form.
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        # Creating a form to change an existing article.
        form = ArticleForm(instance=article)
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/update.html', context)
```

-------

# Login/out crud
```python
from ast import Pass
from django.shortcuts import render, redirect
from django.contrib.auth.forms import (
    AuthenticationForm, 
    PasswordChangeForm,
)
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from .forms import (
    CustomUserChangeForm, 
    CustomUserCreationForm,
)
from django.contrib.auth import update_session_auth_hash


# Create your views here.
def login(request):
    # 인증된 사용자면 로그인 로직 수행할 수 없도록 처리
    if request.user.is_authenticated:
        return redirect('articles:index')
    # 실제 로그인 동작이 일어날 때
    # sesstion이 create 되어 DB에 저장
    # POST 요청일 때 로그인 동작을 처기
    if request.method == 'POST':
        # 사용자의 입력 데이터가 채워진 form을 생성
        form = AuthenticationForm(request, request.POST)
        # 입력이 잘 되었는지, 회원인지 확인
        if form.is_valid():
            # 우리 회원이라면 로그인 처리(sesstion 생성해서 DB에 저장)
            # 유저 인스턴스가 필요한데 AuthenticationForm의 메소드를 이용
            # form.get_user() 의 반환값은 form에 담긴 user 인스턴스
            auth_login(request, form.get_user())
            return redirect('articles:index')
    
    # 로그인 입력 페이지를 띄울 수 있는 GET 요청
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/login.html', context)

def logout(request):
    # 로그아웃은 사용자로부터 입력 받는 것이 없기에
    # GET 요청에 대한 처리는 필요없음
    if request.method == 'POST':
        # 로그아웃을 처리하는 내용
        # session을 DB에서 삭제
        auth_logout(request)
    return redirect('articles:index')

def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # 회원가입 후 곧바로 로그인 진행
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
    }
    return render(request, 'accounts/signup.html', context)

def delete(request):
    # 회원 탈퇴는 DB를 수정하는 것이기에 POST일 떄만 동작
    if request.method == 'POST':
        # user 정보는 request 내부에 가지고 있어서
        # 따로 DB에서 불러올 필요없음
        request.user.delete()
        # 탈퇴 후 로그아웃 (순서 바뀌면 X)
        auth_logout(request)
    return redirect('articles:index')

def update(request):
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/update.html', context)

def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            # 일반 폼을 상속받았지만
            # save 메서드가 정의되어 있다.
            form.save()
            # 비밀번호가 변경되어도 로그아웃 되지 않도록 session data로 session 업데이트
            update_session_auth_hash(request, form.user)
            return redirect('articles:index')
    else:
        # 로그인한 유저의 비밀번호를 저장해야 하기에
        # 첫 번째 인자로 User 정보를 넣어야한다.
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
    }
    return render(request, 'accounts/change_password.html', context)
```

# Limiting access to logged-in users
* 로그인 사용자에 대해 접근 제한

## `is_authenticated` attribute
* 사용자가 인증되었는지 여부 확인
* 일반적으로 request.user에서 이 속성 사용
* 권한과 관련 X, 활성화 상태인지, 유효한 세션을 갖는지 확인 X
* 로그인, 비로그인 상태에서 출력되는 링크 다르게 설정 가능
  * 인증된 사용자만 게시글 작성 링크 볼 수 있도록..
  * But 비로그인 상태로 url을 입력하면 글 작성 페이지 이동 가능
* 인증된 사용자는 로그인 로직 수행할 수 없도록 처리
  
## The `login_required` decorator
* 사용자가 로그인 되어 있으면 정상적으로 view 함수 실행
* 로그인 하지 않은 경우 settings.py의 LOGIN_URL 문자열 주소로 redirect
  * LOGIN_URL 기본 값 => /accounts/login/
* 로그인 상태에서만 글을 작성/수정/삭제 할 수 있도록 수정
  * url 입력 시에도 적용
* 인증 성공 시 사용자가 redirect 되어야 하는 경로는 "next" 쿼리 문자열 매개변수에 저장
  * /accounts/login/?next=/articles/create/
  * `next` query string parameter
    * 로그인이 정상적으로 진행되면 이전에 요청했던 주소로 redirect 하기 위해 제공해주는 쿼리 스트링 파라미터
    * 별도로 처리 해주지 않으면 view에 설정한 redirect경로로 이동
    * 별도 처리 => 로그인 진행 후 원했던 경로로 이동
        ```python 
        next = request.GET.get('next')
        return redirect(next or 'articles:index')
        ```
    * 주의 : login 템플릿에서 form action이 작성되어 있으면 동작X