from django.shortcuts import render, redirect

from articles.forms import ArticleForm
from .models import Article

# Create your views here.
def index(request):
    # 모델의 DB 다 불러오기
    articles = Article.objects.all()
    # 딕셔너리로 변환
    context = {
        'articles': articles,
    }
    return render(request, 'articles/index.html', context)

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
        'form': form
    }
    return render(request, 'articles/create.html', context)

def detail(request, pk):
    article = Article.objects.get(pk=pk)
    context = {
        'article': article
    }
    return render(request, 'articles/detail.html', context)

def update(request, pk):
    # 해당 id의 DB 불러오기
    article = Article.objects.get(pk=pk)
    # 업데이트
    if request.method == 'POST':
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

def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')