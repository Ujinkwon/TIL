from django.shortcuts import render, redirect, get_object_or_404
from .models import Article
from .forms import ArticleForm

from django.contrib.auth.decorators import login_required
from django.views.decorators.http import(
    require_http_methods,
    require_POST,
    require_safe,
)

# Create your views here.
@require_safe
def index(request):
    articles = Article.objects.all()
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

@login_required
@require_http_methods(['POST', 'GET'])
def create(request):
    if request.method == 'POST':
        # 저장
        form = ArticleForm(request.POST)
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        # 생성 페이지 렌더링
        form = ArticleForm()
    context = {
        'form': form,
    }
    return render(request, 'articles/create.html', context)

@require_safe
def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article,
    }
    return render(request, 'articles/detail.html', context)

@login_required
@require_POST
def delete(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        article.delete()
        return redirect('articles:index')
    return redirect('articles:detail', article.pk)

@login_required
@require_http_methods(['GET', 'POST'])
def update(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == 'POST':
        # 업데이트
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        # 수정 페이지 렌더링
        form = ArticleForm(instance=article)
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)