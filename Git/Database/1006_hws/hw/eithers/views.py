from django.shortcuts import render, redirect
from .models import Either, Comment
from .forms import EitherForm, CommentForm
from django.db import connection
import random

# Create your views here.
def index(request):
    eithers = Either.objects.all()
    random_num = random.randrange(1, len(eithers)+1)
    context = {
        'eithers': eithers,
        'random_num': random_num,
    }
    return render(request, 'eithers/index.html', context)

def create(request):
    if request.method == 'POST':
        form = EitherForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('eithers:index')
    else:
        form = EitherForm()
    context = {
        'form': form,
    }
    return render(request, 'eithers/create.html', context)

def detail(request, pk):
    either = Either.objects.get(pk=pk)
    comment_form = CommentForm()
    comments = Comment.objects.filter(either=either)

    eithers = Either.objects.all()
    random_num = random.randrange(1, len(eithers)+1)

    cmd = [
        "SELECT COUNT(*) FROM eithers_comment WHERE pick = 'RED' and ",
        "SELECT COUNT(*) FROM eithers_comment WHERE pick = 'BLUE' and ",
        "SELECT COUNT(*) FROM eithers_comment WHERE ",
    ]
    cnt = []
    for c in cmd:
        try:
            cursor = connection.cursor()
            query = c + 'either_id = ' + str(pk)
            result = cursor.execute(query)
            stocks = cursor.fetchall()

            connection.commit()
            connection.close()
        except:
            connection.rollback()
        cnt.append(stocks[0][0])
    if not cnt[2]:
        red_ratio = 50
        blue_ratio = 50
    else:
        red_ratio = round((cnt[0]/cnt[2])*100, 2)
        blue_ratio = round((cnt[1]/cnt[2])*100, 2)

    context = {
        'either': either,
        'comment_form': comment_form,
        'comments': comments,
        'red_ratio': red_ratio,
        'blue_ratio': blue_ratio,
        'random_num': random_num,
    }
    return render(request, 'eithers/detail.html', context)

def comment_create(request, either_pk):
    comment_form = CommentForm(request.POST)
    either = Either.objects.get(pk=either_pk)
    if comment_form.is_valid():
        comment = comment_form.save(commit=False)
        comment.either = either
        comment.save()
        return redirect('eithers:detail', either_pk)
    comments = Comment.objects.filter(either=either)

    context = {
        'comment_form': comment_form,
        'either': either,
        'comments': comments,
    }
    return render(request, 'eithers/detail.html', context)