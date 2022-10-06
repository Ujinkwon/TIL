from django.shortcuts import render, redirect
from .models import Either
from .forms import EitherForm

# Create your views here.
def index(request):
    eithers = Either.objects.all()
    context = {
        'eithers': eithers,
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
    context = {
        'either': either,
    }
    return render(request, 'eithers/detail.html', context)