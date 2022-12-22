from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Movie
from .forms import MovieForm

# Create your views here.
def index(req):
    movie = Movie.objects.all()
    context = {
        'movie_list':movie
    }

    return render(req, 'index.html',context)

def detail(req, movie_id):
    movie = Movie.objects.get(id=movie_id)
    return render(req, "detail.html", {'movie': movie})

def add_movie(req):
    if req.method == "POST":
        name = req.POST.get('name')
        sdesc = req.POST.get('sdesc')
        desc = req.POST.get('desc')
        year = req.POST.get('year')
        img = req.FILES['img']
        movie = Movie(name=name, sdesc=sdesc, desc=desc, year=year, img=img)
        movie.save()

    return render(req, 'add.html')

def update(req, id):
    movie = Movie.objects.get(id=id)
    form = MovieForm(req.POST or None, req.FILES, instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')

    return render(req, 'edit.html', {'form': form, 'movie': movie})

def delete(req, id):
    movie = Movie.objects.get(id=id)
    if req.method == 'POST':
        movie.delete()
        return redirect('/')

    return render(req, 'delete.html', {'movie':movie})
