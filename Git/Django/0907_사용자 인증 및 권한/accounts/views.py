from urllib import request
from django.shortcuts import render, redirect
from django.contrib.auth.forms import (
    AuthenticationForm, 
    PasswordChangeForm,
)
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth import update_session_auth_hash
from .forms import (
    CustomUserChangeForm, 
    CustomUserCreationForm,
)

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_http_methods

# Create your views here.
@require_http_methods(['GET', 'POST'])
def login(request):
    # 로그인한 유저는 로그인 창 띄우지 않도록
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            # 로그인
            auth_login(request, form.get_user())
            return redirect(request.GET.get('next') or 'articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form': form,
        'title': 'LOGIN page',
        'btn_title': 'Login'
    }
    return render(request, 'accounts/form.html', context)

@login_required
def logout(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            auth_logout(request)
    return redirect('articles:index')

@require_http_methods(['GET', 'POST'])
def signup(request):
    if request.user.is_authenticated:
        return redirect('articles:index')

    if request.method == 'POST':
        form =  CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect('articles:index')
    else:
        form = CustomUserCreationForm()
    context = {
        'form': form,
        'title': 'Signup page',
        'btn_title': '회원가입'
    }
    return render(request, 'accounts/form.html', context)

@login_required
def delete(request):
    # 회원탈퇴
    if request.method == 'POST':
        request.user.delete()
        auth_logout(request)
    return redirect('articles:index')

@login_required
@require_http_methods(['GET', 'POST'])
def update(request):
    # 회원정보 수정
    if request.method == 'POST':
        form = CustomUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomUserChangeForm(instance=request.user)
    context = {
        'form': form,
        'title': '회원정보 수정 page',
        'btn_title': '수정하기',
    }
    return render(request, 'accounts/form.html', context)

@login_required
@require_http_methods(['GET', 'POST'])
def change_password(request):
    # 비밀번호 변경
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request, form.user)
            return redirect('articles:index')
    else:
        form = PasswordChangeForm(request.user)
    context = {
        'form': form,
        'title': '비밀번호 변경 page',
        'btn_title': '변경하기',
    }
    return render(request, 'accounts/form.html', context)