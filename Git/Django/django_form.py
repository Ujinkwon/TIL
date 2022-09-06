# 장고 폼을 정리하는 내용
from .forms import ArticleForm   # Article Model을 바탕으로 만들어진 Form

# 게시글을 생성하기 위한 흐름에 집중해서 이해할 필요 있음
def new(request):
    # 1. 게시글을 작성할 수 있는 페이지를 보여줘야 할 필요가 있음
    #   (게시글 요청은 GET method 로 요청)
    # 1.1 ModelForm에 전달 받은 데이터를 넣어서 인스턴스를 생성한다.
    form = ArticleForm()

    #1.2 빈 인스턴스를 딕셔너리 형태로 담아서 html로 렌더링해준다.
    context = {
        'form':form
    }
    return render(request, 'articles/new.html', context)

def create(request):
    # 2. 게시글을 DB에 저장하기 위한 단계
    #    (DB에 저장되는 요청은 POST 요청)
    # 2.1 ModelForm 에 전달 받은 데이터를 넣어서 인스턴스를 생성한다.
    form = ArticleForm(request.POST)

    # 2.2 인스턴스에 담긴 데이터가 저장해도 되는 데이터인지 검수한다. (유효성 검사)
    if form.is_valid():    # 유효성 검사 통과하면 True
        article = form.save()  # 필요하다면 저장되는 데이터를 인스턴스로 받아서 사용
        return redirect('articles:detail', article.pk)

    # 2.2.2 유효성 검사를 통과하지 못한다면? => 에러 메세지 보여줘야 한다.
    # 유효성 검사를 통과하지 못하면 에러 메세지가 form에 알아서 담긴다.
    # 에러 메세지가 담긴 form을 딕셔너리로 담아서 렌더링해준다.
    context = {
        'form':form
    }
    return render(request, 'articles/create.html', context)

def edit(request, pk):
    # 3 게시글을 수정할 수 있는 페이지를 보여줘야 함
    #    (게시글 요청은 GET method 사용)
    # 해당 아이디의 저장된 데이터 불러오기
    article = Article.objects.get(pk=pk)
    # 3.1 ModelForm에 전달 받은 데이터를 넣어서 인스턴스를 생성한다.
    form = ArticleForm(instance=article)
    
    # 3.2 딕셔너리 형태로 담아서 html로 렌더링해준다.
    context = {
        'article': article,
        'form': form,
    }
    return render(request, 'articles/edit.html', context)

def update(request.pk):
    # 4 게시글을 수정할 수 있는 페이지를 보여줘야 함
    #    (게시글 요청은 GET method 사용)
    # 해당 아이디의 저장된 데이터 불러오기
    article = Article.objects.get(pk=pk)
    # 4.1 ModelForm 에 전달 받은 데이터를 넣어서 인스턴스 생성
    form = ArticleForm(request.POST, instance=article)

    # 4.2 인스턴스에 담긴 데이터가 저장해도 되는 데이터인지 검수한다. (유효성 검사)
    if form.is_valid():
        form.save()
        return redirect('articles:detail', article.pk)

    # 4.2.2 유효성 검사를 통과하지 못하면 에러 메세지가 form에 알아서 담긴다.
    # 에러 메세지가 담긴 form을 딕셔너리로 담아서 렌더링해준다.
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)



# 하나의 함수로 통합
def new_create_통합본(request):
    
    if request.method == 'POST':
        # POST
        form = ArticleForm(request.POST)
        if form.is_valid(): 
            article = form.save() 
            return redirect('articles:detail', article.pk)
    else:
        # GET
        form = ArticleForm()

    # GET, POST 요청의 공통된 내용
    context = {
        'form':form
    }
    return render(request, 'articles/create.html', context)

def edit_update_통합본(request, pk):

    article = Article.objects.get(pk=pk)

    if request.method == 'POST':
        # POST
        form = ArticleForm(request.POST, instance=article)
        if form.is_valid():
            form.save()
            return redirect('articles:detail', article.pk)
    else:
        # GET
        form = ArticleForm(instance=article)
    
    # GET, POST 요청의 공통된 내용
    context = {
        'form': form,
        'article': article,
    }
    return render(request, 'articles/update.html', context)
