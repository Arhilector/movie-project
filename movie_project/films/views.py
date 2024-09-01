from django.shortcuts import render, redirect
from .forms import MovieForm
from .models import Movie

def movie_create_view(request):
    form = MovieForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('movie_list')
    return render(request, 'movie_create.html', {'form': form})


def movie_list_view(request):
    form = MovieForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('movie_list')

    movies = Movie.objects.all()
    return render(request, 'movie_list.html', {'movies': movies, 'form': form})
