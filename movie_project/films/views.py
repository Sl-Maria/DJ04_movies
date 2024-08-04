from django.shortcuts import render, redirect
from .models import Films
from .forms import FilmsForm

def index(request):
    films = Films.objects.all()
    return render(request, 'films/index.html', {'films': films})

def add_film(request):
    error = ''
    if request.method == 'POST':
        form = FilmsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Некорректные данные'
    form = FilmsForm()
    return render(request, 'films/add_film.html', {'form': form, 'error': error})

# Create your views here.
